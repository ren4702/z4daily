from utils import wait_and_click
import time


def go_to_active():
    """活跃奖励领取：点击活跃 → 一键领取 → 红叉关闭"""
    print("=== 活跃奖励领取 ===")

    # 1. 点击“活跃”
    if not wait_and_click("active.png", timeout=10, desc="活跃"):
        print("❌ 找不到活跃按钮")
        return False
    time.sleep(1.5)

    # 2. 点击“一键领取”
    if not wait_and_click("claim_all_1.png", timeout=10, desc="一键领取"):
        print("❌ 找不到一键领取")
        return False
    time.sleep(1.5)

    # 3. 点击红叉关闭
    if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
        print("❌ 找不到红叉")
        return False
    time.sleep(3.0)

    print("✅ 活跃奖励领取完成")
    return True


if __name__ == "__main__":
    print("3秒后开始，请手动停在主城界面...")
    go_to_active()