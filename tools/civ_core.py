# -*- coding: utf-8 -*-
"""浮生录 · 文明纪元核心数据与代码生成器
用于同时生成 index.html (JS) 与 life_game.py (Python) 所需的：
  1. 五大文明纪元配置
  2. 从公元前 1600 年至公元 2150 年无间断的连续时代背景解析表
  3. 年份/月份格式化（公元前 / 公元）
"""

# ---------------------------------------------------------------- 五大文明纪元
EPOCHS = [
    {
        "id": "ancient",
        "name": "先秦汉唐 · 华夏奠基",
        "sub_title": "公元前1600年 ~ 公元907年",
        "min_year": -1600,
        "max_year": 907,
        "badge": "青铜风骨 · 盛唐万邦",
        "desc": "武王伐纣、诸子百家争鸣、秦皇一统、大汉雄风凿通西域、盛唐长安万国来朝。",
        "color": "amber",
        "icon": "⚱️",
        "names": ["子墨", "季札", "无咎", "叔夜", "伯禽", "仲卿", "慕之", "清和", "阿禾", "长卿"],
    },
    {
        "id": "premodern",
        "name": "宋韵明清 · 市井千帆",
        "sub_title": "公元960年 ~ 公元1911年",
        "min_year": 960,
        "max_year": 1911,
        "badge": "繁华市井 · 刺桐海丝",
        "desc": "汴京清明上河、大宋风雅格物、郑和远洋宝船、江南机杼与红楼梦回帝制夕阳。",
        "color": "emerald",
        "icon": "🏮",
        "names": ["文昭", "仲舒", "念祖", "砚秋", "守拙", "清嘉", "德昌", "素心", "衡之", "婉卿"],
    },
    {
        "id": "modern",
        "name": "近代破晓 · 烽火涅槃",
        "sub_title": "公元1912年 ~ 公元1977年",
        "min_year": 1912,
        "max_year": 1977,
        "badge": "辛亥觉醒 · 浴血奠基",
        "desc": "民国风雷、五四新文化破晓、十四载抗战御侮、新中国一五计划与大院拓荒岁月。",
        "color": "rose",
        "icon": "🌅",
        "names": ["立本", "振华", "砚君", "望舒", "复生", "慕先", "志远", "素秋", "觉民", "毓秀"],
    },
    {
        "id": "contemporary",
        "name": "当代腾飞 · 浪潮狂飙",
        "sub_title": "公元1978年 ~ 公元2035年",
        "min_year": 1978,
        "max_year": 2035,
        "badge": "包产到户 · 世界工厂",
        "desc": "改革春风拂面、特区下海淘金、加入世贸大国崛起、移动互联百团大战与智算新质。",
        "color": "sky",
        "icon": "🏙️",
        "names": ["陈远", "林栖", "陆明舟", "沈清弦", "许念安", "周子墨", "苏晚亭", "宋平", "唐立本", "顾长风"],
    },
    {
        "id": "future",
        "name": "未来星海 · 戴森纪元",
        "sub_title": "公元2036年 ~ 公元2150年",
        "min_year": 2036,
        "max_year": 2150,
        "badge": "太空天梯 · 戴森跃迁",
        "desc": "常温超导聚变并网、太空电梯贯通、火星农场穹顶、量子脑机自组织与恒星戴森云。",
        "color": "purple",
        "icon": "🚀",
        "names": ["星野", "原野", "艾柯", "零壹", "黎光", "沐辰", "陆知远", "凌云", "苏黎", "纪尘"],
    },
]

