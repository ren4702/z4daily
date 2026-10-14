import time
from test_login import login_and_select_save
from main_city import go_to_main_city
from test_union import go_to_union
from mystery_shop import go_to_mystery_shop
from pet_collect import go_to_pet_collect
from mount_train import go_to_mount_train
from arena import go_to_arena
from douchong import go_to_douchong
from guard import go_to_guard
from adventure import go_to_adventure
from glacier import go_to_glacier
from xuehai import go_to_xuehai
from pet_task import go_to_pet_task
from active import go_to_active
from utils import wait_and_click, calibrate_scale


def run_single_save_tasks():
    """单个存档内的全部日常任务"""
    # 1. 回主城
    if not go_to_main_city():
        print("❌ 无法回到主城")
        return False

   
    # 3. 依次执行任务
    tasks = [
        ("联盟贡献", go_to_union),
        ("神秘商店", go_to_mystery_shop),
        ("宠装采集", go_to_pet_collect),
        ("骑装养成", go_to_mount_train),
        ("竞技场", go_to_arena),
        ("斗宠大会", go_to_douchong),
        ("守卫须弥山", go_to_guard),
        ("冒险", go_to_adventure),
        ("悲鸣冰川", go_to_glacier),
        ("幽冥血海", go_to_xuehai),
        ("宠物任务", go_to_pet_task),
        ("活跃奖励", go_to_active),
    ]

    for task_name, task_func in tasks:
        print(f"\n{'='*40}")
        print(f"▶ 执行：{task_name}")
        print(f"{'='*40}")
        if not task_func():
            print(f"⚠️ {task_name} 失败，继续下一个任务")
        print()

    print("🎉 本存档所有任务完成")
    return True


def run_all_saves(save_numbers):
    """按顺序处理多个存档"""
    # 全程只校准一次（登录界面 start_game.png 可见）
    print("正在校准缩放比例...")
    if not calibrate_scale("start_game.png"):
        print("⚠️ 校准失败，将使用多尺度兜底匹配")
    print()
    
    for num in save_numbers:
        print(f"\n{'#'*50}")
        print(f"# 开始处理存档 {num}")
        print(f"{'#'*50}\n")

        # 1. 登录并选存档
        if not login_and_select_save(num):
            print(f"❌ 存档 {num} 登录失败，跳过")
            continue

        # 2. 执行全部日常任务
        run_single_save_tasks()

        # 3. 返回登录界面
        print(f"\n--- 存档 {num} 完成，返回登录界面 ---")
        if not wait_and_click("back_to_login.png", timeout=10, desc="返回登录界面"):
            print(f"❌ 无法返回登录界面，脚本终止")
            break
        time.sleep(3)


if __name__ == "__main__":
    print("5秒后开始，请确保游戏处于登录界面...")
    run_all_saves([1, 2])   # 先做存档1和2