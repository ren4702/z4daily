import cv2
import numpy as np
import mss
import pyautogui
import time
import re
import os
from paddleocr import PaddleOCR

# ============ 路径配置 ============
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
DEBUG_DIR = os.path.join(BASE_DIR, 'debug')

# ============ 安全设置 ============
pyautogui.FAILSAFE = True

# ============ OCR 初始化（全局一次） ============
print("正在加载 OCR 模型，请稍候...")
ocr = PaddleOCR(use_textline_orientation=True, lang='ch')

# ============ 缓存 ============
_template_cache = {}
_mss_instance = None
_global_scale = None   # 全局缩放比例，None 表示未校准

def calibrate_scale(template_name, threshold=0.7):
    """
    用指定模板跑一次多尺度匹配，记录全局缩放比例。
    应该在进入游戏后、第一次点击某个必定出现的按钮前调用一次。
    """
    global _global_scale
    screen = capture_full_screen()
    path = os.path.join(TEMPLATE_DIR, template_name)
    if not os.path.exists(path):
        print(f"  ⚠️ 校准失败：找不到 {template_name}")
        return None
    template = cv2.imread(path)
    if template is None:
        return None

    scales = np.linspace(0.4, 2.0, 33)   # 精细搜索
    best_val = 0
    best_scale = 1.0

    for scale in scales:
        w = int(template.shape[1] * scale)
        h = int(template.shape[0] * scale)
        if w < 5 or h < 5 or w > screen.shape[1] or h > screen.shape[0]:
            continue
        resized = cv2.resize(template, (w, h), interpolation=cv2.INTER_AREA)
        result = cv2.matchTemplate(screen, resized, cv2.TM_CCOEFF_NORMED)
        _, val, _, _ = cv2.minMaxLoc(result)
        if val > best_val:
            best_val = val
            best_scale = scale

    if best_val >= threshold:
        _global_scale = best_scale
        print(f"  ✅ 校准成功：全局缩放 = {best_scale:.2f}x（相似度 {best_val:.2f}）")
        return best_scale

    print(f"  ⚠️ 校准失败：最高相似度 {best_val:.2f}")
    return None

def capture_full_screen():
    """截取整个主屏幕"""
    global _mss_instance
    if _mss_instance is None:
        _mss_instance = mss.MSS()
    monitor = _mss_instance.monitors[1]
    return cv2.cvtColor(np.array(_mss_instance.grab(monitor)), cv2.COLOR_BGRA2BGR)


