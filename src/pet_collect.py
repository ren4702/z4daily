from utils import wait_and_click, find_all_images, click_at, capture_full_screen
import time


def go_to_pet_collect():
    print("=== 宠装采集 ===")

    # 1. 点击“宠装采集”
    if not wait_and_click("pet_collect.png", timeout=10, desc="宠装采集"):
        print("❌ 找不到宠装采集")
        return False
    time.sleep(1.5)  # 等采集界面加载

    # 2. 找到所有“领取”按钮，点击前 3 个
    screen = capture_full_screen()
    claims = find_all_images(screen, "claim.png", threshold=0.7)
    claims.sort(key=lambda p: (p[1], p[0]))  # 先按 y，再按 x 排序

    if len(claims) < 3:
        print(f"  ⚠️ 只找到 {len(claims)} 个领取按钮（期望 3 个）")

    for i, (x, y) in enumerate(claims[:3]):
        print(f"  点击第 {i+1} 个领取 ({int(x)}, {int(y)})")
        click_at(x, y)
        time.sleep(0.8)  # 等“采集”按钮出现

    # 3. 等采集按钮完全出现
    time.sleep(0.8)

    # 4. 找到所有“采集”按钮，点击前 3 个
    screen = capture_full_screen()
    collects = find_all_images(screen, "collect.png", threshold=0.7)
    collects.sort(key=lambda p: (p[1], p[0]))

    if len(collects) < 3:
        print(f"  ⚠️ 只找到 {len(collects)} 个采集按钮（期望 3 个）")

    for i, (x, y) in enumerate(collects[:3]):
        print(f"  点击第 {i+1} 个采集 ({int(x)}, {int(y)})")
        click_at(x, y)
        time.sleep(0.8)

    # 5. 点击红叉返回主城
    if not wait_and_click("red_x.png", timeout=10, desc="红叉返回"):
        print("❌ 找不到红叉")
        return False
    time.sleep(1.0)
    print("✅ 宠装采集完成")
    return True


if __name__ == "__main__":
    print("3秒后开始，请手动停在主城界面...")
    go_to_pet_collect()