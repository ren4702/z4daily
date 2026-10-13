from utils import wait_and_click, capture_full_screen, find_image, click_at
import time

def login_and_select_save():
    print("=== 登录并选择存档 ===")
    
    # 1. 点击“开始游戏”
    if not wait_and_click("begin.png", timeout=10, desc="开始游戏按钮"):
        print("❌ 找不到开始游戏按钮")
        return False
    time.sleep(2)  # 等待存档界面弹出

    # 2. 找到“玉兔”存档并点击
    screen = capture_full_screen()
    pos, conf, _ = find_image(screen, "yutu.png", threshold=0.7)
    if pos:
        print(f"✅ 找到玉兔存档（相似度 {conf:.2f}），点击 {pos}")
        click_at(pos[0], pos[1])
        return True
    else:
        print(f"❌ 没找到玉兔存档，最高相似度 {conf:.2f}")
        return False


if __name__ == "__main__":
    print("3秒后开始，请切到游戏开始界面...")
    time.sleep(3)
    if login_and_select_save():
        print("✅ 登录流程完成")
    else:
        print("⚠️ 登录流程中断")