# -------------------------------------------- 连续时代背景解析表（上限为开区间）
# 每项: (year_upper_exclusive, 名称, 描述)。按年份升序排列，最后一项兜底 (None)。
GRAND_ERA_BUCKETS = [
    (-1600, "华夏破晓 · 禹画九州",
     "大禹治水疏导江河，定九州铸九鼎，泥陶与早期玉器诉说着文明开端的朴拙与坚韧。"),
    (-1046, "殷商青铜 · 占卜甲骨",
     "洹水之滨甲骨刻辞，青铜重器饕餮纹神秘庄重，巫祝与王权在祭祀与征伐中奠基礼仪雏形。"),
    (-771, "西周分封 · 礼乐井田",
     "武王克商封建万邦，周公制礼作乐，宗法井田井然有序，郁郁乎文哉而文明大备。"),
    (-476, "春秋争霸 · 百家争鸣",
     "诸侯争盟礼崩乐坏，孔丘问道老聃，士阶层崛起，思想星空迸发人类童年最璀璨的光芒。"),
    (-221, "战国兼并 · 铁血大争",
     "七雄并立商鞅变法，合纵连横名将辈出，郡县初萌，华夏在金戈铁马中奔向终极一统。"),
    (-202, "秦扫六合 · 帝国初成",
     "始皇帝车同轨书同文，修万里长城筑直道，废分封立郡县，开启两千年中央集权大一统。"),
    (9, "大汉雄风 · 丝路凿空",
     "文景休养汉武远拓，张骞策马绝域西域，卫青霍去病封狼居胥，丝绸之路首通亚欧大陆。"),
    (220, "光武中兴 · 经纬通达",
     "洛阳古都经学兴盛，蔡伦造纸张衡候风，班超投笔从戎定远三十六国，儒术与豪族相融。"),
    (280, "三国风云 · 英雄逐鹿",
     "曹操酾酒临江，刘备三顾草庐，赤壁烈火燎原，群雄在乱世烽烟中留下千古侠义奇谋。"),
    (420, "两晋风流 · 偏安江左",
     "洛神赋与竹林七贤，衣冠南渡金陵建康，名士清谈与山水诗赋在大动荡中绽放异彩。"),
    (581, "南北对峙 · 民族大融",
     "北魏孝文帝汉化改制，南朝烟雨四百八十寺，长城内外血脉相融，大一统生机悄然孕育。"),
    (618, "隋代风帆 · 运河科举",
     "开创科举抡才大典，开凿南北大运河贯通南北，营建大兴长安，气象恢弘却二世而斩。"),
    (755, "盛唐气象 · 万邦来朝",
     "贞观之治开元盛世，李白举杯邀明月，长安朱雀大街胡姬起舞，万国来朝气象万千。"),
    (907, "藩镇割据 · 残唐落日",
     "安史之乱两京陆沉，藩镇割据黄巢揭竿而起，晚唐诗韵苍凉沉郁，繁华落尽余晖脉脉。"),
    (960, "五代十国 · 烽火乱局",
     "朱温篡唐沙陀入主，城头变换大王旗，乱象纷呈却催生南方市井与刻书商业萌芽。"),
    (1127, "北宋风雅 · 汴京繁华",
     "清明上河图虹桥喧闹，苏轼赋赤壁，瓦舍勾栏百戏杂陈，活字印刷与指南针泽被后世。"),
    (1279, "南宋偏安 · 海丝千帆",
     "西湖歌舞与岳飞满江红，泉州刺桐港千帆竞发，海运航路遍及印度洋，富庶冠绝当世。"),
    (1368, "大元一统 · 欧亚驿道",
     "忽必烈定都大都，开辟横跨欧亚大驿道，马可波罗惊叹东方繁盛，杂剧元曲唱彻街巷。"),
    (1644, "大明风华 · 远洋郑和",
     "太祖布衣起兵，成祖永乐大典，郑和七下西洋宝船扬帆，江南机杼声中萌生新的萌芽。"),
    (1840, "康乾盛世 · 红楼斜阳",
     "人口突破三亿疆域辽阔，编纂四库全书，红楼梦笔力惊神，然闭关锁国已落后于世界大潮。"),
    (1912, "晚清危局 · 变法求存",
     "鸦片战争炮声惊醒天朝，洋务运动自强求富，甲午海战、辛亥秋风，两千年帝制轰然崩塌。"),
    (1937, "民国风雷 · 思想破晓",
     "新文化运动德先生赛先生震荡古老神州，白话文觉醒，黄埔风云激荡，实业救国步履维艰。"),
    (1949, "烽火抗战 · 浴血奠基",
     "十四年抗战御侮血肉筑长城，台儿庄百团大战，三大战役定乾坤，民族在血火中涅槃站立。"),
    (1958, "建国初期 · 一五筑基",
     "没收官僚资本土改归农，抗美援朝保家卫国，苏联援建重点工厂开工，红旗招展百废俱兴。"),
    (1966, "大庆精神 · 自力更生",
     "铁人王进喜跃进泥浆，原子弹大漠爆鸣，全国人民勒紧裤带自力更生，独立工业体系初成。"),
    (1978, "风雨激荡 · 红砖岁月",
     "凭票供应与粮本油票，红砖大院广播操与样板戏，千百万青年上山下乡磨砺筋骨。"),
    (1984, "真理讨论 · 春风破冰",
     "小岗村大包干与十一届三中全会，恢复高考改变千万学子命运，喇叭裤与流行乐悄然传遍。"),
    (1992, "商品初潮 · 特区拔地",
     "价格双轨制松动，民间个体户提皮包闯天下，深圳特区高楼平地起，商品意识全面觉醒。"),
    (1998, "南方谈话 · 市场狂潮",
     "春天的故事响彻神州，大批体制内骨干下海淘金，股票交易所开门红，沿海迎来狂飙发展。"),
    (2003, "世纪之交 · 世贸扬帆",
     "国企下岗阵痛与世纪之交相撞，加入WTO后外贸代工厂遍地开花，中国正式成为世界工厂。"),
    (2010, "北京奥运 · 四万亿潮",
     "鸟巢烟花点亮苍穹，四万亿基建全面铺开，高铁大网向全国延伸，房地产狂飙揭开大幕。"),
    (2016, "移动互联 · 创业神话",
     "智能手机普及与移动支付颠覆日常，百团大战风起云涌，大众创业催生无数科技风口神话。"),
    (2023, "动荡考验 · 产业洗牌",
     "疫情风波与全球产业链重构，教培互联网地产退潮，考公稳健与内生硬核制造成为共识。"),
    (2035, "生成式AI · 智算新质",
     "国产大模型颠覆知识脑力，新能源车横扫全球，商业航天与深空空间站并进，迈向高阶现代。"),
    (2045, "常温超导 · 聚变初并",
     "商业托卡马克聚变堆首度向城市群并网供电，常温超导输电网贯通，大城市建起恒温穹顶。"),
    (2055, "太空天梯 · 地月微重",
     "赤道太空电梯贯通低轨，微重力芯片晶圆厂常态生产，月球南极氦-3采掘船队往返穿梭。"),
    (2065, "神经脑机 · 算力配额",
     "视网膜脑机接口成为入世标配，全球碳积分与算力账户直接绑定，肉体与数据分化显现。"),
    (2075, "火星农业 · 外星拓荒",
     "水手峡谷基地人口突破两百万，地火航线常态化轮渡，年轻人在地球引力与异星自由间抉择。"),
    (2085, "自组超脑 · 硅基共治",
     "中央分布式超脑自主接管全球能源与司法调度，算法特区与旧人类自由城邦形成二元平衡。"),
    (2100, "强恒星暴 · 旧网归寂",
     "数十年一遇的超强太阳磁暴冲击内太阳系，行星偏转护盾彻夜泛起极光，考验文明抗灾韧性。"),
    (2110, "半人马座 · 星际点火",
     "人类首艘亚光速恒星际巨舰点火升空飞向比邻星，火种散播银河，正式迈向多恒星纪元。"),
    (None, "戴森云环 · 终幕跃迁",
     "人造能量金环环绕恒星熠熠生辉，戴森云初具规模，碳硅同辉，生命形式迈向全新维度。"),
]


