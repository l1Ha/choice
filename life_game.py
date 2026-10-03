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
        self.epithet = "垂髫稚子" if is_classical_epoch(epoch_mode) else ("基因胚萌" if is_future_epoch(epoch_mode) else "幼学赤子")
        self.values = {"righteousness": 0, "duty": 0}
        self.mindset = "兼济天下 · 铁肩义士"
        self.active_saga = None

    def show_dashboard(self, stage_idx, total_stages):
        clear_screen()
        curr_year = self.birth_year + self.age
        era_title, era_desc = resolve_era_details(curr_year, self.epoch_mode)
        g_symbol = "女 ♀" if self.gender == "female" else "男 ♂"

        print(f"{Color.GOLD}{'='*68}{Color.RESET}")
        print(f" {Color.BOLD}{self.name}{Color.RESET} ({g_symbol}) · {curr_year} 年 ({self.age} 岁) | 尊号: {Color.PURPLE}【{self.epithet}】{Color.RESET} | 至亲: {Color.GREEN}{format_family_status(self)}{Color.RESET} | 进度 [{stage_idx}/{total_stages}]")
        print(f" 时代背景: {Color.YELLOW}{era_title}{Color.RESET} · {Color.GRAY}{era_desc}{Color.RESET}")
        print(f" 历史备考: {Color.YELLOW}{resolve_landmark(curr_year)}{Color.RESET}")
        print(f" 心性境界: {Color.CYAN}【{self.mindset}】{Color.RESET} | 轨迹坐标: {Color.CYAN}{self.career_track} · {self.social_rank}{Color.RESET}" + (f" | 支线: {Color.YELLOW}{self.active_saga['title']} [{self.active_saga['stage']}/{self.active_saga['max_stage']}]{Color.RESET}" if self.active_saga else ""))
        print(f"{Color.GOLD}{'-'*68}{Color.RESET}")
        print(f" [健康]: {int(self.health):<3}♥  |  [财富]: {self.wealth:.1f} {wealth_unit(self.epoch_mode):<4}  |  [智识]: {int(self.intellect):<3}✦  |  [心安]: {int(self.happiness):<3}☼  |  [气运]: {int(self.luck):<3}🎲")
        sc = self.track_scores
        print(f" [赛道罗盘]: {Color.GRAY}体制 {sc['体制政务']} | 商海 {sc['商海实业']} | 学术 {sc['学术科技']} | 文艺 {sc['文艺江湖']} | 守拙 {sc['守拙布衣']}{Color.RESET}")
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


def calculate_fate_bond_modifier(player, choice):
    if not player or not getattr(player, "tags", None) or not choice:
        return 0, []
    total = 0
    reasons = []
    text = (choice.get("text", "") + " " + choice.get("risk_label", "")).lower()

    for tag in player.tags:
        if tag in ("灵光乍现", "博闻强记", "刀笔初成", "深谋远虑", "敏锐嗅觉", "学有渊源"):
            if any(k in text for k in ("书", "考", "学", "官", "案", "法", "算法", "谋", "辨", "计", "文", "算", "策", "文书", "夜校", "科研", "试")):
                total += 7
                reasons.append(f"{tag} +7%")
        elif tag in ("天生神力", "筋骨强健", "不屈不挠", "从戎有功", "弓马娴熟"):
            if any(k in text for k in ("战", "兵", "军", "斗", "山", "逃", "力", "突围", "守卫", "苦力", "涉险", "跋涉", "巡检")):
                total += 7
                reasons.append(f"{tag} +7%")
        elif tag in ("商海通达", "货殖有方", "信誉卓著", "利涉大川", "盘店开坊"):
            if any(k in text for k in ("商", "钱", "货", "盘", "买", "卖", "利", "本", "股", "资", "仓", "市", "账", "店", "铺")):
                total += 7
                reasons.append(f"{tag} +7%")
        elif tag in ("八面玲珑", "厚道人家", "广结善缘", "清心寡欲"):
            if any(k in text for k in ("人", "友", "交", "亲", "邻", "辞", "退", "和", "隐", "朋", "客", "族", "里")):
                total += 6
                reasons.append(f"{tag} +6%")
        elif tag == "结发齐心":
            if any(k in text for k in ("难", "危", "险", "灾", "劫", "渡", "困", "病", "坚守", "风浪", "关口")):
                total += 5
                reasons.append("同舟共济 +5%")
        elif tag in ("承欢膝下", "儿孙绕膝"):
            if any(k in text for k in ("家", "立业", "基业", "长远", "安居", "置产", "护佑", "传承")):
                total += 5
                reasons.append("庇荫后人 +5%")

    if "暗疾缠身" in player.tags or "旧伤难愈" in player.tags:
        if any(k in text for k in ("病", "劳", "累", "险", "耗", "远行", "重任", "严寒", "高压")):
            total -= 6
            reasons.append("旧疾牵绊 -6%")

    total = max(-10, min(15, total))
    return total, reasons


