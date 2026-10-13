from utils import wait_and_click, find_image, capture_full_screen
from daily_menu import hover_daily_menu_and_click
import time


def wait_for_template(template_name, timeout=15, threshold=0.7, desc=""):
    """轮询等待某张图出现，返回 True/False，不点击"""
    print(f"  等待 {desc or template_name} 出现...")
    start = time.time()
    while time.time() - start < timeout:
        screen = capture_full_screen()
        pos, conf, _ = find_image(screen, template_name, threshold)
        if pos:
            print(f"  ✅ {desc or template_name} 已出现（等了 {time.time()-start:.1f} 秒）")
            return True
        time.sleep(0.3)
    print(f"  ⚠️ 等待 {desc or template_name} 超时")
    return False


def do_sutong(city_template, city_name):
    """对单个城市执行：点城市 → 点速通 → 点开始速通 → 等再次速通 → 点红叉返回守卫界面"""
    print(f"\n--- 处理 {city_name} ---")

    # 1. 点击城市名（选中该城市）
    if not wait_and_click(city_template, timeout=10, desc=city_name):
        print(f"❌ 找不到 {city_name}")
        return False
    time.sleep(0.5)  # 等橙色光晕出现、速通按钮出现

    # 2. 点击“速通”
    if not wait_and_click("sutong.png", timeout=1, desc="速通"):
        print("❌ 找不到速通按钮")
        return False
    time.sleep(0.5)  # 等速通新界面加载

    # 3. 点击“开始速通”
    if not wait_and_click("start_sutong.png", timeout=1, desc="开始速通"):
        print("❌ 找不到开始速通")
        return False

    # 4. 等待“再次速通”出现（说明速通完成）
    if not wait_for_template("again_sutong.png", timeout=1, desc="再次速通"):
        print("⚠️ 再次速通未出现，仍尝试点红叉")

    # 5. 点击红叉返回守卫须弥山界面
    if not wait_and_click("red_x.png", timeout=10, desc="红叉返回守卫界面"):
        print("❌ 找不到红叉")
        return False
    time.sleep(1.5)  # 等回到守卫界面

    print(f"✅ {city_name} 完成")
    return True


def go_to_guard():
    print("=== 守卫须弥山 ===")

    # 1. 通过日常活动菜单进入守卫须弥山
    if not hover_daily_menu_and_click("guard.png", target_desc="守卫须弥山"):
        print("❌ 无法进入守卫须弥山")
        return False
    time.sleep(2)  # 等界面加载

    # 2. 依次处理城南、城东、城北
    cities = [
        ("city_nan.png", "城南"),
        ("city_dong.png", "城东"),
        ("city_bei.png", "城北"),
    ]

    for city_template, city_name in cities:
        if not do_sutong(city_template, city_name):
            print(f"⚠️ {city_name} 失败，尝试返回守卫界面后继续")
            wait_and_click("red_x.png", timeout=5, desc="尝试返回守卫界面")
            time.sleep(1.5)

    # 3. 三个城市都完成后，点红叉返回主城
    if not wait_and_click("red_x.png", timeout=10, desc="红叉返回主城"):
        print("❌ 找不到红叉")
        return False
    time.sleep(1.0)
    print("✅ 守卫须弥山完成")
    return True


if __name__ == "__main__":
    print("3秒后开始，请手动停在主城界面...")
    go_to_guard()