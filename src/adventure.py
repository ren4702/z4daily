from utils import wait_and_click
from daily_menu import hover_daily_menu_and_click
import time


def go_to_adventure():
    print("=== 冒险 ===")

    # 1. 通过日常活动菜单进入冒险
    if not hover_daily_menu_and_click("adventure.png", target_desc="冒险"):
        print("❌ 无法进入冒险")
        return False
    time.sleep(1)

    # 2. 点击“一键领取”
    if not wait_and_click("claim_all.png", timeout=1, desc="一键领取"):
        print("❌ 找不到一键领取")

    # 4. 点击“一键投掷”
    if not wait_and_click("throw_all.png", timeout=10, desc="一键投掷"):
        print("❌ 找不到一键投掷")

    # 5. 等待 5 秒
    print("  等待 5 秒...")
    time.sleep(5)

    # 6. 点击红叉返回主城
    if not wait_and_click("red_x.png", timeout=10, desc="红叉返回"):
        print("❌ 找不到红叉")
    time.sleep(1.0)
    print("✅ 冒险完成")
    return True


if __name__ == "__main__":
    print("3秒后开始，请手动停在主城界面...")
    go_to_adventure()