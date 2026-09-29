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
"""纪元内容「代码包」生成器（JS / Python 双端共用）。

内容源：tools/civ_meta_*.py + tools/civ_stages_*.py + tools/civ_women_*.py
输出：data/epochs.js（网页端数据层）、fsl_epochs.py（命令行端数据层）
两端共用同一份内容源，因此叙事与数值完全一致。
"""

import civ_core as C

STAT_KEYS = ("health", "wealth", "intellect", "happiness", "luck", "rep")

NEW_EPOCHS = ("ancient", "premodern", "modern")

DATA = {}

def load_data():
    import civ_loader
    DATA.update(civ_loader.load_all())
    for eid in NEW_EPOCHS:
        d = DATA[eid]
        print("  %s: regions=%d strata=%d stages=%d events=%d"
              % (eid, len(d.REGIONS), len(d.STRATA), len(d.STAGE_EVENTS), d.event_count()))
    load_women()
    for eid in WOMEN_EPOCHS:
        print("  %s: women-events=%d" % (eid, len(WOMEN[eid])))

def build_js_pack():
    L = []
    L.append("    // ==================== 文明五大纪元 · 从华夏溯源到星海跃迁 ====================")
    L.append("    const CIVILIZATION_EPOCHS = [")
    for e in C.EPOCHS:
        L.append("      {")
        L.append("        id: %s," % C.js_str(e["id"]))
        L.append("        name: %s," % C.js_str(e["name"]))
        L.append("        subTitle: %s," % C.js_str(e["sub_title"]))
        L.append("        minYear: %d," % e["min_year"])
        L.append("        maxYear: %d," % e["max_year"])
        L.append("        badge: %s," % C.js_str(e["badge"]))
        L.append("        desc: %s," % C.js_str(e["desc"]))
        L.append("        colorClass: %s," % C.js_str(e["color"]))
        L.append("        eraIcon: %s," % C.js_str(e["icon"]))
        L.append("        legacyNoun: %s," % C.js_str({
            "ancient": "青史竹简", "premodern": "族谱与方志", "modern": "厂志与家书",
            "contemporary": "市井与家书", "future": "星尘档案",
        }[e["id"]]))
        L.append("        namesMale: [%s]," % ", ".join(C.js_str(n) for n in e["names_male"]))
        L.append("        namesFemale: [%s]" % ", ".join(C.js_str(n) for n in e["names_female"]))
        L.append("      },")
    L.append("    ];")
    L.append("")
    L.append("    // 16 个生命阶段的默认年龄（用于 Python 侧对齐，JS 侧由随机时间线覆盖）")
    L.append("    const EPOCH_STAGE_AGES = [6, 10, 15, 18, 21, 24, 27, 31, 36, 40, 45, 51, 58, 66, 74, 80];")
    L.append("")
    L.append("    function getEpochConfig(id) {")
    L.append("      return CIVILIZATION_EPOCHS.find(e => e.id === id) || CIVILIZATION_EPOCHS[3];")
    L.append("    }")
    L.append("    // 由具体年份反查所属纪元（公元前1600 ~ 公元2150，无间断）")
    L.append("    function getEpochIdForYear(year) {")
    L.append("      for (const e of CIVILIZATION_EPOCHS) { if (year <= e.maxYear) return e.id; }")
    L.append("      return CIVILIZATION_EPOCHS[CIVILIZATION_EPOCHS.length - 1].id;")
    L.append("    }")
    L.append("    function isFutureEpoch(id) { return id === \"future\"; }")
    L.append("    function isClassicalEpoch(id) { return id === \"ancient\" || id === \"premodern\" || id === \"modern\"; }")
    L.append("    function pickEpochName(id, gender = 'male') {")
    L.append("      const cfg = getEpochConfig(id);")
    L.append("      const pool = (gender === 'female' ? cfg.namesFemale : cfg.namesMale) || cfg.names || [];")
    L.append("      return pool[Math.floor(Math.random() * pool.length)] || \"无名\";")
    L.append("    }")
    L.append("")
    L.append("    // ---- 连续时代背景表（覆盖公元前1600年至公元2150年及以外，全无间断）----")
    L.append("    const GRAND_ERA_TABLE = [")
    for upper, name, desc in C.GRAND_ERA_BUCKETS:
        L.append("      [%s, %s, %s]," % ("null" if upper is None else upper, C.js_str(name), C.js_str(desc)))
    L.append("    ];")
    L.append("")
    L.append("    function resolveEraDetails(year, epochMode) {")
    L.append("      for (let i = 0; i < GRAND_ERA_TABLE.length; i++) {")
    L.append("        const row = GRAND_ERA_TABLE[i];")
    L.append("        if (row[0] === null || year < row[0]) return { name: row[1], desc: row[2] };")
    L.append("      }")
    L.append("      const last = GRAND_ERA_TABLE[GRAND_ERA_TABLE.length - 1];")
    L.append("      return { name: last[1], desc: last[2] };")
    L.append("    }")
    L.append("")
    L.append("    function formatYearOnly(year) {")
    L.append("      const y = Math.round(year);")
    L.append("      if (y < 0) return `公元前 ${Math.abs(y)} 年`;")
    L.append("      if (y === 0) return '公元元年';")
    L.append("      return `公元 ${y} 年`;")
    L.append("    }")
    L.append("    function formatYearMonth(year, month) {")
    L.append("      const m = month || 1;")
    L.append("      return `${formatYearOnly(year)} ${m}月`;")
    L.append("    }")
    L.append("    function randomMonth() { return Math.floor(Math.random() * 12) + 1; }")
    L.append("")
    L.append("    // 一生穿越过的所有大时代（按时间顺序去重）")
    L.append("    function listErasBetween(y0, y1) {")
    L.append("      const out = [];")
    L.append("      const a = Math.round(Math.min(y0, y1)), b = Math.round(Math.max(y0, y1));")
    L.append("      for (let y = a; y <= b; y++) {")
    L.append("        const n = resolveEraDetails(y, null).name;")
    L.append("        if (out[out.length - 1] !== n) out.push(n);")
    L.append("      }")
    L.append("      if (out.length === 0) out.push(resolveEraDetails(a, null).name);")
    L.append("      return out;")
    L.append("    }")
    L.append("")

    # 各纪元出身表
    for eid in NEW_EPOCHS:
        mod = DATA[eid]
        L.append("    // ---- %s 出身地域（8）与门第阶层（10）----" % getattr(mod, "EPOCH_ID", eid))
        L.append("    const %s_REGIONS = [" % eid.upper())
        L.append(",\n".join(C.region_to_js(r) for r in mod.REGIONS))
        L.append("    ];")
        L.append("    const %s_SOCIAL_STRATA = [" % eid.upper())
        L.append(",\n".join(C.strata_to_js(s) for s in mod.STRATA))
        L.append("    ];")
        L.append("")

    # 各纪元 16 阶段事件池
    for eid in NEW_EPOCHS:
        mod = DATA[eid]
        L.append("    // ---- %s 16 大生命阶段事件池（每阶段多个候选，单局随机抽取）----" % eid)
        L.append("    const %s_STAGE_POOLS = [" % eid.upper())
        stages = []
        for i, st in enumerate(mod.STAGE_EVENTS):
            evs = ",\n".join(C.event_to_js(ev, i) for ev in st)
            stages.append("      [\n%s\n      ]" % evs)
        L.append(",\n".join(stages))
        L.append("    ];")
        L.append("")

    L.append("    // ---- 出身表 / 事件池 按纪元统一取用 ----")
    L.append("    function getEpochOriginTables(id) {")
    L.append("      if (id === \"ancient\") return { regions: ANCIENT_REGIONS, strata: ANCIENT_SOCIAL_STRATA };")
    L.append("      if (id === \"premodern\") return { regions: PREMODERN_REGIONS, strata: PREMODERN_SOCIAL_STRATA };")
    L.append("      if (id === \"modern\") return { regions: MODERN_REGIONS, strata: MODERN_SOCIAL_STRATA };")
    L.append("      if (id === \"contemporary\") return { regions: PAST_REGIONS, strata: PAST_SOCIAL_STRATA };")
    L.append("      return { regions: FUTURE_REGIONS, strata: FUTURE_SOCIAL_STRATA };")
    L.append("    }")
    L.append("    function getEpochStagePools(id) {")
    L.append("      if (id === \"ancient\") return ANCIENT_STAGE_POOLS;")
    L.append("      if (id === \"premodern\") return PREMODERN_STAGE_POOLS;")
    L.append("      if (id === \"modern\") return MODERN_STAGE_POOLS;")
    L.append("      if (id === \"contemporary\") return PAST_STAGE_POOLS;")
    L.append("      return FUTURE_STAGE_POOLS;")
    L.append("    }")
    L.append("")
    L.append("" )
    L.append("// 各纪元货币单位：避免先秦人生出现「万元」这类时代错位")
    L.append("function wealthUnit(epochId) {")
    L.append('  if (epochId === "ancient") return "两金";')
    L.append('  if (epochId === "premodern") return "两银";')
    L.append('  if (epochId === "modern") return "块银元";')
    L.append('  if (epochId === "contemporary") return "万元";')
    L.append('  return "信用点";')
    L.append("}")
    L.append("")
    L.append("function wealthUnitShort(epochId) {")
    L.append('  if (epochId === "ancient") return "两";')
    L.append('  if (epochId === "premodern") return "两";')
    L.append('  if (epochId === "modern") return "元";')
    L.append('  if (epochId === "contemporary") return "万";')
    L.append('  return "点";')
    L.append("}")
    return "\n".join(L) + "\n"

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
        L.append('        "names_male": [%s],' % ", ".join(C.py_str(n) for n in e["names_male"]))
        L.append('        "names_female": [%s],' % ", ".join(C.py_str(n) for n in e["names_female"]))
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
    L.append("def pick_epoch_name(epoch_id, gender=\"male\"):")
    L.append("    cfg = get_epoch_config(epoch_id)")
    L.append('    key = "names_female" if gender == "female" else "names_male"')
    L.append('    pool = cfg.get(key) or cfg.get("names_male") or []')
    L.append('    return random.choice(pool) if pool else "无名"')
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
    L.append('    gender = "female" if random.random() < 0.5 else "male"')
    L.append("    origin = generate_procedural_origin(epoch_id)")
    L.append("    trait = random.choice(RANDOM_TRAITS)")
    L.append("    return b_year, b_month, gender, origin, trait")
    L.append("")
    L.append("")
    return "\n".join(L)

