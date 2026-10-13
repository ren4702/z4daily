from utils import wait_and_click
import time


def go_to_union():
    print("=== 进入联盟并贡献 ===")


    # 3. 点击“联盟”
    if not wait_and_click("union.png", timeout=10, desc="联盟"):
        print("❌ 找不到联盟")
        return False
    time.sleep(1.5)

    # 4. 点击“联盟贡献”
    if not wait_and_click("union_contribute.png", timeout=10, desc="联盟贡献"):
        print("❌ 找不到联盟贡献")
        return False
    time.sleep(1.5)

    # 5. 点击“灵魂贡献”
    if not wait_and_click("soul_contribute.png", timeout=10, desc="灵魂贡献"):
        print("❌ 找不到灵魂贡献")
        return False
    time.sleep(1.5)

    # 6. 第一次点击红叉（关闭当前弹窗）
    if not wait_and_click("red_x.png", timeout=10, desc="第一个红色叉号"):
        print("❌ 找不到第一个红色叉号")
        return False
    time.sleep(1.2)  # 等界面变化，出现第二个红叉

    # 7. 第二次点击红叉（关闭剩下的弹窗）
    if not wait_and_click("red_x.png", timeout=10, desc="第二个红色叉号"):
        print("❌ 找不到第二个红色叉号")
        return False
    time.sleep(1)

    print("✅ 联盟贡献流程完成")
    return True


if __name__ == "__main__":
    print("3秒后开始，请切到主城界面...")
    go_to_union()