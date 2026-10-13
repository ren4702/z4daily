from utils import wait_and_click
import time


def go_to_pet_task():
    """宠物任务完整流程"""
    print("=== 宠物任务 ===")

    # 1. 点击“宠物”标签（日常任务界面里）
    if not wait_and_click("pet_tab.png", timeout=10, desc="宠物标签"):
        print("❌ 找不到宠物标签")
        if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
             print("❌ 找不到红叉")
             return False
             time.sleep(0.5)
        return False
    time.sleep(0.5)

    # 2. 点击“静磐或静武”
    if not wait_and_click("jingpan_jingwu.png", timeout=10, desc="静磐或静武"):
        print("❌ 找不到静磐或静武")
        if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
             print("❌ 找不到红叉")
             return False
             time.sleep(0.5)
        return False
    time.sleep(0.5)

    # 3. 点击“接受任务”
    if not wait_and_click("accept_task.png", timeout=10, desc="接受任务（静磐/静武）"):
        print("❌ 找不到接受任务")
        if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
             print("❌ 找不到红叉")
             return False
             time.sleep(0.5)
        return False
    time.sleep(0.5)

    # 4. 点击“静幻或静行”
    if not wait_and_click("jinghuan_jingxing.png", timeout=10, desc="静幻或静行"):
        print("❌ 找不到静幻或静行")
        if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
             print("❌ 找不到红叉")
             return False
             time.sleep(0.5)
        return False
    time.sleep(0.5)

    # 5. 点击“接受任务”
    if not wait_and_click("accept_task.png", timeout=10, desc="接受任务（静幻/静行）"):
        print("❌ 找不到接受任务")
        if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
             print("❌ 找不到红叉")
             return False
             time.sleep(0.5)
    time.sleep(0.5)

    # 6. 点击“前往副本”
    if not wait_and_click("go_dungeon.png", timeout=10, desc="前往副本"):
        print("❌ 找不到前往副本")
        if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
             print("❌ 找不到红叉")
             return False
             time.sleep(0.5)
    time.sleep(2)

    # 7. 点击静幻图标
    if not wait_and_click("jinghuan_icon.png", timeout=10, desc="静幻图标"):
        print("❌ 找不到静幻图标")
        if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
             print("❌ 找不到红叉")
             return False
             time.sleep(0.5)
    time.sleep(0.5)

    # 8. 点击“挑战”
    if not wait_and_click("challenge.png", timeout=10, desc="挑战（静幻）"):
        print("❌ 找不到挑战")
        if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
             print("❌ 找不到红叉")
             return False
             time.sleep(0.5)

    # 9. 等待“返回训练营”出现并点击
    if not wait_and_click("return_camp.png", timeout=30, desc="返回训练营（静幻）"):
        print("❌ 找不到返回训练营")
        if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
             print("❌ 找不到红叉")
             return False
             time.sleep(0.5)
    time.sleep(1.5)

    # 10. 点击静磐图标
    if not wait_and_click("jingpan_icon.png", timeout=10, desc="静磐图标"):
        print("❌ 找不到静磐图标")
        if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
             print("❌ 找不到红叉")
             return False
             time.sleep(0.5)
    time.sleep(0.5)

    # 11. 点击“挑战”
    if not wait_and_click("challenge.png", timeout=10, desc="挑战（静磐）"):
        print("❌ 找不到挑战")
        if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
             print("❌ 找不到红叉")
             return False
             time.sleep(0.5)

    # 12. 等待“返回训练营”出现并点击
    if not wait_and_click("return_camp.png", timeout=30, desc="返回训练营（静磐）"):
        print("❌ 找不到返回训练营")
        if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
             print("❌ 找不到红叉")
             return False
             time.sleep(0.5)
    time.sleep(1.5)

    # 13. 点击“设置”
    if not wait_and_click("settings.png", timeout=10, desc="设置"):
        print("❌ 找不到设置")
        if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
             print("❌ 找不到红叉")
             return False
             time.sleep(0.5)
    time.sleep(1.5)

    # 14. 点击“返回地图”
    if not wait_and_click("return_map.png", timeout=10, desc="返回地图"):
        print("❌ 找不到返回地图")
        if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
             print("❌ 找不到红叉")
             return False
             time.sleep(0.5)
    time.sleep(2)

    # 15. 点击“任务”
    if not wait_and_click("task.png", timeout=10, desc="任务"):
        print("❌ 找不到任务")
        if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
             print("❌ 找不到红叉")
             return False
             time.sleep(0.5)
    time.sleep(1.5)

    # 16. 点击“日常任务”
    if not wait_and_click("daily_task.png", timeout=10, desc="日常任务"):
        print("❌ 找不到日常任务")
        if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
             print("❌ 找不到红叉")
             return False
             time.sleep(0.5)
    time.sleep(1.5)

    # 17. 点击“宠物”标签
    if not wait_and_click("pet_tab.png", timeout=10, desc="宠物标签"):
        print("❌ 找不到宠物标签")
        if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
             print("❌ 找不到红叉")
             return False
             time.sleep(0.5)
    time.sleep(1.5)

    # 18. 点击“领取奖励”（第一次）
    if not wait_and_click("claim_reward.png", timeout=10, desc="领取奖励（第一次）"):
        print("❌ 找不到领取奖励（第一次）")
        if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
             print("❌ 找不到红叉")
             return False
             time.sleep(0.5)
    time.sleep(1.5)

    # 19. 点击“领取奖励”（第二次）
    if not wait_and_click("claim_reward.png", timeout=10, desc="领取奖励（第二次）"):
        print("❌ 找不到领取奖励（第二次）")
        if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
             print("❌ 找不到红叉")
             return False
             time.sleep(0.5)
    time.sleep(1.5)

    # 20. 点击红叉关闭
    if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
        print("❌ 找不到红叉")
        if not wait_and_click("red_x.png", timeout=10, desc="红叉"):
             print("❌ 找不到红叉")
             return False
             time.sleep(0.5)
    time.sleep(1.0)

    print("✅ 宠物任务完成")
    return True


if __name__ == "__main__":
    print("3秒后开始，请手动停在日常任务界面...")
    go_to_pet_task()