# ==================== 女性专属处境事件 ====================
WOMEN_EPOCHS = ("ancient", "premodern", "modern", "contemporary", "future")
WOMEN = {}


def load_women():
    """载入五个纪元的女性专属事件（tools/civ_women_<epoch>.py）。"""
    import importlib
    for eid in WOMEN_EPOCHS:
        mod = importlib.import_module("civ_women_" + eid)
        events = list(mod.WOMEN_EVENTS)
        stages = sorted(set(e["stage"] for e in events))
        assert stages == [2, 3, 4, 5, 6, 7, 9, 12], (eid, stages)
        for e in events:
            assert len(e["choices"]) == 2, (eid, e["title"])
        WOMEN[eid] = events
    return WOMEN


def build_women_js():
    L = []
    L.append("    // ==================== 女性专属处境事件（主角为女性时进入该阶段候选池） ====================")
    L.append("    const WOMEN_EVENT_POOLS = {")
    for eid in WOMEN_EPOCHS:
        L.append("      %s: {" % C.js_str(eid))
        stages = {}
        for ev in WOMEN[eid]:
            stages.setdefault(ev["stage"], []).append(ev)
        for st in sorted(stages):
            L.append("        %d: [" % st)
            L.append(",\n".join(C.event_to_js(ev, st) for ev in stages[st]))
            L.append("        ],")
        L.append("      },")
    L.append("    };")
    return "\n".join(L)