def find_image(screen, template_name, threshold=0.7):
    """
    模板匹配。
    如果已校准缩放，只用该缩放匹配一次（快）。
    如果未校准，跑多尺度兜底（慢）。
    返回 (中心坐标, 相似度, 实际匹配尺寸)。
    """
    global _global_scale
    path = os.path.join(TEMPLATE_DIR, template_name)
    if not os.path.exists(path):
        return None, 0, None
    if template_name not in _template_cache:
        _template_cache[template_name] = cv2.imread(path)
    template = _template_cache[template_name]
    if template is None:
        return None, 0, None
    if template.shape[0] > screen.shape[0] or template.shape[1] > screen.shape[1]:
        return None, 0, None

    # ========== 已校准：单尺度快速匹配 ==========
    if _global_scale is not None:
        w = int(template.shape[1] * _global_scale)
        h = int(template.shape[0] * _global_scale)
        if w < 5 or h < 5 or w > screen.shape[1] or h > screen.shape[0]:
            return None, 0, None
        resized = cv2.resize(template, (w, h), interpolation=cv2.INTER_AREA)
        result = cv2.matchTemplate(screen, resized, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)
        if max_val >= threshold:
            return (max_loc[0] + w // 2, max_loc[1] + h // 2), max_val, (w, h)
        return None, max_val, (w, h)

    # ========== 未校准：多尺度兜底 ==========
    scales = np.linspace(0.5, 1.5, 11)
    best_val = 0
    best_pos = None
    best_size = None
    for scale in scales:
        w = int(template.shape[1] * scale)
        h = int(template.shape[0] * scale)
        if w < 5 or h < 5 or w > screen.shape[1] or h > screen.shape[0]:
            continue
        resized = cv2.resize(template, (w, h), interpolation=cv2.INTER_AREA)
        result = cv2.matchTemplate(screen, resized, cv2.TM_CCOEFF_NORMED)
        _, val, _, loc = cv2.minMaxLoc(result)
        if val > best_val:
            best_val = val
            best_pos = (loc[0] + w // 2, loc[1] + h // 2)
            best_size = (w, h)
    if best_val >= threshold:
        return best_pos, best_val, best_size
    return None, best_val, best_size


def wait_and_click(template_name, timeout=10, threshold=0.7, desc=""):
    """等待图片出现并点击，成功返回 True"""
    print(f"  等待并点击: {desc or template_name}")
    start = time.time()
    while time.time() - start < timeout:
        screen = capture_full_screen()
        pos, conf, _ = find_image(screen, template_name, threshold)
        if pos:
            pyautogui.moveTo(pos[0], pos[1], duration=0.2)
            pyautogui.click()
            print(f"  ✅ 点击 {template_name}（相似度 {conf:.2f}，坐标 {pos}）")
            return True
        time.sleep(0.3)
    print(f"  ⚠️ 超时未找到 {template_name}")
    return False


def click_at(x, y, delay=0.3):
    """在指定坐标点击"""
    pyautogui.moveTo(x, y, duration=0.2)
    pyautogui.click()
    time.sleep(delay)


def read_text_from_roi(roi, regex=None, scale=2):
    """在指定区域 OCR 读取文字，返回文字或提取的数字"""
    with mss.MSS() as sct:
        screenshot = np.array(sct.grab(roi))
        screen = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
        screen = cv2.resize(screen, None, fx=scale, fy=scale, interpolation=cv2.INTER_CUBIC)
        gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)
        screen = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)
    result = ocr.predict(screen)
    if not result:
        return None
    full_text = "".join("".join(res.get('rec_texts', [])) for res in result)
    print(f"  识别文字: 【{full_text}】")
    if regex:
        match = re.search(regex, full_text)
        if match:
            return match.group(1)
        return None
    return full_text

def find_all_images(screen, template_name, threshold=0.7):
    """
    在 screen 中查找所有匹配位置，返回按 x 排序的中心坐标列表。
    已校准时用单尺度（快），未校准时用多尺度兜底（慢但能匹配）。
    """
    global _global_scale
    path = os.path.join(TEMPLATE_DIR, template_name)
    if not os.path.exists(path):
        return []
    if template_name not in _template_cache:
        _template_cache[template_name] = cv2.imread(path)
    template = _template_cache[template_name]
    if template is None:
        return []

    def _match_at_scale(scale):
        w = int(template.shape[1] * scale)
        h = int(template.shape[0] * scale)
        if w < 5 or h < 5 or w > screen.shape[1] or h > screen.shape[0]:
            return []
        resized = cv2.resize(template, (w, h), interpolation=cv2.INTER_AREA)
        result = cv2.matchTemplate(screen, resized, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)
        pts = []
        for pt in zip(*loc[::-1]):
            pts.append((pt[0] + w // 2, pt[1] + h // 2))
        return pts

    # 已校准：单尺度
    if _global_scale is not None:
        points = _match_at_scale(_global_scale)
    else:
        # 未校准：多尺度兜底
        points = []
        for s in np.linspace(0.5, 1.6, 12):
            points += _match_at_scale(s)

    # 去重：距离小于 15 像素的只保留一个
    unique = []
    for p in points:
        if all(abs(p[0] - q[0]) > 15 or abs(p[1] - q[1]) > 15 for q in unique):
            unique.append(p)
    unique.sort(key=lambda p: (p[0], p[1]))
    return unique