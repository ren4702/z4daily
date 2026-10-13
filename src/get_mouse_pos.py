import pyautogui
import time

print("5秒后开始读取鼠标位置，请立刻把鼠标移到你想点击的地方（不要动）...")
for i in range(5, 0, -1):
    print(f"倒计时: {i}")
    time.sleep(1)

x, y = pyautogui.position()
print(f"\n✅ 当前鼠标坐标: X = {x}, Y = {y}")
print("把这个坐标记下来，填到点击脚本里。")