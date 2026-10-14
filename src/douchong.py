import pyautogui
import time
from utils import wait_and_click, scale_pos
from daily_menu import hover_daily_menu_and_click

pyautogui.FAILSAFE = True

# 基准状态下的对手图标坐标（在你基准分辨率/缩放下测的）
BASE_OPPONENT_POS = (2099, 634)


def go_to_douchong():
    print("=== 斗宠大会 ===")

    # 1. 进入斗宠大会
    if not hover_daily_menu_and_click("douchong.png", target_desc="斗宠大会"):
        print("❌ 无法进入斗宠大会")
        return False
    time.sleep(2)

    # 2. 循环战斗
    round_num = 0
    while True:
        round_num += 1
        print(f"\n--- 第 {round_num} 轮循环 ---")

        opponent_pos = scale_pos(BASE_OPPONENT_POS)
        if not opponent_pos:
            print("❌ 未校准，退出")
            return False

        print(f"  点击对手 {opponent_pos}")
        pyautogui.moveTo(opponent_pos[0], opponent_pos[1], duration=0.2)
        pyautogui.click()

        # 等待返回按钮（超时说明次数为0）
        if not wait_and_click("return_button.png", timeout=20, desc="返回按钮"):
            print("❌ 返回按钮未出现，判定次数为0，退出斗宠大会")
            break

        # 等待回到斗宠页面
        if not wait_and_click("page_marker.png", timeout=15, desc="斗宠页面标志物"):
            print("⚠️ 没回到斗宠页面，等 2 秒重试")
            time.sleep(2)
            continue

    # 3. 点红叉返回主城
    if not wait_and_click("red_x.png", timeout=10, desc="红叉返回主城"):
        print("❌ 找不到红叉")
        return False
    time.sleep(1.0)
    print("✅ 斗宠大会完成")
    return True


if __name__ == "__main__":
    print("3秒后开始，请手动停在主城界面...")
    time.sleep(3)
    go_to_douchong()