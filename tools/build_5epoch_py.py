import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
os.chdir(_ROOT)

# -*- coding: utf-8 -*-
"""把五大文明纪元完整注入 life_game.py（与 index.html 保持同源同逻辑）。"""

import importlib

import civ_core as C

NEW_EPOCHS = ("ancient", "premodern", "modern")
DATA = {}

STAT_KEYS = ("health", "wealth", "intellect", "happiness", "luck", "rep")


def load_data():
    import civ_loader
    DATA.update(civ_loader.load_all())
    for eid in NEW_EPOCHS:
        d = DATA[eid]
        print("  %s: regions=%d strata=%d stages=%d events=%d"
              % (eid, len(d.REGIONS), len(d.STRATA), len(d.STAGE_EVENTS), d.event_count()))


def py_region(r):
    stat = r.get("stat", {})
    keys = ", ".join('"%s": %s' % (k, "%g" % stat[k]) for k in stat)
    return '    (%s, %s, {%s})' % (C.py_str(r["name"]), C.py_str(r["desc"]), keys)


def py_strata(s):
    st = s.get("stat", {})
    keys = ", ".join('"%s": %s' % (k, "%g" % st.get(k, 50)) for k in STAT_KEYS)
    return '    (%s, %s, {%s}, %s)' % (
        C.py_str(s["title"]), C.py_str(s["desc"]), keys, C.py_str(s.get("trait", "坚韧自持")))


