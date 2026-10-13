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
from active import go_to_active
from pet_task import go_to_pet_task
from utils import calibrate_scale

def run_daily_tasks():
    print("🚀 开始执行每日任务\n")

    # 1. 登录并选择存档
   #if not login_and_select_save():
       #print("❌ 登录流程失败，任务终止")
       #return
   #print()

    # 2. 回到主城（只做一次）
    #if not go_to_main_city():
      #  print("❌ 无法回到主城，任务终止")
      #  return
   # print()

    # 登录完成、回到主城后
    print("正在校准缩放比例...")
    calibrate_scale("mystery_shop.png")   # 用"世界"按钮校准，因为它稳定且一直可见

    # 3. 联盟贡献（结束时自己点红叉回主城）
    if not go_to_union():
        print("⚠️ 联盟贡献失败，继续下一个任务")
    print()

    # 4. 神秘商店（结束时自己点红叉回主城）
    if not go_to_mystery_shop():
        print("⚠️ 神秘商店失败，继续下一个任务")
    print()

    # 5. 宠装采集
    if not go_to_pet_collect():
        print("⚠️ 宠装采集失败，继续下一个任务")
    print()

    # 6. 骑装养成
    if not go_to_mount_train():
        print("⚠️ 骑装养成失败，继续下一个任务")
    print()

    # 7. 竞技场
    if not go_to_arena():
        print("⚠️ 竞技场失败，继续下一个任务")
    print()

    # 8. 斗宠大会
    if not go_to_douchong():
        print("⚠️ 斗宠大会失败，继续下一个任务")
    print()

    # 9. 守卫须弥山
    if not go_to_guard():
        print("⚠️ 守卫须弥山失败，继续下一个任务")
    print()

    # 10. 悲鸣冰川系列（枯焰流沙 + 迷雾沮泽）
    if not go_to_glacier():
        print("⚠️ 悲鸣冰川系列失败，继续下一个任务")
    print()

    # 11. 冒险
    if not go_to_adventure():
        print("⚠️ 冒险失败，继续下一个任务")
    print()

    print("🎉 所有日常任务执行完毕")

    # 12. 幽冥血海任务
    if not go_to_xuehai():
        print("⚠️ 幽冥血海任务失败，继续下一个任务")
    print()

    # 13. 宠物任务
    if not go_to_pet_task():
        print("⚠️ 宠物任务失败，继续下一个任务")
    print()

    # 14. 活跃奖励领取
    if not go_to_active():
        print("⚠️ 活跃奖励领取失败，继续下一个任务")
    print()

if __name__ == "__main__":
    print("5秒后开始，请确保游戏处于登录界面（开始游戏按钮可见）...")
    run_daily_tasks()