def resolve_era(year):
    """返回 (name, desc)，任意年份（含公元前）均有归属，无间断。"""
    for upper, name, desc in GRAND_ERA_BUCKETS:
        if upper is None or year < upper:
            return name, desc
    return GRAND_ERA_BUCKETS[-1][1], GRAND_ERA_BUCKETS[-1][2]


# ------------------------------------------------------------------ 格式化工具
def format_year_month(year, month):
    ms = "%d月" % month
    if year < 0:
        return "公元前 %d 年 %s" % (abs(year), ms)
    if year == 0:
        return "公元元年 %s" % ms
    return "公元 %d 年 %s" % (year, ms)


def format_year_only(year):
    if year < 0:
        return "公元前 %d 年" % abs(year)
    if year == 0:
        return "公元元年"
    return "公元 %d 年" % year


# ------------------------------------------------------------------ 代码生成
def js_str(s):
    """转 Python 字符串为安全的 JS 双引号字符串字面量。"""
    s = s.replace("\\n", "\n")
    out = []
    for ch in s:
        if ch == "\\":
            out.append("\\\\")
        elif ch == '"':
            out.append('\\"')
        elif ch == "\n":
            out.append("\\n")
        elif ch == "\r":
            out.append("")
        elif ch == "\t":
            out.append("\\t")
        else:
            out.append(ch)
    return '"' + "".join(out) + '"'


