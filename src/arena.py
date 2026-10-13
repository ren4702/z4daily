from utils import wait_and_click, find_all_images, click_at, capture_full_screen
from daily_menu import hover_daily_menu_and_click
import time


def go_to_arena():
    print("=== 竞技场 ===")

    # 1. 通过日常活动菜单进入竞技场
    if not hover_daily_menu_and_click("arena.png", target_desc="竞技场"):
        print("❌ 无法进入竞技场")
        return False
    time.sleep(1) # 等竞技场界面加载

    # 2. 循环点击 10 次最右侧的“通”字
    for i in range(10):
        screen = capture_full_screen()
        points = find_all_images(screen, "tong.png", threshold=0.7)

        if not points:
            print(f"  第 {i+1} 次找不到'通'字，提前退出")
            break

        # 取最右侧的那个（x 最大）
        rightmost = max(points, key=lambda p: p[0])
        print(f"  点击第 {i+1} 次最右'通'字 ({int(rightmost[0])}, {int(rightmost[1])})")
        click_at(rightmost[0], rightmost[1])
          # 等战斗结算/界面刷新

    # 3. 点击红叉返回主城
    if not wait_and_click("red_x.png", timeout=10, desc="红叉返回"):
        print("❌ 找不到红叉")
        return False
    time.sleep(1.0)
    print("✅ 竞技场完成")
    return True


if __name__ == "__main__":
    print("3秒后开始，请手动停在主城界面...")
    go_to_arena()