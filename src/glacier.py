from utils import wait_and_click
from daily_menu import hover_daily_menu_and_click
import time


def do_kuyan_liusha():
    """枯焰流沙：地图 → 速通 → 加号1 → 加号2×10 → 使用 → 特殊红叉 → 3次开始速通 → 红叉"""
    print("\n--- 处理 枯焰流沙 ---")

    # 1. 点击“枯焰流沙”
    if not wait_and_click("kuyan_map.png", timeout=10, desc="枯焰流沙"):
        print("❌ 找不到枯焰流沙")
        return False
    time.sleep(1.5)

    # 2. 点击“速通”（枯焰流沙专属）
    if not wait_and_click("kuyan_sutong.png", timeout=10, desc="枯焰流沙速通"):
        print("❌ 找不到枯焰流沙速通")
        return False
    time.sleep(1.5)

    # 3. 点击加号 1（1 次）
    print("  点击第一个加号（1次）")
    if not wait_and_click("plus_1.png", timeout=10, desc="加号1"):
        print("❌ 找不到第一个加号")
        return False
    time.sleep(0.8)

    # 4. 点击另一个样式的加号（10 次）
    print("  点击第二个加号（10次）")
    for i in range(10):
        if not wait_and_click("plus_2.png", timeout=8, desc=f"加号2（第{i+1}次）"):
            print(f"  ⚠️ 第 {i+1} 次找不到加号2，提前结束")
            break
        time.sleep(0.5)

    # 5. 点击“使用”
    if not wait_and_click("use.png", timeout=10, desc="使用"):
        print("❌ 找不到使用按钮")
        return False
    time.sleep(1.0)

    # 6. 点击特殊样式的红叉
    if not wait_and_click("red_x_special.png", timeout=10, desc="特殊红叉"):
        print("⚠️ 找不到特殊红叉，用通用红叉兜底")
        wait_and_click("red_x.png", timeout=5, desc="通用红叉")
    time.sleep(1.0)

    # 7. 连续点击3次“开始速通”
    for i in range(3):
        print(f"  第 {i+1} 次点击开始速通")
        if not wait_and_click("start_sutong.png", timeout=10, desc=f"开始速通（第{i+1}次）"):
            print(f"  ⚠️ 第 {i+1} 次找不到开始速通，跳过剩余次数")
            break
        time.sleep(1.5)

    # 8. 点击红叉返回地图选择界面
    if not wait_and_click("red_x.png", timeout=10, desc="红叉返回地图选择界面"):
        print("❌ 找不到红叉")
        return False
    time.sleep(1.5)

    print("✅ 枯焰流沙完成")
    return True


def do_miwu_juzhe():
    """迷雾沮泽：地图 → 速通 → 3次开始速通 → 红叉"""
    print("\n--- 处理 迷雾沮泽 ---")

    # 1. 点击“迷雾沮泽”
    if not wait_and_click("miwu_map.png", timeout=10, desc="迷雾沮泽"):
        print("❌ 找不到迷雾沮泽")
        return False
    time.sleep(1.5)

    # 2. 点击“速通”（通用模板）
    if not wait_and_click("sutong.png", timeout=10, desc="迷雾沮泽速通"):
        print("❌ 找不到迷雾沮泽速通")
        return False
    time.sleep(1.5)

    # 3. 连续点击3次“开始速通”
    for i in range(3):
        print(f"  第 {i+1} 次点击开始速通")
        if not wait_and_click("start_sutong.png", timeout=10, desc=f"开始速通（第{i+1}次）"):
            print(f"  ⚠️ 第 {i+1} 次找不到开始速通，跳过剩余次数")
            break
        time.sleep(1.5)

    # 4. 点击红叉返回地图选择界面
    if not wait_and_click("red_x.png", timeout=10, desc="红叉返回地图选择界面"):
        print("❌ 找不到红叉")
        return False
    time.sleep(1.5)

    print("✅ 迷雾沮泽完成")
    return True


def go_to_glacier():
    """悲鸣冰川完整流程：枯焰流沙 + 迷雾沮泽"""
    print("=== 悲鸣冰川系列 ===")

    # 1. 展开日常活动菜单，点击“悲鸣冰川”
    if not hover_daily_menu_and_click("glacier.png", target_desc="悲鸣冰川"):
        print("❌ 无法进入悲鸣冰川")
        return False
    time.sleep(2)

    # 2. 枯焰流沙（含加号流程）
    if not do_kuyan_liusha():
        print("⚠️ 枯焰流沙失败，尝试返回后继续")
        wait_and_click("red_x.png", timeout=5, desc="尝试返回地图选择界面")
        time.sleep(1.5)

    # 3. 迷雾沮泽（无加号流程）
    if not do_miwu_juzhe():
        print("⚠️ 迷雾沮泽失败，尝试返回后继续")
        wait_and_click("red_x.png", timeout=5, desc="尝试返回地图选择界面")
        time.sleep(1.5)

    # 4. 最终点击红叉返回主城
    if not wait_and_click("red_x.png", timeout=10, desc="红叉返回主城"):
        print("❌ 找不到红叉")
        return False
    time.sleep(1.0)
    print("✅ 悲鸣冰川系列完成")
    return True


if __name__ == "__main__":
    print("3秒后开始，请手动停在主城界面...")
    go_to_glacier()