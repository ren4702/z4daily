from utils import find_image, capture_full_screen, click_at
import pyautogui
import time


def open_daily_menu():
    """
    将鼠标移动到“日常活动”上，竖直向下移动展开菜单。
    成功返回 True，失败返回 False。
    """
    print("  打开日常活动菜单...")

    # 1. 找到“日常活动”按钮的位置
    screen = capture_full_screen()
    pos, conf, _ = find_image(screen, "daily_activity.png", threshold=0.7)
    if not pos:
        print(f"  ⚠️ 找不到日常活动按钮（最高相似度 {conf:.2f}）")
        return False

    x, y = pos
    print(f"  找到日常活动 ({x}, {y})，准备悬停")

    # 2. 鼠标先移动到“日常活动”上
    pyautogui.moveTo(x, y, duration=0.3)
    time.sleep(0.6)  # 等菜单弹出

    # 3. 竖直向下移动，x 不变，y 增加
    # 这里的 +150 是根据菜单高度估算的，需要根据实际情况调整
    pyautogui.moveTo(x, y + 150, duration=0.4)
    time.sleep(0.5)  # 让鼠标停在菜单上

    print(f"  鼠标已悬停在日常活动菜单上 ({x}, {y + 150})")
    return True


def hover_daily_menu_and_click(target_template, target_desc="", menu_offset=150,
                                threshold=0.7, timeout=10):
    """
    打开日常活动菜单，然后在菜单里找目标并点击。
    适用场景：竞技场、斗宠大会、守卫须弥山、冒险。
    """
    print(f"=== 通过日常活动菜单进入 {target_desc or target_template} ===")

    # 1. 打开菜单
    if not open_daily_menu():
        return False

    # 2. 保持鼠标在菜单上，找到目标按钮并点击
    start = time.time()
    while time.time() - start < timeout:
        screen = capture_full_screen()
        pos, conf, _ = find_image(screen, target_template, threshold)
        if pos:
            print(f"  找到 {target_desc or target_template}（相似度 {conf:.2f}），点击 {pos}")
            pyautogui.moveTo(pos[0], pos[1], duration=0.2)
            pyautogui.click()
            time.sleep(1.5)
            return True
        time.sleep(0.3)

    print(f"  ⚠️ 菜单里没找到 {target_desc or target_template}")
    return False


if __name__ == "__main__":
    print("3秒后开始，请手动停在主城界面...")
    open_daily_menu()
    