def update_player_values(player, choice, tag):
    if not hasattr(player, "values") or not player.values:
        player.values = {"righteousness": 0, "duty": 0}
    text = (choice.get("text", "") + " " + (tag or "")).lower()

    if any(k in text for k in ("义", "公", "救", "民", "助", "施", "恤", "舍", "正道", "廉", "保全", "仁")):
        player.values["righteousness"] = min(20, player.values["righteousness"] + 2)
    if any(k in text for k in ("利", "商", "钱", "私", "财", "银", "金", "富", "夺", "争", "本钱", "盈余")):
        player.values["righteousness"] = max(-20, player.values["righteousness"] - 2)
    if any(k in text for k in ("出仕", "官", "国", "责", "战", "御", "守", "朝", "公门", "天下", "救亡", "社稷")):
        player.values["duty"] = min(20, player.values["duty"] + 2)
    if any(k in text for k in ("隐", "辞", "退", "诗", "酒", "田园", "自然", "山水", "清心", "避", "忘机", "放歌")):
        player.values["duty"] = max(-20, player.values["duty"] - 2)

    r = player.values["righteousness"]
    d = player.values["duty"]
    if d >= 0 and r >= 0:
        player.mindset = "兼济天下 · 铁肩义士"
    elif d >= 0 and r < 0:
        player.mindset = "经世致用 · 实干能臣"
    elif d < 0 and r >= 0:
        player.mindset = "清虚自守 · 孤芳高士"
    else:
        player.mindset = "陶然忘机 · 市井智者"


def update_player_epithet(player):
    age = player.age
    is_future = is_future_epoch(player.epoch_mode)
    is_classical = is_classical_epoch(player.epoch_mode)
    trk = player.career_track or "守拙布衣"
    rank = player.social_rank or "风雨布衣"
    tags = player.tags or []

    if age < 14:
        player.epithet = "垂髫稚子" if is_classical else ("基因胚萌" if is_future else "幼学赤子")
        return
    if age <= 18:
        player.epithet = "志学秀木" if is_classical else ("初阶算力学徒" if is_future else "意气少年")
        return

    if trk == "体制政务":
        if rank == "时代领军巨擘":
            player.epithet = "经邦宰辅" if is_classical else ("中枢大执政官" if is_future else "治世定鼎者")
        elif rank == "德高望重栋梁":
            player.epithet = "按察重臣" if is_classical else ("防区调度长" if is_future else "中流砥柱")
        else:
            player.epithet = "案头佐吏" if is_classical else ("巡防志愿役" if is_future else "奉公文吏")
    elif trk == "商海实业":
        if rank == "时代领军巨擘":
            player.epithet = "江南陶朱" if is_classical else ("星海矿业大亨" if is_future else "实业泰斗")
        elif rank == "德高望重栋梁":
            player.epithet = "通商巨掌柜" if is_classical else ("轨道工坊东主" if is_future else "商界翘楚")
        else:
            player.epithet = "市井货郎" if is_classical else ("黑市调试匠" if is_future else "行商干员")
    elif trk == "学术科技":
        if any("医" in t for t in tags):
            player.epithet = "杏林国手" if rank == "时代领军巨擘" else "青囊草医"
        elif rank == "时代领军巨擘":
            player.epithet = "百代宗师" if is_classical else ("虚空构筑大宗师" if is_future else "科学先驱")
        elif rank == "德高望重栋梁":
            player.epithet = "书院讲席" if is_classical else ("高阶算法导师" if is_future else "资深技术专家")
        else:
            player.epithet = "笃学文士" if is_classical else ("数据探针技工" if is_future else "求真学子")
    elif trk == "文艺江湖":
        if rank == "时代领军巨擘":
            player.epithet = "绝代游侠" if is_classical else ("赛博浪潮乐圣" if is_future else "时代文化图腾")
        elif rank == "德高望重栋梁":
            player.epithet = "竹林名士" if is_classical else ("自由频段诗人" if is_future else "海内知音")
        else:
            player.epithet = "江湖闲客" if is_classical else ("离线吟游者" if is_future else "随性行者")
    else:
        if age >= 70:
            player.epithet = "德劭乡耆" if is_classical else ("旧地表元老" if is_future else "寿考尊长")
        elif player.happiness >= 75:
            player.epithet = "林泉逸民" if is_classical else ("纯粹碳基隐者" if is_future else "知足安乐翁")
        else:
            player.epithet = "晴耕雨读" if is_classical else ("穹顶寻常客" if is_future else "寻常布衣")


SAGAS_DEF = [
    {"id": "saga_official", "title": "青云之志 · 庙堂沉浮录", "keywords": ("科举", "入仕", "公门", "政务", "官场", "为吏", "行政", "公职", "调任"), "max_stage": 3},
    {"id": "saga_merchant", "title": "陶朱之路 · 四海通商志", "keywords": ("商号", "经商", "买卖", "票号", "创业", "开厂", "货殖", "电商", "盘店"), "max_stage": 3},
    {"id": "saga_healer", "title": "大医精诚 · 悬壶济世篇", "keywords": ("医", "药", "草医", "救护", "接生", "病患", "青囊", "良方"), "max_stage": 3},
    {"id": "saga_wanderer", "title": "天涯长歌 · 快意江湖行", "keywords": ("游历", "江湖", "剑", "诗社", "乐团", "摇滚", "归隐", "浪迹", "放歌"), "max_stage": 3},
    {"id": "saga_star", "title": "九天揽月 · 星海求索录", "keywords": ("深空", "天梯", "电梯", "算力", "超导", "火星", "聚变", "脑机", "戴森"), "max_stage": 3}
]


