"""
在基准状态下运行一次，自动生成 config.json 的 base_saves。
使用场景：第一次配置项目时，或游戏 UI 改版后需要重测基准时。
"""
import json
import os
import sys
import time
from utils import capture_full_screen, find_image, BASE_DIR

CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

# 你要测的存档编号（对应 templates/save_X.png）
SAVE_NUMBERS = ["1", "4", "5", "8"]


def generate_base_config():
    print("5秒后开始，请手动停在存档界面...")
    for i in range(5, 0, -1):
        print(f"  倒计时: {i}")
        time.sleep(1)

    screen = capture_full_screen()

    base_saves = {}
    for num in SAVE_NUMBERS:
        pos, conf, _ = find_image(screen, f"save_{num}.png", threshold=0.7)
        if pos:
            base_saves[num] = {"x": pos[0], "y": pos[1]}
            print(f"  ✅ 存档 {num}: ({pos[0]}, {pos[1]}) 相似度 {conf:.2f}")
        else:
            print(f"  ❌ 存档 {num} 匹配失败，跳过")

    if len(base_saves) < 2:
        print("❌ 至少需要匹配到 2 个存档，生成失败")
        return

    # 保留 config.json 里其他字段（如果存在）
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            config = json.load(f)
    else:
        config = {}

    config["base_saves"] = base_saves

    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

    print(f"\n✅ 已生成 {CONFIG_PATH}")
    print(f"   基准数据: {base_saves}")


if __name__ == "__main__":
    generate_base_config()