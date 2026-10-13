from utils import wait_and_click, capture_full_screen, find_image
import pyautogui
import time


def go_to_xuehai():
    """幽冥血海任务流程：世界 → 幽冥血海 → 右移鼠标 → 任务 → 日常任务 → 2 → 血海真身 → 接受任务 → 前往副本 → 速通 → 6次开始速通 → 两次红叉"""
    print("=== 幽冥血海任务 ===")

    # 1. 点击右上角“世界”
    if not wait_and_click("world_1.png", timeout=10, desc="世界按钮"):
        print("❌ 找不到世界按钮")
        return False
    time.sleep(1.5)

    # 2. 点击“幽冥血海”
    if not wait_and_click("youming_xuehai.png", timeout=10, desc="幽冥血海"):
        print("❌ 找不到幽冥血海")
        return False
    time.sleep(2)

       # 3. 向右移动鼠标（不点击），触发悬停效果
    print("  向右移动鼠标（不点击）...")
    cx, cy = pyautogui.position()
    pyautogui.moveTo(cx, cy, duration=0.3)
    time.sleep(0.3)
    pyautogui.moveTo(cx + 300, cy, duration=0.5)
    time.sleep(0.8)
    print(f"  鼠标从 ({cx}, {cy}) 移动到 ({cx + 300}, {cy})")

    # 4. 点击“任务”
    if not wait_and_click("task.png", timeout=10, desc="任务"):
        print("❌ 找不到任务按钮")
        return False
    time.sleep(1.5)

    # 5. 点击“日常任务”
    if not wait_and_click("daily_task.png", timeout=10, desc="日常任务"):
        print("❌ 找不到日常任务")
        return False
    time.sleep(1.5)

    if not wait_and_click("xuehai_zhenshen.png", timeout=10, desc="血海真身"):
        print("❌ 找不到血海真身")
    time.sleep(0.5)

    # 6. 点击“2”
    if not wait_and_click("tab_2.png", timeout=10, desc="任务分类2"):
        print("❌ 找不到任务分类2")
    time.sleep(0.5)

    # 7. 点击“血海真身”
    if not wait_and_click("xuehai_zhenshen.png", timeout=10, desc="血海真身"):
        print("❌ 找不到血海真身")
        return False
    time.sleep(0.5)

    # 8. 点击“接受任务”
    if not wait_and_click("accept_task.png", timeout=10, desc="接受任务"):
        print("❌ 找不到接受任务")
        return False
    time.sleep(0.5)

    # 9. 点击“前往副本”
    if not wait_and_click("go_dungeon.png", timeout=10, desc="前往副本"):
        
        print("❌ 找不到前往副本")
    time.sleep(0.5)


    # 10. 点击“速通”
    if not wait_and_click("sutong.png", timeout=10, desc="速通"):
        print("❌ 找不到速通")
    time.sleep(0.5)

    # 11. 连续点击6次“开始速通”
    for i in range(6):
        print(f"  第 {i+1} 次点击开始速通")
        if not wait_and_click("start_sutong.png", timeout=10, desc=f"开始速通（第{i+1}次）"):
            print(f"  ⚠️ 第 {i+1} 次找不到开始速通，跳过剩余次数")
            break
        time.sleep(0.5)

    # 12. 第一次点击红叉
    if not wait_and_click("red_x.png", timeout=10, desc="第一次红叉"):
        print("❌ 找不到第一个红叉")
    time.sleep(0.5)

    # 13. 第二次点击红叉（返回主城）
    if not wait_and_click("red_x.png", timeout=10, desc="第二次红叉返回主城"):
        print("❌ 找不到第二个红叉")
    time.sleep(1.0)

    # 点击“任务”
    if not wait_and_click("task.png", timeout=10, desc="任务"):
        print("❌ 找不到任务")
        return False
    time.sleep(1.5)

    # 点击“日常任务”
    if not wait_and_click("daily_task.png", timeout=10, desc="日常任务"):
        print("❌ 找不到日常任务")
    time.sleep(1.5)

    # 点击“领取奖励”
    if not wait_and_click("claim_reward.png", timeout=10, desc="领取奖励"):
        print("❌ 找不到领取奖励")
    time.sleep(1.0)
    
    print("✅ 幽冥血海任务完成")
    return True


if __name__ == "__main__":
    print("3秒后开始，请手动停在主城界面...")
    go_to_xuehai()