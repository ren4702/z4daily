import cv2
import numpy as np
import mss
from paddleocr import PaddleOCR
import time
import re

# 初始化 OCR
ocr = PaddleOCR(use_textline_orientation=True, lang='ch')

# 划定“今日剩余挑战次数”所在的专属区域（ROI）
# 基于你截图识别到的坐标 (1610, 331)，我们稍微向外扩展一点
# 格式： left, top, width, height
ROI = {"left": 1560, "top": 380, "width": 700, "height": 80}

def get_challenge_count():
    with mss.MSS() as sct:
        # 只截取这一小块区域，而不是全屏
        screenshot = np.array(sct.grab(ROI))
        screen = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)

    # 识别这一小块区域里的文字
    result = ocr.predict(screen)
    
    if not result:
        print("没有识别到任何文字")
        return None

    # 提取识别出的文字
    full_text = ""
    for res in result:
        texts = res.get('rec_texts', [])
        full_text = "".join(texts)

    print(f"识别到的文字是: 【{full_text}】")

    # 使用正则表达式提取数字
    # 查找“次数”后面跟着的数字，如果没找到“次数”，就找所有的数字
    match = re.search(r'次数\s*(\d+)', full_text)
    if not match:
        match = re.search(r'(\d+)', full_text)
    
    if match:
        count = int(match.group(1))
        print(f"提取出的剩余次数是: {count}")
        return count
    else:
        print("❌ 未能从文字中提取出数字")
        return None

if __name__ == "__main__":
    print("3秒后开始读取挑战次数...")
    time.sleep(3)
    count = get_challenge_count()
    if count is not None:
        if count > 0:
            print("✅ 还有挑战次数，可以继续运行脚本")
        else:
            print("❌ 挑战次数为0，停止运行")