def build_women_py():
    L = []
    L.append("# ==================== 女性专属处境事件（主角为女性时进入该阶段候选池） ====================")
    L.append("WOMEN_EVENT_POOLS = {")
    for eid in WOMEN_EPOCHS:
        L.append("    %s: {" % C.py_str(eid))
        stages = {}
        for ev in WOMEN[eid]:
            stages.setdefault(ev["stage"], []).append(ev)
        for st in sorted(stages):
            L.append("        %d: [" % st)
            L.append(",\n".join(C.event_to_py(ev, st) for ev in stages[st]))
            L.append("        ],")
        L.append("    },")
    L.append("}")
    return "\n".join(L)


def build_random_events_js():
    import civ_random_events as R
    L = []
    L.append("    // ==================== 文明五大纪元专属突发偶发事件库 ====================")
    L.append("    const RANDOM_EVENT_POOLS = {")
    for eid, evts in R.RANDOM_EVENT_POOLS.items():
        L.append("      %s: [" % C.js_str(eid))
        for ev in evts:
            eff_parts = []
            for k, v in ev["effect"].items():
                eff_parts.append("%s: %s" % (k, "%g" % v))
            eff_str = "{ " + ", ".join(eff_parts) + " }"
            L.append("        { id: %s, title: %s, tag: %s, desc: %s, effect: %s },"
                     % (C.js_str(ev["id"]), C.js_str(ev["title"]), C.js_str(ev["tag"]), C.js_str(ev["desc"]), eff_str))
        L.append("      ],")
    L.append("    };")
    return "\n".join(L)


def build_random_events_py():
    import civ_random_events as R
    L = []
    L.append("# ==================== 文明五大纪元专属突发偶发事件库 ====================")
    L.append("RANDOM_EVENT_POOLS = {")
    for eid, evts in R.RANDOM_EVENT_POOLS.items():
        L.append("    %s: [" % C.py_str(eid))
        for ev in evts:
            eff_parts = []
            for k, v in ev["effect"].items():
                eff_parts.append('"%s": %s' % (k, "%g" % v))
            eff_str = "{" + ", ".join(eff_parts) + "}"
            L.append('        {"id": %s, "title": %s, "tag": %s, "desc": %s, "effect": %s},'
                     % (C.py_str(ev["id"]), C.py_str(ev["title"]), C.py_str(ev["tag"]), C.py_str(ev["desc"]), eff_str))
        L.append("    ],")
    L.append("}")
    return "\n".join(L)