def check_saga_progress(player, choice, is_success):
    text = (choice.get("text", "") + " " + choice.get("risk_label", "")).lower()

    if not player.active_saga and choice.get("is_key"):
        for sg in SAGAS_DEF:
            if any(k in text for k in sg["keywords"]):
                player.active_saga = {"id": sg["id"], "title": sg["title"], "stage": 1, "max_stage": sg["max_stage"]}
                player.tags.append(f"开启:{sg['title'].split(' · ')[0]}")
                return f"【开启传奇支线】{sg['title']} [1/{sg['max_stage']}]"

    if player.active_saga and is_success and player.active_saga["stage"] < player.active_saga["max_stage"]:
        sg = next((s for s in SAGAS_DEF if s["id"] == player.active_saga["id"]), None)
        if sg and any(k in text for k in sg["keywords"]):
            player.active_saga["stage"] += 1
            if player.active_saga["stage"] >= player.active_saga["max_stage"]:
                player.tags.append(f"功成:{sg['title'].split(' · ')[0]}")
                player.reputation += 10
                player.happiness += 10
                return f"【传奇支线圆满】{sg['title']} 功成名就！(+10声望 +10心安)"
            return f"【传奇支线进展】{sg['title']} [{player.active_saga['stage']}/{player.active_saga['max_stage']}]"
    return None


def play_terminal_flashback(player, archetype, epitaph):
    clear_screen()
    print(f"\n{Color.GOLD}{'='*68}{Color.RESET}")
    print(f"{Color.BOLD}{Color.GOLD}    🎬  人 生 走 马 灯  ·  浮 生 高 光 回 眸{Color.RESET}")
    print(f"{Color.GOLD}{'='*68}{Color.RESET}\n")

    end_year = player.birth_year + player.age
    fam = getattr(player, "family", None) or initialize_family(player)
    g_text = "女 ♀" if player.gender == "female" else "男 ♂"

    # Slide 1: 降世
    print(f"{Color.YELLOW}【第一幕 · 降世初元】{Color.RESET}")
    slow_print(f" {format_year_month(player.birth_year, getattr(player, 'birth_month', 1))}，你作为一名{g_text}降生于【{player.origin['title']}】。\n"
               f" 慈父【{fam['father']['name']}】与严母【{fam['mother']['name']}】护你在膝下成长，骨子里刻下了【{player.trait['name']}】的命格基底。\n", 0.015)
    time.sleep(0.3)

    # Slide 2: 志学
    youth = [h for h in player.history if h["age"] <= 22]
    y_act = next((h for h in youth if h.get("is_key")), youth[0] if youth else None)
    if y_act:
        print(f"\n{Color.YELLOW}【第二幕 · 志学之年】{Color.RESET}")
        slow_print(f" {y_act['year']}年（{y_act['age']}岁），你在【{y_act['title']}】关口做出决断：“{y_act['choice_text']}”。\n"
                   f" 回响：{y_act['feedback']} 这一步落子，定下了日后的航向。\n", 0.015)
        time.sleep(0.3)

    # Slide 3: 伴侣/立业
    print(f"\n{Color.YELLOW}【第三幕 · 琴瑟同舟】{Color.RESET}")
    if fam.get("spouse"):
        s = fam["spouse"]
        slow_print(f" {s['married_year']}年，你与结发{s['role']}【{s['name']}】缔结良缘，风雨同舟数十载。\n"
                   f" 家门温润，相濡以沫，在这浩瀚人世间撑起了一处遮风避雨的暖阁。\n", 0.015)
    else:
        slow_print(" 行至壮年，你未入凡尘围城，选择以一身傲骨寄情于天地山海，探索属于自己的大道。\n", 0.015)
    time.sleep(0.3)

    # Slide 4: 命运惊涛
    mature = [h for h in player.history if h["age"] >= 26]
    if mature:
        m_act = min(mature, key=lambda h: abs(h.get("roll", 50) - h.get("chance", 50)))
        print(f"\n{Color.YELLOW}【第四幕 · 惊涛骇浪】{Color.RESET}")
        slow_print(f" {m_act['year']}年（{m_act['age']}岁），直面【{m_act['title']}】的考验：“{m_act['choice_text']}”。\n"
                   f" 掷骰定格——{m_act['feedback']}\n", 0.015)
        time.sleep(0.3)

    # Slide 5: 盖棺绝唱
    print(f"\n{Color.YELLOW}【终章 · 浮生绝唱】{Color.RESET}")
    slow_print(f" 享年 {player.age} 岁，最终留下时人誉称【{player.epithet}】与心性【{player.mindset}】。\n"
               f" 终极称号：《{archetype}》\n"
               f" 墓志铭：“{epitaph}”\n"
               f" 大浪淘沙，唯心自守。人间这一遭，未曾虚度。\n", 0.015)

    input(f"\n{Color.GOLD}按回车返回时代大门...{Color.RESET}")


