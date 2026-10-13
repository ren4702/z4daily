from utils import wait_and_click
import time


def go_to_main_city():
    """从任意界面回到主城：点击世界 → 点击须弥山"""
    print("=== 回到主城 ===")

    if not wait_and_click("world.png", timeout=10, desc="世界按钮"):
        print("❌ 找不到世界按钮")
    time.sleep(1.5)

    if not wait_and_click("xumishan.png", timeout=10, desc="须弥山"):
        print("❌ 找不到须弥山")
        return False
    time.sleep(2)

    print("✅ 已回到主城")
    return True


if __name__ == "__main__":
    print("3秒后开始，请手动停在任意界面...")
    go_to_main_city()