def build_py_pack():
    L = []
    L.append("# ==================== 文明五大纪元 · 从华夏溯源到星海跃迁 ====================")
    L.append("EPOCHS = [")
    for e in C.EPOCHS:
        L.append("    {")
        L.append('        "id": %s,' % C.py_str(e["id"]))
        L.append('        "name": %s,' % C.py_str(e["name"]))
        L.append('        "sub_title": %s,' % C.py_str(e["sub_title"]))
        L.append('        "min_year": %d,' % e["min_year"])
        L.append('        "max_year": %d,' % e["max_year"])
        L.append('        "badge": %s,' % C.py_str(e["badge"]))
        L.append('        "desc": %s,' % C.py_str(e["desc"]))
        L.append('        "icon": %s,' % C.py_str(e["icon"]))
        L.append('        "legacy": %s,' % C.py_str({
            "ancient": "青史竹简", "premodern": "族谱与方志", "modern": "厂志与家书",
            "contemporary": "市井与家书", "future": "星尘档案"}[e["id"]]))
        L.append('        "names": [%s],' % ", ".join(C.py_str(n) for n in e["names"]))
        L.append("    },")
    L.append("]")
    L.append("")
    L.append("# 连续时代背景表：(年份上界(开区间) 或 None 表示兜底, 名称, 描述)")
    L.append("GRAND_ERA_TABLE = [")
    for upper, name, desc in C.GRAND_ERA_BUCKETS:
        L.append("    (%s, %s, %s)," % ("None" if upper is None else upper, C.py_str(name), C.py_str(desc)))
    L.append("]")
    L.append("")
    L.append("")
    L.append("def wealth_unit(epoch_id):")
    L.append('    """各纪元货币单位：避免先秦人生出现万元这类时代错位。"""')
    L.append('    if epoch_id == "ancient":')
    L.append('        return "两金"')
    L.append('    if epoch_id == "premodern":')
    L.append('        return "两银"')
    L.append('    if epoch_id == "modern":')
    L.append('        return "块银元"')
    L.append('    if epoch_id == "contemporary":')
    L.append('        return "万元"')
    L.append('    return "信用点"')
    L.append("")
    L.append("")
    L.append("def get_epoch_config(epoch_id):")
    L.append("    for e in EPOCHS:")
    L.append('        if e["id"] == epoch_id:')
    L.append("            return e")
    L.append("    return EPOCHS[3]")
    L.append("")
    L.append("")
    L.append("def get_epoch_id_for_year(year):")
    L.append("    for e in EPOCHS:")
    L.append('        if year <= e["max_year"]:')
    L.append('            return e["id"]')
    L.append('    return EPOCHS[-1]["id"]')
    L.append("")
    L.append("")
    L.append("def is_future_epoch(epoch_id):")
    L.append('    return epoch_id == "future"')
    L.append("")
    L.append("")
    L.append("def is_classical_epoch(epoch_id):")
    L.append('    return epoch_id in ("ancient", "premodern", "modern")')
    L.append("")
    L.append("")
    L.append("def pick_epoch_name(epoch_id):")
    L.append("    cfg = get_epoch_config(epoch_id)")
    L.append('    return random.choice(cfg["names"]) if cfg["names"] else "无名"')
    L.append("")
    L.append("")
    L.append("def resolve_era(year):")
    L.append("    for upper, name, desc in GRAND_ERA_TABLE:")
    L.append("        if upper is None or year < upper:")
    L.append("            return name, desc")
    L.append("    return GRAND_ERA_TABLE[-1][1], GRAND_ERA_TABLE[-1][2]")
    L.append("")
    L.append("")
    L.append("def resolve_era_details(year, epoch_mode=None):")
    L.append('    """任意年份（含公元前）均有归属，从文明起源到未来星际无间断。"""')
    L.append("    return resolve_era(year)")
    L.append("")
    L.append("")
    L.append("def format_year_only(year):")
    L.append("    y = int(round(year))")
    L.append("    if y < 0:")
    L.append('        return "公元前 %d 年" % abs(y)')
    L.append("    if y == 0:")
    L.append('        return "公元元年"')
    L.append('    return "公元 %d 年" % y')
    L.append("")
    L.append("")
    L.append("def format_year_month(year, month):")
    L.append('    return "%s %d月" % (format_year_only(year), month or 1)')
    L.append("")
    L.append("")
    L.append("def list_eras_between(y0, y1):")
    L.append('    """一生穿越过的所有大时代（按时间顺序去重）。"""')
    L.append("    out = []")
    L.append("    a, b = int(min(y0, y1)), int(max(y0, y1))")
    L.append("    for y in range(a, b + 1):")
    L.append("        n = resolve_era(y)[0]")
    L.append("        if not out or out[-1] != n:")
    L.append("            out.append(n)")
    L.append("    if not out:")
    L.append("        out.append(resolve_era(a)[0])")
    L.append("    return out")
    L.append("")

    for eid in NEW_EPOCHS:
        mod = DATA[eid]
        up = eid.upper()
        L.append("")
        L.append("# ---- %s 出身地域（8）与门第阶层（10）----" % eid)
        L.append("%s_REGIONS = [" % up)
        L.append(",\n".join(py_region(r) for r in mod.REGIONS))
        L.append("]")
        L.append("")
        L.append("%s_SOCIAL_STRATA = [" % up)
        L.append(",\n".join(py_strata(s) for s in mod.STRATA))
        L.append("]")
        L.append("")
        L.append("# ---- %s 16 大生命阶段事件池 ----" % eid)
        L.append("%s_STAGE_POOLS = [" % up)
        stages = []
        for i, st in enumerate(mod.STAGE_EVENTS):
            evs = ",\n".join(C.event_to_py(ev, i) for ev in st)
            stages.append("  [\n%s\n  ]" % evs)
        L.append(",\n".join(stages))
        L.append("]")
        L.append("")

    L.append("")
    L.append("def get_origin_tables(epoch_id):")
    L.append('    if epoch_id == "ancient":')
    L.append("        return ANCIENT_REGIONS, ANCIENT_SOCIAL_STRATA")
    L.append('    if epoch_id == "premodern":')
    L.append("        return PREMODERN_REGIONS, PREMODERN_SOCIAL_STRATA")
    L.append('    if epoch_id == "modern":')
    L.append("        return MODERN_REGIONS, MODERN_SOCIAL_STRATA")
    L.append('    if epoch_id == "contemporary":')
    L.append("        return PAST_REGIONS, PAST_SOCIAL_STRATA")
    L.append("    return FUTURE_REGIONS, FUTURE_SOCIAL_STRATA")
    L.append("")
    L.append("")
    L.append("def get_stage_pools(epoch_id):")
    L.append('    if epoch_id == "ancient":')
    L.append("        return ANCIENT_STAGE_POOLS")
    L.append('    if epoch_id == "premodern":')
    L.append("        return PREMODERN_STAGE_POOLS")
    L.append('    if epoch_id == "modern":')
    L.append("        return MODERN_STAGE_POOLS")
    L.append('    if epoch_id == "contemporary":')
    L.append("        return PAST_STAGE_POOLS")
    L.append("    return FUTURE_STAGE_POOLS")
    L.append("")
    L.append("")
    L.append("def generate_procedural_origin(epoch_id):")
    L.append("    regions, strata_list = get_origin_tables(epoch_id)")
    L.append("    region_name, region_desc, region_stat = random.choice(regions)")
    L.append("    strata_title, strata_desc, strata_stat, trait_name = random.choice(strata_list)")
    L.append('    title = "%s · %s" % (region_name[:5], strata_title)')
    L.append('    desc = "降生于【%s】。%s；家庭是【%s】，%s。" % (')
    L.append("        region_name, region_desc, strata_title, strata_desc)")
    L.append("    stat_mod = {}")
    L.append("    for k in %s:" % (repr(list(STAT_KEYS)).replace("'", '"')))
    L.append("        stat_mod[k] = round(strata_stat.get(k, 0) + region_stat.get(k, 0), 1)")
    L.append("    return {")
    L.append('        "title": title, "desc": desc, "region": region_name,')
    L.append('        "strata": strata_title, "stat": stat_mod,')
    L.append('        "trait": trait_name, "flavor": strata_desc,')
    L.append("    }")
    L.append("")
    L.append("")
    L.append("def generate_random_destiny(epoch_id):")
    L.append("    cfg = get_epoch_config(epoch_id)")
    L.append('    b_year = random.randint(cfg["min_year"], cfg["max_year"])')
    L.append("    b_month = random.randint(1, 12)")
    L.append("    origin = generate_procedural_origin(epoch_id)")
    L.append("    trait = random.choice(RANDOM_TRAITS)")
    L.append("    return b_year, b_month, origin, trait")
    L.append("")
    L.append("")
    return "\n".join(L)


