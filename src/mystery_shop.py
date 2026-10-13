from utils import wait_and_click, find_all_images, click_at, read_text_from_roi, capture_full_screen
import time

# 只框住数字本身，比如“9”或“10”，不含“今日剩余购买次数”文字
SHOP_COUNT_ROI = {"left": 2100, "top": 400, "width": 120, "height": 50}


def get_remaining_buy_count():
    """读取今日剩余购买次数（只识别数字区域）"""
    text = read_text_from_roi(SHOP_COUNT_ROI, regex=r'(\d+)', scale=2)
    if text is not None:
        return int(text)
    return None


def go_to_mystery_shop():
    print("=== 神秘商店 ===")

    # 1. 点击“神秘商店”
    if not wait_and_click("mystery_shop.png", timeout=10, desc="神秘商店"):
        print("❌ 找不到神秘商店")
        return False
    time.sleep(1.5)

    # 2. 点击 10 次购买（每次选最右边的按钮）
    for i in range(10):
        screen = capture_full_screen()
        points = find_all_images(screen, "buy.png", threshold=0.7)
        if not points:
            print(f"  ⚠️ 第 {i+1} 次找不到购买按钮，提前结束")
            break
        rightmost = points[-1]
        print(f"  点击第 {i+1} 次购买 ({int(rightmost[0])}, {int(rightmost[1])})")
        click_at(rightmost[0], rightmost[1])
        time.sleep(0.6)

    # 3. 红叉返回
    if not wait_and_click("red_x.png", timeout=10, desc="红叉返回"):
        print("❌ 找不到红叉")
        return False
    time.sleep(1.0)
    print("✅ 神秘商店完成")
    return True


if __name__ == "__main__":
    print("3秒后开始，请手动停在主城界面...")
    go_to_mystery_shop()