def get_dynamic_choices_for_event(stage, player, curr_year):
    base_choices = list(stage.get("choices", []))
    if stage.get("_active_choices") and len(stage["_active_choices"]) >= 2:
        return stage["_active_choices"]

    roll = random.random()
    target_count = 2 if roll < 0.25 else (3 if roll < 0.75 else 4)
    if target_count <= len(base_choices):
        stage["_active_choices"] = base_choices
        return base_choices

    extra_choices = []
    era_id = player.epoch_mode
    is_classical = is_classical_epoch(era_id)
    is_future = is_future_epoch(era_id)

    # 1. 先天特质专属破局
    if getattr(player, "trait", None):
        t_name = player.trait["name"]
        if t_name == "商海通达":
            extra_choices.append({
                "text": "动用私房余资托商帮掌柜打点，以商贾变通之法周旋暗通款曲" if is_classical else ("调拨未上市的算力衍生品期权，通过暗网对冲掉眼前的危机缺口" if is_future else "敏锐把握市场供求失衡，借商业信息差反向操作，以小搏大破局"),
                "risk_label": "商道融通 · 财帛破关",
                "calc_chance": lambda p: min(92, max(25, 65 + (12 if p.wealth > 3 else 0))),
                "succ_feedback": "商道流转自有其玄妙。虽折损了少许启动资财，却极巧妙地避开了正面风浪！",
                "fail_feedback": "打点的本钱被中途盘剥截留，非但未能息事宁人，反倒折了微薄细软。",
                "succ_eff": {"wealth": -0.8, "rep": 6, "happiness": 4},
                "fail_eff": {"wealth": -1.5, "happiness": -6},
                "tag_succ": "以商破关",
                "tag_fail": "折本失算",
                "is_key": True,
            })
        elif t_name in ("灵光乍现", "洞若观火"):
            extra_choices.append({
                "text": "闭门研析古籍律条，从朝廷典章与文契字缝中寻得先例据理力争" if is_classical else ("调用深层神经逆向分析算法，直接推演博弈系统的底层判定漏洞" if is_future else "冷静避开所有情绪宣泄，直击事物核心本质，寻找制度规则内的破局点"),
                "risk_label": "智计透辟 · 规矩破局",
                "calc_chance": lambda p: min(95, max(25, 55 + int((p.intellect - 50) / 2))),
                "succ_feedback": "文思泉涌，切中肯綮！你呈递的条陈无懈可击，令在场众人皆刮目相看。",
                "fail_feedback": "即便看穿了关窍，人世间的成见与私利却比道理更坚硬，徒留一声叹息。",
                "succ_eff": {"intellect": 8, "rep": 8, "happiness": 6},
                "fail_eff": {"happiness": -8, "health": -4},
                "tag_succ": "算无遗策",
                "tag_fail": "书生迂阔",
                "is_key": True,
            })
        elif t_name in ("天生神力", "不屈不挠"):
            extra_choices.append({
                "text": "凭一身强悍筋骨与血勇骨气，亲涉险地冲在人前，硬扛下时代磨砺" if is_classical else ("启动义体应急超频过载协议，以生物电强行突破身体机能红线" if is_future else "凭着一股不服输的硬骨头韧劲，哪怕日夜熬煎也咬牙顶在一线硬拼到底"),
                "risk_label": "血性刚猛 · 勇者突围",
                "calc_chance": lambda p: min(92, max(25, 60 + int((p.health - 60) / 2))),
                "succ_feedback": "凡人之躯竟爆发出惊人伟力！你生生用血肉之躯在绝境中凿出了一条大道！",
                "fail_feedback": "血勇之气终敌不过无常造化，拼尽了全力依然伤痕累累，元气大伤。",
                "succ_eff": {"health": 4, "rep": 12, "happiness": 8},
                "fail_eff": {"health": -14, "happiness": -6},
                "tag_succ": "勇烈过人",
                "tag_fail": "负创抱憾",
                "is_key": True,
            })
        elif t_name in ("八面玲珑", "清心寡欲"):
            extra_choices.append({
                "text": "备办薄礼登门拜望四邻旧故与长辈，温言软语，以和为贵借众人声势从中斡旋",
                "risk_label": "谦冲自牧 · 柔顺克刚",
                "calc_chance": lambda p: 100,
                "succ_feedback": "做人留一线，日后好相见。你谦和圆融的处世之道抚平了剑拔弩张的争端。",
                "succ_eff": {"rep": 8, "happiness": 8, "wealth": -0.4},
                "tag_succ": "广结善缘",
                "is_key": False,
            })

    # 2. 至亲伴侣患难共济路线
    fam = getattr(player, "family", None)
    if len(extra_choices) < 2 and fam and fam.get("spouse") and fam["spouse"].get("alive"):
        s = fam["spouse"]
        extra_choices.append({
            "text": f"与结发{s['role']}【{s['name']}】秉烛夜话，二人同心，共分肩头风霜",
            "risk_label": "琴瑟同舟 · 患难结发",
            "calc_chance": lambda p: min(95, max(30, 75 + (10 if p.happiness > 60 else 0))),
            "succ_feedback": f"夫妻俩相视一笑，无论世道如何寒凉，有了身边知冷知热的人，风雪亦觉温存。",
            "fail_feedback": f"伴侣虽全力宽慰体贴，可眼前的沟坎实在太深，双双在长夜中对着残灯长吁短叹。",
            "succ_eff": {"happiness": 12, "health": 4, "rep": 4},
            "fail_eff": {"happiness": -8, "health": -3},
            "tag_succ": "同甘共苦",
            "tag_fail": "贫贱忧伤",
            "is_key": False,
        })

    # 3. 抱朴守拙退隐路线
    if len(extra_choices) < 2:
        extra_choices.append({
            "text": "看淡虚名浮利，索性闭门谢客守拙自持，借半亩桑田清谈度日" if is_classical else ("关闭社交神经流与算力推送，退回低能耗离线模式，静观世间喧嚣" if is_future else "索性断舍离，退居二线看淡内卷，陪着家人过好眼下一粥一饭"),
            "risk_label": "抱朴守拙 · 避其锐芒",
            "calc_chance": lambda p: 100,
            "succ_feedback": "退一步天地自宽。不去赶那一时的喧嚣红利，倒在浮躁尘世中守住了一方清净心田。",
            "succ_eff": {"happiness": 12, "health": 6, "wealth": -0.6},
            "tag_succ": "守拙知足",
            "is_key": False,
        })

    # 4. 破釜沉舟豪赌路线
    if len(extra_choices) < 2:
        extra_choices.append({
            "text": "将全副家底抵押孤注一掷，破釜沉舟，誓要在这乱世浪潮中博个滔天富贵" if is_classical else ("将全部算力资产全仓质押押注极端跃迁算法，生死在此一搏" if is_future else "抵押房车孤注一掷全力下注，破釜沉舟，搏击时代最激荡的风口"),
            "risk_label": "孤注一掷 · 豪赌天命",
            "calc_chance": lambda p: min(82, max(15, 45 + int((p.luck - 50) / 2))),
            "succ_feedback": "天地逆转，竟真教你搏出了翻天覆地的造化！在悬崖边缘惊险过关，声名震动四方！",
            "fail_feedback": "胜天半子终归太难。孤注一掷落了空，多年积攒的家底几乎折损殆尽，大伤元气。",
            "succ_eff": {"wealth": 18.0, "rep": 16, "happiness": 14, "health": -6},
            "fail_eff": {"wealth": -12.0, "happiness": -15, "health": -8, "rep": -6},
            "tag_succ": "绝境翻盘",
            "tag_fail": "折戟沉沙",
            "is_key": True,
        })

    result = list(base_choices)
    for ec in extra_choices:
        if len(result) >= target_count:
            break
        result.append(ec)

    stage["_active_choices"] = result
    return result

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
KARMA_FILE = ".fushenglu_karma.json"


