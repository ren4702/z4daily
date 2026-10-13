import pyautogui
import time

# 把这里换成你测出来的坐标
TARGET_X = 2100
TARGET_Y = 649

print("3秒后点击目标位置...")
time.sleep(3)
pyautogui.moveTo(TARGET_X, TARGET_Y, duration=0.2)
pyautogui.click()
print(f"✅ 已点击 ({TARGET_X}, {TARGET_Y})")