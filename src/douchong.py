import cv2
import numpy as np
import mss
import pyautogui
import time
import re
import os
from paddleocr import PaddleOCR
from utils import wait_and_click, find_image, capture_full_screen, TEMPLATE_DIR
from daily_menu import hover_daily_menu_and_click

pyautogui.FAILSAFE = True

print("正在加载 OCR 模型，请稍候...")
ocr = PaddleOCR(use_textline_orientation=True, lang='ch')

# ============ 配置区 ============
# 基准数据：在你自己的机器上测一次
BASE_TITLE_SIZE = (300, 40)          # count_title.png 这张模板图的宽高
BASE_OPPONENT_OFFSET = (140, 207)    # 标题中心 → 对手中心的偏移

PAGE_MARKER = os.path.join(TEMPLATE_DIR, "page_marker.png")
PAGE_MARKER_ROI = {"left": 1400, "top": 300, "width": 900, "height": 200}
BASE_TITLE_WIDTH = 434   # 先估一个值
# ============ 全局缓存 ============
_page_marker_cache = None
_mss_instance = None
_title_pos = None
_current_scale = 1.0


def find_count_title_position():
    screen = capture_full_screen()

    # 第一步：快速模板匹配（毫秒级）
    pos, conf, size = find_image(screen, "count_title.png", threshold=0.7)
    if pos and size:
        scale = size[0] / BASE_TITLE_WIDTH
        print(f"  ✅ 模板匹配到标题: {pos}（相似度 {conf:.2f}，缩放 {scale:.2f}x）")
        return pos, scale

    # 第二步：模板失败，降级到 OCR
    print("  ⚠️ 模板匹配失败，降级到 OCR...")
    """用 OCR 全屏查找'今日剩余挑战次数'标题的位置，返回 (位置, 缩放比例)"""
    screen = capture_full_screen()
    h, w = screen.shape[:2]

    # 只搜索屏幕上半部分（标题通常在上方），减少 OCR 耗时
    top_region = screen[0:int(h * 0.5), :]

    result = ocr.predict(top_region)
    if not result:
        print("  ⚠️ OCR 没识别到任何文字")
        return None, None

    for res in result:
        texts = res.get('rec_texts', [])
        polys = res.get('rec_polys', res.get('dt_polys', []))
        for text, poly in zip(texts, polys):
            # 宽松匹配，防止 OCR 错字
            if "今日剩余挑战次数" in text or ("今日" in text and "挑战" in text):
                x1, y1 = int(poly[0][0]), int(poly[0][1])
                x2, y2 = int(poly[2][0]), int(poly[2][1])
                cx = (x1 + x2) // 2
                cy = (y1 + y2) // 2
                title_width = abs(x2 - x1)
                # 缩放比例 = OCR 识别到的标题宽度 / 基准宽度
                scale = title_width / BASE_TITLE_WIDTH
                print(f"  ✅ OCR 标题位置: ({cx}, {cy})，文字:【{text}】，宽度: {title_width}，缩放: {scale:.2f}x")
                return (cx, cy), scale

    # 没找到，把识别到的所有文字打印出来便于调试
    all_text = " | ".join("".join(res.get('rec_texts', [])) for res in result)
    print(f"  ⚠️ 没找到标题，识别到的文字: {all_text}")
    return None, None


def get_opponent_position():
    """根据标题位置 + 缩放后的偏移，计算对手图标的位置"""
    if not _title_pos:
        return None
    dx = int(BASE_OPPONENT_OFFSET[0] * _current_scale)
    dy = int(BASE_OPPONENT_OFFSET[1] * _current_scale)
    return (_title_pos[0] + dx, _title_pos[1] + dy)


def is_count_page_ready():
    """模板匹配快速判断'今日'两个字是否出现（毫秒级）"""
    global _page_marker_cache, _mss_instance
    if not os.path.exists(PAGE_MARKER):
        return False
    if _page_marker_cache is None:
        _page_marker_cache = cv2.imread(PAGE_MARKER)
        if _page_marker_cache is None:
            return False
    if _mss_instance is None:
        _mss_instance = mss.MSS()
    screenshot = np.array(_mss_instance.grab(PAGE_MARKER_ROI))
    screen = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
    template = _page_marker_cache
    if template.shape[0] > screen.shape[0] or template.shape[1] > screen.shape[1]:
        return False
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(result)
    return max_val >= 0.5


def wait_for_count_page(timeout=5):
    """等待回到次数页面（只用模板匹配）"""
    print("  等待回到次数页面...")
    start = time.time()
    while time.time() - start < timeout:
        if is_count_page_ready():
            print(f"  ✅ 已回到次数页面（等了 {time.time()-start:.1f} 秒）")
            return True
        time.sleep(0.2)
    print(f"  ⚠️ 等待次数页面超时（{timeout} 秒）")
    return False


def go_to_douchong():
    """从主城通过日常活动菜单进入斗宠大会，然后循环战斗直到返回按钮超时"""
    global _title_pos, _current_scale

    print("=== 斗宠大会 ===")

    # 1. 进入斗宠大会
    if not hover_daily_menu_and_click("douchong.png", target_desc="斗宠大会"):
        print("❌ 无法进入斗宠大会")
        return False
    time.sleep(2)

    # 2. 定位标题位置和缩放比例，全程复用
    print("  第一次定位标题位置...")
    _title_pos, _current_scale = find_count_title_position()
    if not _title_pos:
        print("❌ 无法定位标题位置，退出")
        return False

    opponent_pos = get_opponent_position()
    print(f"  对手位置: ({int(opponent_pos[0])}, {int(opponent_pos[1])})")

    # 3. 循环战斗
    round_num = 0

    while True:
        round_num += 1
        print(f"\n--- 第 {round_num} 轮循环 ---")
        t_round_start = time.time()

        # 点击对手
        print(f"  点击对手 ({int(opponent_pos[0])}, {int(opponent_pos[1])})")
        pyautogui.moveTo(opponent_pos[0], opponent_pos[1], duration=0.2)
        pyautogui.click()

        # 等待并点击“返回按钮”（模板匹配，超时说明次数为 0）
        if not wait_and_click("return_button.png", timeout=20, desc="返回按钮"):
            print("❌ 返回按钮未出现，判定次数为 0 或战斗无法进入，退出斗宠大会")
            break

        # 等待回到次数页面
        if not wait_for_count_page(timeout=15):
            print("⚠️ 没回到次数页面，等 2 秒后重试")
            time.sleep(2)
            continue

        t_round_end = time.time()
        print(f"⏱️ 本轮总耗时: {t_round_end - t_round_start:.1f} 秒")

    # 4. 点击红叉返回主城
    if not wait_and_click("red_x.png", timeout=10, desc="红叉返回主城"):
        print("❌ 找不到红叉")
        return False
    time.sleep(1.0)
    print("✅ 斗宠大会完成")
    return True


if __name__ == "__main__":
    print("3秒后开始，请手动停在主城界面...")
    go_to_douchong()