def py_str(s):
    """转 Python 字符串为安全的 Python 双引号字面量。"""
    s = s.replace("\\n", "\n")
    out = []
    for ch in s:
        if ch == "\\":
            out.append("\\\\")
        elif ch == '"':
            out.append('\\"')
        elif ch == "\n":
            out.append("\\n")
        elif ch == "\r":
            out.append("")
        elif ch == "\t":
            out.append("\\t")
        else:
            out.append(ch)
    return '"' + "".join(out) + '"'


STAT_KEYS = ("health", "wealth", "intellect", "happiness", "luck", "rep")


def normalize_choice(ch):
    """把生成器产出的选择项（嵌套 chance / succ_eff 形式）规整为扁平结构。"""
    if not isinstance(ch, dict):
        raise TypeError("choice must be dict, got %r" % type(ch))

    def g(*names, **kw):
        dflt = kw.get("default")
        for n in names:
            if n in ch and ch[n] is not None:
                return ch[n]
        return dflt

    chance = ch.get("chance") or {}
    base = chance.get("base", g("base", default=70)) or 70

    succ_eff = ch.get("succ_eff")
    if not isinstance(succ_eff, dict):
        succ_eff = ch.get("successEffect")
    if not isinstance(succ_eff, dict):
        succ_eff = {}
        for k in STAT_KEYS:
            key = "succ" + k.capitalize()
            if key in ch:
                succ_eff[k] = ch[key]

    fail_eff = ch.get("fail_eff")
    if not isinstance(fail_eff, dict):
        fail_eff = ch.get("failEffect")
    if not isinstance(fail_eff, dict):
        fail_eff = {}
        for k in STAT_KEYS:
            key = "fail" + k.capitalize()
            if key in ch:
                fail_eff[k] = ch[key]

    def num(d, k):
        try:
            return float(d.get(k, 0) or 0)
        except (TypeError, ValueError):
            return 0.0

    return {
        "text": str(g("text", default="")),
        "risk": str(g("risk", "risk_label", "riskLevel", default="审时度势 · 各有代价")),
        "base": int(round(float(base))),
        "int_div": int(round(float(chance.get("int_div", g("int_div", default=0) or 0) or 0))),
        "luck_bonus": int(round(float(chance.get("luck_bonus", g("luck_bonus", default=0) or 0) or 0))),
        "health_bonus": int(round(float(chance.get("health_bonus", g("health_bonus", default=0) or 0) or 0))),
        "succ_fb": str(g("succ_fb", "succFb", "successFeedback", default="")),
        "fail_fb": str(g("fail_fb", "failFb", "failFeedback", default="")),
        "succ_eff": {k: num(succ_eff, k) for k in STAT_KEYS},
        "fail_eff": {k: num(fail_eff, k) for k in STAT_KEYS},
        "tag_succ": str(g("tag_succ", "tagSucc", "tagSuccess", default="顺势而为")),
        "tag_fail": str(g("tag_fail", "tagFail", "tagFail", default="另寻他途")),
        "is_key": bool(g("is_key", "isKey", default=False)),
    }


