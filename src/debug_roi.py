import cv2
import numpy as np
import mss
import time
import os

# 自动定位到项目根目录下的 debug 文件夹
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEBUG_DIR = os.path.join(BASE_DIR, "debug")
os.makedirs(DEBUG_DIR, exist_ok=True)

# 修改这个 ROI 到你想要的位置
ROI = {"left": 820, "top": 500, "width": 100, "height": 60}

print("8秒后开始截取屏幕，请立刻切换到《造梦西游4》游戏界面...")
for i in range(1, 0, -1):
    print(f"倒计时: {i}")
    time.sleep(1)

with mss.MSS() as sct:
    screenshot = np.array(sct.grab(ROI))
    save_path = os.path.join(DEBUG_DIR, "debug_roi.png")
    cv2.imwrite(save_path, screenshot)
    print(f"✅ 已保存到: {save_path}")
    print(f"当前截取区域：left={ROI['left']}, top={ROI['top']}, width={ROI['width']}, height={ROI['height']}")