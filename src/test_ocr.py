import cv2
import numpy as np
import mss
from paddleocr import PaddleOCR
import time

# 初始化 OCR（新版参数已改为 use_textline_orientation）
ocr = PaddleOCR(use_textline_orientation=True, lang='ch')

def scan_screen():
    print("3秒后开始截取屏幕并识别文字...")
    time.sleep(3)
    
    with mss.MSS() as sct:
        monitor = sct.monitors[1]
        screenshot = np.array(sct.grab(monitor))
        screen = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

    print("正在识别，请稍候...")
    # 新版调用方式：使用 predict 而不是 ocr
    result = ocr.predict(screen)
    
    if not result:
        print("❌ 没有识别到任何文字")
        return

    print("\n--- 识别结果如下 ---")
    for res in result:
        # 新版返回的是一个字典结构，用 get 取键更安全
        texts = res.get('rec_texts', [])
        polys = res.get('rec_polys', res.get('dt_polys', []))
        
        for text, poly in zip(texts, polys):
            # poly 是四个角点坐标，取左上角那个点
            x1, y1 = int(poly[0][0]), int(poly[0][1])
            print(f"文字: 【{text}】 | 左上角坐标: ({x1}, {y1})")
    print("--------------------")

if __name__ == "__main__":
    scan_screen()