def normalize_event(ev, stage_index=0):
    """规整事件 dict。"""
    period_default = {
        0: "幼年启蒙", 1: "童年韶光", 2: "少年分流", 3: "成人立志",
        4: "青春韶华", 5: "初涉人世", 6: "成家立业", 7: "三十而立",
        8: "负重前行", 9: "中年险滩", 10: "动荡考验", 11: "知命之年",
        12: "花甲在望", 13: "桑榆晚景", 14: "古稀沧桑", 15: "夕阳辞章",
    }[max(0, min(15, stage_index))]
    choices = [normalize_choice(c) for c in ev.get("choices", [])]
    return {
        "period": str(ev.get("period") or period_default),
        "title": str(ev.get("title") or "命运的路口"),
        "narrative": str(ev.get("narrative") or ev.get("desc") or ""),
        "choices": choices,
        "_age_rel": DEFAULT_STAGE_AGES[max(0, min(15, stage_index))],
    }


DEFAULT_STAGE_AGES = [6, 10, 15, 18, 21, 24, 27, 31, 36, 40, 45, 51, 58, 66, 74, 80]


def _eff_expr(eff):
    parts = []
    for k in STAT_KEYS:
        v = eff.get(k, 0) or 0
        if v:
            parts.append("%s: %s" % (k, ("%g" % v)))
    return "{ " + ", ".join(parts) + " }"


def _eff_expr_py(eff):
    parts = []
    for k in STAT_KEYS:
        v = eff.get(k, 0) or 0
        if v:
            parts.append('"%s": %s' % (k, ("%g" % v)))
    return "{" + ", ".join(parts) + "}"


def _chance_expr_js(ch):
    base = ch["base"]
    if base >= 100:
        return "(p) => 100"
    terms = [str(base)]
    if ch["int_div"]:
        terms.append("(p.intellect > 50 ? Math.floor((p.intellect - 50) / %d) : 0)" % ch["int_div"])
    if ch["luck_bonus"]:
        terms.append("(p.luck > 50 ? %d : 0)" % ch["luck_bonus"])
    if ch["health_bonus"]:
        terms.append("(p.health > 60 ? %d : 0)" % ch["health_bonus"])
    return "(p) => " + " + ".join(terms)


def _chance_expr_py(ch):
    base = ch["base"]
    if base >= 100:
        return "lambda p: 100"
    terms = [str(base)]
    if ch["int_div"]:
        terms.append("(int((p.intellect - 50) / %d) if p.intellect > 50 else 0)" % ch["int_div"])
    if ch["luck_bonus"]:
        terms.append("(%d if p.luck > 50 else 0)" % ch["luck_bonus"])
    if ch["health_bonus"]:
        terms.append("(%d if p.health > 60 else 0)" % ch["health_bonus"])
    return "lambda p: " + " + ".join(terms)


def risk_label(ch):
    if ch["base"] >= 100:
        return "%s · 稳妥必成" % ch["risk"]
    return "%s · 成功率 %d%%" % (ch["risk"], ch["base"])