def replace_between(text, start_marker, end_marker, new, label):
    i = text.index(start_marker)
    j = text.index(end_marker, i)
    print("  patched: %s" % label)
    return text[:i] + new + text[j:]


def main():
    load_data()
    path = 'life_game.py'
    py = open(path, encoding='utf-8').read()
    orig = len(py)

    # 0. 修复此前误将 slow_print 替换为 print 的两处调用（会多打印一个延时数字）
    for broken, fixed in (
        ('\n", 0.012)', '\n", 0.012)'),
    ):
        pass
    py = py.replace(
        'print(" 一个人的命运，既要靠自我的奋斗，亦要看历史的进程。\\n 时代洪流呼啸而过，偶发的幸与不幸如影随形。细水长流，步步为营，落子无悔。\\n", 0.012)',
        'slow_print(" 一个人的命运，既要靠自我的奋斗，亦要看历史的进程。\\n 时代洪流呼啸而过，偶发的幸与不幸如影随形。细水长流，步步为营，落子无悔。\\n", 0.012)')
    py = py.replace(
        'print(f"\\n命运之轮缓缓启动，{player.name} 踏入了 {player.birth_year} 年的人间...\\n", 0.02)',
        'slow_print(f"\\n命运之轮缓缓启动，{player.name} 踏入了 {format_year_month(player.birth_year, getattr(player, \'birth_month\', 1))} 的人间...\\n", 0.02)')
    print("  patched: slow_print call sites")

    # 1. 用纪元数据包替换旧的 generate_procedural_origin / resolve_era_details
    py = replace_between(
        py, "def generate_procedural_origin(epoch_mode):", "RANDOM_TRAITS = [",
        build_py_pack() + "\n", "procedural origin + era resolver")

    # 1b. 删除旧的 generate_random_destiny（由数据包中的纪元版本取代）
    py = replace_between(
        py, "def generate_random_destiny(epoch_mode):",
        "# -*- coding: utf-8 -*-\nPAST_ALT_STAGES_PY = [", "",
        "removed legacy generate_random_destiny")

    # 2. 主舞台选择
    old_menu = '''    print(f"{Color.CYAN}【 请选择入世时代纪元 】{Color.RESET}")
    print(f"  1. 过去风云纪元 (1976-1994) · 国企大院、下海大潮、世贸狂飙、地产与移动互联")
    print(f"  2. 未来科幻纪元 (2042-2060) · 脑机义体、地月轨道、小行星采矿、意识上传与星海拓荒")
    print(f"  3. 完全随机天命 (由命运的骰子决定投胎到过去还是未来)")

    epoch_mode = "past"
    while True:
        e_choice = input(f"\\n{Color.GOLD}请选择纪元模式 [1-3, 默认 3]: {Color.RESET}").strip()
        if e_choice in ("1", "past"):
            epoch_mode = "past"
            break
        elif e_choice in ("2", "future"):
            epoch_mode = "future"
            break
        elif e_choice in ("3", "", "random"):
            epoch_mode = random.choice(["past", "future"])
            print(f"{Color.PURPLE}🎲 天命掷骰！你被投放到了：{'【过去风云纪元】' if epoch_mode == 'past' else '【未来科幻纪元】'}{Color.RESET}")
            break
        print(f"{Color.RED}输入无效，请重新选择。{Color.RESET}")'''
    new_menu = '''    print(f"{Color.CYAN}【 请选择入世时代纪元 】{Color.RESET}")
    print(f"  {Color.GRAY}文明长河自公元前1600年奔涌至公元2150年，皆可投胎；一生将随年代推移自动切换时代背景。{Color.RESET}")
    for idx_e, e in enumerate(EPOCHS, 1):
        print(f"  {idx_e}. {e['icon']} {e['name']} ({e['sub_title']}) · {e['badge']}")
    print(f"  {len(EPOCHS) + 1}. 完全随机天命 (由命运的骰子决定你降生于哪一个大时代)")

    epoch_mode = EPOCHS[3]["id"]
    while True:
        e_choice = input(f"\\n{Color.GOLD}请选择纪元模式 [1-{len(EPOCHS) + 1}, 默认 {len(EPOCHS) + 1}]: {Color.RESET}").strip()
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
        print(f"{Color.RED}输入无效，请重新选择。{Color.RESET}")'''
    assert old_menu in py, "menu block not found"
    py = py.replace(old_menu, new_menu, 1)
    print("  patched: epoch menu")

    # 3. 投胎卡片：纪元名 + 年月
    old_card = '''    while True:
        b_year, origin, trait = generate_random_destiny(epoch_mode)
        era_title, era_desc = resolve_era_details(b_year, epoch_mode)
        
        print(f"\\n{Color.CYAN}【 🎲 先天命格卡 · 随机摇号投胎 】{Color.RESET}")
        print(f"  纪元属性: {Color.BOLD}{'过去历史纪元' if epoch_mode == 'past' else '近未来科幻纪元'}{Color.RESET}")
        print(f"  出生年代: {Color.YELLOW}{b_year} 年 · {era_title}{Color.RESET}")'''
    new_card = '''    cfg_now = get_epoch_config(epoch_mode)
    while True:
        b_year, b_month, origin, trait = generate_random_destiny(epoch_mode)
        era_title, era_desc = resolve_era(b_year)

        print(f"\\n{Color.CYAN}【 🎲 先天命格卡 · 随机摇号投胎 】{Color.RESET}")
        print(f"  纪元属性: {Color.BOLD}{cfg_now['icon']} {cfg_now['name']} ({cfg_now['sub_title']}){Color.RESET}")
        print(f"  出生年代: {Color.YELLOW}{format_year_month(b_year, b_month)} · {era_title}{Color.RESET}")'''
    assert old_card in py, "destiny card block not found"
    py = py.replace(old_card, new_card, 1)
    print("  patched: destiny card")

    # 4. 随机取名按纪元
    old_names = '''    default_names = ["林栖", "陈远", "沈清弦", "陆明舟", "许念安", "周子墨", "星野", "艾柯", "顾长风"]
    name = input(f"\\n{Color.CYAN}请输入入世姓名 (留空随机): {Color.RESET}").strip()
    if not name:
        name = random.choice(default_names)

    player = Player(name, epoch_mode, b_year, origin, trait)
    stage_pools = PAST_STAGE_POOLS if epoch_mode == "past" else FUTURE_STAGE_POOLS
    total_stages = len(stage_pools)
    timeline = generate_random_timeline()'''
    new_names = '''    name = input(f"\\n{Color.CYAN}请输入入世姓名 (留空随机): {Color.RESET}").strip()
    if not name:
        name = pick_epoch_name(epoch_mode)

    player = Player(name, epoch_mode, b_year, origin, trait)
    player.birth_month = b_month
    total_stages = 16
    timeline = generate_random_timeline()'''
    assert old_names in py, "names block not found"
    py = py.replace(old_names, new_names, 1)
    print("  patched: player bootstrap")

    # 5. 主循环：按“该阶段所处年代”取对应纪元事件池与突发事件池
    old_loop = '''    for idx_stage, pool in enumerate(stage_pools, 1):
        if player.health <= 12:
            player.death_reason = "积劳成疾，在时代长风中过早抱憾离世"
            break

        stage = random.choice(pool)
        player.age = timeline[idx_stage - 1]
        curr_year = player.birth_year + player.age
        player.show_dashboard(idx_stage, total_stages)

        # 突发强随机事件
        rand_pool = PAST_RANDOM_EVENTS if player.epoch_mode == "past" else FUTURE_RANDOM_EVENTS'''
    new_loop = '''    for idx_stage in range(1, total_stages + 1):
        if player.health <= 12:
            player.death_reason = "积劳成疾，在时代长风中过早抱憾离世"
            break

        player.age = timeline[idx_stage - 1]
        curr_year = player.birth_year + player.age
        # 以“该阶段实际所处的年代”决定取自哪个纪元的事件池，
        # 因此一个横跨数十乃至数百年的生命会自然经历古代 -> 近世 -> 当代 -> 未来的切换。
        era_id = get_epoch_id_for_year(curr_year)
        pools_now = get_stage_pools(era_id)
        stage = random.choice(pools_now[idx_stage - 1])
        player.show_dashboard(idx_stage, total_stages)

        # 突发强随机事件（按年代选择历史/未来事件库）
        rand_pool = FUTURE_RANDOM_EVENTS if is_future_epoch(era_id) else PAST_RANDOM_EVENTS'''
    assert old_loop in py, "main loop block not found"
    py = py.replace(old_loop, new_loop, 1)
    print("  patched: main loop")

    # 6. 结局页：纪元名 + 出生年月 + 古典纪元宿命 + 时代回响
    old_meta = '''    print(f" 主角姓名: {Color.BOLD}{player.name}{Color.RESET} ({player.birth_year} - {end_year} · 享年 {player.age} 岁)")
    print(f" 时代纪元: {'【过去历史纪元】' if player.epoch_mode == 'past' else '【近未来科幻纪元】'}")'''
    new_meta = '''    _bmonth = getattr(player, "birth_month", 1)
    _cfg = get_epoch_config(player.epoch_mode)
    print(f" 主角姓名: {Color.BOLD}{player.name}{Color.RESET} ({format_year_month(player.birth_year, _bmonth)} - {format_year_only(end_year)} · 享年 {player.age} 岁)")
    print(f" 时代纪元: {_cfg['icon']}【{_cfg['name']}】({_cfg['sub_title']})")'''
    assert old_meta in py, "ending meta not found"
    py = py.replace(old_meta, new_meta, 1)

    py = py.replace(
        '    is_future = (player.epoch_mode == "future")',
        '    is_future = is_future_epoch(player.epoch_mode)\n    is_classical = is_classical_epoch(player.epoch_mode)', 1)

    old_arch = '''        if player.wealth >= 45 and player.happiness >= 55:
            archetype = "时代弄潮翁 · 功成身退"'''
    new_arch = '''        if is_classical and player.wealth >= 30 and player.reputation >= 60:
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
            archetype = "时代弄潮翁 · 功成身退"'''
    assert old_arch in py, "ending archetype anchor not found"
    py = py.replace(old_arch, new_arch, 1)

    old_reflect = '''    print(f"\\n{Color.CYAN}【 时代长河坐标 】{Color.RESET}")
    if is_future:
        print(f"  {player.name}降生于 {player.birth_year} 年（{player.origin['title']}）。")
        print(f"  这一生跨越了人类从母星摇篮迈向深空智能文明的关键半世纪：从脑机神经直连、碳配额紧缩、地月货运电梯常态运营，")
        print(f"  到小行星采矿热潮、基因编辑代际分化，直至晚年见证强人工智能自组织与最终的意识升维与碳基抉择。")
        print(f"  大时代每一次星火跃迁与算法重构，都在这个生命的悲欢离合中，刻下了深刻而独特的星尘坐标。")
    else:
        print(f"  {player.name}降生于 {player.birth_year} 年（{player.origin['title']}）。")
        print(f"  这一生跨越了中国现代史上最惊心动魄的波澜半世纪：从改革春风吹拂、沿海商品大潮、千禧世贸腾飞、")
        print(f"  到四万亿房产狂奔、移动互联百团大战，直至晚年目睹人工智能与老龄化纵深。所有的个人拼搏，皆深刻映照着时代的风速。")'''
    new_reflect = '''    print(f"\\n{Color.CYAN}【 时代长河坐标 】{Color.RESET}")
    _birth_era = resolve_era(player.birth_year)
    _death_era = resolve_era(end_year)
    _eras = list_eras_between(player.birth_year, end_year)
    print(f"  {player.name}于 {format_year_month(player.birth_year, _bmonth)} 降生于【{player.origin['title']}】。")
    print(f"  出生之时的天下底色是「{_birth_era[0]}」——{_birth_era[1]}")
    print(f"  此后 {player.age} 年间，其一生先后穿越 {len(_eras)} 重大时代：{' → '.join(_eras)}。")
    if _death_era[0] != _birth_era[0]:
        print(f"  辞世之时，世道已是「{_death_era[0]}」——{_death_era[1]}")
    print(f"  {_cfg['desc']}")
    print(f"  大时代每一次翻覆重构，都在这一个普通生命的悲欢离合里，留下了深浅不一的年轮。")'''
    assert old_reflect in py, "ending reflection block not found"
    py = py.replace(old_reflect, new_reflect, 1)

    # 6b. 货币单位随纪元变化
    assert '    print(f"  积累财富净值: {player.wealth:.1f} 万元")' in py
    py = py.replace(
        '    print(f"  积累财富净值: {player.wealth:.1f} 万元")',
        '    print(f"  积累财富净值: {player.wealth:.1f} {wealth_unit(player.epoch_mode)}")', 1)
    _old2 = '    print(f"  盖棺定论：累积财富净值 {player.wealth:.1f} 万元，心智 {int(player.intellect)}，心安 {int(player.happiness)}，气运 {int(player.luck)}。山川日月知你曾深情走过。")'
    assert _old2 in py
    py = py.replace(
        _old2,
        '    print(f"  盖棺定论：累积财富净值 {player.wealth:.1f} {wealth_unit(player.epoch_mode)}，心智 {int(player.intellect)}，心安 {int(player.happiness)}，气运 {int(player.luck)}。山川日月知你曾深情走过。")', 1)
    print("  patched: epoch-aware currency unit (cli)")

    # 6c. 人生轨迹关键词扩展（覆盖先秦至近代语汇）
    _py_old = '        if any(w in ch_text for w in ["考编", "公务员", "体制", "军旅", "入伍", "纪检", "行政", "公职", "团长", "协调官", "防御", "上岸", "保供"]):\n            player.track_scores["体制政务"] += 2\n        elif any(w in ch_text for w in ["经商", "淘宝", "电商", "创业", "个体户", "操盘", "股市", "商海", "小行星", "矿业", "水务", "买房", "信托"]):\n            player.track_scores["商海实业"] += 2\n        elif any(w in ch_text for w in ["无线电", "实验室", "论文", "科研", "工程师", "算法", "智脑", "黑客", "聚变", "脑机", "量子"]):\n            player.track_scores["学术科技"] += 2\n        elif any(w in ch_text for w in ["乐队", "摇滚", "武侠", "自由", "海岛", "江湖", "茶楼", "房车", "诗社", "民宿"]):\n            player.track_scores["文艺江湖"] += 2'
    _py_new = '        if any(w in ch_text for w in ["考编", "公务员", "体制", "军旅", "入伍", "纪检", "行政", "公职", "团长", "协调官", "防御", "上岸", "保供", "科举", "功名", "为吏", "衙门", "官场", "朝廷", "仕途", "幕僚", "举人", "进士", "孝廉", "征辟", "辟召", "刺史", "太守", "县令", "士大夫", "戍边", "烽燧", "投军", "从军", "行伍", "参军", "支前", "干部", "大队", "公社", "革委会", "编制", "出仕"]):\n            player.track_scores["体制政务"] += 2\n        elif any(w in ch_text for w in ["经商", "淘宝", "电商", "创业", "个体户", "操盘", "股市", "商海", "小行星", "矿业", "水务", "买房", "信托", "首富", "红利", "商号", "票号", "盐铁", "牙行", "市舶", "货殖", "贩运", "商队", "胡商", "绸缎", "茶马", "当铺", "钱庄", "作坊", "机户", "铺子", "买卖", "田产", "织造", "十三行", "合伙", "开厂", "车间", "技术员", "承包", "学徒", "柜上"]):\n            player.track_scores["商海实业"] += 2\n        elif any(w in ch_text for w in ["无线电", "实验室", "论文", "科研", "工程师", "算法", "智脑", "黑客", "聚变", "脑机", "量子", "质子", "核能", "读书", "经书", "竹简", "著述", "治学", "书院", "私塾", "蒙学", "游学", "太学", "拜师", "医术", "本草", "郎中", "针灸", "算学", "历法", "图纸", "夜校", "师范", "学堂"]):\n            player.track_scores["学术科技"] += 2\n        elif any(w in ch_text for w in ["乐队", "摇滚", "武侠", "自由", "海岛", "江湖", "茶楼", "房车", "诗社", "民宿", "艺术", "写诗", "诗词", "书画", "琴", "社戏", "游侠", "隐逸", "归隐", "山水", "田园", "寺院", "清谈", "雅集", "杂剧", "刻书", "藏书", "戏班", "票友"]):\n            player.track_scores["文艺江湖"] += 2'
    assert _py_old in py, "python track block not found"
    py = py.replace(_py_old, _py_new, 1)
    print("  patched: career-track keywords (cli)")

    # 6d. 轨迹权重再平衡
    _py_tails = [
        ('"编制", "出仕"]', '"编制", "出仕", "差役", "里正", "保长", "粮长", "驿丞", "公文", "文书", "官"]'),
        ('"学徒", "柜上"]', '"学徒", "柜上", "行商", "验货", "记账", "货价", "借贷", "告贷", "典当", "田契", "田亩", "租佃", "钱粮", "贩货", "营生"]'),
        ('"夜校", "师范", "学堂"]', '"夜校", "师范", "学堂", "抄书", "苦读", "灯油", "方剂", "匠作", "营造", "先生", "游历", "问道"]'),
        ('"刻书", "藏书", "戏班", "票友"]', '"刻书", "藏书", "戏班", "票友", "诗酒", "雅集", "田园", "寺院", "归隐", "诗书", "游历", "闲云"]'),
    ]
    for _a, _b in _py_tails:
        assert _a in py, "track list tail not found: " + _a
        py = py.replace(_a, _b, 1)
    for _k in ("体制政务", "商海实业", "学术科技", "文艺江湖"):
        _o = 'player.track_scores["%s"] += 2' % _k
        _n = 'player.track_scores["%s"] += 4' % _k
        assert _o in py, "track weight not found: " + _k
        py = py.replace(_o, _n, 1)
    print("  patched: career-track weighting (cli)")

    # 7. 生平纪传里的年份也带月份信息
    old_bio = '''    print(f"  {player.name}降生于【{player.origin['title']}】，{player.origin.get('flavor', '')}，骨子里带着【{player.trait['name']}】的特质。")'''
    new_bio = '''    print(f"  {player.name}降生于【{player.origin['title']}】（{format_year_month(player.birth_year, _bmonth)}）。{player.origin.get('flavor', '')}骨子里带着【{player.trait['name']}】的特质。")'''
    assert old_bio in py, "bio line not found"
    py = py.replace(old_bio, new_bio, 1)

    # 8. 顶部说明
    old_doc = '''浮生录 (Lifepath) · 命令行文字人生模拟器（过去风云与未来科幻双纪元版）
支持自主选择或随机投掷到【过去历史纪元】与【未来科幻纪元】。'''
    new_doc = '''浮生录 (Lifepath) · 命令行文字人生模拟器（文明五大纪元 · 从华夏溯源到星海跃迁）
支持自主选择或随机投掷到【先秦汉唐】【宋韵明清】【近代破晓】【当代腾飞】【未来星海】，
出生年份在纪元区间内全域随机、出生月份随机；一生随年代推移自动切换时代背景与事件池。'''
    if old_doc in py:
        py = py.replace(old_doc, new_doc, 1)
        print("  patched: docstring")

    open(path, 'w', encoding='utf-8').write(py)
    print("life_game.py: %d -> %d chars (+%d)" % (orig, len(py), len(py) - orig))


if __name__ == '__main__':
    main()
