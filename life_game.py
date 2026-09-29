#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
浮生录 (Lifepath) · 命令行文字人生模拟器（文明五大纪元 · 从华夏溯源到星海跃迁）
支持自主选择或随机投掷到【先秦汉唐】【宋韵明清】【近代破晓】【当代腾飞】【未来星海】，
出生年份在纪元区间内全域随机、出生月份随机；一生随年代推移自动切换时代背景与事件池。
构思了常温超导、聚变能源、脑机接口、碳配额、地月轨道、小行星采矿与数字永生等未来社会演进路径。
标准库零依赖，沉浸式体验大时代下的小人物史诗。
"""

import sys
import time
import os
import random
import json

# ANSI 颜色与高亮排版
class Color:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    
    BG_DARK = "\033[48;5;235m"
    GOLD = "\033[38;5;220m"
    PURPLE = "\033[38;5;141m"
    GRAY = "\033[38;5;244m"

def slow_print(text, delay=0.012, newline=True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# 纪元内容数据层（由 tools/build_epochs_data_py.py 生成，见 fsl_epochs.py）
from fsl_epochs import *  # noqa: F401,F403


class Player:
    def __init__(self, name, epoch_mode, birth_year, origin, trait, gender="male"):
        self.name = name
        self.gender = gender
        self.epoch_mode = epoch_mode
        self.birth_year = birth_year
        self.origin = origin
        self.trait = trait
        self.age = 0
        
        o_stat = origin["stat"]
        t_mod = trait["mod"]
        
        self.health = o_stat.get("health", 85) + t_mod.get("health", 0) + random.randint(-4, 4)
        self.wealth = round(o_stat.get("wealth", 2.0) + t_mod.get("wealth", 0) + random.uniform(-0.5, 0.5), 1)
        self.intellect = o_stat.get("intellect", 50) + t_mod.get("intellect", 0) + random.randint(-3, 3)
        self.happiness = o_stat.get("happiness", 60) + t_mod.get("happiness", 0)
        self.luck = o_stat.get("luck", 50) + t_mod.get("luck", 0) + random.randint(-6, 6)
        self.reputation = o_stat.get("rep", 40)
        
        self.tags = [origin["trait"], trait["name"], "巾帼女史" if gender == "female" else "须眉男儿"]
        self.history = []
        self.key_choices = []
        self.random_events = []
        self.family = initialize_family(self)
        self.family_logs = []
        self.is_dead = False
        self.death_reason = ""
        self.career_track = "探索未定"
        self.social_rank = "风雨布衣"
        self.track_scores = {"体制政务": 0, "商海实业": 0, "学术科技": 0, "文艺江湖": 0, "守拙布衣": 0}

    def show_dashboard(self, stage_idx, total_stages):
        clear_screen()
        curr_year = self.birth_year + self.age
        era_title, era_desc = resolve_era_details(curr_year, self.epoch_mode)
        g_symbol = "女 ♀" if self.gender == "female" else "男 ♂"

        print(f"{Color.GOLD}{'='*68}{Color.RESET}")
        print(f" {Color.BOLD}{self.name}{Color.RESET} ({g_symbol}) · {curr_year} 年 ({self.age} 岁) | 轨迹: {Color.CYAN}{self.career_track} · {self.social_rank}{Color.RESET} | 至亲: {Color.GREEN}{format_family_status(self)}{Color.RESET} | 进度 [{stage_idx}/{total_stages}]")
        print(f" 时代背景: {Color.YELLOW}{era_title}{Color.RESET} · {Color.GRAY}{era_desc}{Color.RESET}")
        print(f"{Color.GOLD}{'-'*68}{Color.RESET}")
        print(f" [健康]: {int(self.health):<3}♥  |  [财富]: {self.wealth:.1f} {wealth_unit(self.epoch_mode):<4}  |  [智识]: {int(self.intellect):<3}✦  |  [心安]: {int(self.happiness):<3}☼  |  [气运]: {int(self.luck):<3}🎲")
        print(f"{Color.GOLD}{'='*68}{Color.RESET}\n")


def initialize_family(player):
    era_id = player.epoch_mode
    father_birth = player.birth_year - random.randint(20, 30)
    mother_birth = player.birth_year - random.randint(18, 26)
    father_name = pick_epoch_name(era_id, "male")
    mother_name = pick_epoch_name(era_id, "female")
    return {
        "father": {"role": "父亲", "name": father_name, "birth_year": father_birth, "death_year": None, "alive": True},
        "mother": {"role": "母亲", "name": mother_name, "birth_year": mother_birth, "death_year": None, "alive": True},
        "spouse": None,
        "children": [],
        "grandchildren_count": 0,
    }


def get_era_life_expectancy(year):
    if year < 1912:
        return 58
    if year < 1978:
        return 68
    if year < 2035:
        return 80
    return 98


def advance_family(player, stage_age, current_year):
    if not hasattr(player, "family") or not player.family:
        player.family = initialize_family(player)
    fam = player.family
    expectancy = get_era_life_expectancy(current_year)
    logs = []

    # 1. 父母寿夭推演
    for k in ("father", "mother"):
        parent = fam[k]
        if parent["alive"]:
            p_age = current_year - parent["birth_year"]
            risk = 0.35 if p_age >= expectancy else (0.12 if p_age >= 52 else 0.02)
            if random.random() < risk:
                parent["alive"] = False
                parent["death_year"] = current_year
                player.happiness = max(10, player.happiness - 12)
                msg = f"{parent['role']}【{parent['name']}】于 {p_age} 岁寿终长逝，你抚棺尽哀"
                player.family_logs.append(msg)
                logs.append(msg)
                player.tags.append("承重失怙" if k == "father" else "萱堂日落")

    # 2. 婚配成家 (18 - 36 岁)
    if not fam["spouse"] and 18 <= stage_age <= 36:
        base_p = 0.48 if 21 <= stage_age <= 30 else 0.25
        w_factor = 0.15 if player.wealth >= 3.0 else (-0.15 if player.wealth < 0 else 0)
        if random.random() < (base_p + w_factor):
            spouse_gender = "male" if player.gender == "female" else "female"
            spouse_name = pick_epoch_name(player.epoch_mode, spouse_gender)
            spouse_role = "丈夫" if player.gender == "female" else "妻子"
            fam["spouse"] = {
                "role": spouse_role,
                "name": spouse_name,
                "gender": spouse_gender,
                "birth_year": current_year - random.randint(stage_age - 3, stage_age + 2),
                "married_year": current_year,
                "married_age": stage_age,
                "death_year": None,
                "alive": True,
            }
            player.happiness = min(100, player.happiness + 12)
            msg = f"与【{spouse_name}】缔结良缘，结为夫妻，风雨同舟"
            player.family_logs.append(msg)
            logs.append(msg)
            player.tags.append("结发齐心")

    # 3. 伴侣寿夭
    if fam["spouse"] and fam["spouse"]["alive"]:
        s_age = current_year - fam["spouse"]["birth_year"]
        if s_age >= expectancy and random.random() < 0.20:
            fam["spouse"]["alive"] = False
            fam["spouse"]["death_year"] = current_year
            player.happiness = max(10, player.happiness - 16)
            msg = f"结发{fam['spouse']['role']}【{fam['spouse']['name']}】相伴多年后撒手人寰，独对残灯"
            player.family_logs.append(msg)
            logs.append(msg)
            player.tags.append("悼亡孤影")

    # 4. 生儿育女 (19 - 42 岁)
    if fam["spouse"] and fam["spouse"]["alive"] and 19 <= stage_age <= 42 and len(fam["children"]) < 4:
        b_prob = 0.60 if len(fam["children"]) == 0 else (0.45 if len(fam["children"]) == 1 else 0.25)
        if random.random() < b_prob:
            child_gender = "female" if random.random() < 0.5 else "male"
            child_name = pick_epoch_name(player.epoch_mode, child_gender)
            ordinals = ["长", "次", "三", "四"]
            role_name = f"{ordinals[len(fam['children'])]}{'女' if child_gender == 'female' else '子'}"
            fam["children"].append({
                "role": role_name,
                "name": child_name,
                "gender": child_gender,
                "birth_year": current_year,
                "birth_age": stage_age,
            })
            player.happiness = min(100, player.happiness + 8)
            cost = 1.0 if is_future_epoch(player.epoch_mode) else (0.3 if player.epoch_mode == "ancient" else 0.8)
            player.wealth = round(max(-10.0, player.wealth - cost), 1)
            msg = f"家门添丁，喜得{role_name}【{child_name}】，满堂笑语"
            player.family_logs.append(msg)
            logs.append(msg)
            if len(fam["children"]) == 1:
                player.tags.append("承欢膝下")

    # 5. 孙辈成群
    if stage_age >= 56 and fam["children"] and fam["grandchildren_count"] == 0:
        fam["grandchildren_count"] = random.randint(1, 3) + len(fam["children"])
        player.happiness = min(100, player.happiness + 6)
        msg = f"儿女各自自立，膝下增添孙辈，门楣香火蔚然"
        player.family_logs.append(msg)
        logs.append(msg)
        player.tags.append("儿孙绕膝")

    return logs


def format_family_status(player):
    if not hasattr(player, "family") or not player.family:
        return "父母膝下"
    fam = player.family
    parts = []
    if fam["spouse"]:
        parts.append(f"{fam['spouse']['role']}:{fam['spouse']['name']}{'' if fam['spouse']['alive'] else '(故)'}")
    else:
        alive_cnt = (1 if fam["father"]["alive"] else 0) + (1 if fam["mother"]["alive"] else 0)
        if alive_cnt == 2:
            parts.append("双亲健在")
        elif alive_cnt == 1:
            parts.append("独亲在堂")
        else:
            parts.append("孑然自立")
    if fam["children"]:
        parts.append(f"{len(fam['children'])}子嗣")
    return " · ".join(parts)


def pick_stage_event(era_id, stage_idx, gender="male"):
    pools_now = get_stage_pools(era_id)
    pool = list(pools_now[stage_idx])
    women_events = WOMEN_EVENT_POOLS.get(era_id, {}).get(stage_idx, [])
    if gender == "female" and women_events:
        male_coded = ("科举", "进士", "举人", "为吏", "出仕", "功名", "投军", "从军", "入伍", "兵营", "察举", "太学", "东宫")
        candidates = []
        for ev in pool:
            w = 1.0
            nar = ev.get("narrative", "")
            title = ev.get("title", "")
            if is_classical_epoch(era_id) and any(k in title or k in nar for k in male_coded):
                w = 0.25
            candidates.append((ev, w))
        for wev in women_events:
            candidates.append((wev, 2.6))
        total_w = sum(w for _, w in candidates)
        r = random.uniform(0, total_w)
        for ev, w in candidates:
            r -= w
            if r <= 0:
                return ev
        return candidates[0][0]
    return random.choice(pool)

# 过去纪元 16 大关卡

LIFE_STAGE_BRACKETS = [
    {"id": 0, "min_age": 5, "max_age": 7, "period": "幼年启蒙"},
    {"id": 1, "min_age": 9, "max_age": 11, "period": "童年韶光"},
    {"id": 2, "min_age": 14, "max_age": 16, "period": "少年分流"},
    {"id": 3, "min_age": 17, "max_age": 19, "period": "成人立志"},
    {"id": 4, "min_age": 20, "max_age": 22, "period": "青春韶华"},
    {"id": 5, "min_age": 23, "max_age": 25, "period": "初涉人世"},
    {"id": 6, "min_age": 26, "max_age": 29, "period": "成家立业"},
    {"id": 7, "min_age": 30, "max_age": 33, "period": "三十而立"},
    {"id": 8, "min_age": 34, "max_age": 38, "period": "负重前行"},
    {"id": 9, "min_age": 39, "max_age": 42, "period": "中年险滩"},
    {"id": 10, "min_age": 43, "max_age": 47, "period": "动荡考验"},
    {"id": 11, "min_age": 49, "max_age": 53, "period": "知命之年"},
    {"id": 12, "min_age": 56, "max_age": 61, "period": "花甲在望"},
    {"id": 13, "min_age": 64, "max_age": 69, "period": "桑榆晚景"},
    {"id": 14, "min_age": 72, "max_age": 76, "period": "古稀沧桑"},
    {"id": 15, "min_age": 78, "max_age": 83, "period": "夕阳辞章"}
]

def generate_random_timeline():
    timeline = []
    prev_age = 0
    for b in LIFE_STAGE_BRACKETS:
        min_v = max(prev_age + 1, b["min_age"])
        max_v = max(min_v, b["max_age"])
        assigned = random.randint(min_v, max_v)
        timeline.append(assigned)
        prev_age = assigned
    return timeline

SAVE_FILE = ".fushenglu_save.json"
RECORDS_FILE = ".fushenglu_records.json"


def save_game_state(player, stage_idx, timeline):
    if not player or player.is_dead:
        if os.path.exists(SAVE_FILE):
            try:
                os.remove(SAVE_FILE)
            except Exception:
                pass
        return
    state = {
        "version": 1,
        "stage_idx": stage_idx,
        "timeline": timeline,
        "player": {
            "name": player.name,
            "gender": getattr(player, "gender", "male"),
            "epoch_mode": player.epoch_mode,
            "birth_year": player.birth_year,
            "birth_month": getattr(player, "birth_month", 1),
            "origin": player.origin,
            "trait": player.trait,
            "age": player.age,
            "health": player.health,
            "wealth": player.wealth,
            "intellect": player.intellect,
            "happiness": player.happiness,
            "luck": player.luck,
            "reputation": player.reputation,
            "tags": player.tags,
            "history": player.history,
            "key_choices": player.key_choices,
            "random_events": player.random_events,
            "family": getattr(player, "family", None),
            "family_logs": getattr(player, "family_logs", []),
            "career_track": player.career_track,
            "social_rank": player.social_rank,
            "track_scores": player.track_scores,
        }
    }
    try:
        with open(SAVE_FILE, "w", encoding="utf-8") as f:
            json.dump(state, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def load_game_state():
    if not os.path.exists(SAVE_FILE):
        return None
    try:
        with open(SAVE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def record_to_hall_of_fame(player, archetype, epitaph):
    records = []
    if os.path.exists(RECORDS_FILE):
        try:
            with open(RECORDS_FILE, "r", encoding="utf-8") as f:
                records = json.load(f)
        except Exception:
            records = []
    end_year = player.birth_year + player.age
    rec = {
        "name": player.name,
        "gender": getattr(player, "gender", "male"),
        "epoch_mode": player.epoch_mode,
        "birth_year": player.birth_year,
        "end_year": end_year,
        "age": player.age,
        "archetype": archetype,
        "epitaph": epitaph,
        "career_track": player.career_track,
        "social_rank": player.social_rank,
        "wealth": player.wealth,
        "wealth_unit": wealth_unit(player.epoch_mode),
        "happiness": int(player.happiness),
        "intellect": int(player.intellect),
        "luck": int(player.luck),
        "family_summary": format_family_status(player),
        "date": time.strftime("%Y-%m-%d %H:%M")
    }
    records.insert(0, rec)
    records = records[:50]
    try:
        with open(RECORDS_FILE, "w", encoding="utf-8") as f:
            json.dump(records, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def view_hall_of_fame():
    clear_screen()
    print(f"{Color.GOLD}{'='*68}{Color.RESET}")
    print(f"{Color.BOLD}{Color.GOLD}    🏛️  万 世 祠  ·  百 世 轮 回 功 业 谱{Color.RESET}")
    print(f"{Color.GOLD}{'='*68}{Color.RESET}\n")
    if not os.path.exists(RECORDS_FILE):
        print(f" {Color.GRAY}尚无立传先烈。请先进入人世，完成一轮完整的浮生轮回。{Color.RESET}\n")
    else:
        try:
            with open(RECORDS_FILE, "r", encoding="utf-8") as f:
                records = json.load(f)
        except Exception:
            records = []
        if not records:
            print(f" {Color.GRAY}祠堂寂寂，尚无英名。{Color.RESET}\n")
        else:
            print(f" {Color.CYAN}已收录 {len(records)} 世凡尘功业长卷：{Color.RESET}\n")
            for idx, r in enumerate(records, 1):
                cfg = get_epoch_config(r["epoch_mode"])
                g_str = "女 ♀" if r.get("gender") == "female" else "男 ♂"
                print(f"  {Color.YELLOW}{idx}. {r['name']}{Color.RESET} ({g_str}) | {cfg['icon']} {cfg['name']} ({r['birth_year']} - {r['end_year']} · {r['age']}岁)")
                print(f"     称号: {Color.BOLD}《{r['archetype']}》{Color.RESET} | 位阶: {r['career_track']} · {r['social_rank']}")
                print(f"     铭文: {Color.GRAY}“{r['epitaph']}”{Color.RESET}")
                print(f"     至亲: {Color.GREEN}{r.get('family_summary', '自立一人')}{Color.RESET} | 财富: {r['wealth']} {r['wealth_unit']}\n")
    input(f"{Color.GOLD}按回车返回时代大门...{Color.RESET}")


def main():
    clear_screen()
    print(f"{Color.GOLD}{'='*68}{Color.RESET}")
    print(f"{Color.BOLD}{Color.GOLD}    浮 生 录  ·  过 去 与 未 来 浪 潮 模 拟 器 (全 卷 纪 传 版){Color.RESET}")
    print(f"{Color.GOLD}{'='*68}{Color.RESET}")
    slow_print(" 一个人的命运，既要靠自我的奋斗，亦要看历史的进程。\n 时代洪流呼啸而过，偶发的幸与不幸如影随形。细水长流，步步为营，落子无悔。\n", 0.012)

    # 检查是否有未结束的即时存档
    save_data = load_game_state()
    if save_data and save_data.get("player") and not save_data["player"].get("is_dead"):
        sp = save_data["player"]
        s_cfg = get_epoch_config(sp["epoch_mode"])
        s_gender = "女 ♀" if sp.get("gender") == "female" else "男 ♂"
        print(f"{Color.GREEN}【 ⏳ 发现未竟之途 】检测到上一世存档：{sp['name']} ({s_gender}) · {s_cfg['name']} · {sp['age']}岁{Color.RESET}")
        res_choice = input(f"{Color.GOLD}按 c 继续上一世，或按回车开启全新轮回: {Color.RESET}").strip().lower()
        if res_choice == 'c':
            player = Player(sp["name"], sp["epoch_mode"], sp["birth_year"], sp["origin"], sp["trait"], gender=sp.get("gender", "male"))
            for k, v in sp.items():
                setattr(player, k, v)
            start_stage = save_data.get("stage_idx", 1) + 1
            timeline = save_data.get("timeline", generate_random_timeline())
            total_stages = 16
            run_game_loop(player, start_stage, total_stages, timeline)
            return

    # 纪元模式选择
    while True:
        clear_screen()
        print(f"{Color.GOLD}{'='*68}{Color.RESET}")
        print(f"{Color.BOLD}{Color.GOLD}    浮 生 录  ·  入 世 纪 元 选 择{Color.RESET}")
        print(f"{Color.GOLD}{'='*68}{Color.RESET}")
        print(f"{Color.CYAN}【 请选择入世时代纪元 】{Color.RESET}")
        print(f"  {Color.GRAY}文明长河自公元前1600年奔涌至公元2150年，皆可投胎；一生将随年代推移自动切换时代背景。{Color.RESET}")
        for idx_e, e in enumerate(EPOCHS, 1):
            print(f"  {idx_e}. {e['icon']} {e['name']} ({e['sub_title']}) · {e['badge']}")
        print(f"  {len(EPOCHS) + 1}. 完全随机天命 (由命运的骰子决定你降生于哪一个大时代)")
        print(f"  {len(EPOCHS) + 2}. 🏛️ 步入万世祠 (查阅百世轮回长卷与历史功业)")

        e_choice = input(f"\n{Color.GOLD}请选择 [1-{len(EPOCHS) + 2}, 默认 {len(EPOCHS) + 1}]: {Color.RESET}").strip()
        if e_choice == str(len(EPOCHS) + 2):
            view_hall_of_fame()
            continue
        if e_choice.isdigit() and 1 <= int(e_choice) <= len(EPOCHS):
            epoch_mode = EPOCHS[int(e_choice) - 1]["id"]
            break
        if e_choice in ("", "random") or e_choice == str(len(EPOCHS) + 1):
            epoch_mode = random.choice(EPOCHS)["id"]
            cfg_r = get_epoch_config(epoch_mode)
            print(f"{Color.PURPLE}🎲 天命掷骰！你被投放到了：{cfg_r['icon']}【{cfg_r['name']}】{Color.RESET}")
            break
        matched = [e for e in EPOCHS if e["id"] == e_choice]
        if matched:
            epoch_mode = matched[0]["id"]
            break
        print(f"{Color.RED}输入无效，请重新选择。{Color.RESET}")

    cfg_now = get_epoch_config(epoch_mode)
    while True:
        b_year, b_month, gender, origin, trait = generate_random_destiny(epoch_mode)
        era_title, era_desc = resolve_era(b_year)
        g_text = "女 ♀" if gender == "female" else "男 ♂"
        g_color = Color.MAGENTA if gender == "female" else Color.CYAN

        print(f"\n{Color.CYAN}【 🎲 先天命格卡 · 随机摇号投胎 】{Color.RESET}")
        print(f"  纪元属性: {Color.BOLD}{cfg_now['icon']} {cfg_now['name']} ({cfg_now['sub_title']}){Color.RESET}")
        print(f"  先天性别: {Color.BOLD}{g_color}{g_text}{Color.RESET}")
        print(f"  出生年代: {Color.YELLOW}{format_year_month(b_year, b_month)} · {era_title}{Color.RESET}")
        print(f"  时代缩影: {Color.GRAY}{era_desc}{Color.RESET}")
        print(f"  出生家庭: {Color.BOLD}{origin['title']}{Color.RESET}")
        print(f"  门第机缘: {origin['desc']}")
        print(f"  先天特质: {Color.PURPLE}[{trait['name']}] - {trait['desc']}{Color.RESET}\n")

        cmd = input(f"{Color.GOLD}按回车接受此命格进入人间，或输入 r 重新摇号投胎: {Color.RESET}").strip().lower()
        if cmd != 'r':
            break
        print(f"\n{Color.GRAY}重新祈求天命...{Color.RESET}\n")
        time.sleep(0.05)

    name = input(f"\n{Color.CYAN}请输入入世姓名 (留空随机): {Color.RESET}").strip()
    if not name:
        name = pick_epoch_name(epoch_mode, gender)

    player = Player(name, epoch_mode, b_year, origin, trait, gender=gender)
    player.birth_month = b_month
    total_stages = 16
    timeline = generate_random_timeline()

    slow_print(f"\n命运之轮缓缓启动，{player.name} ({g_text}) 踏入了 {format_year_month(player.birth_year, getattr(player, 'birth_month', 1))} 的人间...\n", 0.02)
    time.sleep(0.05)

    run_game_loop(player, 1, total_stages, timeline)


def run_game_loop(player, start_stage, total_stages, timeline):
    # 游戏主轮次
    for idx_stage in range(start_stage, total_stages + 1):
        if player.health <= 12:
            player.death_reason = "积劳成疾，在时代长风中过早抱憾离世"
            break

        player.age = timeline[idx_stage - 1]
        curr_year = player.birth_year + player.age
        # 以“该阶段实际所处的年代”决定取自哪个纪元的事件池，
        # 因此一个横跨数十乃至数百年的生命会自然经历古代 -> 近世 -> 当代 -> 未来的切换。
        era_id = get_epoch_id_for_year(curr_year)
        stage = pick_stage_event(era_id, idx_stage - 1, player.gender)
        player.show_dashboard(idx_stage, total_stages)

        # 家族亲情推演
        fam_logs = advance_family(player, player.age, curr_year)
        if fam_logs:
            for fl in fam_logs:
                print(f"{Color.GREEN}【🏡 至亲时序】{fl}{Color.RESET}")
            print()

        # 突发强随机事件（按年代选择历史/未来事件库）
        rand_pool = FUTURE_RANDOM_EVENTS if is_future_epoch(era_id) else PAST_RANDOM_EVENTS
        if random.random() < 0.32:
            re = random.choice(rand_pool)
            print(f"{Color.PURPLE}【 🎲 命运无常 · 偶发事件 】{re['title']}{Color.RESET}")
            print(f"  {Color.GRAY}{re['desc']}{Color.RESET}")
            
            eff = re["effect"]
            player.wealth = round(player.wealth + eff.get("wealth", 0), 1)
            player.health = max(10, min(100, player.health + eff.get("health", 0)))
            player.happiness = max(10, min(100, player.happiness + eff.get("happiness", 0)))
            player.intellect = max(20, min(100, player.intellect + eff.get("intellect", 0)))
            player.luck = max(10, min(100, player.luck + eff.get("luck", 0)))
            player.random_events.append((curr_year, player.age, re["title"]))
            time.sleep(0.05)

        print(f"{Color.BOLD}{Color.YELLOW}【{curr_year}年 · {stage['title']}】{Color.RESET}")
        print(f"{Color.WHITE}{stage['narrative']}{Color.RESET}\n")

        print(f"{Color.CYAN}面临抉择：{Color.RESET}")
        for idx, c in enumerate(stage["choices"], 1):
            chance = c["calc_chance"](player)
            badge = f"{Color.GREEN}[稳妥必成]{Color.RESET}" if chance >= 100 else f"{Color.YELLOW}[成功率约 {chance}%]{Color.RESET}"
            print(f"  {idx}. {c['text']}  {badge} ({c['risk_label']})")

        while True:
            c_input = input(f"\n{Color.GOLD}请选择 [1-{len(stage['choices'])}]: {Color.RESET}").strip()
            if c_input.isdigit() and 1 <= int(c_input) <= len(stage["choices"]):
                chosen_idx = int(c_input) - 1
                break
            print(f"{Color.RED}输入无效，请重新选择。{Color.RESET}")

        chosen = stage["choices"][chosen_idx]
        chance = chosen["calc_chance"](player)
        roll = random.randint(1, 100)
        is_success = roll <= chance

        if is_success:
            eff = chosen.get("succ_eff", {})
            fb = chosen.get("succ_feedback", "")
            tag = chosen.get("tag_succ", "")
        else:
            eff = chosen.get("fail_eff", {})
            fb = chosen.get("fail_feedback", "")
            tag = chosen.get("tag_fail", "")

        player.health = max(0, min(100, player.health + eff.get("health", 0)))
        player.wealth = round(player.wealth + eff.get("wealth", 0), 1)
        player.intellect = max(0, min(100, player.intellect + eff.get("intellect", 0)))
        player.happiness = max(0, min(100, player.happiness + eff.get("happiness", 0)))
        player.luck = max(0, min(100, player.luck + eff.get("luck", 0)))
        player.reputation = max(0, min(100, player.reputation + eff.get("rep", 0)))

        if tag and tag not in player.tags:
            player.tags.append(tag)

        record = {
            "year": curr_year,
            "age": player.age,
            "title": stage["title"],
            "choice_text": chosen["text"],
            "is_success": is_success,
            "roll": roll,
            "chance": chance,
            "feedback": fb,
            "is_key": chosen.get("is_key", False)
        }
        player.history.append(record)
        # 实时动态轨迹演进研判
        ch_text = (chosen['text'] + " " + chosen.get('tag_succ', '') + " " + chosen.get('tag_fail', '')).lower()
        if any(w in ch_text for w in ["考编", "公务员", "体制", "军旅", "入伍", "纪检", "行政", "公职", "团长", "协调官", "防御", "上岸", "保供", "科举", "功名", "为吏", "衙门", "官场", "朝廷", "仕途", "幕僚", "举人", "进士", "孝廉", "征辟", "辟召", "刺史", "太守", "县令", "士大夫", "戍边", "烽燧", "投军", "从军", "行伍", "参军", "支前", "干部", "大队", "公社", "革委会", "编制", "出仕", "差役", "里正", "保长", "粮长", "驿丞", "公文", "文书", "官"]):
            player.track_scores["体制政务"] += 4
        elif any(w in ch_text for w in ["经商", "淘宝", "电商", "创业", "个体户", "操盘", "股市", "商海", "小行星", "矿业", "水务", "买房", "信托", "首富", "红利", "商号", "票号", "盐铁", "牙行", "市舶", "货殖", "贩运", "商队", "胡商", "绸缎", "茶马", "当铺", "钱庄", "作坊", "机户", "铺子", "买卖", "田产", "织造", "十三行", "合伙", "开厂", "车间", "技术员", "承包", "学徒", "柜上", "行商", "验货", "记账", "货价", "借贷", "告贷", "典当", "田契", "田亩", "租佃", "钱粮", "贩货", "营生"]):
            player.track_scores["商海实业"] += 4
        elif any(w in ch_text for w in ["无线电", "实验室", "论文", "科研", "工程师", "算法", "智脑", "黑客", "聚变", "脑机", "量子", "质子", "核能", "读书", "经书", "竹简", "著述", "治学", "书院", "私塾", "蒙学", "游学", "太学", "拜师", "医术", "本草", "郎中", "针灸", "算学", "历法", "图纸", "夜校", "师范", "学堂", "抄书", "苦读", "灯油", "方剂", "匠作", "营造", "先生", "游历", "问道"]):
            player.track_scores["学术科技"] += 4
        elif any(w in ch_text for w in ["乐队", "摇滚", "武侠", "自由", "海岛", "江湖", "茶楼", "房车", "诗社", "民宿", "艺术", "写诗", "诗词", "书画", "琴", "社戏", "游侠", "隐逸", "归隐", "山水", "田园", "寺院", "清谈", "雅集", "杂剧", "刻书", "藏书", "戏班", "票友", "诗酒", "雅集", "田园", "寺院", "归隐", "诗书", "游历", "闲云"]):
            player.track_scores["文艺江湖"] += 4
        else:
            player.track_scores["守拙布衣"] += 1

        best_t = max(player.track_scores, key=player.track_scores.get)
        player.career_track = best_t

        if player.reputation >= 70 and player.wealth >= 18:
            player.social_rank = "时代领军巨擘"
        elif player.reputation >= 60:
            player.social_rank = "德高望重栋梁"
        elif player.wealth >= 25:
            player.social_rank = "殷实一方富户"
        elif player.wealth >= 5:
            player.social_rank = "小康体面人家"
        else:
            player.social_rank = "风雨坚韧布衣"

        if chosen.get("is_key"):
            player.key_choices.append(record)

        if chance < 100:
            print(f"\n{Color.PURPLE}🎲 命运掷骰：出目 {roll} / 胜率基线 {chance}%  ➔  {'★ 顺遂如愿' if is_success else '✕ 天不遂人'}{Color.RESET}")
        print(f"{Color.GREEN}抉择回响：{Color.RESET}{fb}")

        save_game_state(player, idx_stage, timeline)

        input(f"\n{Color.GRAY}按回车继续步入岁月下一程...{Color.RESET}")
        time.sleep(0.05)

    if not player.death_reason:
        player.death_reason = "寿终正寝，在安详与温情中平静合眼"

    render_terminal_ending(player)

def render_terminal_ending(player):
    clear_screen()
    end_year = player.birth_year + player.age
    print(f"\n{Color.GOLD}{'='*68}{Color.RESET}")
    print(f"{Color.BOLD}{Color.GOLD}    《 浮 生 录 · 人 物 一 生 长 卷 纪 传 与 时 代 回 响 》{Color.RESET}")
    print(f"{Color.GOLD}{'='*68}{Color.RESET}\n")

    _bmonth = getattr(player, "birth_month", 1)
    _cfg = get_epoch_config(player.epoch_mode)
    g_str = '女 ♀' if getattr(player, 'gender', 'male') == 'female' else '男 ♂'
    print(f" 主角姓名: {Color.BOLD}{player.name}{Color.RESET} ({g_str} · {format_year_month(player.birth_year, _bmonth)} - {format_year_only(end_year)} · 享年 {player.age} 岁)")
    print(f" 时代纪元: {_cfg['icon']}【{_cfg['name']}】({_cfg['sub_title']})")
    print(f" 出生家庭: {player.origin['title']}")
    print(f" 离世归宿: {player.death_reason}")

    print(f"\n{Color.CYAN}【 终生数据结算 】{Color.RESET}")
    print(f"  生命健康值 : {int(player.health)} / 100")
    print(f"  积累财富净值: {player.wealth:.1f} {wealth_unit(player.epoch_mode)}")
    print(f"  学识心智值 : {int(player.intellect)} / 100")
    print(f"  心境安宁度 : {int(player.happiness)} / 100")
    print(f"  终生天命气运: {int(player.luck)} / 100")

    print(f"\n{Color.CYAN}【 人生印记标签 】{Color.RESET}")
    print("  " + "  ".join([f"{Color.BG_DARK}#{t}{Color.RESET}" for t in player.tags]))

    is_future = is_future_epoch(player.epoch_mode)
    is_classical = is_classical_epoch(player.epoch_mode)
    if is_future:
        if player.wealth >= 45 and player.happiness >= 55:
            archetype = "星海拓荒巨擘 · 载誉深空"
            epitaph = "你从人造穹顶起步，乘上了人类迈向星海的巍峨巨舰。在引力与虚空中纵横开阖，无愧为宇宙的孩子。"
        elif player.wealth >= 25 and player.happiness < 45:
            archetype = "赛博齿轮 · 冰冷义体攀登者"
            epitaph = "你在代码洪流与钛合金内脏间奔波一生，换来了令人艳羡的算力与配额，却在深夜怀念母亲曾哼唱过的古老摇篮曲。"
        elif player.happiness >= 70 and player.wealth < 25:
            archetype = "纯粹碳基散人 · 地表哲人"
            epitaph = "世人争先恐后抛弃肉身飞升云端，唯有你深情守望脚下的每一寸泥土。虽无万贯算力，胸中自有一整座真实星汉。"
        elif player.intellect >= 80:
            archetype = "文明先知 · 灵境守望者"
            epitaph = "你以澄澈的智识看穿了技术膨胀与人性异化的迷局，在冷酷的代码矩阵中，为人类守护住了最后一丝温热的诗意。"
        elif player.age < 50:
            archetype = "星轨流星 · 破晓之光"
            epitaph = "你在异星极端风暴中疾驰，生命璀璨夺目如超新星爆发。深空寂静，而你的火种早已照亮了母星的天平。"
        else:
            archetype = "星尘守夜人 · 凡人的尊严"
            epitaph = "既没有成为神话般的星际领主，亦未沦为算法的附庸。守住爱人，守护家人，堂堂正正走完了属于人的壮丽一生。"
    else:
        if is_classical and player.wealth >= 30 and player.reputation >= 60:
            archetype = "名标青史 · 一世风流"
            epitaph = "你的名字被郑重写进了%s，与那个时代的山川人物并列。富贵或已散去，声名却比血肉活得更久。" % _cfg["legacy"]
        elif is_classical and player.wealth >= 15 and player.happiness < 45:
            archetype = "负重跋涉者 · 寒暑苦行"
            epitaph = "你一生都在为一族人的口粮与体面奔波，风霜刻在额角，未曾有一日懈怠，也未曾真正为自己活过。"
        elif is_classical and player.happiness >= 70 and player.wealth < 15:
            archetype = "林泉散人 · 自在一生"
            epitaph = "不慕朱门车马，只爱一壶浊酒、半亩薄田。你以清贫换得心安，是那个时代少数真正自由的人。"
        elif is_classical and player.intellect >= 78:
            archetype = "明哲通达 · 洞观兴替"
            epitaph = "你冷眼看尽王朝更迭与人事翻覆，读懂了兴衰的规律，因而对世人多了一份悲悯与宽恕。"
        elif is_classical and player.age < 50:
            archetype = "断弦流星 · 孤勇悲歌"
            epitaph = "乱世里的性命如风中烛火，你疾行过，灿然过，终是太早熄灭了。山河依旧，只是再无你的消息。"
        elif is_classical:
            archetype = "烟火凡人 · 坚韧一生"
            epitaph = "你没有在史书上留下一行字，却用一粥一饭把血脉与家训传了下去。这本身就是了不起的功业。"
        elif player.wealth >= 45 and player.happiness >= 55:
            archetype = "时代弄潮翁 · 功成身退"
            epitaph = "你乘上了历史最激荡的风帆，饱览过财富的壮阔，亦未曾迷失于物欲的深壑。行过大江大河，落子无悔。"
        elif player.wealth >= 25 and player.happiness < 45:
            archetype = "负重攀登者 · 时代苦行僧"
            epitaph = "在狂飙的城市化与债务大山中，你用肩膀扛起了几代人的体面与产证，却在深夜加班室里耗尽了青春灵气。"
        elif player.happiness >= 70 and player.wealth < 25:
            archetype = "旷达布衣 · 自在散人"
            epitaph = "世人慌慌张张图碎银几两，而你早早参透了内卷的虚妄。向青山借得满怀清风，虽无万贯财，胸中自安然。"
        elif player.intellect >= 80:
            archetype = "清醒明哲者 · 孤峰观澜"
            epitaph = "你以澄澈的智识洞穿了时代周期演进的规律，在浮华中冷眼旁观，在下行中从容不迫。懂得了历史，因而深怀悲悯。"
        elif player.age < 50:
            archetype = "断弦流星 · 孤勇悲歌"
            epitaph = "生命这根弦绷得太紧，你在烈火中疾驰，走得太急太烈。人间热闹非凡，而你已悄然化作微尘。"
        else:
            archetype = "人间守望者 · 平凡的伟力"
            epitaph = "没有成为站在风口的神话，亦未沦为时代的叹息。尽职岗位，尽心家庭，平凡而坚韧地走完了真诚的一生。"

    print(f"\n{Color.CYAN}【 宿命评定与墓志铭 】{Color.RESET}")
    print(f"  终极称号: {Color.BOLD}{Color.GOLD}《{archetype}》{Color.RESET}")
    print(f"  墓志铭  : {Color.ITALIC}“{epitaph}”{Color.RESET}")

    print(f"\n{Color.CYAN}【 时代长河坐标 】{Color.RESET}")
    _birth_era = resolve_era(player.birth_year)
    _death_era = resolve_era(end_year)
    _eras = list_eras_between(player.birth_year, end_year)
    print(f"  {player.name}于 {format_year_month(player.birth_year, _bmonth)} 降生于【{player.origin['title']}】。")
    print(f"  出生之时的天下底色是「{_birth_era[0]}」——{_birth_era[1]}")
    print(f"  此后 {player.age} 年间，其一生先后穿越 {len(_eras)} 重大时代：{' → '.join(_eras)}。")
    if _death_era[0] != _birth_era[0]:
        print(f"  辞世之时，世道已是「{_death_era[0]}」——{_death_era[1]}")
    print(f"  {_cfg['desc']}")
    print(f"  大时代每一次翻覆重构，都在这一个普通生命的悲欢离合里，留下了深浅不一的年轮。")

    print(f"\n{Color.CYAN}【 家族谱系与至亲因缘 】{Color.RESET}")
    fam = getattr(player, 'family', None) or initialize_family(player)
    f_age = (fam["father"]["death_year"] - fam["father"]["birth_year"]) if fam["father"]["death_year"] else (end_year - fam["father"]["birth_year"])
    m_age = (fam["mother"]["death_year"] - fam["mother"]["birth_year"]) if fam["mother"]["death_year"] else (end_year - fam["mother"]["birth_year"])
    f_str = f"享年 {f_age} 岁" if fam["father"]["death_year"] else "安享晚年"
    m_str = f"享年 {m_age} 岁" if fam["mother"]["death_year"] else "长寿健在"
    print(f"  父母所出: 慈父【{fam['father']['name']}】({f_str}) · 严母【{fam['mother']['name']}】({m_str})")
    if fam["spouse"]:
        s_age = (fam["spouse"]["death_year"] or end_year) - fam["spouse"]["birth_year"]
        s_dur = (fam["spouse"]["death_year"] or end_year) - fam["spouse"]["married_year"]
        s_str = f"享年 {s_age} 岁仙逝" if fam["spouse"]["death_year"] else "相伴余生"
        print(f"  结发伴侣: 结发{fam['spouse']['role']}【{fam['spouse']['name']}】({fam['spouse']['married_year']}年结缡，相守 {s_dur} 载，{s_str})")
    else:
        print(f"  结发伴侣: 一生未入凡尘婚姻，清修立世，独行天地。")
    if fam["children"]:
        c_str = "、".join([f"{c['role']}【{c['name']}】({c['birth_year']}年生)" for c in fam["children"]])
        if fam["grandchildren_count"]:
            c_str += f"；晚年孙辈成群（约 {fam['grandchildren_count']} 人），香火绵延。"
        print(f"  血脉子嗣: {c_str}")
    else:
        print(f"  血脉子嗣: 膝下未有亲生子嗣，清虚自守。")

    print(f"\n{Color.CYAN}【 生平纪传 · 时代回响长卷 】{Color.RESET}")
    print(f"  {player.name}降生于【{player.origin['title']}】（{format_year_month(player.birth_year, _bmonth)}）。{player.origin.get('flavor', '')}骨子里带着【{player.trait['name']}】的特质。")
    for h in player.history:
        print(f"  · [{h['year']}年 · {h['age']}岁] 在【{h['title']}】的关口，选择“{h['choice_text']}”。{h['feedback']}")
    if player.random_events:
        print(f"  · 途中偶发掷骰：{', '.join([f'{re[1]}岁遭遇【{re[2]}】' for re in player.random_events])}。")
    print(f"  盖棺定论：累积财富净值 {player.wealth:.1f} {wealth_unit(player.epoch_mode)}，心智 {int(player.intellect)}，心安 {int(player.happiness)}，气运 {int(player.luck)}。山川日月知你曾深情走过。")

    print(f"\n{Color.CYAN}【 关键命运分水岭（重要决策与掷骰实录） 】{Color.RESET}")
    for idx, kc in enumerate(player.key_choices, 1):
        chance_str = f"出目 {kc['roll']} / 胜率 {kc['chance']}%" if kc['chance'] < 100 else "确定性契约"
        status_str = f"{Color.GREEN}顺遂{Color.RESET}" if kc['is_success'] else f"{Color.RED}受挫{Color.RESET}"
        print(f"  {idx}. [{kc['year']}年 · {kc['age']}岁] {kc['title']} ({chance_str} ➔ {status_str})")
        print(f"     决策: {Color.YELLOW}{kc['choice_text']}{Color.RESET}")
        print(f"     回响: {Color.GRAY}{kc['feedback']}{Color.RESET}")

    print(f"\n{Color.GOLD}{'='*68}{Color.RESET}")
    print(f"{Color.DIM}大浪淘沙，唯心自守。愿你在人间的每一程都无怨无悔。{Color.RESET}\n")

    record_to_hall_of_fame(player, archetype, epitaph)
    if os.path.exists(SAVE_FILE):
        try:
            os.remove(SAVE_FILE)
        except Exception:
            pass

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n岁月如风，中途隐退。")