def event_to_js(ev, stage_index=0):
    ev = normalize_event(ev, stage_index)
    choices = []
    for ch in ev["choices"]:
        parts = [
            "text: %s" % js_str(ch["text"]),
            "riskLevel: %s" % js_str(risk_label(ch)),
            "successChance: %s" % _chance_expr_js(ch),
            "successFeedback: %s" % js_str(ch["succ_fb"]),
            "failFeedback: %s" % js_str(ch["fail_fb"]),
            "successEffect: %s" % _eff_expr(ch["succ_eff"]),
            "failEffect: %s" % _eff_expr(ch["fail_eff"]),
            "tagSuccess: %s" % js_str(ch["tag_succ"]),
            "tagFail: %s" % js_str(ch["tag_fail"]),
            "isKey: %s" % ("true" if ch["is_key"] else "false"),
        ]
        choices.append("          { " + ", ".join(parts) + " }")
    return (
        "      {\n"
        "        period: %s,\n"
        "        title: %s,\n"
        "        narrative: (p, y) => %s,\n"
        "        choices: [\n%s\n        ]\n"
        "      }"
    ) % (js_str(ev["period"]), js_str(ev["title"]), js_str(ev["narrative"]), ",\n".join(choices))


def event_to_py(ev, stage_index=0):
    ev = normalize_event(ev, stage_index)
    choices = []
    for ch in ev["choices"]:
        parts = [
            '            "text": %s' % py_str(ch["text"]),
            '            "risk_label": %s' % py_str(risk_label(ch)),
            '            "calc_chance": %s' % _chance_expr_py(ch),
            '            "succ_feedback": %s' % py_str(ch["succ_fb"]),
            '            "succ_eff": %s' % _eff_expr_py(ch["succ_eff"]),
            '            "fail_feedback": %s' % py_str(ch["fail_fb"]),
            '            "fail_eff": %s' % _eff_expr_py(ch["fail_eff"]),
            '            "tag_succ": %s' % py_str(ch["tag_succ"]),
            '            "tag_fail": %s' % py_str(ch["tag_fail"]),
            '            "is_key": %s' % ("True" if ch["is_key"] else "False"),
        ]
        choices.append("          {\n" + ",\n".join(parts) + "\n          }")
    return (
        "    {\n"
        '        "age_rel": %d,\n'
        '        "period": %s,\n'
        '        "title": %s,\n'
        '        "narrative": %s,\n'
        '        "choices": [\n%s\n        ]\n'
        "    }"
    ) % (ev["_age_rel"], py_str(ev["period"]), py_str(ev["title"]),
         py_str(ev["narrative"]), ",\n".join(choices))


def region_to_js(r):
    stat = r.get("stat", {})
    keys = ", ".join("%s: %s" % (k, "%g" % stat[k]) for k in stat)
    return "{ name: %s, desc: %s, stat: { %s } }" % (js_str(r["name"]), js_str(r["desc"]), keys)


def strata_to_js(s):
    st = s.get("stat", {})
    keys = ", ".join("%s: %s" % (k, "%g" % st.get(k, 50)) for k in STAT_KEYS)
    return (
        "{\n"
        "        title: %s,\n"
        "        desc: %s,\n"
        "        statMod: { %s },\n"
        "        trait: %s\n"
        "      }"
    ) % (js_str(s["title"]), js_str(s["desc"]), keys, js_str(s.get("trait", "坚韧自持")))


def region_to_py(r):
    stat = r.get("stat", {})
    keys = ", ".join('"%s": %s' % (k, "%g" % stat[k]) for k in stat)
    return '    {"name": %s, "desc": %s, "stat": {%s}}' % (
        py_str(r["name"]), py_str(r["desc"]), keys)


def strata_to_py(s):
    st = s.get("stat", {})
    keys = ", ".join('"%s": %s' % (k, "%g" % st.get(k, 50)) for k in STAT_KEYS)
    return '    {"title": %s, "desc": %s, "stat": {%s}, "trait": %s}' % (
        py_str(s["title"]), py_str(s["desc"]), keys, py_str(s.get("trait", "坚韧自持")))
