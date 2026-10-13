import cv2
import numpy as np
import mss
import pyautogui
import time

# 启用失效安全保护：如果鼠标移动到屏幕最角落，脚本会自动报错并停止运行
pyautogui.FAILSAFE = True

def find_and_click():
    # 1. 读取你准备好的目标图案
    template = cv2.imread('target.png')
    if template is None:
        print("找不到 target.png，请检查图片是否放在同一个文件夹下！")
        return

    # 2. 获取当前屏幕画面
    with mss.mss() as sct:
        # 获取主屏幕（monitors[1]）
        monitor = sct.monitors[1]
        # 截取整个屏幕
        screenshot = np.array(sct.grab(monitor))
        # 将颜色通道从 BGRA 转换为 BGR（OpenCV 默认格式）
        screen = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

    # 3. 在屏幕画面中寻找目标图案（使用相关系数匹配法）
    result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    
    # 4. 找到匹配度最高的位置
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    
    # 5. 设定一个阈值（0.8 代表 80% 相似度才点击，防止找错）
    threshold = 0.7
    
    if max_val >= threshold:
        # 计算图案的中心点坐标
        h, w = template.shape[:2]
        center_x = max_loc[0] + w // 2
        center_y = max_loc[1] + h // 2
        
        print(f"找到了！相似度: {max_val:.2f}，正在点击坐标: ({center_x}, {center_y})")
        
        # 移动鼠标并点击
        pyautogui.moveTo(center_x, center_y, duration=0.2)
        pyautogui.click()
    else:
        print(f"没有找到目标，最高相似度只有: {max_val:.2f}，请检查图案是否清晰或是否在屏幕上。")

if __name__ == "__main__":
    print("3秒后开始寻找并点击目标，请将游戏窗口或桌面保持在最前面...")
    time.sleep(3) # 给自己留3秒钟切窗口的时间
    find_and_click()