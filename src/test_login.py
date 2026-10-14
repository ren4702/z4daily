from utils import wait_and_click, calibrate_from_saves
import time


def login_and_select_save(save_number):
    print(f"=== 登录并选择存档 {save_number} ===")

    # 1. 点击“开始游戏”
    if not wait_and_click("start_game.png", timeout=10, desc="开始游戏按钮"):
        print("❌ 找不到开始游戏按钮")
        return False
    time.sleep(2)

    # 2. 校准
    print("  正在校准缩放和位置...")
    if not calibrate_from_saves():
        print("❌ 校准失败，退出")
        return False

    # 3. 点击指定存档
    template = f"save_{save_number}.png"
    if not wait_and_click(template, timeout=10, desc=f"存档 {save_number}"):
        print(f"❌ 找不到存档 {save_number}")
        return False
    time.sleep(5)

    print(f"✅ 存档 {save_number} 进入完成")
    return True


if __name__ == "__main__":
    print("3秒后开始，请手动停在登录界面...")
    login_and_select_save(1)