def get_karma_points():
    if not os.path.exists(KARMA_FILE):
        return 15
    try:
        with open(KARMA_FILE, "r", encoding="utf-8") as f:
            return json.load(f).get("karma", 15)
    except Exception:
        return 15


def add_karma_points(n):
    cur = get_karma_points()
    updated = max(0, cur + n)
    try:
        with open(KARMA_FILE, "w", encoding="utf-8") as f:
            json.dump({"karma": updated}, f)
    except Exception:
        pass
    return updated


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
            "epithet": getattr(player, "epithet", "寻常布衣"),
            "values": getattr(player, "values", {"righteousness": 0, "duty": 0}),
            "mindset": getattr(player, "mindset", "兼济天下 · 铁肩义士"),
            "active_saga": getattr(player, "active_saga", None),
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
        "epithet": getattr(player, "epithet", "寻常布衣"),
        "mindset": getattr(player, "mindset", "兼济天下 · 铁肩义士"),
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
                print(f"     尊号: {Color.PURPLE}【{r.get('epithet', '寻常布衣')}】{Color.RESET} | 心性: {Color.CYAN}【{r.get('mindset', '兼济天下')}】{Color.RESET}")
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

    # 六道轮回祖荫赐福 (消耗5点轮回业力)
    karma = get_karma_points()
    blessing_chosen = None
    if karma >= 5:
        print(f"  {Color.PURPLE}🌌 当前六道轮回业力: {karma} 点{Color.RESET}")
        b_input = input(f"  {Color.GOLD}是否求取【祖荫赐福】(消耗5点业力)? [1.青云有路(+8✦) 2.殷实祖荫(+2.5万) 3.体魄如钟(+10♥) 4.福星临门(+12🎲) 0.不求取]: {Color.RESET}").strip()
        if b_input == "1":
            blessing_chosen = ("bless_intellect", "青云有路")
        elif b_input == "2":
            blessing_chosen = ("bless_wealth", "殷实祖荫")
        elif b_input == "3":
            blessing_chosen = ("bless_health", "体魄如钟")
        elif b_input == "4":
            blessing_chosen = ("bless_luck", "福星临门")

    name = input(f"\n{Color.CYAN}请输入入世姓名 (留空随机): {Color.RESET}").strip()
    if not name:
        name = pick_epoch_name(epoch_mode, gender)

    player = Player(name, epoch_mode, b_year, origin, trait, gender=gender)
    if blessing_chosen:
        add_karma_points(-5)
        bid, bname = blessing_chosen
        if bid == "bless_intellect":
            player.intellect = min(100, player.intellect + 8)
        elif bid == "bless_wealth":
            player.wealth = round(player.wealth + 2.5, 1)
        elif bid == "bless_health":
            player.health = min(100, player.health + 10)
        elif bid == "bless_luck":
            player.luck = min(100, player.luck + 12)
        player.tags.append(bname)
        print(f"  {Color.GREEN}【祖荫庇护】已加持【{bname}】！结余轮回业力: {get_karma_points()} 点。{Color.RESET}")

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

        # 突发强随机事件（严格按所属大纪元取用专属微观事件）
        rand_pool = RANDOM_EVENT_POOLS.get(era_id, FUTURE_RANDOM_EVENTS if is_future_epoch(era_id) else PAST_RANDOM_EVENTS)
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

        active_choices = get_dynamic_choices_for_event(stage, player, curr_year)

        print(f"{Color.CYAN}面临抉择：{Color.RESET}")
        for idx, c in enumerate(active_choices, 1):
            base_chance = c["calc_chance"](player)
            fate_bonus, reasons = calculate_fate_bond_modifier(player, c)
            eff_chance = 100 if base_chance >= 100 else min(95, max(15, base_chance + fate_bonus))
            fate_tip = f" {Color.PURPLE}[羁绊: {reasons[0]}]{Color.RESET}" if (base_chance < 100 and reasons) else ""
            badge = f"{Color.GREEN}[稳妥必成]{Color.RESET}" if eff_chance >= 100 else f"{Color.YELLOW}[成功率约 {eff_chance}%]{Color.RESET}{fate_tip}"
            print(f"  {idx}. {c['text']}  {badge} ({c['risk_label']})")

        while True:
            c_input = input(f"\n{Color.GOLD}请选择 [1-{len(active_choices)}]: {Color.RESET}").strip()
            if c_input.isdigit() and 1 <= int(c_input) <= len(active_choices):
                chosen_idx = int(c_input) - 1
                break
            print(f"{Color.RED}输入无效，请重新选择。{Color.RESET}")

        chosen = active_choices[chosen_idx]
        base_chance = chosen["calc_chance"](player)
        fate_bonus, reasons = calculate_fate_bond_modifier(player, chosen)
        chance = 100 if base_chance >= 100 else min(95, max(15, base_chance + fate_bonus))
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

        other_choice = active_choices[1 - chosen_idx]["text"] if (len(active_choices) > 1 and chosen_idx < len(active_choices)) else ""
        record = {
            "year": curr_year,
            "age": player.age,
            "title": stage["title"],
            "choice_text": chosen["text"],
            "other_choice": other_choice,
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

        update_player_values(player, chosen, tag)
        update_player_epithet(player)
        saga_msg = check_saga_progress(player, chosen, is_success)
        if saga_msg:
            print(f"\n{Color.PURPLE}{saga_msg}{Color.RESET}")
            fb += f"\n{saga_msg}"

        if chosen.get("is_key"):
            player.key_choices.append(record)

        if chance < 100:
            fate_note = f" ({Color.PURPLE}羁绊加成: {', '.join(reasons)}{Color.RESET})" if reasons else ""
            print(f"\n{Color.PURPLE}🎲 命运掷骰：出目 {roll} / 胜率基线 {chance}%{fate_note}  ➔  {'★ 顺遂如愿' if is_success else '✕ 天不遂人'}{Color.RESET}")
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
    print(f" 主角姓名: {Color.BOLD}{player.name}{Color.RESET} ({g_str}) · {Color.PURPLE}【{player.epithet}】{Color.RESET} ({format_year_month(player.birth_year, _bmonth)} - {format_year_only(end_year)} · 享年 {player.age} 岁)")
    print(f" 时代纪元: {_cfg['icon']}【{_cfg['name']}】({_cfg['sub_title']})")
    print(f" 心性境界: {Color.CYAN}【{player.mindset}】{Color.RESET}" + (f" | 传奇支线: {Color.YELLOW}{player.active_saga['title']} [功德圆满]{Color.RESET}" if player.active_saga and player.active_saga['stage'] >= player.active_saga['max_stage'] else ""))
    print(f" 出生家庭: {player.origin['title']}")
    print(f" 离世归宿: {player.death_reason}")

    print(f"\n{Color.CYAN}【 终生数据结算 】{Color.RESET}")
    print(f"  生命健康值 : {int(player.health)} / 100")
    print(f"  积累财富净值: {player.wealth:.1f} {wealth_unit(player.epoch_mode)}")
    print(f"  学识心智值 : {int(player.intellect)} / 100")
    print(f"  心境安宁度 : {int(player.happiness)} / 100")
    print(f"  终生天命气运: {int(player.luck)} / 100")
    sc = player.track_scores
    print(f"  赛道罗盘积分: 体制政务 {sc['体制政务']} | 商海实业 {sc['商海实业']} | 学术科技 {sc['学术科技']} | 文艺江湖 {sc['文艺江湖']} | 守拙自持 {sc['守拙布衣']}")
    print(f"  终身位阶坐标: {Color.BOLD}{player.career_track} · {player.social_rank}{Color.RESET}")

    print(f"\n{Color.CYAN}【 人生印记标签 】{Color.RESET}")
    print("  " + "  ".join([f"{Color.BG_DARK}#{t}{Color.RESET}" for t in player.tags]))

    is_future = is_future_epoch(player.epoch_mode)
    is_classical = is_classical_epoch(player.epoch_mode)
    trk = player.career_track
    w = player.wealth
    hap = player.happiness
    i = player.intellect
    rep = player.reputation
    tags = player.tags or []

    if is_future:
        if trk == "学术科技" and i >= 85:
            archetype = "智械天启 · 虚空构筑者"
            epitaph = "在量子与超弦间构筑起包容百亿生灵的精神圣殿，思维在此彻底摆脱了重力与肉身的束缚。"
        elif trk == "守拙布衣" and hap >= 65:
            archetype = "地表植林者 · 纯真守望"
            epitaph = "当整个文明争相飞升虚空，你深情守望脚下的每一寸泥土，是大地最质朴、最深情的孩子。"
        elif w >= 45 and hap >= 55:
            archetype = "星海拓荒巨擘 · 载誉深空"
            epitaph = "你从人造穹顶起步，乘上了人类迈向星海的巍峨巨舰。在引力与虚空中纵横开阖，无愧为宇宙的孩子。"
        elif w >= 25 and hap < 45:
            archetype = "赛博齿轮 · 冰冷义体攀登者"
            epitaph = "你在代码洪流与钛合金内脏间奔波一生，换来了令人艳羡的算力与配额，却在深夜怀念母亲曾哼唱过的古老摇篮曲。"
        elif hap >= 70 and w < 25:
            archetype = "纯粹碳基散人 · 地表哲人"
            epitaph = "世人争先恐后抛弃肉身飞升云端，唯有你深情守望脚下的每一寸泥土。虽无万贯算力，胸中自有一整座真实星汉。"
        elif i >= 80:
            archetype = "文明先知 · 灵境守望者"
            epitaph = "你以澄澈的智识看穿了技术膨胀与人性异化的迷局，在冷酷的代码矩阵中，为人类守护住了最后一丝温热的诗意。"
        elif player.age < 50:
            archetype = "星轨流星 · 破晓之光"
            epitaph = "你在异星极端风暴中疾驰，生命璀璨夺目如超新星爆发。深空寂静，而你的火种早已照亮了母星的天平。"
        else:
            archetype = "星尘守夜人 · 凡人的尊严"
            epitaph = "既没有成为神话般的星际领主，亦未沦为算法的附庸。守住爱人，守护家人，堂堂正正走完了属于人的壮丽一生。"
    elif is_classical:
        if trk == "体制政务" and rep >= 68:
            archetype = "宰辅梁栋 · 经邦济世"
            epitaph = "受命于微时，总摄纲纪，居庙堂之高而忧其民。修明庶政，澄清海宇，为万民立万代规矩。"
        elif trk == "商海实业" and w >= 28:
            archetype = "陶朱遗风 · 富甲八荒"
            epitaph = "贾道通天下，积散有方，贾亦有道。兼济宗族邻里，千金散尽还复来，青史留清誉。"
        elif trk == "文艺江湖" and hap >= 62:
            archetype = "仗剑放歌 · 绝尘游侠"
            epitaph = "行止由心，不问王侯。诗词墨宝与快意恩仇冠绝一时，人间留下了你无羁的歌哭与传说。"
        elif trk == "学术科技" and (i >= 76 or any("医" in t for t in tags)):
            archetype = "杏林大医 · 悬壶济世"
            epitaph = "常怀大慈恻隐之心，博极医源，救含灵之苦。一剂温凉解百代沉疴，大德长留民间。"
        elif w >= 30 and rep >= 60:
            archetype = "名标青史 · 一世风流"
            epitaph = "你的名字被郑重写进了%s，与那个时代的山川人物并列。富贵或已散去，声名却比血肉活得更久。" % _cfg["legacy"]
        elif w >= 15 and hap < 45:
            archetype = "负重跋涉者 · 寒暑苦行"
            epitaph = "你一生都在为一族人的口粮与体面奔波，风霜刻在额角，未曾有一日懈怠，也未曾真正为自己活过。"
        elif hap >= 70 and w < 15:
            archetype = "林泉散人 · 自在一生"
            epitaph = "不慕朱门车马，只爱一壶浊酒、半亩薄田。你以清贫换得心安，是那个时代少数真正自由的人。"
        elif i >= 78:
            archetype = "明哲通达 · 洞观兴替"
            epitaph = "你冷眼看尽王朝更迭与人事翻覆，读懂了兴衰的规律，因而对世人多了一份悲悯与宽恕。"
        elif player.age < 50:
            archetype = "断弦流星 · 孤勇悲歌"
            epitaph = "乱世里的性命如风中烛火，你疾行过，灿然过，终是太早熄灭了。山河依旧，只是再无你的消息。"
        else:
            archetype = "烟火凡人 · 坚韧一生"
            epitaph = "你没有在史书上留下一行字，却用一粥一饭把血脉与家训传了下去。这本身就是了不起的功业。"
    else:
        if trk == "学术科技" and i >= 80:
            archetype = "科学先驱 · 拓荒真知"
            epitaph = "一生淡泊名利，以求真为唯一航标。在代码与实验室的枯寂中，为人类推开了一扇通往明天的窗。"
        elif trk == "文艺江湖" and hap >= 66:
            archetype = "旷达行者 · 浪潮诗人"
            epitaph = "世人奔波于功名利禄，你却把一生活成了一首自由散漫的诗。走过山海，满心温热与坦荡。"
        elif w >= 45 and hap >= 55:
            archetype = "时代弄潮翁 · 功成身退"
            epitaph = "你乘上了历史最激荡的风帆，饱览过财富的壮阔，亦未曾迷失于物欲的深壑。行过大江大河，落子无悔。"
        elif w >= 25 and hap < 45:
            archetype = "负重攀登者 · 时代苦行僧"
            epitaph = "在狂飙的城市化与债务大山中，你用肩膀扛起了几代人的体面与产证，却在深夜加班室里耗尽了青春灵气。"
        elif hap >= 70 and w < 25:
            archetype = "旷达布衣 · 自在散人"
            epitaph = "世人慌慌张张图碎银几两，而你早早参透了内卷的虚妄。向青山借得满怀清风，虽无万贯财，胸中自安然。"
        elif i >= 80:
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

    # 身后遗泽与子孙后记推演
    postscript_parts = []
    child_count = len(fam.get("children", []))
    if fam.get("spouse") and fam["spouse"].get("alive"):
        postscript_parts.append(f"你溘然长逝之后，结发{fam['spouse']['role']}【{fam['spouse']['name']}】于灵前默坐良久。余生每逢忌辰，案头皆敬供着你生前最喜爱的清茶。")
    if child_count >= 2:
        if player.wealth >= 20:
            if is_classical:
                postscript_parts.append("长子谨遵你留下的家训主持析产，各房和睦相持未起阋墙之争。借着厚实家底，孙辈中终有俊杰应试入泮，诗礼传家。")
            elif is_future:
                postscript_parts.append("你留存的高阶算力信托与深空股权平稳交割，多代人得以在穹顶安稳生活，你的基因档案被永久镌刻于家族家系库。")
            else:
                postscript_parts.append("儿女们分得你的积蓄与房产，在激荡时代中各自成家立业。每逢清明聚首，晚辈们仍会翻看老相册，感念你当年艰辛打下的基业。")
        else:
            postscript_parts.append(f"儿女们虽无万贯资财可继，却秉承了你一生【{player.trait['name']}】的风骨，在世道中各安其业，守住了普通人最真切的尊严。")
    elif child_count == 1:
        ch = fam["children"][0]
        postscript_parts.append(f"独{ch['role']}【{ch['name']}】抚棺承家，将你的生前遗物细致包好珍藏，时常向儿孙絮絮讲起你当年的那段峥嵘岁月。")
    else:
        if is_classical:
            postscript_parts.append("你一身傲骨孤行天地，无子嗣之累。辞世后故旧好友凑资为你具棺收殓，葬于故园青山之阳，岁岁清明自有人携酒凭吊。")
        elif is_future:
            postscript_parts.append("你未育子嗣，辞世后全部算力盈余捐入深空引航基金，在猎户座星云间，有一颗信标灯塔永远闪烁着你的名字。")
        else:
            postscript_parts.append("你一生独行潇洒，落子无憾。遗存的字画手稿被故旧转赠市图书馆，偶尔有驻足翻阅的青年，重新相遇了你当年的心跳。")
    
    if player.reputation >= 70:
        postscript_parts.append("乡党士绅深感其公德，多年后提起你的名讳，依旧赞叹为一方楷模，称你“行事端方，无负天地”。")
    elif player.wealth >= 30:
        postscript_parts.append("商街字号与邻里行帮皆盛传你当年经营的义利信条，后辈经商之人多奉你的法度为标尺。")

    print(f"\n{Color.CYAN}【 身后长河遗泽 · 子孙后记 】{Color.RESET}")
    print(f"  {Color.GRAY}{' '.join(postscript_parts)}{Color.RESET}")

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
        if kc.get("other_choice"):
            print(f"     未竞: {Color.DIM}“{kc['other_choice']}” · 终是一别两宽，未曾相逢。{Color.RESET}")

    print(f"\n{Color.GOLD}{'='*68}{Color.RESET}")
    print(f"{Color.DIM}大浪淘沙，唯心自守。愿你在人间的每一程都无怨无悔。{Color.RESET}\n")

    # 轮回业力结算
    earned_karma = max(5, int(player.age * 0.15 + (player.wealth * 0.35 if player.wealth > 0 else 0) + player.reputation * 0.2))
    total_k = add_karma_points(earned_karma)
    print(f"{Color.PURPLE}【 🌌 六道轮回业力结算 】{Color.RESET}")
    print(f"  本世功业转化为 {Color.BOLD}{Color.GOLD}+{earned_karma}{Color.RESET} 点轮回业力，累计结余: {Color.BOLD}{total_k}{Color.RESET} 点。\n")

    record_to_hall_of_fame(player, archetype, epitaph)
    if os.path.exists(SAVE_FILE):
        try:
            os.remove(SAVE_FILE)
        except Exception:
            pass

    f_input = input(f"{Color.GOLD}是否播放【🎬 人生走马灯 · 浮生高光回眸】? (输入 y 播放，按回车跳过): {Color.RESET}").strip().lower()
    if f_input == 'y':
        play_terminal_flashback(player, archetype, epitaph)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n岁月如风，中途隐退。")
