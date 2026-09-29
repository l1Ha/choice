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

# 过去纪元背景
PAST_TIMELINE = {
    1975: ("文革晚期与初苏", "物质匮乏凭票供应，广播里播放样板戏，民间暗潮涌动，期盼春天的微光。"),
    1982: ("改革春风与倒爷潮", "包产到户在全国推行，沿海小商品市场萌动，喇叭裤与流行乐在青年中风靡。"),
    1988: ("物价闯关与商海涌动", "价格双轨制松动，民间现抢购狂潮，第一批敢下海倒货者开始斩获第一桶金。"),
    1992: ("南方谈话与全民下海", "春天的故事响彻神州，大批体制内干部与知识分子下海经商，海南与特区迎淘金潮。"),
    1998: ("国企改革与下岗大潮", "体制重组阵痛蔓延，千百万工人直面下岗转型，大街小巷回荡着'重头再来'的歌声。"),
    2001: ("加入WTO与世界工厂", "中国正式入世，沿海外贸如火如荼，农民工进城与中国制造出海掀起巨澜。"),
    2008: ("北京奥运与四万亿投资", "鸟巢烟花璀璨，四万亿基建落地，高铁全面延伸，房地产迎来狂飙十年。"),
    2015: ("移动互联与大众创业", "智能手机全面普及，移动支付改变日常，'大众创业、万众创新'催生风口狂热。"),
    2020: ("突发疫情与行业洗牌", "教培、地产、大厂相继迎收缩调整，考公热潮席卷，社会回归安全与稳健。"),
    2028: ("AI时代与老龄化纵深", "人工智能接管日常智力工作，老龄化加速，面对不确定性的未来，人们探索心安之道。")
}

# 未来纪元背景 (常温超导、聚变能源、脑机接口、碳配额、深空采矿与数字生命)
FUTURE_TIMELINE = {
    2042: ("脑机义体与聚合穹顶", "常温超导与聚变堆商业并网，大都市被巨型穹顶罩覆，脑机神经元接口成为新生代入世标配。"),
    2048: ("碳税配额与合成蛋白", "全球气候阈值突破，天然肉类变为顶奢，合成蛋白与碳排放配额直接锚定公民信用额度。"),
    2054: ("地月地平线与近地轨道", "地月货运电梯常态运营，无数技术工前往月球南极氦-3矿区，深空采矿重塑全球资本格局。"),
    2060: ("数字永生与合成意识", "首批'思维云端备份'合法化，贫富阶层从生理寿命撕裂到算力时长，老旧碳基人面对前所未有的认知分化。"),
    2068: ("基因定制与仿生迭代", "CRISPR-IV 代际基因编辑普及，定制免疫基因的'纯净种'与原生态碳基人形成隐性就业鸿沟。"),
    2075: ("火星拓荒与深空公约", "火星水手峡谷基地人口破百万，地球老牌巨企与外星拓荒联盟摩擦不断，年轻一代在重力与星际自由间摇摆。"),
    2085: ("量子觉醒与全网智械", "强人工智能突破自指图灵极限，中央智脑自主调度全球基础设施，人类重新探索作为'诗意观察者'的终极价值。"),
    2095: ("恒星风暴与旧网归寂", "强地磁太阳风暴席卷近地空间，云端数据部分失落，幸存者们在废墟与星光中重温古老的实体纸书与真实体温。"),
    2105: ("生物共生与灵境纪元", "人类放弃了纯机械赛博化，转向与合成生物圈深度嵌合，寿命突破百岁门槛，宁静与超越成为文明底色。")
}

# 过去家庭背景池
PAST_REGIONS = [
    ("三线内陆工业基地", "秦岭或太行深山里的红砖厂区，群山环抱，汽笛日夜长鸣", {"health": 2, "intellect": 1}),
    ("江浙水乡沿海古镇", "青石板路旁摇橹的乌篷船，弄堂商贾往来，早早浸润在商品交易的萌芽中", {"wealth": 1.5, "intellect": 3}),
    ("中原农耕沃野平原", "一眼望不到头的麦浪与泥土芳香，父辈面朝黄土背朝天，深知粒粒皆辛苦", {"health": 4, "happiness": 2}),
    ("南粤沿海开放特区", "紧邻港澳的风口浪尖，到处是淘金客匆匆的步伐与粤语叫卖声", {"wealth": 3.0, "luck": 3}),
    ("白山黑水重工业老林", "烟囱耸立的钢城与大煤田，大雪纷飞的冬夜里热腾腾的澡堂与大铁锅", {"health": 3, "rep": 2}),
    ("西南巴蜀青石码头", "川江号子在江面上回荡，茶馆里龙门阵摆得热闹，生活悠闲却暗藏激流", {"happiness": 4, "intellect": 2}),
    ("西北戈壁军垦绿洲", "胡杨林与白杨树庇护下的军垦地，坎儿井流水清冽，见惯了长风与星河", {"health": 4, "rep": 3}),
    ("京畿皇城根胡同巷陌", "斑驳的朱门与鸽哨掠过天空，长辈在槐树下品茶论国事，市井与朝堂声息相通", {"intellect": 4, "rep": 5})
]

PAST_SOCIAL_STRATA = [
    ("国企大厂八级技工世家", "厂长也要客客气气递烟的技术大拿，工具箱擦得锃亮，手艺过硬骨气硬", {"health": 90, "wealth": 2.5, "intellect": 52, "happiness": 65, "luck": 50, "rep": 50}, "大院情怀"),
    ("世代躬耕贫瘠农户", "手里捧着泥土过活，吃尽了风吹日晒之苦，对'读书进城吃商品粮'有着刻骨执念", {"health": 94, "wealth": 0.4, "intellect": 48, "happiness": 55, "luck": 52, "rep": 32}, "野草劲骨"),
    ("省城书香教书先生门第", "一墙发黄的文史古籍与教案批注，重视修身立德，清贫中透着书卷傲骨与敏锐见识", {"health": 84, "wealth": 5.5, "intellect": 66, "happiness": 58, "luck": 54, "rep": 58}, "书香灵慧"),
    ("敢为人先个体商贩家庭", "最早摆摊卖电子表喇叭裤的弄潮儿，提着蛇皮袋挤绿皮车，在算盘与现金中讨生活", {"health": 88, "wealth": 11.5, "intellect": 55, "happiness": 60, "luck": 58, "rep": 46}, "市井嗅觉"),
    ("机关大院行政干事家庭", "父母任职于地方行政机关，住在一号机关家属楼。言行沉稳讲究方寸，知晓规矩早慧", {"health": 86, "wealth": 7.5, "intellect": 60, "happiness": 62, "luck": 56, "rep": 68}, "洞察人情"),
    ("边防军旅驻扎军烈门第", "挂满军功章的军大衣与清脆的起床军号，家教极严，骨子里流淌着刚正与担当", {"health": 96, "wealth": 4.0, "intellect": 53, "happiness": 56, "luck": 50, "rep": 68}, "铁血脊梁"),
    ("老城回春堂中医世家", "满屋甘草陈皮与青草药香，自幼习得搭脉问诊与望闻问切，看淡生死多怀悲悯", {"health": 92, "wealth": 6.8, "intellect": 63, "happiness": 64, "luck": 54, "rep": 60}, "仁心济世"),
    ("老弄堂巧手钟表锁匠铺", "一盏台灯放大镜前拆装精密发条齿轮，一厘一毫不差，靠真本事在街坊立足", {"health": 85, "wealth": 3.2, "intellect": 64, "happiness": 58, "luck": 52, "rep": 45}, "工匠微雕"),
    ("北方煤铁矿山采掘之家", "头顶矿灯下几百米矿井的硬汉，性格豪迈如酒，视生死兄弟如手足，大口吃肉喝酒", {"health": 92, "wealth": 3.6, "intellect": 47, "happiness": 62, "luck": 48, "rep": 40}, "矿山粗粝"),
    ("地方京剧歌舞团曲艺人家", "后台油彩箱与练功房的飞天水袖，在流行曲浪潮冲击下守望着传统粉墨风华", {"health": 87, "wealth": 4.2, "intellect": 58, "happiness": 66, "luck": 56, "rep": 52}, "粉墨风华")
]

FUTURE_REGIONS = [
    ("近地低轨第二聚合环站", "透过透明抗辐射舷窗俯瞰地球日出日落，常年处于人工离心重力环境", {"intellect": 4, "health": -2}),
    ("东亚中央恒温气候巨穹顶", "数十平方公里的全息天幕屏蔽了地表酸雨，人工微气候四季恒定在22度", {"health": 3, "wealth": 2.0}),
    ("马里亚纳深海核聚变方舟", "沉浸于万米深蓝海沟，伴着深海热液喷口与发光生物，与世隔绝静谧安宁", {"health": 4, "happiness": 3}),
    ("火星水手大峡谷殖民前哨", "红砂岩地表之下的蜂窝防护洞穴，仰望夜空微弱的蓝色地球母星", {"health": 2, "luck": 4}),
    ("月球静海背阴面超导基地", "终年避开强烈太阳直射的永夜环形山，常温超导流水线无声飞速运转", {"intellect": 3, "wealth": 1.5}),
    ("青藏高原稀疏大气聚变中心", "依托地表最高海拔建设的磁约束聚变堆，雪山巍峨，蓝天纯净无瑕", {"health": 5, "happiness": 2}),
    ("地表失控区地下掩体自由邦", "未接入官方超脑云端的废墟防空洞，依靠手工燃油机与古董电子管维系自由", {"intellect": 3, "luck": 5}),
    ("太平洋漂浮人工珊瑚矩阵", "漂浮在赤道洋流上的生物自给自足岛，与基因改造蓝藻群紧密共生", {"happiness": 5, "health": 2})
]

FUTURE_SOCIAL_STRATA = [
    ("低轨聚变管路高级技术工", "负责太空天梯与电磁推进阀的无重力焊接检修，生活在蜂巢舱，渴望攒够地表绿区产权", {"health": 86, "wealth": 4.8, "intellect": 62, "happiness": 54, "luck": 52, "rep": 48}, "真空坚毅"),
    ("次级穹顶垂直藻类农场主", "在受控光照与营养液架间照料高能螺旋藻，远离核心算力区，但保持了天然食物与质朴情感", {"health": 95, "wealth": 2.2, "intellect": 50, "happiness": 66, "luck": 50, "rep": 40}, "大地复归"),
    ("跨国巨企算力中继核心架构师", "为中央神经网络设计容灾拓扑，出入有反重力浮空艇，生活被高昂的义体维护与算力指数绑死", {"health": 82, "wealth": 12.0, "intellect": 72, "happiness": 50, "luck": 55, "rep": 62}, "数据感知"),
    ("地下暗网自由频段游民首领", "拒绝官方神经接口的旧人类守望者，藏身地下维修古董电子仪器与私密通信中继，守卫思想自由", {"health": 88, "wealth": 3.5, "intellect": 65, "happiness": 58, "luck": 60, "rep": 38}, "断网自守"),
    ("深空引力波观测站首席学者", "供职于月背引力波阵列，整夜演算黑洞碰撞与量子微扰，对宇宙充满敬畏，骨子里有着极致求真欲", {"health": 83, "wealth": 11.5, "intellect": 76, "happiness": 52, "luck": 52, "rep": 65}, "宇宙深眸"),
    ("灵境虚拟现实特级织梦大师", "为数百万人编织永不落幕的虚拟感官梦境，现实居室极简，但神经储物柜里存有万千幻界坐标", {"health": 85, "wealth": 9.0, "intellect": 66, "happiness": 68, "luck": 58, "rep": 56}, "幻境编织"),
    ("月球南极重型采矿队工段长", "驾驶重型电磁盾构机开采极地氦-3聚变能源，在月岩深处耐得住极度严寒与绝对死寂", {"health": 93, "wealth": 6.5, "intellect": 54, "happiness": 56, "luck": 50, "rep": 48}, "极地冷淬"),
    ("地月联合行政协调署特派专员", "负责地火关税调停与星际配额调度，掌握前沿星际法规，深谙在硅基逻辑与碳基民众间权衡", {"health": 88, "wealth": 14.5, "intellect": 67, "happiness": 60, "luck": 55, "rep": 75}, "星际权衡"),
    ("深海万米生态方舟维生总监", "在千个大气压的核潜方舟中维护全息生命循环系统，心如止水，拥有超乎常人的定力", {"health": 91, "wealth": 5.8, "intellect": 64, "happiness": 62, "luck": 54, "rep": 46}, "渊底沉潜"),
    ("赛博地下黑诊所义体调试工匠", "地下黑市神经缝合与钛合金骨骼校准大师，看惯了为一副仿生器官押上身家的市井百态", {"health": 87, "wealth": 7.5, "intellect": 65, "happiness": 54, "luck": 56, "rep": 52}, "神机剖解")
]

# ==================== 文明五大纪元 · 从华夏溯源到星海跃迁 ====================
EPOCHS = [
    {
        "id": "ancient",
        "name": "先秦汉唐 · 华夏奠基",
        "sub_title": "公元前2070年 ~ 公元907年",
        "min_year": -2070,
        "max_year": 907,
        "badge": "青铜风骨 · 盛唐万邦",
        "desc": "武王伐纣、诸子百家争鸣、秦皇一统、大汉雄风凿通西域、盛唐长安万国来朝。",
        "icon": "⚱️",
        "legacy": "青史竹简",
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
        "icon": "🏮",
        "legacy": "族谱与方志",
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
        "icon": "🌅",
        "legacy": "厂志与家书",
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
        "icon": "🏙️",
        "legacy": "市井与家书",
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
        "icon": "🚀",
        "legacy": "星尘档案",
        "names": ["星野", "原野", "艾柯", "零壹", "黎光", "沐辰", "陆知远", "凌云", "苏黎", "纪尘"],
    },
]

# 连续时代背景表：(年份上界(开区间) 或 None 表示兜底, 名称, 描述)
GRAND_ERA_TABLE = [
    (-2070, "上古传说 · 三皇五帝", "文字未立而口耳相传，炎黄逐鹿、尧舜禅让、洪水滔天与英雄治水，构成了华夏文明最深处的集体记忆。"),
    (-1600, "夏代肇兴 · 禹画九州", "大禹治水疏导江河，定九州铸九鼎，家天下自此始，泥陶与早期玉器诉说着文明开端的朴拙与坚韧。"),
    (-1046, "殷商青铜 · 占卜甲骨", "洹水之滨甲骨刻辞，青铜重器饕餮纹神秘庄重，巫祝与王权在祭祀与征伐中奠基礼仪雏形。"),
    (-771, "西周分封 · 礼乐井田", "武王克商封建万邦，周公制礼作乐，宗法井田井然有序，郁郁乎文哉而文明大备。"),
    (-476, "春秋争霸 · 百家争鸣", "诸侯争盟礼崩乐坏，孔丘问道老聃，士阶层崛起，思想星空迸发人类童年最璀璨的光芒。"),
    (-221, "战国兼并 · 铁血大争", "七雄并立商鞅变法，合纵连横名将辈出，郡县初萌，华夏在金戈铁马中奔向终极一统。"),
    (-202, "秦扫六合 · 帝国初成", "始皇帝车同轨书同文，修万里长城筑直道，废分封立郡县，开启两千年中央集权大一统。"),
    (9, "大汉雄风 · 丝路凿空", "文景休养汉武远拓，张骞策马绝域西域，卫青霍去病封狼居胥，丝绸之路首通亚欧大陆。"),
    (220, "光武中兴 · 经纬通达", "洛阳古都经学兴盛，蔡伦造纸张衡候风，班超投笔从戎定远三十六国，儒术与豪族相融。"),
    (280, "三国风云 · 英雄逐鹿", "曹操酾酒临江，刘备三顾草庐，赤壁烈火燎原，群雄在乱世烽烟中留下千古侠义奇谋。"),
    (420, "两晋风流 · 偏安江左", "洛神赋与竹林七贤，衣冠南渡金陵建康，名士清谈与山水诗赋在大动荡中绽放异彩。"),
    (581, "南北对峙 · 民族大融", "北魏孝文帝汉化改制，南朝烟雨四百八十寺，长城内外血脉相融，大一统生机悄然孕育。"),
    (618, "隋代风帆 · 运河科举", "开创科举抡才大典，开凿南北大运河贯通南北，营建大兴长安，气象恢弘却二世而斩。"),
    (755, "盛唐气象 · 万邦来朝", "贞观之治开元盛世，李白举杯邀明月，长安朱雀大街胡姬起舞，万国来朝气象万千。"),
    (907, "藩镇割据 · 残唐落日", "安史之乱两京陆沉，藩镇割据黄巢揭竿而起，晚唐诗韵苍凉沉郁，繁华落尽余晖脉脉。"),
    (960, "五代十国 · 烽火乱局", "朱温篡唐沙陀入主，城头变换大王旗，乱象纷呈却催生南方市井与刻书商业萌芽。"),
    (1127, "北宋风雅 · 汴京繁华", "清明上河图虹桥喧闹，苏轼赋赤壁，瓦舍勾栏百戏杂陈，活字印刷与指南针泽被后世。"),
    (1279, "南宋偏安 · 海丝千帆", "西湖歌舞与岳飞满江红，泉州刺桐港千帆竞发，海运航路遍及印度洋，富庶冠绝当世。"),
    (1368, "大元一统 · 欧亚驿道", "忽必烈定都大都，开辟横跨欧亚大驿道，马可波罗惊叹东方繁盛，杂剧元曲唱彻街巷。"),
    (1644, "大明风华 · 远洋郑和", "太祖布衣起兵，成祖永乐大典，郑和七下西洋宝船扬帆，江南机杼声中萌生新的萌芽。"),
    (1840, "康乾盛世 · 红楼斜阳", "人口突破三亿疆域辽阔，编纂四库全书，红楼梦笔力惊神，然闭关锁国已落后于世界大潮。"),
    (1912, "晚清危局 · 变法求存", "鸦片战争炮声惊醒天朝，洋务运动自强求富，甲午海战、辛亥秋风，两千年帝制轰然崩塌。"),
    (1937, "民国风雷 · 思想破晓", "新文化运动德先生赛先生震荡古老神州，白话文觉醒，黄埔风云激荡，实业救国步履维艰。"),
    (1949, "烽火抗战 · 浴血奠基", "十四年抗战御侮血肉筑长城，台儿庄百团大战，三大战役定乾坤，民族在血火中涅槃站立。"),
    (1958, "建国初期 · 一五筑基", "没收官僚资本土改归农，抗美援朝保家卫国，苏联援建重点工厂开工，红旗招展百废俱兴。"),
    (1966, "大庆精神 · 自力更生", "铁人王进喜跃进泥浆，原子弹大漠爆鸣，全国人民勒紧裤带自力更生，独立工业体系初成。"),
    (1978, "风雨激荡 · 红砖岁月", "凭票供应与粮本油票，红砖大院广播操与样板戏，千百万青年上山下乡磨砺筋骨。"),
    (1984, "真理讨论 · 春风破冰", "小岗村大包干与十一届三中全会，恢复高考改变千万学子命运，喇叭裤与流行乐悄然传遍。"),
    (1992, "商品初潮 · 特区拔地", "价格双轨制松动，民间个体户提皮包闯天下，深圳特区高楼平地起，商品意识全面觉醒。"),
    (1998, "南方谈话 · 市场狂潮", "春天的故事响彻神州，大批体制内骨干下海淘金，股票交易所开门红，沿海迎来狂飙发展。"),
    (2003, "世纪之交 · 世贸扬帆", "国企下岗阵痛与世纪之交相撞，加入WTO后外贸代工厂遍地开花，中国正式成为世界工厂。"),
    (2010, "北京奥运 · 四万亿潮", "鸟巢烟花点亮苍穹，四万亿基建全面铺开，高铁大网向全国延伸，房地产狂飙揭开大幕。"),
    (2016, "移动互联 · 创业神话", "智能手机普及与移动支付颠覆日常，百团大战风起云涌，大众创业催生无数科技风口神话。"),
    (2023, "动荡考验 · 产业洗牌", "疫情风波与全球产业链重构，教培互联网地产退潮，考公稳健与内生硬核制造成为共识。"),
    (2035, "生成式AI · 智算新质", "国产大模型颠覆知识脑力，新能源车横扫全球，商业航天与深空空间站并进，迈向高阶现代。"),
    (2045, "常温超导 · 聚变初并", "商业托卡马克聚变堆首度向城市群并网供电，常温超导输电网贯通，大城市建起恒温穹顶。"),
    (2055, "太空天梯 · 地月微重", "赤道太空电梯贯通低轨，微重力芯片晶圆厂常态生产，月球南极氦-3采掘船队往返穿梭。"),
    (2065, "神经脑机 · 算力配额", "视网膜脑机接口成为入世标配，全球碳积分与算力账户直接绑定，肉体与数据分化显现。"),
    (2075, "火星农业 · 外星拓荒", "水手峡谷基地人口突破两百万，地火航线常态化轮渡，年轻人在地球引力与异星自由间抉择。"),
    (2085, "自组超脑 · 硅基共治", "中央分布式超脑自主接管全球能源与司法调度，算法特区与旧人类自由城邦形成二元平衡。"),
    (2100, "强恒星暴 · 旧网归寂", "数十年一遇的超强太阳磁暴冲击内太阳系，行星偏转护盾彻夜泛起极光，考验文明抗灾韧性。"),
    (2110, "半人马座 · 星际点火", "人类首艘亚光速恒星际巨舰点火升空飞向比邻星，火种散播银河，正式迈向多恒星纪元。"),
    (None, "戴森云环 · 终幕跃迁", "人造能量金环环绕恒星熠熠生辉，戴森云初具规模，碳硅同辉，生命形式迈向全新维度。"),
]


def wealth_unit(epoch_id):
    """各纪元货币单位：避免先秦人生出现万元这类时代错位。"""
    if epoch_id == "ancient":
        return "两金"
    if epoch_id == "premodern":
        return "两银"
    if epoch_id == "modern":
        return "块银元"
    if epoch_id == "contemporary":
        return "万元"
    return "信用点"


def get_epoch_config(epoch_id):
    for e in EPOCHS:
        if e["id"] == epoch_id:
            return e
    return EPOCHS[3]


def get_epoch_id_for_year(year):
    for e in EPOCHS:
        if year <= e["max_year"]:
            return e["id"]
    return EPOCHS[-1]["id"]


def is_future_epoch(epoch_id):
    return epoch_id == "future"


def is_classical_epoch(epoch_id):
    return epoch_id in ("ancient", "premodern", "modern")


def pick_epoch_name(epoch_id):
    cfg = get_epoch_config(epoch_id)
    return random.choice(cfg["names"]) if cfg["names"] else "无名"


def resolve_era(year):
    for upper, name, desc in GRAND_ERA_TABLE:
        if upper is None or year < upper:
            return name, desc
    return GRAND_ERA_TABLE[-1][1], GRAND_ERA_TABLE[-1][2]


def resolve_era_details(year, epoch_mode=None):
    """任意年份（含公元前）均有归属，从文明起源到未来星际无间断。"""
    return resolve_era(year)


def format_year_only(year):
    y = int(round(year))
    if y < 0:
        return "公元前 %d 年" % abs(y)
    if y == 0:
        return "公元元年"
    return "公元 %d 年" % y


def format_year_month(year, month):
    return "%s %d月" % (format_year_only(year), month or 1)


def list_eras_between(y0, y1):
    """一生穿越过的所有大时代（按时间顺序去重）。"""
    out = []
    a, b = int(min(y0, y1)), int(max(y0, y1))
    for y in range(a, b + 1):
        n = resolve_era(y)[0]
        if not out or out[-1] != n:
            out.append(n)
    if not out:
        out.append(resolve_era(a)[0])
    return out


# ---- ancient 出身地域（8）与门第阶层（10）----
ANCIENT_REGIONS = [
    ("关中秦川", "渭水两岸沃野千里，青铜农具初兴，军功爵下耕战并举，老秦人尚武重法。", {"health": 2, "rep": 1}),
    ("齐鲁之邦", "洙泗之间儒风最盛，稷下论学、盐铁通商，士人抱竹简讲经，乡里重礼尚俭。", {"intellect": 3, "rep": 2}),
    ("荆楚云梦", "江汉泽国水汽弥漫，稻作渔猎相济，漆器编钟见其工巧，楚人信巫好祀。", {"health": 1, "happiness": 2}),
    ("江南会稽", "水乡稻熟鱼肥，越人断发文身，冶剑煮盐之利颇丰，商船沿江上下。", {"wealth": 2, "luck": 1}),
    ("陇西凉州", "河西走廊胡商络绎，丝路驼铃与烽燧相望，边民自幼习骑射，风沙苦寒。", {"health": -1, "luck": 2}),
    ("中原洛邑", "天下之中车马辐辏，诸侯会盟、百工聚居，市井喧嚣而礼法森严。", {"intellect": 2, "wealth": 1, "health": -1}),
    ("燕赵之地", "北接胡狄铁马边关，慷慨悲歌多壮士游侠，冬日苦寒而民风刚烈。", {"health": 2, "rep": -1}),
    ("巴蜀成都", "岷江冲积沃野，都江堰引水灌田，蜀锦漆器行销四方，山高路险少兵祸。", {"health": 1, "wealth": 2.5, "happiness": 2})
]

ANCIENT_SOCIAL_STRATA = [
    ("没落公族后裔", "祖上曾列诸侯之卿，如今封邑尽削，只剩旧宅与几捆竹简；仍守祭祀礼数，却要变卖青铜器度日。", {"health": 88, "wealth": 3.2, "intellect": 68, "happiness": 52, "luck": 49, "rep": 58}, "守礼自持"),
    ("老秦耕战农卒", "家在关中乡里，丁男按爵授田，农时扶犁、战时执戈；一纸军功文书便可改换门庭，故尚武不畏苦。", {"health": 92, "wealth": 0.8, "intellect": 50, "happiness": 55, "luck": 50, "rep": 40}, "耐苦尚武"),
    ("齐鲁经学儒士", "世居洙泗之滨，家中藏经书数箧，子弟自幼习礼诵诗；以讲学授徒为业，虽清贫却颇受乡里敬重。", {"health": 85, "wealth": 2.5, "intellect": 74, "happiness": 58, "luck": 52, "rep": 66}, "温厚好古"),
    ("临淄盐铁巨贾", "凭煮盐冶铁起家，车马奴婢成群，与官府往来密切；家中账册堆积，最怕朝廷一纸抑商之令。", {"health": 86, "wealth": 11.5, "intellect": 66, "happiness": 60, "luck": 56, "rep": 55}, "精明豪爽"),
    ("大唐西市胡商", "自粟特远来，在长安西市经营香料珠宝，通数种语言；虽家资丰厚，却始终被视为异乡客，常思故土。", {"health": 87, "wealth": 9.8, "intellect": 64, "happiness": 57, "luck": 58, "rep": 42}, "机敏健谈"),
    ("终南山采药隐士", "结庐终南山中，采药炼丹、观星著书，与樵夫野老为邻；不慕功名，只求清静长寿。", {"health": 94, "wealth": 0.6, "intellect": 70, "happiness": 66, "luck": 54, "rep": 62}, "恬淡自适"),
    ("太学博士门第", "父祖累世为太学博士，家学以经义为本，子弟须通一经方能入仕；门庭清贵而俸禄微薄。", {"health": 84, "wealth": 4.6, "intellect": 76, "happiness": 60, "luck": 51, "rep": 74}, "端方守正"),
    ("边郡戍卒之家", "父兄远戍烽燧，家中只有老母与幼弟，靠屯田薄收糊口；书信难通，年年盼望换防归乡的那一天。", {"health": 91, "wealth": 0.5, "intellect": 47, "happiness": 50, "luck": 48, "rep": 36}, "坚忍寡言"),
    ("织室匠户之家", "隶属官营织室，母女终年坐机杼前，织成锦帛尽数入官；手艺极精却身役难脱，只盼朝廷宽免匠籍。", {"health": 88, "wealth": 1.4, "intellect": 55, "happiness": 53, "luck": 52, "rep": 34}, "灵巧安分"),
    ("豪强庄园宾客", "寄身大姓庄园为宾客，耕其田、护其坞堡，得衣食与庇护；虽无户籍自由，却比编户安稳。", {"health": 90, "wealth": 7.6, "intellect": 58, "happiness": 56, "luck": 53, "rep": 60}, "忠勇仗义")
]

# ---- ancient 16 大生命阶段事件池 ----
ANCIENT_STAGE_POOLS = [
  [
    {
        "age_rel": 6,
        "period": "幼年启蒙",
        "title": "竹简刀笔间初识天下字",
        "narrative": "蒙学设在族中旧屋，先生以刀笔在竹简上刻字，命你逐字摹写。窗外井田里父兄正忙春耕，缺一个递水送饭的帮手。先生却道今日十简未成，不许归家。你握着刻刀，手心渐渐发汗。",
        "choices": [
          {
            "text": "咬牙刻完十简，宁可饿着肚子也要让先生点头",
            "risk_label": "寒窗苦读 · 稳妥积淀 · 成功率 75%",
            "calc_chance": lambda p: 75 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "先生抚简称善，将你的名字写在学簿头一行，族中长辈闻讯，派人送来一块干肉。",
            "succ_eff": {"intellect": 10, "rep": 5},
            "fail_feedback": "手指被刀笔磨破，简上字迹歪斜，先生叹你心浮，罚你明日再刻二十简。",
            "fail_eff": {"intellect": 4, "happiness": -5},
            "tag_succ": "刀笔初成",
            "tag_fail": "手拙受罚",
            "is_key": True
          },
          {
            "text": "借口腹痛溜去田头，帮父兄递水送饭，趁隙偷听农事",
            "risk_label": "亲近田垄 · 事功渐长 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "父兄夸你懂事，教你辨认节气与土色，你把一句句农谚默默记在心里。",
            "succ_eff": {"health": 6, "wealth": 2, "happiness": 6},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "田垄情长",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 6,
        "period": "幼年启蒙",
        "title": "宗庙习礼初见尊卑",
        "narrative": "岁末祭祖，族中长者命你捧青铜小俎，立于阶下随众行礼。你腿脚酸麻，忽见邻家小儿在庙外招手，邀你去河边看新捕的鱼。长者目光沉沉扫来，俎中祭肉须捧到礼毕方止。",
        "choices": [
          {
            "text": "屏息站定，把俎捧到礼毕，一步也不曾挪动",
            "risk_label": "恪守宗法 · 沉稳有度 · 成功率 80%",
            "calc_chance": lambda p: 80,
            "succ_feedback": "长者当众赞你知礼，把祭余的一块肉亲手分给你，道此子可教，将来可托付。",
            "succ_eff": {"intellect": 4, "rep": 8},
            "fail_feedback": "你终究忍不住回头张望，被长者一眼看见，罚你跪在阶下，直到日头西沉。",
            "fail_eff": {"health": -3, "happiness": -6, "rep": -5},
            "tag_succ": "知礼守节",
            "tag_fail": "失仪受罚",
            "is_key": True
          },
          {
            "text": "趁长者低头祝祷，悄悄溜出庙门去河边看鱼",
            "risk_label": "任性贪玩 · 快意当前 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你摸到一尾滑鱼，笑得很大声，回家时衣襟尽湿，心头却痛快极了。",
            "succ_eff": {"health": 4, "happiness": 10, "rep": -3},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "童心未泯",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 10,
        "period": "童年韶光",
        "title": "乡塾比试射御夺头筹",
        "narrative": "乡塾春日较艺，诸童须张弓射柳，胜者得先生一支刻字木牍。你用的弓是兄长旧物，弦已松软。同窗中有一人箭术极精，正笑你弓弱，先生却已击柝催令，众人列队上前。",
        "choices": [
          {
            "text": "借力巧射，专瞄近处柳枝，稳中求胜不逞强",
            "risk_label": "审时度势 · 巧取头筹 · 成功率 70%",
            "calc_chance": lambda p: 70 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (3 if p.luck > 50 else 0),
            "succ_feedback": "三箭两中，先生将木牍递到你手中，同窗们围上来要摸那支箭，眼里都是羡慕。",
            "succ_eff": {"health": 4, "intellect": 6, "rep": 8},
            "fail_feedback": "弓弦忽然崩断，箭落在柳树根下，众人哄笑，你脸红到耳根，握弓的手发颤。",
            "fail_eff": {"health": -2, "happiness": -6, "rep": -5},
            "tag_succ": "箭无虚发",
            "tag_fail": "弦断人笑",
            "is_key": True
          },
          {
            "text": "远远退开十步再射，赌自己臂力过人，一箭惊人",
            "risk_label": "逞强好胜 · 意气用事 · 成功率 40%",
            "calc_chance": lambda p: 40 + (3 if p.health > 60 else 0),
            "succ_feedback": "箭如流星穿柳而过，满塾哗然，连先生也捋须颔首，说你力气不小。",
            "succ_eff": {"health": 6, "happiness": 5, "rep": 10},
            "fail_feedback": "臂力不济，箭软软坠地，你被同窗起了绰号，半月抬不起头来。",
            "fail_eff": {"health": -3, "happiness": -8, "rep": -4},
            "tag_succ": "一箭惊人",
            "tag_fail": "力不从心",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 10,
        "period": "童年韶光",
        "title": "随父兄入市贩粟议价",
        "narrative": "秋收之后，父兄推车入市贩粟，命你看守钱袋并学着与买主议价。市中有掮客愿出高价全收，却要赊账至来年。族里正等这笔钱添置铁镰，你也想给自己买一册旧竹书。",
        "choices": [
          {
            "text": "压价卖给散客，宁可多等半日也要现钱落袋",
            "risk_label": "稳妥持家 · 细水长流 · 成功率 78%",
            "calc_chance": lambda p: 78 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "粟卖得干净，钱袋沉实，父兄允你留下一枚小钱，你买回半册旧书。",
            "succ_eff": {"wealth": 8, "intellect": 5, "happiness": 4},
            "fail_feedback": "散客挑拣压价，日暮仍有半车粟，父兄沉沉叹息，你懊恼地收摊。",
            "fail_eff": {"wealth": -4, "happiness": -5},
            "tag_succ": "粒粟皆金",
            "tag_fail": "坐失良机",
            "is_key": True
          },
          {
            "text": "贪那高价，劝父兄赊给掮客，立下竹券为凭",
            "risk_label": "放债图利 · 险中求财 · 成功率 50%",
            "calc_chance": lambda p: 50 + (4 if p.luck > 50 else 0),
            "succ_feedback": "掮客如约践诺，来年送来双倍粟钱，还引你认得几位往来行商。",
            "succ_eff": {"wealth": 14, "luck": 3, "rep": 5},
            "fail_feedback": "掮客一去无踪，竹券成了废简，家中当年缺了农具，你愧疚良久。",
            "fail_eff": {"wealth": -10, "happiness": -6},
            "tag_succ": "券约得偿",
            "tag_fail": "券成废简",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 15,
        "period": "少年分流",
        "title": "负笈远行千里求见名师",
        "narrative": "闻邻郡有位饱学先生开门授徒，讲论百家之说，士子往来如云。你欲负笈前往，然家中田亩将收，父母盼你留下帮工；路远盘缠不足，须卖掉母亲亲手织的一匹布。",
        "choices": [
          {
            "text": "卖掉那匹布作盘缠，星夜启程，投帖拜入先生门下",
            "risk_label": "负笈千里 · 孤注一掷 · 成功率 65%",
            "calc_chance": lambda p: 65 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (4 if p.luck > 50 else 0),
            "succ_feedback": "先生见你衣衫破旧而应答不俗，破例收你为徒，还赐半间草舍安身。",
            "succ_eff": {"intellect": 14, "happiness": 5, "rep": 6},
            "fail_feedback": "先生门徒已满，你被拒之门外，盘缠耗尽，只好沿路乞食徒步归家。",
            "fail_eff": {"wealth": -8, "intellect": 5, "happiness": -7},
            "tag_succ": "得列门墙",
            "tag_fail": "白走一遭",
            "is_key": True
          },
          {
            "text": "先留家中收完秋粮，再挑一担新粟去换书简自学",
            "risk_label": "耕读两全 · 稳中有进 · 成功率 85%",
            "calc_chance": lambda p: 85,
            "succ_feedback": "秋粮入仓，你换回几卷书简，夜里就着灶火抄读，字迹工整可观。",
            "succ_eff": {"wealth": 4, "intellect": 8, "happiness": 3},
            "fail_feedback": "白日劳碌，夜里读不上两行便困倒，书简在手边积了一层灰。",
            "fail_eff": {"intellect": 2, "happiness": -4},
            "tag_succ": "耕读自持",
            "tag_fail": "灯下倦读",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 15,
        "period": "少年分流",
        "title": "里正登门点选徭役",
        "narrative": "郡县征发徭役，里正捧名册登门，你已够岁数，须随众去修驰道、筑边城。同里有人愿出钱代役，只求顶你的名额；父母年迈，你亦想去外头见见世面。",
        "choices": [
          {
            "text": "接下名册，随队上路，在役夫中多学一门手艺",
            "risk_label": "应役远行 · 见闻渐广 · 成功率 72%",
            "calc_chance": lambda p: 72 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (5 if p.health > 60 else 0),
            "succ_feedback": "你在工地上跟匠人学会夯土与量绳，还结识了一位识字的小吏。",
            "succ_eff": {"health": 8, "intellect": 6, "rep": 5},
            "fail_feedback": "烈日之下水土不服，你病倒在工棚，被提前遣送回乡，一路颠簸。",
            "fail_eff": {"health": -10, "happiness": -6, "rep": -3},
            "tag_succ": "应役有成",
            "tag_fail": "病卧工棚",
            "is_key": True
          },
          {
            "text": "收下那人的钱替家里添牛，自己躲过这趟徭役",
            "risk_label": "以钱代役 · 安守家门 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "家中添了一头小牛，秋耕省力不少，父母难得舒展了眉头。",
            "succ_eff": {"wealth": 10, "happiness": 5},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "以钱代役",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 18,
        "period": "成人立志",
        "title": "郡府征辟与边关募兵",
        "narrative": "郡府小吏来乡里访贤，言你若通经明法，可先充书佐；同时边关募兵，斩首有赏，立功可入行伍。两条路摆在眼前：一条稳而慢，一条险而快。父母只盼你平安，却也盼你出息。",
        "choices": [
          {
            "text": "投身边关，执戈从军，凭军功博一个出身",
            "risk_label": "投笔从戎 · 险中求贵 · 成功率 55%",
            "calc_chance": lambda p: 55 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (5 if p.luck > 50 else 0) + (4 if p.health > 60 else 0),
            "succ_feedback": "你随军破敌，斩获首级，校尉记你首功，授你什长之职，同伍皆服。",
            "succ_eff": {"health": 6, "wealth": 8, "rep": 15},
            "fail_feedback": "初战即伤，你被抬回营帐，虽保住性命，却落下每逢阴雨便痛的旧疾。",
            "fail_eff": {"health": -15, "happiness": -6, "rep": -4},
            "tag_succ": "首功授职",
            "tag_fail": "负伤而归",
            "is_key": True
          },
          {
            "text": "入郡府为书佐，掌文书簿册，在案牍间积累人望",
            "risk_label": "案牍立身 · 稳进仕途 · 成功率 88%",
            "calc_chance": lambda p: 88 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "你抄录文书从不出错，郡丞颇赏识，将你举荐给上官，前途渐明。",
            "succ_eff": {"wealth": 6, "intellect": 10, "rep": 10},
            "fail_feedback": "一笔误抄惹出是非，你被罚俸半月，同僚也渐渐疏远了你。",
            "fail_eff": {"wealth": -3, "happiness": -5, "rep": -6},
            "tag_succ": "文牍见赏",
            "tag_fail": "误抄见罚",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 18,
        "period": "成人立志",
        "title": "胡商车队过境邀你同行",
        "narrative": "一支胡商驼队过境歇脚，领头的胡商见你通晓数算、口齿伶俐，邀你随队西行贩运丝绸，许诺分你一份厚利。此去关山万里，归期难料；而家中正为你议亲，只待你点头。",
        "choices": [
          {
            "text": "收拾行囊随商队西行，把命与运押在长路上",
            "risk_label": "万里行商 · 富贵险求 · 成功率 50%",
            "calc_chance": lambda p: 50 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (6 if p.luck > 50 else 0),
            "succ_feedback": "驼队平安出关，你贩丝获利数倍，归来时乡人皆出门观看，啧啧称奇。",
            "succ_eff": {"wealth": 25, "luck": 4, "rep": 8},
            "fail_feedback": "途中遇劫，货物尽失，你徒步东归，瘦得父母几乎认不出你来。",
            "fail_eff": {"health": -8, "wealth": -18, "happiness": -8},
            "tag_succ": "满载而归",
            "tag_fail": "货失人还",
            "is_key": True
          },
          {
            "text": "留在乡里，用积蓄开一间小肆，收售乡邻杂物",
            "risk_label": "守土小贾 · 安稳度日 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "小肆开张，乡邻常来赊账却也常来照顾，日子过得安稳而有盈余。",
            "succ_eff": {"wealth": 12, "happiness": 6, "rep": 3},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "小肆安稳",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 21,
        "period": "青春韶华",
        "title": "县廷征召，试为刀笔小吏",
        "narrative": "乡啬夫传话过来，县廷缺一名书佐，要识字的年轻人前去应试。你案头摊着几卷残简，父亲却盼你留在家中照看田亩与年迈的祖母。同里已有人在县衙当差，衣冠整齐，说话也硬气。去试，或许能踏上吏途；不去，家中秋收便少一双手。",
        "choices": [
          {
            "text": "收拾好简牍笔墨，天明便去县廷报名应考书佐",
            "risk_label": "求名有路 · 失家劳力 · 成功率 65%",
            "calc_chance": lambda p: 65 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (3 if p.luck > 50 else 0),
            "succ_feedback": "主吏考你书算，见你小篆工整，当场录为书佐，递来一枚竹简作凭信。",
            "succ_eff": {"wealth": 3, "intellect": 8, "rep": 6},
            "fail_feedback": "你小篆尚可，算数却慢，主吏摇头让你回去，祖母的汤药钱仍无着落。",
            "fail_eff": {"intellect": 3, "happiness": -5},
            "tag_succ": "刀笔初试",
            "tag_fail": "铩羽而归",
            "is_key": True
          },
          {
            "text": "先留在家中操持农事，夜里就着豆灯自读律令",
            "risk_label": "守家尽责 · 缓图后计 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你白日扶犁，夜里诵律，乡邻都称你稳重，来日征召必先念及你。",
            "succ_eff": {"intellect": 4, "happiness": 5, "rep": 4},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "耕读自守",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 21,
        "period": "青春韶华",
        "title": "负笈远游，拜入名师门下",
        "narrative": "听说郡中有位老儒开门授徒，讲《春秋》与律令，弟子多被州府辟用。你背着一箱旧简走了三日，可拜师需奉束脩，家中只凑出一匹粗帛。同舍生多是豪族子弟，衣冠整齐，谈笑间已互称表字。留下，或可博一个出身；折返，则这三日脚程白费。",
        "choices": [
          {
            "text": "情愿奉上一匹粗帛，甘居下座替师门抄书抵束脩",
            "risk_label": "虚心求教 · 以劳补拙 · 成功率 70%",
            "calc_chance": lambda p: 70 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "老儒见你抄录细密无误，留你居下舍，命你专掌经卷，同门也来借问。",
            "succ_eff": {"intellect": 10, "rep": 5},
            "fail_feedback": "抄错三处经文，被罚立在庭中背诵，粗帛已收，颜面也丢了半截。",
            "fail_eff": {"intellect": 4, "happiness": -6},
            "tag_succ": "师门垂青",
            "tag_fail": "当庭受责",
            "is_key": True
          },
          {
            "text": "不拜师门，只在市旁赁屋替旅人代写书信契券",
            "risk_label": "自谋生计 · 学无常师 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你替旅人写家书、替乡邻写契券，铜钱虽少，识字的名声却传开了。",
            "succ_eff": {"wealth": 5, "happiness": 3, "rep": 3},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "市井笔耕",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 24,
        "period": "初涉人世",
        "title": "边郡征戍，登烽燧望狼烟",
        "narrative": "县里张榜，北边烽燧缺戍卒，去者免一岁赋，归来可叙功受爵。你新婚未久，妻子腹中已有身孕。里正说，边地苦寒，胡骑时来劫掠，也有人一去三年杳无音信。应征，或能凭军功脱去布衣；不去，则要纳钱代役，家中粟米本就见底。",
        "choices": [
          {
            "text": "应征北上，把自己的姓名报入戍卒名册，随队出发",
            "risk_label": "军功可期 · 生死难卜 · 成功率 55%",
            "calc_chance": lambda p: 55 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (4 if p.luck > 50 else 0) + (4 if p.health > 60 else 0),
            "succ_feedback": "你随队登燧瞭望，一日烽火骤起，你率先举炬示警，都尉记你一功。",
            "succ_eff": {"health": 3, "wealth": 6, "rep": 8},
            "fail_feedback": "深秋一场疫病，同伍倒了三人，你虽活下来，归期又拖了半年。",
            "fail_eff": {"health": -10, "wealth": 3, "happiness": -8},
            "tag_succ": "烽燧立功",
            "tag_fail": "边地病归",
            "is_key": True
          },
          {
            "text": "留在乡里，替戍边之人纳粟代役并代为照料其家",
            "risk_label": "破财免行 · 结好乡邻 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你典卖半亩薄田完纳代役钱，乡邻念你信义，常来帮你收割。",
            "succ_eff": {"wealth": -8, "happiness": 4, "rep": 6},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "信义乡里",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 24,
        "period": "初涉人世",
        "title": "随商队西行，贩缯帛于关市",
        "narrative": "姑臧来的商队缺一个记账的伙计，说走一趟河西，缯帛换回玉与苜蓿，利可数倍。妻子不愿你远行，族中长辈却想借你探探关市行情。此行要过边关，路上有盗匪，也有盘查的关吏。若得利，家业可起；若折本，连聘礼的欠账都还不上。",
        "choices": [
          {
            "text": "随队西行，一路上替商主记账、验货、押运缯帛",
            "risk_label": "重利远行 · 关山险阻 · 成功率 60%",
            "calc_chance": lambda p: 60 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (4 if p.luck > 50 else 0) + (3 if p.health > 60 else 0),
            "succ_feedback": "你在关市议价得当，缯帛脱手极快，商主分你两匹绢，另许下次同行。",
            "succ_eff": {"wealth": 18, "intellect": 6, "rep": 4},
            "fail_feedback": "半途遇盗，货物折了大半，商主未责你，你却分文未得，还病了一场。",
            "fail_eff": {"health": -6, "wealth": -12, "happiness": -5},
            "tag_succ": "关市获利",
            "tag_fail": "折货空归",
            "is_key": True
          },
          {
            "text": "不涉远途，只在县邑集市之间做些零碎转贩生意",
            "risk_label": "小本经营 · 稳中求进 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你收乡下的布、卖城里的盐，薄利细攒，一年下来也添了两只健牛。",
            "succ_eff": {"wealth": 7, "happiness": 3},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "小贩积财",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 27,
        "period": "成家立业",
        "title": "纳采问名，聘礼尚差一筹",
        "narrative": "你与邻县女子相看已定，媒人来回奔走，只差最后一道纳征。女方家说，聘礼不论厚薄，只求体面；可你清点家中，粟不足十石，布只两匹。族兄劝你借债备礼，以免失了脸面；也有人劝你据实相告，莫为一时风光耗尽来年的种粮。",
        "choices": [
          {
            "text": "向族兄借贷，也要备齐聘礼风风光光地纳征",
            "risk_label": "顾全颜面 · 负债成婚 · 成功率 72%",
            "calc_chance": lambda p: 72 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "女方家见礼数周全，欣然许婚，乡里都说这门亲事体面，你也得了个贤内助。",
            "succ_eff": {"wealth": -10, "happiness": 12, "rep": 6},
            "fail_feedback": "债主催得紧，婚后第一年你常为还钱奔忙，妻子虽无怨言，你心里不好受。",
            "fail_eff": {"wealth": -16, "happiness": 4, "rep": 2},
            "tag_succ": "六礼告成",
            "tag_fail": "婚成债重",
            "is_key": True
          },
          {
            "text": "据实相告，以自家织的两匹布和十石粟为礼",
            "risk_label": "坦诚量力 · 平淡成礼 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "女方父母见你诚实持重，反赞你可靠，婚事从简而办，两家都无怨言。",
            "succ_eff": {"happiness": 9, "rep": 4},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "布粟为聘",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 27,
        "period": "成家立业",
        "title": "族中分家，一卷薄田起争执",
        "narrative": "父亲过世，族老主持析产。兄长的儿子多、人口重，主张按口分田；你只一房妻小，按理可分较肥的近水田。族老却劝你顾全兄弟情面，先让一步。争，或可多得几亩活命田；让，则要在族中落个谦让的名声。可来年春耕，种子和耕牛都等着用钱。",
        "choices": [
          {
            "text": "据理力争，务必请族老依据律令与旧契当众明断",
            "risk_label": "寸土必争 · 伤了手足 · 成功率 68%",
            "calc_chance": lambda p: 68 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "族老翻出旧契，判你分得近水田两段，秋收丰足，妻子终于展颜。",
            "succ_eff": {"wealth": 12, "happiness": -3, "rep": 4},
            "fail_feedback": "兄长当众骂你刻薄，田虽多争半亩，族中却许久不与你往来。",
            "fail_eff": {"wealth": 5, "happiness": -8, "rep": -8},
            "tag_succ": "依法得田",
            "tag_fail": "析产失和",
            "is_key": True
          },
          {
            "text": "主动让出近水肥田，另择坡地并多要农具",
            "risk_label": "谦让全亲 · 另图桑麻 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你让了好田却得全套农具与耕牛，坡地种桑养蚕，来年另有一份进项。",
            "succ_eff": {"wealth": -3, "happiness": 6, "rep": 8},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "让田得牛",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 31,
        "period": "三十而立",
        "title": "郡国举荐，孝廉之名在望",
        "narrative": "郡守下教，要举一名孝廉入京对策，乡里议论纷纷，数你的孝行与文书最好。可另一家是本地豪族的子弟，门生故吏众多，已暗中打点。郡中主吏暗示，你若肯送些土物，事便可成。举，则一生仕途由此起；不举，则数年耕读尽付流水。",
        "choices": [
          {
            "text": "备下薄礼拜访郡中主吏，请其在郡守面前美言",
            "risk_label": "通融求举 · 名节有损 · 成功率 58%",
            "calc_chance": lambda p: 58 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (4 if p.luck > 50 else 0),
            "succ_feedback": "郡守果以你为孝廉，车马入京对策，你第一次望见宫阙的飞檐。",
            "succ_eff": {"wealth": -5, "intellect": 6, "rep": 10},
            "fail_feedback": "主吏收了礼却不认账，豪族子弟得举，你反落下结交吏胥的话柄。",
            "fail_eff": {"wealth": -8, "happiness": -8, "rep": -10},
            "tag_succ": "举为孝廉",
            "tag_fail": "求举见欺",
            "is_key": True
          },
          {
            "text": "不送一物，只把历年劝农赈济的簿册呈给郡守",
            "risk_label": "以实自荐 · 静候公论 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "郡守翻阅簿册，见你历年赈济灾民条条有据，叹你朴实，将你列入备选。",
            "succ_eff": {"intellect": 4, "happiness": 4, "rep": 7},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "簿册自明",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 31,
        "period": "三十而立",
        "title": "岁大饥，流民叩门求一斗粟",
        "narrative": "连月大旱，邻郡流民成群过境，篷车停在里门外。你家仓中尚存粟三十石，是来年春耕与全家口粮。里正说，郡府令各户出粟赈济，可事后未必补偿；也有人说，此时开仓能结下四方人望，来日或有大用。妻子抱着幼子，望着你的脸不说话。",
        "choices": [
          {
            "text": "开仓出粟十石赈济流民，并邀壮者留下垦荒",
            "risk_label": "散粟结众 · 来年恐饥 · 成功率 70%",
            "calc_chance": lambda p: 70 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (3 if p.luck > 50 else 0),
            "succ_feedback": "流民感你恩义，数十壮者留下替你开垦荒坡，里中皆称你有长者之风。",
            "succ_eff": {"wealth": -10, "happiness": 6, "rep": 12},
            "fail_feedback": "流民一哄而散，粟去了大半，来年春耕你只得向族兄借种。",
            "fail_eff": {"wealth": -16, "happiness": -6, "rep": 3},
            "tag_succ": "散粟得众",
            "tag_fail": "粟尽人散",
            "is_key": True
          },
          {
            "text": "只在门外施粥三日，其余时候闭门护住自家粮种",
            "risk_label": "量力施惠 · 先保家门 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你施粥三日全了情面，又保住大半粮种，春耕未误，一家安然。",
            "succ_eff": {"wealth": 2, "happiness": 2, "rep": 3},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "施粥护仓",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 36,
        "period": "负重前行",
        "title": "郡府辟召，党锢之祸风声紧",
        "narrative": "郡府征辟的檄文送到柴门，你却在乡里听闻朝中党锢再起，名士下狱者众。老母卧病在床，药石将尽；长子方习《春秋》，指望你谋一官半职。受辟可光门楣，却也恐被列为党人；拒之则清名自保，家中却要再熬几个荒年。你该何去何从？",
        "choices": [
          {
            "text": "应辟入府，只理刑名钱谷，不与清流名士往来结党",
            "risk_label": "宦海风波 · 清誉难全 · 成功率 62%",
            "calc_chance": lambda p: 62 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (3 if p.luck > 50 else 0),
            "succ_feedback": "同僚只当你是个谨慎的佐吏，党狱大兴时未有人攀扯你。三年后你升任郡丞，俸禄渐丰，老母的药也未曾断过。",
            "succ_eff": {"wealth": 12, "intellect": 8, "rep": 4},
            "fail_feedback": "党人名单上终究添了你的名字。免官下狱半年，虽未丧命，家资却折了大半，出狱时鬓边已白。",
            "fail_eff": {"wealth": -5, "happiness": -6, "rep": -8},
            "tag_succ": "明哲保身",
            "tag_fail": "党锢牵连",
            "is_key": True
          },
          {
            "text": "称病谢辟，闭门奉母教子，把余粮换成桑田与书卷",
            "risk_label": "清贫自守 · 门第渐衰 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你闭门谢客，日日为母亲煎药，灯下教长子读《春秋》。乡里称你孝谨，州府后来竟以孝廉相举。",
            "succ_eff": {"intellect": 5, "happiness": 8, "rep": 6},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "守拙养亲",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 36,
        "period": "负重前行",
        "title": "丁忧三载，族中田产待分",
        "narrative": "老母终究没能熬过这个冬天。你按礼制解官持丧，庐墓三年。丧事方毕，族中长辈便提起祖田析分：叔父主张按房均分，堂兄却说你久宦在外，田界早已含混。妻儿要生计，亡母遗训在耳，你握着那卷发黄的田契，指节发白。",
        "choices": [
          {
            "text": "依礼庐墓，请族中三老作证，按旧契重新丈量田界",
            "risk_label": "丁忧守制 · 争产伤亲 · 成功率 68%",
            "calc_chance": lambda p: 68 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (2 if p.luck > 50 else 0),
            "succ_feedback": "你请三老与乡邻作证，旧契界石一一勘明，祖田按房均分。族人虽有小怨，终究服你的公道。",
            "succ_eff": {"wealth": 10, "happiness": 4, "rep": 8},
            "fail_feedback": "丈量时界石早被人挪动，堂兄又串通书吏改了鱼鳞册。你只争回薄田几亩，与堂兄从此不相往来。",
            "fail_eff": {"wealth": -8, "happiness": -8, "rep": -5},
            "tag_succ": "依礼析产",
            "tag_fail": "阋墙生隙",
            "is_key": True
          },
          {
            "text": "索性把名下好田尽让堂兄，只留薄田数亩供祭扫",
            "risk_label": "让产全族 · 家计转薄 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你把好田尽让堂兄，只留祭田数亩。族中皆称你重义，此后每逢荒年，堂兄反倒常送粮相济。",
            "succ_eff": {"wealth": -10, "happiness": 6, "rep": 12},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "让田全义",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 40,
        "period": "中年险滩",
        "title": "遭诬下狱，讼牒压在案头",
        "narrative": "县廷一纸牒文将你收系狱中，告你侵吞漕粮。实情是主吏改了斛斗，账目被做了手脚。狱吏索钱，同囚劝你认罪求轻判；妻子在门外奔走，变卖嫁妆疏通门路。若屈招，家产可保一半，清名尽毁；若死扛，或能等到按察使覆核，也可能毙于杖下。",
        "choices": [
          {
            "text": "拒不画押，托旧交将原账与证人姓名递到州府按察",
            "risk_label": "生死一纸 · 昭雪难期 · 成功率 45%",
            "calc_chance": lambda p: 45 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (4 if p.luck > 50 else 0) + (3 if p.health > 60 else 0),
            "succ_feedback": "按察使覆核旧账，果然查出主吏改斛之弊。你无罪开释，那吏员反坐，乡里都赞你骨头硬。",
            "succ_eff": {"intellect": 6, "happiness": 5, "rep": 12},
            "fail_feedback": "证据未及递出，你已在狱中染了寒疾。杖责之后落下病根，出狱时人瘦如柴，家财也无几了。",
            "fail_eff": {"health": -18, "wealth": -10, "happiness": -12},
            "tag_succ": "沉冤得雪",
            "tag_fail": "瘐死狱中",
            "is_key": True
          },
          {
            "text": "认下部分罪责，纳粟赎刑，保住性命与半数家产",
            "risk_label": "纳粟赎刑 · 名节有亏 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你纳粟赎了刑，虽有乡议指你软弱，命却是保住了。归家后你烧了旧账，从此只教子读书。",
            "succ_eff": {"health": -6, "wealth": -14, "rep": -8},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "忍辱全生",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 40,
        "period": "中年险滩",
        "title": "中正定品，长子前程待择",
        "narrative": "州中正将行乡品，你的长子已能属文。门第不算高，中正又是旧日政敌的门生。族老劝你倾尽家资为长子营求清望之职，走门阀捷径；塾师却说不如让他去州学苦读经义，凭才学取品。眼看秋集将至，这一步关乎儿孙后世，你须在人情与学问之间落子。",
        "choices": [
          {
            "text": "备下名帖与绢帛，登门拜谒中正，请为长子叙品",
            "risk_label": "攀附门第 · 清议可畏 · 成功率 58%",
            "calc_chance": lambda p: 58 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (5 if p.luck > 50 else 0),
            "succ_feedback": "中正念你礼数周全，又碍着旧交情面，终给长子叙了个中品。门第渐起，只是清议间偶有讥声。",
            "succ_eff": {"wealth": -8, "happiness": 6, "rep": 8},
            "fail_feedback": "中正收了礼却不肯出力，反将此事播扬出去。乡里讥你攀附，长子的品第反而落了下乘。",
            "fail_eff": {"wealth": -10, "happiness": -6, "rep": -12},
            "tag_succ": "门第得叙",
            "tag_fail": "清议见讥",
            "is_key": True
          },
          {
            "text": "送长子入州学，令其苦读经义，待策试自陈才学",
            "risk_label": "十年寒窗 · 品第难料 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "长子入州学三年，策试名列前茅，中正不得不以才学取之。乡里传为美谈，你也稍慰平生。",
            "succ_eff": {"intellect": 10, "happiness": 4, "rep": 6},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "经明行修",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 45,
        "period": "动荡考验",
        "title": "胡骑南下，举族渡江避乱",
        "narrative": "北地烽烟骤起，胡骑已破邻郡，坞堡里人心惶惶。族中商议南迁：渡江可避锋镝，却要弃下祖坟与百亩良田，舟车资费不菲；留守坞堡，凭高墙与乡曲部曲或许能撑过这个冬天。老族长问你，究竟带多少族人、多少粮种上路。",
        "choices": [
          {
            "text": "尽率族众渡江南下，变卖田宅作舟资，随衣冠士族侨居",
            "risk_label": "弃祖南迁 · 道路艰险 · 成功率 55%",
            "calc_chance": lambda p: 55 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (6 if p.luck > 50 else 0) + (4 if p.health > 60 else 0),
            "succ_feedback": "舟行月余，举族在江南侨郡落脚。虽失了祖田，却以带来的粮种垦出薄田，子弟后来多有入仕者。",
            "succ_eff": {"health": 6, "wealth": 8, "rep": 5},
            "fail_feedback": "半途遇乱兵劫掠，舟资尽失，族中老弱病殁于道。你携余众勉强渡江，从此家道中落，只余一身。",
            "fail_eff": {"health": -15, "wealth": -20, "happiness": -10},
            "tag_succ": "衣冠南渡",
            "tag_fail": "道殣相望",
            "is_key": True
          },
          {
            "text": "留驻坞堡，率部曲坚壁清野，与乡邻共守乡土",
            "risk_label": "死守乡里 · 生死未卜 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "坞堡高墙深壕，乡曲部曲协力死守，胡骑绕城而去。族中老小得以保全，乡邻都推你为坞主。",
            "succ_eff": {"health": -6, "happiness": -4, "rep": 10},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "保境安民",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 45,
        "period": "动荡考验",
        "title": "藩镇征兵，老身与幼子孰往",
        "narrative": "节度使的征兵牒下到里坊，凡丁壮皆须应募。你已年过四十，腰腿旧伤未愈；次子刚满十六，尚未婚配。军府许你以粟代役，可家中义仓才攒下几囤谷子，是族里荒年救命的底子。里正站在门口催得急，妻在灶下抹泪，你须在一炷香内定夺。",
        "choices": [
          {
            "text": "亲自应募，随军北上戍边，把幼子留在乡里承家",
            "risk_label": "从军远戍 · 生死由天 · 成功率 40%",
            "calc_chance": lambda p: 40 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (5 if p.luck > 50 else 0) + (8 if p.health > 60 else 0),
            "succ_feedback": "你在军中因识文断字被擢为书佐，未几边事稍定，得以还乡。虽未立功名，却保住了次子的婚配。",
            "succ_eff": {"health": -8, "intellect": 5, "rep": 12},
            "fail_feedback": "北戍途中你旧伤复发，又逢大雪，同行者死伤大半。你被人抬回时，义仓已空，次子也替了你的名籍。",
            "fail_eff": {"health": -18, "wealth": -6, "happiness": -14},
            "tag_succ": "投笔从戎",
            "tag_fail": "马革裹尸",
            "is_key": True
          },
          {
            "text": "开义仓出粟代役，留次子在乡耕读，另雇乡勇应募",
            "risk_label": "倾仓免役 · 族中生怨 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你开仓出粟免了丁役，次子得以在家耕读。族中虽怨你擅动义仓，来年丰收后终究补上了亏空。",
            "succ_eff": {"wealth": -16, "happiness": 5, "rep": -6},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "破财免丁",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 51,
        "period": "知命之年",
        "title": "宦情已倦，辞官择地而居",
        "narrative": "你在仕途浮沉二十载，如今鬓已染霜。朝中党争又起，门生劝你依附新贵再进一步；老友则来信说，终南山下有薄田数顷，泉石清幽，可终老著书。归隐须弃官俸门荫，儿孙仕途或受影响；留任则日日如履薄冰，恐晚节不保。案上旧砚，正待落笔。",
        "choices": [
          {
            "text": "上表称病辞官，携家卜居山下，以耕读终老",
            "risk_label": "急流勇退 · 门荫渐薄 · 成功率 60%",
            "calc_chance": lambda p: 60 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (4 if p.luck > 50 else 0) + (5 if p.health > 60 else 0),
            "succ_feedback": "你辞官归山，晨起荷锄，夜来著书。二十年后，那部《山居杂记》被门人刻印，乡里皆称你高致。",
            "succ_eff": {"health": 10, "wealth": -6, "happiness": 15, "rep": 8},
            "fail_feedback": "你辞官未久，旧日政敌便奏请削了你的门荫，儿孙仕途受阻。你虽在山中安身，心中终有块垒难平。",
            "fail_eff": {"health": -6, "happiness": -8, "rep": -8},
            "tag_succ": "归园田居",
            "tag_fail": "晚节飘零",
            "is_key": True
          },
          {
            "text": "留任原职只求无过，把心力用在修桥赈饥上",
            "risk_label": "明哲保身 · 宦海浮沉 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你留任不争，只把心力用在修桥赈饥上。虽未再升迁，离任时百姓夹道相送，你也算无愧于心。",
            "succ_eff": {"intellect": 4, "happiness": -4, "rep": 10},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "守拙宥民",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 51,
        "period": "知命之年",
        "title": "灾年起义仓，修谱立训",
        "narrative": "这一年秋旱，四乡饥民流徙，族中义仓的谷子只够撑到开春。祠堂里，族老们争论：是把存粮按丁口平分，还是留作来年的种子与祭田。你已年过半百，正想趁此修一部族谱、立几条家训，好把荒年不闭仓的规矩刻进去，让后人记得今日之难。",
        "choices": [
          {
            "text": "开义仓设粥棚，尽散存粮赈济乡邻，只留祭田种子",
            "risk_label": "倾仓济众 · 来春可忧 · 成功率 65%",
            "calc_chance": lambda p: 65 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (3 if p.luck > 50 else 0),
            "succ_feedback": "粥棚开了一冬，活人无数。来春族中子弟合力垦荒，义仓竟比往年更丰，你的家训也被刻在祠堂。",
            "succ_eff": {"wealth": -12, "happiness": 10, "rep": 15},
            "fail_feedback": "存粮散尽，来春青黄不接，族中饿死了几个老弱。乡邻虽感你的恩，你却在祠堂前垂泪自责。",
            "fail_eff": {"wealth": -18, "happiness": -6, "rep": 6},
            "tag_succ": "义仓活人",
            "tag_fail": "来岁啼饥",
            "is_key": True
          },
          {
            "text": "按丁口均分存粮，余谷封仓，趁冬修族谱立家训",
            "risk_label": "量入为出 · 各有怨言 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你按丁口分粮，余谷封仓，又趁冬修成族谱家训。族人虽嫌你吝，来年却无一人饿毙，渐渐服气。",
            "succ_eff": {"wealth": -6, "intellect": 6, "happiness": 4, "rep": 8},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "修谱立训",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 58,
        "period": "花甲在望",
        "title": "竹简分券，堂前析产定争",
        "narrative": "你年近花甲，鬓上已白。长子束发成家，次子尚在读书，田宅、僮仆、桑麻之利皆要分明。里正劝你趁早析产，免得身后兄弟相争；可老妻说，一分家便如树折其干，人心也散了。堂上竹简与契券摊开，墨尚未干，你须定一个章程。",
        "choices": [
          {
            "text": "请族中尊长与里正作证，立券析产，田宅各半，留一份祭田归祠堂",
            "risk_label": "明分定争 · 人心或散 · 成功率 70%",
            "calc_chance": lambda p: 70 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (10 if p.luck > 50 else 0),
            "succ_feedback": "契券两分，各执其一，祭田入祠。兄弟虽别居，逢节仍同席。族人称你不偏不倚，乡里传为美谈。",
            "succ_eff": {"wealth": -6, "happiness": 4, "rep": 8},
            "fail_feedback": "田亩肥瘠之争终究难免，次子怨你偏袒。家分而心未平，你夜里翻看契券，只觉指节发凉。",
            "fail_eff": {"happiness": -8, "rep": -5},
            "tag_succ": "析产有方",
            "tag_fail": "家分心散",
            "is_key": True
          },
          {
            "text": "暂不分家，先命长子掌田事、次子理书卷，各试其能三年",
            "risk_label": "缓图其成 · 静观其变 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "长子督耕有法，次子抄书得钱。三年之间，各见其长，你只需在堂上点头，家声自然不坠。",
            "succ_eff": {"intellect": 3, "happiness": 5},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "缓图知子",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 58,
        "period": "花甲在望",
        "title": "夜书家训，灯下笔落族规",
        "narrative": "秋夜灯下，你以刀笔在竹简上刻字。族中子弟渐多，有赌博斗鸡者，有弃农从商者。老友劝你：世家大族皆立门风，无谱牒家训者，三代而衰。你提笔欲写，却又迟疑——规矩太严则子弟离心，太宽则门风日下。",
        "choices": [
          {
            "text": "立家训十余条，刻简悬于中堂，令子弟每月朔日诵读一遍",
            "risk_label": "严立门风 · 恐伤亲厚 · 成功率 68%",
            "calc_chance": lambda p: 68 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (5 if p.health > 60 else 0),
            "succ_feedback": "朔日诵读，童子声琅琅。数年之后，族中少赌少讼，邻村皆来求抄录一份。你的名字被写进谱牒序中。",
            "succ_eff": {"intellect": 5, "happiness": 3, "rep": 10},
            "fail_feedback": "子弟当面诵读，背后照旧。侄儿抱怨你迂阔。家训虽悬，风吹简响，倒显得中堂格外空。",
            "fail_eff": {"happiness": -6, "rep": -4},
            "tag_succ": "门风有立",
            "tag_fail": "训而不行",
            "is_key": True
          },
          {
            "text": "只述先人事迹与耕读本分，录成一卷，不设罚则，任子孙自省",
            "risk_label": "述而不作 · 以宽化人 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你写祖上逃荒、垦田、抄书三事，笔笔平实。孙辈围读至夜，竟有人悄悄收起了赌具。",
            "succ_eff": {"happiness": 6, "rep": 4},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "述祖化人",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 66,
        "period": "桑榆晚景",
        "title": "故人零落，素幡又过柴门",
        "narrative": "你六十四岁，今年已送走三位旧交。先是同窗的县吏病故，再是当年同游的僧人圆寂于佛寺。今日门前又过素幡，鼓声低而短。你拄杖立于门下，想去送最后一程，可风湿之疾正发，腿脚不听使唤。",
        "choices": [
          {
            "text": "强撑病体，备一束香与素绢，亲往灵前执绋，送故人入土",
            "risk_label": "抱病尽义 · 折损元气 · 成功率 62%",
            "calc_chance": lambda p: 62 + (8 if p.health > 60 else 0),
            "succ_feedback": "你在灵前添香，说了几句旧年之事，满堂皆泣。归途虽疲，心中郁结却松了，夜里睡得极沉。",
            "succ_eff": {"health": -4, "happiness": 6, "rep": 8},
            "fail_feedback": "归途淋了秋雨，当夜寒热交作，延医煎了两剂柴胡。故人已送，病却添了三分。",
            "fail_eff": {"health": -10, "happiness": -4},
            "tag_succ": "执绋尽义",
            "tag_fail": "抱病添疾",
            "is_key": True
          },
          {
            "text": "在自家堂上设一席素菜，向北遥祭，唤儿孙同拜，代为尽礼",
            "risk_label": "遥祭代之 · 礼数稍减 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你率子孙向北三拜，说故人生平。孩子们第一次知道父辈也曾有肝胆之交，席间安静而恭敬。",
            "succ_eff": {"happiness": 4, "rep": 3},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "遥祭寄怀",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 66,
        "period": "桑榆晚景",
        "title": "口述旧事，弟子执笔记之",
        "narrative": "你六十七岁，眼已昏花，抄书吃力。当年随军出关、亲见荒年与流民的旧事，若无人记下，便要随你入土。一位年轻的书生愿执笔为你笔录，只是他家境清寒，需你供纸墨与口粮；而你自家的仓廪也不算丰足。",
        "choices": [
          {
            "text": "留书生在家中厢房，每日口述两时辰，以帛书抄录，成卷后藏于祠堂",
            "risk_label": "耗资存史 · 家计有损 · 成功率 72%",
            "calc_chance": lambda p: 72 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (8 if p.luck > 50 else 0),
            "succ_feedback": "三月成三卷，笔笔皆有年月。乡中长者传阅，说这是本地难得的实录。你把书卷放进祠堂木匣，手抚良久。",
            "succ_eff": {"wealth": -8, "intellect": 6, "rep": 12},
            "fail_feedback": "帛贵墨残，抄到第二卷便断了粮。书生告辞远行，散简留在案头，你翻看时总觉缺了一段。",
            "fail_eff": {"wealth": -6, "happiness": -5},
            "tag_succ": "帛书记事",
            "tag_fail": "书残未竟",
            "is_key": True
          },
          {
            "text": "只将最要紧的三件事口授长孙，让他记住年月与乡里旧姓",
            "risk_label": "择要而传 · 所存无几 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "长孙记性极好，反复背诵，连荒年赈粮的斗数都没错。夜里他复述给你听，你听着听着笑了。",
            "succ_eff": {"intellect": 3, "happiness": 6},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "口授择要",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 74,
        "period": "古稀沧桑",
        "title": "稚孙绕膝，次子远赴边戍",
        "narrative": "你七十二岁，膝下孙儿绕膝嬉闹，最是舍不下。可州府征发，次子被点入军中，要去北边戍守三年。临行前夜，他要你一句话。堂上烛短，里屋孙儿睡熟的呼吸声清晰可闻。",
        "choices": [
          {
            "text": "取出旧箭一枚与祖传短刀相赠，嘱其守军令、护同伴，勿以勇犯险",
            "risk_label": "壮其行色 · 忧在心头 · 成功率 65%",
            "calc_chance": lambda p: 65 + (10 if p.luck > 50 else 0),
            "succ_feedback": "次子跪受刀箭，起身时腰背挺直。三年后他随军归来，肩上添了疤，却带回了整队同乡的性命。",
            "succ_eff": {"health": -3, "happiness": 6, "rep": 10},
            "fail_feedback": "边境风雪苦寒，消息一断数月。你每日倚门望北，白发又添一层，直到来年开春才有书信。",
            "fail_eff": {"health": -6, "happiness": -10},
            "tag_succ": "壮子从军",
            "tag_fail": "倚门望北",
            "is_key": True
          },
          {
            "text": "把家中积攒的钱帛分一半与他，广托同乡照应，只求他平安归来",
            "risk_label": "破财求安 · 未必如愿 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "钱帛分装在两个布囊里，你一一数清。次子含泪收下，说爹放心。你只回了一句：活着回来。",
            "succ_eff": {"wealth": -10, "happiness": 4},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "破财求安",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 74,
        "period": "古稀沧桑",
        "title": "重修坟茔，勒石立于墓前",
        "narrative": "你七十五岁，祖坟经年风雨，封土塌了一角，墓碑字迹也漫漶难辨。族中商议重修，需按门阀谱牒上的世系，把父祖名讳官位一一勒石。可请人撰墓志、雇石工立碑，是一笔不小的开销，族人各房心思不一。",
        "choices": [
          {
            "text": "自出半数资财，按谱牒考订世系，请乡中老儒撰墓志，重立石碑",
            "risk_label": "考系立石 · 耗财招议 · 成功率 70%",
            "calc_chance": lambda p: 70 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (6 if p.health > 60 else 0),
            "succ_feedback": "封土重新培厚，碑上名讳世系分明。清明之日，各房齐来拜扫，连多年不往来的远支也到了。",
            "succ_eff": {"wealth": -12, "happiness": 5, "rep": 12},
            "fail_feedback": "世系一考便生出争议，某房说漏了他家一支。碑虽立起，祭日里的寒脸却比石还冷。",
            "fail_eff": {"wealth": -10, "happiness": -6, "rep": -6},
            "tag_succ": "立石收族",
            "tag_fail": "考系生争",
            "is_key": True
          },
          {
            "text": "先只培土加固，另以墨笔在木牌上重书名讳，待来年从容再议立碑",
            "risk_label": "权宜培土 · 事缓礼存 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "众人担土夯筑一日，木牌新墨黑亮。你亲手把坟前杂草拔净，说先人住处不能荒。",
            "succ_eff": {"happiness": 4, "rep": 3},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "培土守茔",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 80,
        "period": "夕阳辞章",
        "title": "灯尽堂深，子孙环侍榻前",
        "narrative": "你七十九岁，入冬后便少下床。儿孙轮番侍药，煎的是本草上的方子，也请过僧人诵经、医者针灸。今夜灯火将残，你气息微而心却清明。堂下子孙环立，人人等你开口；窗外月色如水，照见你一生走过的那条村路。",
        "choices": [
          {
            "text": "唤子孙近前，一一叫出名字，嘱其守住耕读家风，然后安然闭目",
            "risk_label": "含笑付托 · 灯尽而终 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你把每个孩子的名字都叫了一遍，最后说：田要种，书要读，人要和。说完手一松，面色平静如水，满堂低泣。",
            "succ_eff": {"happiness": 8, "rep": 10},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "含笑而终",
            "tag_fail": "另寻他途",
            "is_key": False
          },
          {
            "text": "命人扶你起身，换上旧日布衣，独自倚窗看最后一轮月，不再言语",
            "risk_label": "独对山水 · 坦然归去 · 成功率 88%",
            "calc_chance": lambda p: 88 + (10 if p.luck > 50 else 0),
            "succ_feedback": "月色移过窗棂，你看了许久，眉目舒展。天明时子孙来唤，你已端坐而去，衣冠整齐，如睡一般。",
            "succ_eff": {"happiness": 8, "rep": 6},
            "fail_feedback": "夜半寒气入骨，你咳了几声才稳下来。虽未如你所愿那般静好，终究是在自家窗下合了眼。",
            "fail_eff": {"health": -8, "happiness": -2},
            "tag_succ": "月下归真",
            "tag_fail": "寒夜灯残",
            "is_key": True
          }
        ]
    },
    {
        "age_rel": 80,
        "period": "夕阳辞章",
        "title": "病榻托付，散尽余财济乡",
        "narrative": "你八十二岁，卧床已久，自知来日无多。匣中还有田契数纸、钱帛若干，另有一卷家训未完。族中侄辈眼望匣子，乡里却有数户因去年旱灾卖儿鬻女。你要在闭眼之前，把这两件事一并了断。",
        "choices": [
          {
            "text": "唤族中尊长与诸子到榻前，逐条交付家训与田契，立下分付之契，各无异议",
            "risk_label": "榻前分付 · 争心暗伏 · 成功率 82%",
            "calc_chance": lambda p: 82 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "你一条条念，一条条指给人看，诸子唯唯。契成之后，你让人扶你靠好，说：我无事矣。是夜遂卒。",
            "succ_eff": {"happiness": 6, "rep": 10},
            "fail_feedback": "念到第三卷时，侄儿忽然插嘴争祭田。你气息一滞，终究按住不提，只把契纸塞进长子手中。",
            "fail_eff": {"happiness": -8, "rep": -4},
            "tag_succ": "榻前交付",
            "tag_fail": "遗言见争",
            "is_key": True
          },
          {
            "text": "命开仓散尽余财与存粮，济助乡里受灾之户，只留家训一卷与薄田数亩",
            "risk_label": "散财济乡 · 身后萧然 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "门前来领粮的人排出半里地。你躺在床上听外头人声，说够了，够了。第三日清晨，你在人声渐远时安然离世，乡人白衣相送。",
            "succ_eff": {"wealth": -25, "happiness": 8, "rep": 15},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "散财归去",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ]
]


# ---- premodern 出身地域（8）与门第阶层（10）----
PREMODERN_REGIONS = [
    ("汴京宣德门", "御街宽阔，瓦舍勾栏彻夜喧闹，酒楼茶坊林立，四方商旅云集，市井繁华。", {"health": 1, "wealth": 3, "rep": 2}),
    ("江南姑苏", "水乡河道纵横，机户织坊林立，漕运码头帆樯相接，文风鼎盛，丝米富庶。", {"wealth": 3.5, "intellect": 2, "happiness": 1}),
    ("泉州刺桐港", "市舶司设于此，蕃商海舶辐辏，香料珠宝云集，海风咸湿，通贸四海。", {"wealth": 4, "luck": 2, "rep": -1}),
    ("徽州休宁", "山多田少，男子多出门行贾，宗族祠堂巍然，重儒重信，勤俭成风。", {"intellect": 3, "rep": 4}),
    ("直隶顺天", "京师首善之地，官署林立，旗民杂居，街市规整，礼法森严。", {"rep": 3, "wealth": 1.5, "happiness": -1}),
    ("天府成都", "沃野千里，茶馆戏台声声入耳，蜀锦名扬，百姓闲适安逸。", {"happiness": 3, "health": 1, "intellect": 1}),
    ("山陕商道", "驼铃古道，晋商票号往来不绝，风沙扑面，商旅重诺守信。", {"wealth": 2, "luck": 1, "health": -1}),
    ("广州十三行", "海禁之下独口通商，洋货行栈毗邻，商贾云集，银钱往来浩繁。", {"wealth": 5, "rep": -2, "luck": 1})
]

PREMODERN_SOCIAL_STRATA = [
    ("江南织造机户", "家中织机数张，日夜赶织绸缎，靠机户手艺营生，日子殷实却辛苦。", {"health": 86, "wealth": 6.5, "intellect": 58, "happiness": 58, "luck": 52, "rep": 55}, "勤巧持家"),
    ("徽州儒商门第", "祖上经商起家，亦贾亦儒，家训以诚信为本，子弟须读书应试，光耀门楣。", {"health": 88, "wealth": 9.5, "intellect": 70, "happiness": 60, "luck": 54, "rep": 68}, "贾而好儒"),
    ("钱塘书院耕读", "家有薄田数亩，耕读并重，父辈供子弟入书院受业，盼科举改换门庭。", {"health": 87, "wealth": 3.2, "intellect": 74, "happiness": 57, "luck": 50, "rep": 62}, "诗礼传家"),
    ("泉州远洋海商", "家中有海船股份，货通南洋诸国，风浪里讨生活，富贵与凶险并存。", {"health": 84, "wealth": 11, "intellect": 62, "happiness": 56, "luck": 58, "rep": 60}, "敢闯重信"),
    ("京畿旗人食禄", "隶于旗籍，按月支领钱粮，不必躬耕劳作，闲时遛鸟听戏，日子安稳。", {"health": 92, "wealth": 8, "intellect": 52, "happiness": 64, "luck": 56, "rep": 58}, "安闲守分"),
    ("乡村私塾寒儒", "世代教蒙学为生，束脩微薄，家徒四壁却藏书满架，清高自守，颇受乡邻敬重。", {"health": 85, "wealth": 1.2, "intellect": 76, "happiness": 51, "luck": 49, "rep": 50}, "清贫守志"),
    ("运河漕帮水手", "常年在漕船上搬运粮米，靠力气吃饭，讲义气，风餐露宿，结交帮中兄弟。", {"health": 90, "wealth": 2.4, "intellect": 49, "happiness": 53, "luck": 51, "rep": 44}, "义气耐劳"),
    ("两淮盐引巨富", "持盐引行销数省，家资巨万，宅第连云，仆从成群，与官府往来密切。", {"health": 89, "wealth": 12, "intellect": 66, "happiness": 62, "luck": 57, "rep": 72}, "阔绰通权"),
    ("晋商票号伙计", "在票号学徒出身，掌银钱汇兑，常年奔走各地，精于算计，恪守号规。", {"health": 86, "wealth": 4.8, "intellect": 68, "happiness": 55, "luck": 53, "rep": 57}, "精算守信"),
    ("边镇屯戍军户", "世袭军籍，屯田守边，粮饷微薄，常在风沙中操练巡防，升迁无望。", {"health": 94, "wealth": 0.6, "intellect": 47, "happiness": 50, "luck": 48, "rep": 40}, "粗豪尚武")
]

# ---- premodern 16 大生命阶段事件池 ----
PREMODERN_STAGE_POOLS = [
  [
    {
        "age_rel": 6,
        "period": "幼年启蒙",
        "title": "塾师授三字经，村塾开蒙第一课",
        "narrative": "你年方六岁，父亲提着一方腊肉，领你拜入村塾。塾师姓陈，案上摆着戒尺和一册翻旧的《三字经》，窗外传来邻家舂米的闷响。同窗开蒙都先背这千字，背不出便要在掌心上挨三下。父亲临走只留一句话：家中只供得起一个读书人，你要想清楚。",
        "choices": [
          {
            "text": "端坐案前逐字跟读，把“人之初”背得滚瓜烂熟，再请塾师圈点",
            "risk_label": "勤勉 · 稳妥 · 成功率 75%",
            "calc_chance": lambda p: 75 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "半月后你已能整段背诵，塾师用朱笔在你书页上画了个圈，父亲听说后多要了一碗米酒。",
            "succ_eff": {"intellect": 10, "rep": 5},
            "fail_feedback": "你张口结舌，掌心挨了戒尺，回家抱着书箱坐到油灯下，倒把“性本善”记了个牢。",
            "fail_eff": {"intellect": 4, "happiness": -5},
            "tag_succ": "初通文墨",
            "tag_fail": "涩口难言",
            "is_key": True
          },
          {
            "text": "只顾看窗外货郎的糖人和拨浪鼓，把书页翻得哗哗响",
            "risk_label": "贪玩 · 无伤 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "一日自在，你尝了半块麦芽糖，也记住了货郎吆喝的调子，夜里竟把它当童谣哼给弟弟听。",
            "succ_eff": {"happiness": 8, "luck": 3},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "顽童一乐",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 6,
        "period": "幼年启蒙",
        "title": "上元庙会，随母亲看社戏傀儡",
        "narrative": "上元夜，镇上搭起灯棚，母亲用粗布巾裹着你挤进人堆。台上傀儡正演《劈山救母》，锣鼓一响，满街都是卖糖炒栗子和面人的吆喝。父亲给的几枚铜钱还揣在你怀里，母亲却攥紧你的手，说散场前要赶回去给祖母熬药。",
        "choices": [
          {
            "text": "挣开母亲的手，钻到台前去摸那傀儡的丝线，看它如何抬手",
            "risk_label": "好奇 · 冒险 · 成功率 70%",
            "calc_chance": lambda p: 70 + (5 if p.luck > 50 else 0),
            "succ_feedback": "你挤到台角，看清老艺人十指翻飞，回家用竹片和烂布头扎了个小傀儡，逗得祖母咳着也笑了。",
            "succ_eff": {"intellect": 4, "happiness": 8},
            "fail_feedback": "人潮一涌你跌在青石板上，膝盖磕出淤青，回家被母亲数落，却记住了那句唱词。",
            "fail_eff": {"health": -4, "happiness": 3},
            "tag_succ": "眼明手巧",
            "tag_fail": "跌撞有得",
            "is_key": False
          },
          {
            "text": "陪母亲守在药炉边，把庙会听来的故事讲给祖母听",
            "risk_label": "孝顺 · 安稳 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "祖母听得合眼微笑，赏你一枚磨得发亮的旧铜钱，母亲看你的眼神也柔和了几分。",
            "succ_eff": {"happiness": 6, "rep": 4},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "膝下承欢",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 10,
        "period": "童年韶光",
        "title": "随父兄入商号，学记账打算盘",
        "narrative": "镇上的米行兼卖布匹，你十岁那年被父亲领进后柜。掌柜姓吴，先让你磨墨誊账，再把一把旧算盘推过来，珠子被前头学徒摸得发亮。门外有交子铺的伙计来兑钱，柜上银钱出出进进。兄长小声提醒你：账目错一笔，一年工钱都赔不起。",
        "choices": [
          {
            "text": "每日临一遍账簿，把算盘口诀背熟，宁可晚睡也要对清当日进出",
            "risk_label": "勤恳 · 立身 · 成功率 72%",
            "calc_chance": lambda p: 72 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "一季下来你算珠不乱，吴掌柜当众把一本小账交你管，还添了两文月钱。",
            "succ_eff": {"wealth": 6, "intellect": 10, "rep": 5},
            "fail_feedback": "你错记了两笔布价，被罚跪在柜台后重抄账本，手指发酸，却把珠算口诀记死了。",
            "fail_eff": {"intellect": 5, "happiness": -6},
            "tag_succ": "心中有账",
            "tag_fail": "错中学乖",
            "is_key": True
          },
          {
            "text": "陪东家少爷斗蛐蛐，替他跑腿买糖糕，图个清闲热闹",
            "risk_label": "随和 · 无争 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你与少爷混熟了，常有零嘴分润，也从他口里听来不少城里商号的闲话门道。",
            "succ_eff": {"happiness": 7, "luck": 3},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "街头人缘",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 10,
        "period": "童年韶光",
        "title": "村中拳师设场，授你扎马步习射",
        "narrative": "村西的打谷场上，一位走镖回乡的老拳师摆开场子，教孩子们扎马步、拉硬弓。弓是竹胎牛筋的，拉满时手臂发抖。同来的孩童多熬不住，跑去看瓦舍说书。拳师眯眼看你，说学武先学忍痛，你若怕苦，趁早回家挑水。",
        "choices": [
          {
            "text": "咬牙扎稳马步，日日拉弓百次，手心磨破也不肯先收势",
            "risk_label": "坚忍 · 强身 · 成功率 65%",
            "calc_chance": lambda p: 65 + (8 if p.health > 60 else 0),
            "succ_feedback": "两月后你一箭射中草人咽喉，拳师点头收你入正式弟子行列，村人见了都称你有股狠劲。",
            "succ_eff": {"health": 10, "intellect": 3, "rep": 5},
            "fail_feedback": "你拉伤了肩，被拳师按在药酒里揉搓，疼得直咧嘴，却把弓步的架势记进了骨头。",
            "fail_eff": {"health": -4, "intellect": 3, "happiness": -4},
            "tag_succ": "筋骨渐壮",
            "tag_fail": "带伤知法",
            "is_key": False
          },
          {
            "text": "只学几路防身招式，余下时辰去瓦舍听人说书",
            "risk_label": "取巧 · 安稳 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你学了三招护身，又听了几回《三国》故事，回家讲给玩伴听，颇受欢迎。",
            "succ_eff": {"health": 4, "happiness": 6},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "粗通拳脚",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 15,
        "period": "少年分流",
        "title": "县试将近，你提篮赴童子试",
        "narrative": "县衙前贴出考期，你十四岁，父亲翻出压箱底的青布长衫，又托人寻廪生作保。考棚里一人一桌，墨臭混着汗味，试题出自四书。邻座少年进场时被搜出夹带，当场逐出，围观的人指指点点。父亲只说了一句：若考不中，明年就得下田或入铺。",
        "choices": [
          {
            "text": "闭门苦读经义，把历年考题逐篇揣摩，孤注一掷赴考",
            "risk_label": "拼搏 · 险中 · 成功率 55%",
            "calc_chance": lambda p: 55 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (5 if p.luck > 50 else 0),
            "succ_feedback": "榜上你的名字列在末等，虽未中秀才，县学先生却记住了你，愿留你在塾中帮教蒙童。",
            "succ_eff": {"intellect": 12, "rep": 8},
            "fail_feedback": "卷上文章写偏了题，你落榜归家，父亲没骂你，只把一盏灯留到深夜，让你自己想明白。",
            "fail_eff": {"intellect": 6, "happiness": -8},
            "tag_succ": "榜上有名",
            "tag_fail": "落榜知耻",
            "is_key": True
          },
          {
            "text": "与乡邻结伴同行，只求稳妥应考，考完便回家帮忙收麦",
            "risk_label": "平稳 · 务实 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你规规矩矩考完，回来赶上割麦，父亲看你惜力气又肯下力，心里踏实了几分。",
            "succ_eff": {"wealth": 3, "intellect": 4, "happiness": 5},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "安分守拙",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 15,
        "period": "少年分流",
        "title": "家道中落，父亲欲送你投师学艺",
        "narrative": "家里为祖母治病借了印子钱，父亲把几亩薄田抵了出去。饭桌上他沉默半晌，说读书这条道恐怕走不通了，城里木匠铺正收学徒，三年出师，管饭不给工钱。你床头还压着读了一半的《千字文》，油灯芯烧得只剩一点亮，窗外雨敲着瓦。",
        "choices": [
          {
            "text": "次日便去木匠铺叩头拜师，从拉大锯、刨木料学起，三年不悔",
            "risk_label": "务实 · 立身 · 成功率 78%",
            "calc_chance": lambda p: 78 + (5 if p.health > 60 else 0),
            "succ_feedback": "师父见你手稳心细，半年便许你上刨台，说这门手艺饿不死人，你也第一次挣回自己的工钱。",
            "succ_eff": {"health": 5, "wealth": 8, "rep": 5},
            "fail_feedback": "你刨坏了东家的门板，赔了半月工钱，师父骂你手笨，你却把那道木纹记了一辈子。",
            "fail_eff": {"wealth": -4, "intellect": 4, "happiness": -6},
            "tag_succ": "一技在手",
            "tag_fail": "赔钱长艺",
            "is_key": True
          },
          {
            "text": "白天替人挑水打短工，夜里就着残灯把旧书再读一遍",
            "risk_label": "倔强 · 苦撑 · 成功率 45%",
            "calc_chance": lambda p: 45 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "塾中先生听说你夜读不辍，让你白日抄书换米，你竟又摸回了笔墨生计。",
            "succ_eff": {"intellect": 10, "rep": 6},
            "fail_feedback": "连熬几夜你病倒了，草药钱花去大半积蓄，书到底没能接着读下去。",
            "fail_eff": {"health": -10, "wealth": -6, "intellect": 5},
            "tag_succ": "灯下不辍",
            "tag_fail": "贫病折志",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 18,
        "period": "成人立志",
        "title": "晋商票号招学徒，你随乡人入号",
        "narrative": "镇上几位老西儿回乡招人，说票号要在南边开分庄，收识字的少年学汇兑。你十七岁，能写会算，正合他们眼缘。号中规矩极严：白日算银、誊写汇票，夜里还要习字，三年不得私留一文钱。同乡有人劝你留下守几亩田，安稳一生。",
        "choices": [
          {
            "text": "入号立契，苦练珠算与汇券笔法，随掌柜远行分庄见世面",
            "risk_label": "远行 · 搏业 · 成功率 60%",
            "calc_chance": lambda p: 60 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (6 if p.luck > 50 else 0),
            "succ_feedback": "三年后你已能独当一面，一封汇票在你笔下分毫不差，掌柜许你跟着走南闯北，见识了白银的斤两。",
            "succ_eff": {"wealth": 18, "intellect": 8, "rep": 8},
            "fail_feedback": "分庄遇上官府封号查账，你被扣了半年工钱，虽失了财，却学会了如何与官面周旋。",
            "fail_eff": {"wealth": -8, "intellect": 6, "happiness": -6},
            "tag_succ": "汇通四方",
            "tag_fail": "折银长识",
            "is_key": True
          },
          {
            "text": "留在本号打杂，替老掌柜抄信记账，静观行情再作打算",
            "risk_label": "守成 · 观望 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你在总号站住了脚，识得银钱往来的门道，虽未出门，也攒下了一份踏实名声。",
            "succ_eff": {"wealth": 8, "intellect": 6, "rep": 4},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "稳坐总号",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 18,
        "period": "成人立志",
        "title": "粤海开市，十三行招记账伙计",
        "narrative": "海禁稍有松弛，广州城外十三行的商馆又热闹起来。有行商到内地招识字伙计，管账、验货、招呼番客。你十九岁，正想立一番事业，族中长辈却摇头：与番人打交道，弄不好便倾家荡产，还落个通番的名声。行商给的工钱，是你眼下活计的三倍。",
        "choices": [
          {
            "text": "应招南下，学说几句番话，替行商验货记账，摸清海上货价",
            "risk_label": "闯荡 · 逐利 · 成功率 58%",
            "calc_chance": lambda p: 58 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (8 if p.luck > 50 else 0),
            "succ_feedback": "你记清了茶叶与生丝的行情，一季下来分得花红，行商许你独自押货看仓，眼界大开。",
            "succ_eff": {"wealth": 25, "intellect": 8, "luck": 5},
            "fail_feedback": "一船货物遇上风浪延误，你被扣了月钱，还替人赔了亏空，好在学明白了海船的凶险。",
            "fail_eff": {"wealth": -12, "intellect": 5, "happiness": -7},
            "tag_succ": "行商起家",
            "tag_fail": "亏空识险",
            "is_key": True
          },
          {
            "text": "谢过行商，留在乡中守着祖业，农闲时教几个蒙童识字",
            "risk_label": "安分 · 守拙 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你守着几亩田与一屋旧书，日子清淡却无风波，乡邻都称你是个稳妥后生。",
            "succ_eff": {"wealth": 4, "happiness": 8, "rep": 6},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "耕读传家",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 21,
        "period": "青春韶华",
        "title": "贡院秋风里的一场落第",
        "narrative": "秋闱放榜，你挤在贡院墙外的人群里，从杏榜上寻到自己的名字，却只落在副榜。同乡的富家子已备下回乡的骡马，你若再留一年，盘缠只够赁一间城郊破屋；若就此南归，塾师的束脩与母亲的期盼又该如何交代。",
        "choices": [
          {
            "text": "留在京城赁屋再读一年，替书铺抄书换取灯油与饭食",
            "risk_label": "盘缠告罄 · 得失难料 · 成功率 65%",
            "calc_chance": lambda p: 65 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (5 if p.luck > 50 else 0),
            "succ_feedback": "你抄书换来的铜钱勉强够用，寒夜里就着一盏油灯把八股文章磨了又磨。次年乡试，你的名字终于登上正榜，同乡再不敢轻看你。",
            "succ_eff": {"intellect": 10, "rep": 6},
            "fail_feedback": "冬衣当了又当，抄书的钱终究不敷。你病倒在破屋里，被人抬上南归的船；功名未成，倒把身子与家财都赔了进去。",
            "fail_eff": {"health": -8, "wealth": -12, "intellect": 4},
            "tag_succ": "苦读成名",
            "tag_fail": "铩羽而归",
            "is_key": True
          },
          {
            "text": "收拾行囊趁早回乡，把落第之事说与母亲，先做几年塾师",
            "risk_label": "安分守拙 · 无甚波澜 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你回到乡里设馆授徒，束脩虽薄，却能晨昏侍奉母亲。旧日同窗来寄书信，你提笔回了一首自嘲的诗，竟也渐渐在乡里有了些名声。",
            "succ_eff": {"happiness": 4, "rep": 3},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "安分守拙",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 21,
        "period": "青春韶华",
        "title": "商号柜前的第一封荐书",
        "narrative": "族叔在城里缎庄做二掌柜，愿为你写一封荐书，引荐你入商号当伙计。可同乡又说，口外的茶马道上利厚，只消两三年便能攒下本钱。你攥着那封信站在城门口，风把信角吹得发响，一时不知该往哪边走。",
        "choices": [
          {
            "text": "揣着荐书入商号，从扫地抹柜学起，先攒见识与人脉",
            "risk_label": "寄人篱下 · 前程未卜 · 成功率 72%",
            "calc_chance": lambda p: 72 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (6 if p.luck > 50 else 0),
            "succ_feedback": "你手脚勤快，账目记得分明，掌柜渐渐许你上柜。三年下来，你识得银钱成色、行市涨落，也攒下第一笔体己银子。",
            "succ_eff": {"wealth": 15, "intellect": 8, "rep": 4},
            "fail_feedback": "你算错一笔货账，掌柜当众斥责，伙计们背后叫你外乡呆子。工钱扣了大半，年节也不好意思回乡。",
            "fail_eff": {"wealth": -8, "happiness": -6, "rep": -3},
            "tag_succ": "柜前立身",
            "tag_fail": "算错一账",
            "is_key": True
          },
          {
            "text": "留在族叔的缎庄里做个帮闲，先看清行情再定去留",
            "risk_label": "稳扎稳打 · 不冒大险 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你在缎庄里看货议价，学着分辨绸缎的成色与产地。虽没赚到大钱，却把行里的门道摸清，来日若自立门户便不吃亏。",
            "succ_eff": {"wealth": 5, "intellect": 6, "happiness": 2},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "稳扎稳打",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 24,
        "period": "初涉人世",
        "title": "县衙书吏房的一纸投充",
        "narrative": "县衙书吏房缺一名缮写，熟人递话，说只消纳几两银子的纸笔费便可投充。可书吏俸薄，衙中陋规却多；你若接了这差，往后经手的田赋册籍，难免要替人做手脚，夜里还能否睡得安稳。",
        "choices": [
          {
            "text": "纳银投充书吏，专管抄录田契与钱粮册，暗记其中门道",
            "risk_label": "近墨者黑 · 心怀惴惴 · 成功率 68%",
            "calc_chance": lambda p: 68 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (4 if p.luck > 50 else 0),
            "succ_feedback": "你字迹端正，册籍抄得清楚，县丞也肯赏脸。三年间你把田赋、里甲的关节都看在眼里，往后替人办一桩事，便有人情可收。",
            "succ_eff": {"wealth": 10, "intellect": 8, "rep": 5},
            "fail_feedback": "一桩钱粮亏空追查下来，上官只拿书吏顶罪。你赔了银子，还落了个手脚不净的名声，走在街上都被人指点。",
            "fail_eff": {"wealth": -15, "happiness": -5, "rep": -8},
            "tag_succ": "衙中老手",
            "tag_fail": "替人顶罪",
            "is_key": True
          },
          {
            "text": "婉言推却这桩差事，宁可回乡守着几亩薄田度日",
            "risk_label": "安贫守拙 · 无欲则刚 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你没接那纸投充，照旧在乡里耕种读书。日子虽清苦，夜里睡觉却安稳，族中长辈也说你是个本分人。",
            "succ_eff": {"happiness": 6, "rep": 4},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "清白持身",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 24,
        "period": "初涉人世",
        "title": "漕船离岸前的生死文书",
        "narrative": "漕帮船主招人押货北上，说这一趟走运河，过了清江浦便要签一张生死文书，翻船则人货两空，与船主无涉。给的船资是你在乡下做一年活计也攒不下的数，可母亲这两日正犯咳疾，药钱尚无着落。",
        "choices": [
          {
            "text": "签下文书随漕船北上，替船主看货对单、照料舱中货物",
            "risk_label": "风涛莫测 · 命悬一线 · 成功率 60%",
            "calc_chance": lambda p: 60 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (8 if p.luck > 50 else 0) + (6 if p.health > 60 else 0),
            "succ_feedback": "一路过闸穿坝，你学着看水位、认码头，也替船主识破一回掺假的货色。到通州卸货时，你揣着船资，第一次觉出运河水有多养人。",
            "succ_eff": {"wealth": 22, "intellect": 7, "rep": 3},
            "fail_feedback": "船在风口搁浅，货物浸水，你虽捡回性命，船资却被扣个干净，还落下寒疾，回乡整整咳了一个冬天。",
            "fail_eff": {"health": -12, "wealth": -6, "happiness": -6},
            "tag_succ": "漕河历练",
            "tag_fail": "风涛受挫",
            "is_key": True
          },
          {
            "text": "谢过船主，留在岸上替人挑脚搬运，守着母亲煎药",
            "risk_label": "粗茶淡饭 · 亲侍汤药 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你日日挑担换几文铜钱，夜里替母亲煎药捶背。银钱不多，母亲的病却渐渐好了，邻里都说你是个孝子。",
            "succ_eff": {"health": 2, "happiness": 8, "rep": 4},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "孝养亲前",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 27,
        "period": "成家立业",
        "title": "三媒六聘里的一桩难事",
        "narrative": "媒婆来递庚帖，说的是绸缎行东家的女儿，嫁妆丰厚，只是要你入赘，日后孩子须随女家姓。你自家也有一位青梅竹马的姑娘，聘礼却拿不出，她父母已放出话来，说要另许人家。",
        "choices": [
          {
            "text": "咬牙四处告贷，典当祖传银镯，凑齐聘礼娶那位青梅竹马",
            "risk_label": "债台高筑 · 情义两全 · 成功率 66%",
            "calc_chance": lambda p: 66 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (5 if p.luck > 50 else 0),
            "succ_feedback": "你典了祖父留下的一对银镯，又向同窗告贷，聘礼总算凑齐。花轿进门那日，她掀帘看你，眼睛红红的，往后的苦日子也算有了奔头。",
            "succ_eff": {"wealth": -8, "happiness": 12, "rep": 5},
            "fail_feedback": "银子到底没凑够，姑娘被许给了邻县的粮商。你背着一身债回乡，夜里听见锣鼓声，都觉得像是替别人办的喜事。",
            "fail_eff": {"wealth": -6, "happiness": -15},
            "tag_succ": "有情人成",
            "tag_fail": "聘礼成空",
            "is_key": True
          },
          {
            "text": "婉拒入赘，也暂缓婚事，先攒两年本钱再从容议亲",
            "risk_label": "缓议婚期 · 稳中求全 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你把心思都放在生计上，两年间攒下些本钱。虽误了婚期，说亲的人反倒多了起来，你也不必再看谁的脸色行事。",
            "succ_eff": {"wealth": 10, "intellect": 4, "happiness": -2},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "缓议婚期",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 27,
        "period": "成家立业",
        "title": "巷口小铺开张前的那一夜",
        "narrative": "你在城隍庙巷口赁下半间门面，打算开一间杂货铺，卖些针头线脑、酱醋茶盐。牙行的人却来讨行帖钱，说没有牙帖，货便不许过秤；隔壁的老铺也放出风来，说要与你斗价。",
        "choices": [
          {
            "text": "照数交了牙帖钱，再从一个利字上让利三分，先留住街坊主顾",
            "risk_label": "本小利薄 · 前途难料 · 成功率 70%",
            "calc_chance": lambda p: 70 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (5 if p.luck > 50 else 0),
            "succ_feedback": "你把秤放足，货色又实在，街坊渐渐认你的招牌。半年下来，隔壁老铺没挤倒你，你倒添了两口货柜，还雇了个半大孩子看店。",
            "succ_eff": {"wealth": 18, "intellect": 5, "rep": 6},
            "fail_feedback": "让利太狠，本钱周转不开，赊出去的账又收不回来。入冬时你只得把货柜折价盘给隔壁，铺面换了别家的幌子。",
            "fail_eff": {"wealth": -18, "happiness": -6, "rep": -4},
            "tag_succ": "铺面兴隆",
            "tag_fail": "折本关张",
            "is_key": True
          },
          {
            "text": "先不开铺，挑担走街串巷叫卖，摸清行情再谈门面",
            "risk_label": "小本经营 · 稳妥无虞 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你挑着担子走遍几条街巷，什么货好卖、哪位街坊讲信用，心里都有了数。攒下的铜钱虽少，却是实打实的本钱。",
            "succ_eff": {"wealth": 8, "intellect": 6},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "货郎识市",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 31,
        "period": "三十而立",
        "title": "族祠分产时的那纸田契",
        "narrative": "族中长辈故去，祠堂里议分祭田与房舍。你这一支寡母幼弟，按旧例只该得薄田两亩；可你手里另有一纸祖父手书的字据，写着祭田归长房掌管，余田三房均分，眼下正该不该当众取出来。",
        "choices": [
          {
            "text": "当众取出祖父手书字据，请族长与三房长辈一同验看",
            "risk_label": "族议难测 · 得罪长房 · 成功率 64%",
            "calc_chance": lambda p: 64 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (6 if p.luck > 50 else 0),
            "succ_feedback": "族老传看字据，认得出是祖父笔迹，长房无话可说。你分得田六亩，还替寡母争下一间正屋；只是长房从此见你便冷着脸。",
            "succ_eff": {"wealth": 20, "happiness": -3, "rep": 5},
            "fail_feedback": "长房一口咬定字据是伪造，族老们各打圆场，最后你只得薄田三亩了事。兄弟间从此生分，逢年过节也不相往来。",
            "fail_eff": {"wealth": -5, "happiness": -10, "rep": -4},
            "tag_succ": "据理分产",
            "tag_fail": "族中生隙",
            "is_key": True
          },
          {
            "text": "不与长房相争，只领应得的薄田，另谋别业养家",
            "risk_label": "吃亏是福 · 家和为上 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你拱手让了祭田，族长反觉得你识大体，日后族中有事，总先想着你。你带着妻儿另谋生计，日子虽窄，心却是齐的。",
            "succ_eff": {"happiness": 5, "rep": 8},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "让产得和",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 31,
        "period": "三十而立",
        "title": "清丈田亩时那根丈量绳",
        "narrative": "县里奉文清丈田亩，重新攒造鱼鳞图册。丈量书手到了你们村，说你家那块河滩地量出来比原册多出三分，若不多纳粮，便要报作隐田。乡邻私下劝你塞些银子，把弓绳放松些。",
        "choices": [
          {
            "text": "如数认下多出的田亩，照新册纳税，免得日后被人首告",
            "risk_label": "赋役加重 · 问心无愧 · 成功率 74%",
            "calc_chance": lambda p: 74 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (4 if p.luck > 50 else 0) + (4 if p.health > 60 else 0),
            "succ_feedback": "你当着里正与书手的面把田亩一一认下。虽每年多纳几斗粮，却换得一身清白；后来邻村有人因隐田被追缴三年，你家安然无事。",
            "succ_eff": {"wealth": -6, "happiness": 4, "rep": 10},
            "fail_feedback": "新册虽上了，你的名字却被人记下。往后乡里摊派差役、修堤筑坝，总先点你出钱出力，你才知老实二字也是要付利息的。",
            "fail_eff": {"wealth": -12, "happiness": -6, "rep": 3},
            "tag_succ": "奉公守册",
            "tag_fail": "忠厚受累",
            "is_key": True
          },
          {
            "text": "私下寻书手说合，松一松弓绳，仍旧按旧册完粮",
            "risk_label": "因循旧例 · 稳中有险 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你塞了两串铜钱，书手在树荫下把弓绳松了半寸，田亩终按旧册报了上去。事情办得隐秘，只是你从此见着官差便心里发虚。",
            "succ_eff": {"wealth": 6, "happiness": -4, "rep": -2},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "旧册完粮",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 36,
        "period": "负重前行",
        "title": "里甲催征秋粮，牙行压价",
        "narrative": "秋粮开征，里长沿门催逼，你家中尚缺三成。本欲挑新谷往镇上牙行粜卖，牙人却串通压价，还说可代你垫纳、秋后加利偿还。邻家老陈欠粮未清，已被锁进班房。天一亮便要点名赴县衙听点，你手里只剩一夜工夫。",
        "choices": [
          {
            "text": "连夜挑谷进城，寻熟识米行现银粜卖，绕开牙人",
            "risk_label": "风霜夜路 · 行市难料 · 成功率 65%",
            "calc_chance": lambda p: 65 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (5 if p.luck > 50 else 0),
            "succ_feedback": "米行掌柜念旧交，按市价收了你的谷，现银到手，粮数凑足。里长见你爽利，点名时也未多加刁难。",
            "succ_eff": {"wealth": 6, "intellect": 8, "rep": 5},
            "fail_feedback": "夜半遇雨，谷袋受潮折了斤两，只得贱价出手。粮数仍缺一斗，里长记了你一笔，日后再补。",
            "fail_eff": {"wealth": -8, "intellect": 4, "happiness": -5},
            "tag_succ": "谷贱心稳",
            "tag_fail": "夜雨折粮",
            "is_key": True
          },
          {
            "text": "变卖家里那头耕牛，凑足粮数封纳，先保清白",
            "risk_label": "断腕保身 · 来年乏力 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "牛贩趁急压价，你仍咬牙卖了。粮数如数封纳，里长挑了挑眉，把名字从欠单上划去。来年春耕，只能借邻家牛力。",
            "succ_eff": {"wealth": -5, "happiness": -4, "rep": 4},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "清白封纳",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 36,
        "period": "负重前行",
        "title": "兄弟析产，老宅该归谁",
        "narrative": "父亲故去三年，族中长辈终于发话析产。兄长以长子奉祀为由，要独占临街老宅；你出力最多，却只分得城外两亩薄田。宗祠议事这日，族长捻着胡须等你表态，妻子在屏后红了眼眶。",
        "choices": [
          {
            "text": "请族长与族老公议，立下分家文书，各执一纸为凭",
            "risk_label": "对簿宗祠 · 亲情生隙 · 成功率 60%",
            "calc_chance": lambda p: 60 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "族老翻出旧年账簿，说你侍疾出力最多，判老宅归你、兄长另得田租补偿。文书用印，各有凭据，兄长脸色难看。",
            "succ_eff": {"wealth": 12, "happiness": 3, "rep": 8},
            "fail_feedback": "兄长跪在祠堂前哭诉奉祀之责，族老动了恻隐，老宅仍归他，只补你十两银子，兄弟从此生分。",
            "fail_eff": {"wealth": 5, "happiness": -8, "rep": -3},
            "tag_succ": "文书为凭",
            "tag_fail": "手足生隙",
            "is_key": True
          },
          {
            "text": "让出老宅，只求兄长立契，替你供母亲晚年汤药",
            "risk_label": "退让求稳 · 人情难倚 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "兄长当众立契，允诺母亲药食由他承担。族长点头称善，你搬出老宅，心里空了一块，却也卸下一副担子。",
            "succ_eff": {"happiness": -3, "rep": 5},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "让宅求安",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 40,
        "period": "中年险滩",
        "title": "遭诬入狱，衙役暗索贿",
        "narrative": "邻村失窃的绸缎，竟从你佃户家中搜出，仇家趁机递了状纸。县衙差役将你锁走，牢头在耳旁低语：使些银子便可取保候审。堂上老爷尚未升座，家中已当尽首饰，狱卒开始按日索要饭钱。",
        "choices": [
          {
            "text": "托旧友向刑房书吏递银打点，先求取保，再寻反证",
            "risk_label": "官门似海 · 理屈难明 · 成功率 55%",
            "calc_chance": lambda p: 55 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (5 if p.luck > 50 else 0),
            "succ_feedback": "书吏收了银子，替你递上一纸保状。你出狱寻到当日买绸的货郎，对上了牙行账簿，冤情终于有了转机。",
            "succ_eff": {"wealth": -10, "intellect": 8, "rep": 3},
            "fail_feedback": "银子如泥牛入海，牢头翻脸，将你与盗贼同押。你在稻草上熬了半月，人瘦了一圈，所幸未曾屈打成招。",
            "fail_eff": {"health": -10, "wealth": -12, "happiness": -8},
            "tag_succ": "银通枢吏",
            "tag_fail": "钱落黑牢",
            "is_key": True
          },
          {
            "text": "请里正与乡邻二十人联名具保，先行出狱，再慢慢辩白",
            "risk_label": "众口为凭 · 只保一时 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "里正念你平素修桥补路，邀二十户联名画押。县衙准了保状，你暂得归家，案卷却仍悬着，日子过得提心吊胆。",
            "succ_eff": {"happiness": -4, "rep": 6},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "乡邻具保",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 40,
        "period": "中年险滩",
        "title": "商号倒账，债主登门",
        "narrative": "你与人合开的布号，因合伙人在苏州囤货失手，账面亏空三百两。年关将近，债主揣着借据堵在门口，伙计已散了大半。掌柜劝你连夜关铺走人，账上却还压着十几户织工的工钱。",
        "choices": [
          {
            "text": "召集债主当众盘账，变卖铺面存货，按成分还",
            "risk_label": "砸锅卖铁 · 信誉扛肩 · 成功率 60%",
            "calc_chance": lambda p: 60 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "债主见你肯变产清账，倒有几人愿意宽限三月。铺面盘出去，还清七成，织工工钱也结了，余下慢慢填补。",
            "succ_eff": {"wealth": -15, "intellect": 5, "rep": 12},
            "fail_feedback": "存货贱卖，只够还四成。有债主一纸诉状告到衙门，你被拘了半日，靠邻里凑银才得脱身。",
            "fail_eff": {"wealth": -18, "happiness": -8, "rep": -5},
            "tag_succ": "变产清账",
            "tag_fail": "债主鸣官",
            "is_key": True
          },
          {
            "text": "先结清织工血汗工钱，再与债主逐一立约缓期归还",
            "risk_label": "先顾人心 · 后补银账 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "织工拿到工钱千恩万谢，替你在街坊间说了不少好话。债主见人心向着你，多半肯宽限。铺子虽关，名声未倒。",
            "succ_eff": {"wealth": -10, "happiness": 3, "rep": 8},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "工钱不欠",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 45,
        "period": "动荡考验",
        "title": "兵信传来，举家何往",
        "narrative": "江北传来兵信，长毛已破邻府，官道上的逃难人一日多过一日。族中议定迁往山里祖坟旁的旧屋，可你铺中还有一批货未脱手，老母又病着经不起颠簸。城门守军开始盘查路引，风声一日紧似一日。",
        "choices": [
          {
            "text": "连夜烧掉欠据，携老母细软先行入山，货留给伙计照看",
            "risk_label": "弃货保命 · 乱世难料 · 成功率 58%",
            "calc_chance": lambda p: 58 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (5 if p.luck > 50 else 0) + (5 if p.health > 60 else 0),
            "succ_feedback": "山路虽险，一家老小终在祖屋安顿。三日后乱兵过境，镇上铺面被抢掠一空，你只损失了那批货。",
            "succ_eff": {"health": 3, "wealth": -8, "rep": 5},
            "fail_feedback": "半路遇溃兵盘查，细软被搜去大半，老母受了风寒。所幸你递上路引，一家才被放过，仓皇抵达山中。",
            "fail_eff": {"health": -8, "wealth": -15, "happiness": -8},
            "tag_succ": "弃货全生",
            "tag_fail": "途中遭掠",
            "is_key": True
          },
          {
            "text": "闭门不出，将粮米藏入地窖，静候官军收复城池",
            "risk_label": "以静待动 · 祸福难卜 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你把门户钉死，粮米分藏三处地窖，阖家缩在后院。乱兵过巷两回，竟未破门。半月后官军入城，市面重开。",
            "succ_eff": {"wealth": -5, "happiness": -3, "rep": 4},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "闭门避乱",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 45,
        "period": "动荡考验",
        "title": "老母病故，丁忧守制",
        "narrative": "老母熬过残冬，终究在三月里去了。按制，你须去官守孝三年，衙署里的差事眼看要被人接手；可若夺情留任，言官一支笔便能参你个不孝。灵前白幡还没挂稳，同僚已上门探问口风。",
        "choices": [
          {
            "text": "上呈丁忧文书，归乡守制三年，田里读书兼课子侄",
            "risk_label": "守礼全孝 · 仕途暂歇 · 成功率 70%",
            "calc_chance": lambda p: 70 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "上司准了丁忧，同僚赞你知礼。三年里你在乡设塾教蒙童，声名反而更重，丧满之日便有旧交来邀。",
            "succ_eff": {"intellect": 6, "happiness": 3, "rep": 10},
            "fail_feedback": "你递了文书，却有人在背后说你借孝避差。差事果然被他人接手，三年后再想复起，位置早已没了。",
            "fail_eff": {"wealth": -5, "happiness": -6, "rep": -5},
            "tag_succ": "守制全孝",
            "tag_fail": "去位失势",
            "is_key": True
          },
          {
            "text": "托上官具疏夺情，留任办完河工再补守制",
            "risk_label": "夺情留任 · 物议难平 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "上官念你河工要紧，具疏夺情。你留任把堤修完，却总有人背地里指点，说你不肯放下乌纱。夜里想起母亲，泪湿枕席。",
            "succ_eff": {"wealth": 8, "happiness": -8, "rep": -6},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "夺情留任",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 51,
        "period": "知命之年",
        "title": "荒年米贵，仓门开否",
        "narrative": "连月大旱，米价一日三涨。你是乡里推举的仓正，社仓里还存着三百石谷。饥民聚在仓外，有人跪地磕头，也有人磨刀扬言要砸仓。县衙的赈粮文书迟迟未到，擅动社仓是罪，不开又怕闹出人命。",
        "choices": [
          {
            "text": "按户造册，先贷后赈，开仓平粜，同时具报县衙",
            "risk_label": "擅动社仓 · 罪责自担 · 成功率 62%",
            "calc_chance": lambda p: 62 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "你按户造册，米价应声落了三成，饥民散了大半。县衙追认你权宜得当，只申饬一句，乡里却记了你的好。",
            "succ_eff": {"wealth": -8, "intellect": 6, "rep": 15},
            "fail_feedback": "仓谷出了大半，账目却对不上，有人告你私吞。你自掏银两补齐亏空，虽免了官司，家底也去了一层。",
            "fail_eff": {"wealth": -15, "happiness": -6, "rep": -8},
            "tag_succ": "开仓济饥",
            "tag_fail": "账亏蒙冤",
            "is_key": True
          },
          {
            "text": "严守仓规，只将自家存粮分与最贫的十余户",
            "risk_label": "量力而行 · 杯水车薪 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你把自家米缸分了一半出去，最难的十余户熬过了青黄不接。其余人家散去，仓谷未动，你也未惹官司。",
            "succ_eff": {"wealth": -6, "happiness": 3, "rep": 5},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "分粮济急",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 51,
        "period": "知命之年",
        "title": "倦于簿书，辞官归乡",
        "narrative": "你在衙署做了半辈子书吏，案牍堆得比人高，升迁却总轮不到。新来的知县带了自家幕友，处处架空老人。故乡来信说老宅漏雨、儿子科考无钱打点。你年过五十，开始盘算这顶帽子还值不值得戴。",
        "choices": [
          {
            "text": "递上辞呈，收拾行囊归乡，设馆授徒兼课子侄",
            "risk_label": "挂冠而去 · 生计另谋 · 成功率 68%",
            "calc_chance": lambda p: 68 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "辞呈递上，知县假意挽留几句便准了。你回到老宅修屋开馆，四乡学子登门，束脩虽薄，日子倒清净自在。",
            "succ_eff": {"intellect": 8, "happiness": 10, "rep": 5},
            "fail_feedback": "归乡后方知人情冷暖，旧日同年避而不见，馆也一时开不起来。你守着薄田熬了两年，才慢慢有了起色。",
            "fail_eff": {"wealth": -8, "happiness": -8, "rep": -3},
            "tag_succ": "挂冠归里",
            "tag_fail": "归乡冷落",
            "is_key": True
          },
          {
            "text": "暂不辞官，暗中誊录旧年案卷，另寻门路调任他县",
            "risk_label": "忍气周旋 · 静待时机 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你把历年案卷誊得清清楚楚，借公差之便结识邻县主簿。调任虽未成，新知县却也看出你的用处，不再处处相逼。",
            "succ_eff": {"wealth": 3, "intellect": 6, "rep": 3},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "案牍周旋",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 58,
        "period": "花甲在望",
        "title": "祠堂灯下与族老重修谱牒",
        "narrative": "族老捧出虫蛀旧谱，叹三代名讳已无从查考。你年近花甲，儿孙绕膝，理当为宗族留下规矩。修谱需银三十两，还要开罪两房旁支；若不修，他日子孙相逢，竟不知同出一祖。",
        "choices": [
          {
            "text": "捐半年束脩，请老塾师秉笔，先订族规十二则，再续谱系",
            "risk_label": "散财 · 结怨 · 成功率 68%",
            "calc_chance": lambda p: 68 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (10 if p.luck > 50 else 0),
            "succ_feedback": "族谱装成，宗祠设宴，旁支虽有不快，终在规条前低了头；小儿辈第一次知道自己从何处来。",
            "succ_eff": {"wealth": -12, "happiness": 6, "rep": 8},
            "fail_feedback": "银钱花去大半，旁支仍藏私册不交，谱中缺了两房；你方知聚族之事，急不得。",
            "fail_eff": {"wealth": -12, "happiness": -4, "rep": -5},
            "tag_succ": "谱牒初成",
            "tag_fail": "聚族未谐",
            "is_key": True
          },
          {
            "text": "只录本支三代，抄成简册藏于家庙，量力而行",
            "risk_label": "守分 · 稳妥 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "简册虽薄，名讳清晰，儿孙日日可诵；族中老人亦赞你稳妥，不争一时之名，反多得几分敬重。",
            "succ_eff": {"happiness": 4, "rep": 4},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "简册传家",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 58,
        "period": "花甲在望",
        "title": "捐田设义庄以赡族中孤寡",
        "narrative": "族中寡嫂无力自养，城外饥民亦常来叩门。你手头有薄田八十亩，若仿范氏旧例设义庄，可养族中孤寡、延师课读；只是自家几个儿子未必情愿，田一捐出，便再收不回。",
        "choices": [
          {
            "text": "划出五十亩作义庄公田，立契入祠，请族中正直者轮管",
            "risk_label": "让利 · 招怨 · 成功率 60%",
            "calc_chance": lambda p: 60 + (10 if p.luck > 50 else 0),
            "succ_feedback": "义庄立成，孤寡按月领米，义学里书声不绝；你路过时，孩子们起身唤你一声太公。",
            "succ_eff": {"wealth": -18, "happiness": 8, "rep": 10},
            "fail_feedback": "管事者中饱私囊，账目不清，儿子们怨你偏心；你亲自查账，追回半数，也看清了人心。",
            "fail_eff": {"wealth": -18, "happiness": -5, "rep": -3},
            "tag_succ": "义庄初立",
            "tag_fail": "账目生疑",
            "is_key": True
          },
          {
            "text": "先设义学一间，请塾师课族中子弟，余田留给儿孙",
            "risk_label": "择要 · 周全 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "义学开在祠堂西厢，族中子弟免费附读；儿孙虽少得几亩，却也无人再怨你偏心。",
            "succ_eff": {"wealth": -8, "happiness": 5, "rep": 6},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "义学开蒙",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 66,
        "period": "桑榆晚景",
        "title": "召齐子侄交付田契账册",
        "narrative": "你年过六旬，眼力不济，账簿细字已看不明。三个儿子各有心思：长子稳妥却懦，次子精明而贪，三子尚幼。田契账册终要交出去，是当众分明立下析产文书，还是只交一半、留一手以观其后？",
        "choices": [
          {
            "text": "请族老作中，当众立析产文书，田宅账目一一分明",
            "risk_label": "明分 · 失权 · 成功率 65%",
            "calc_chance": lambda p: 65 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (10 if p.luck > 50 else 0),
            "succ_feedback": "文书画押，三房各得其所，族老赞你公道；此后你只管含饴弄孙，不再过问钱粮。",
            "succ_eff": {"happiness": 7, "rep": 6},
            "fail_feedback": "次子嫌分得少，当场争执，文书虽立，兄弟已生嫌隙；你夜里辗转，知家业难齐。",
            "fail_eff": {"happiness": -7, "rep": -4},
            "tag_succ": "析产分明",
            "tag_fail": "兄弟生隙",
            "is_key": True
          },
          {
            "text": "只交田契与半数银钱，自留养老之资，余者立遗嘱封存",
            "risk_label": "留手 · 自养 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "儿子们各得其所，你手中有粮心不慌；谁孝顺谁疏懒，日子一长自然看得分明。",
            "succ_eff": {"wealth": 6, "happiness": 4},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "留资自养",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 66,
        "period": "桑榆晚景",
        "title": "延请坐堂郎中细论本草",
        "narrative": "入秋后你咳嗽不止，夜里盗汗。城南药铺有位坐堂郎中，善用本草与针灸，诊金却不薄；另有游方道人自称有祖传丹方，价廉速效。家中积蓄有限，你信哪一个？",
        "choices": [
          {
            "text": "请坐堂郎中诊脉，依本草方子慢慢调养，辅以针灸",
            "risk_label": "费钱 · 缓效 · 成功率 75%",
            "calc_chance": lambda p: 75 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (10 if p.luck > 50 else 0) + (8 if p.health > 60 else 0),
            "succ_feedback": "郎中切脉细问饮食起居，三帖药后咳止，针过几次，腿上旧疾也松快了；钱花得值。",
            "succ_eff": {"health": 10, "wealth": -8},
            "fail_feedback": "药力终究有限，咳是止住了，元气却再难复原；你把药方抄在册上，留与后人。",
            "fail_eff": {"health": 3, "wealth": -8, "happiness": -3},
            "tag_succ": "药石有功",
            "tag_fail": "元气难复",
            "is_key": True
          },
          {
            "text": "谢绝丹药，只取寻常食疗，早睡少思，静养待春",
            "risk_label": "清俭 · 静守 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你不再奔波劳神，晨起散步，午后小睡，入春时咳嗽竟自己好了；省下的钱给孙儿买了纸笔。",
            "succ_eff": {"health": 6, "wealth": 4, "happiness": 5},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "静养待春",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 74,
        "period": "古稀沧桑",
        "title": "故交零落后重订旧时稿",
        "narrative": "同窗故交一年走了三个，白幡一次次挂在巷口。你翻出早年所记的乡里见闻与农桑旧法，纸页已黄。有人劝你刻书传世，只是刻工索价不菲；也有人劝你留着，说人走文散本是常事。",
        "choices": [
          {
            "text": "自费请刻工刊印百部，分赠乡塾与故交诸子弟",
            "risk_label": "破费 · 传世 · 成功率 60%",
            "calc_chance": lambda p: 60 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (10 if p.luck > 50 else 0),
            "succ_feedback": "书成百部，墨香犹新，乡塾先生捧读再三；数十年后，仍有人从旧书肆中翻出你的名字。",
            "succ_eff": {"wealth": -15, "happiness": 8, "rep": 10},
            "fail_feedback": "刻工潦草，错字不少，书成而无人细读；你把残卷抱回家，叹一声也好，总比散了强。",
            "fail_eff": {"wealth": -15, "happiness": -4, "rep": -2},
            "tag_succ": "丹墨传世",
            "tag_fail": "枣梨粗劣",
            "is_key": True
          },
          {
            "text": "灯下亲手抄成两部，一藏家庙，一赠得意门生",
            "risk_label": "费神 · 存真 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你伏案三月，楷字工整，抄成两部；门生跪受，说此生必替先生守着这卷书，一字不敢损。",
            "succ_eff": {"intellect": 4, "happiness": 6},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "手泽犹存",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 74,
        "period": "古稀沧桑",
        "title": "荒年设粥棚兼修乡里桥",
        "narrative": "连月大旱，流民结队入乡，米价一日三涨。乡里公议设粥棚，又逢石桥被洪水冲塌，春耕难行。你仓中尚有陈粮，捐粮则自家儿孙要勒紧裤带，不捐则眼见有人倒毙路旁。",
        "choices": [
          {
            "text": "开仓出粟二百石，设粥棚济饥民，并出资雇人修桥",
            "risk_label": "倾仓 · 积德 · 成功率 62%",
            "calc_chance": lambda p: 62 + (10 if p.luck > 50 else 0),
            "succ_feedback": "粥棚日日不断火，桥也在秋前合龙；乡人立碑记名，你的儿孙走在桥上，总被人拱手称谢。",
            "succ_eff": {"wealth": -22, "happiness": 8, "rep": 12},
            "fail_feedback": "粮尽得比预想快，粥棚被迫撤了半月，有人未能熬过；桥却修成了，也算留下一点实在。",
            "fail_eff": {"wealth": -22, "happiness": -6, "rep": 4},
            "tag_succ": "粥棚济饥",
            "tag_fail": "力有未逮",
            "is_key": True
          },
          {
            "text": "量力捐粟五十石，先保族人，再往县仓告赈请平粜",
            "risk_label": "量力 · 有序 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "族人无一饿倒，县衙也开仓平粜；你虽未博得大名，夜里听着邻家炊烟，心中稍安。",
            "succ_eff": {"wealth": -8, "happiness": 4, "rep": 4},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "量力而行",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 80,
        "period": "夕阳辞章",
        "title": "宗祠灯火子孙环侍榻前",
        "narrative": "自知大限将近，你命人把自己抬进宗祠，在列祖牌位前铺一张竹榻。子孙三十余口跪满一院，烛火照得匾额发亮。你手里还攥着那部修了半生的族谱，是当着众人把话说完，还是留几句体己只与长孙？",
        "choices": [
          {
            "text": "聚齐子孙，将族规与田契当众交付长孙，一一嘱明",
            "risk_label": "传承 · 诀别 · 成功率 70%",
            "calc_chance": lambda p: 70 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (10 if p.luck > 50 else 0),
            "succ_feedback": "你声音渐低，话却句句清楚。阖族叩首，烛芯爆了一声，你在列祖牌位环绕中安然闭目。",
            "succ_eff": {"happiness": 10, "rep": 10},
            "fail_feedback": "话说一半，气息已接不上，末一句未竟；长孙含泪点头，你看着他，终究带着笑意松了手。",
            "fail_eff": {"happiness": 5, "rep": 4},
            "tag_succ": "含笑归祠",
            "tag_fail": "遗言未尽",
            "is_key": True
          },
          {
            "text": "屏退众人只留长孙，指族谱空白处嘱他补全旁支",
            "risk_label": "静托 · 归去 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "长孙伏在榻边记下每一句。窗外晨光初起，你握着他的手慢慢合眼，如一卷书轻轻合上。",
            "succ_eff": {"happiness": 10, "rep": 6},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "书卷轻合",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 80,
        "period": "夕阳辞章",
        "title": "散财济乡后在梅下长眠",
        "narrative": "腊月里你忽觉胸口空了一块，自知时候到了。儿孙问你还有何遗愿，你说想再看一眼故园那株老梅。这些年攒下的银钱与藏书，是散与贫寒乡邻，还是尽数留给子孙？",
        "choices": [
          {
            "text": "取银三百两分赠乡邻，藏书捐与义学，再赴梅下",
            "risk_label": "散尽 · 归去 · 成功率 68%",
            "calc_chance": lambda p: 68 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (10 if p.luck > 50 else 0),
            "succ_feedback": "受赠者跪了一地。你要人搀到梅树下，花瓣落在膝头，你望着满树清影，安静地合上了眼。",
            "succ_eff": {"wealth": -20, "happiness": 12, "rep": 12},
            "fail_feedback": "银钱尚未分完，你已气力不支。儿孙抬你到树下，梅香里你只听清风过枝头，便再无声息。",
            "fail_eff": {"wealth": -20, "happiness": 8, "rep": 6},
            "tag_succ": "梅下长眠",
            "tag_fail": "遗愿未竟",
            "is_key": True
          },
          {
            "text": "将银钱藏书尽付子孙，只携一卷旧书坐于梅下",
            "risk_label": "安然 · 归去 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "子孙跪送，你翻着那卷读过无数遍的旧书，指腹停在某一页；风起梅落，你便不再翻动了。",
            "succ_eff": {"happiness": 10, "rep": 4},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "掩卷而逝",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ]
]


# ---- modern 出身地域（8）与门第阶层（10）----
MODERN_REGIONS = [
    ("上海租界", "黄包车往来于弄堂口，报馆与纱厂汽笛声里，银元与铜板在账房间叮当作响。", {"health": 1, "wealth": 2, "luck": 1}),
    ("江南水乡", "河港交错，乌篷船摇过石桥，蚕桑与稻米支撑着一家老小的口粮。", {"health": 2, "wealth": 1}),
    ("华北平原", "黄土地里刨食，旱涝轮番，麦收之后仍要提防溃兵与散匪过境。", {"health": 2, "wealth": -1}),
    ("东北煤城", "矿井巷道终年不见日头，工棚里煤灰味混着苞米面饼子的热气。", {"health": -1, "wealth": 1, "rep": 1}),
    ("西南山城", "石阶陡斜，雾汽终年不散，滑竿与挑担在坡道间换得一日三餐。", {"health": 2, "luck": 1}),
    ("西北军垦", "风沙扑打营房，屯垦的人白天开渠，夜里听远处传来稀疏的枪声。", {"health": 2, "rep": 1}),
    ("岭南侨乡", "骑楼连廊下茶肆喧嚷，侨批局的信差带来南洋汇款与一纸平安。", {"wealth": 2, "intellect": 1}),
    ("北平皇城根", "城墙根底下卖豆汁与烤白薯，学堂里的读书声压过胡同的鸽哨。", {"intellect": 3, "rep": 1})
]

MODERN_SOCIAL_STRATA = [
    ("纱厂职员门第", "父辈在纱厂账房间做文书，月薪折合几块银元，一家人在亭子间里维持体面。", {"health": 86, "wealth": 4.5, "intellect": 60, "happiness": 58, "luck": 52, "rep": 55}, "谨小慎微"),
    ("乡间佃农之家", "租种东家几亩薄田，丰年缴完租子所剩无几，青黄不接时以野菜掺粮度日。", {"health": 84, "wealth": 0.5, "intellect": 48, "happiness": 52, "luck": 50, "rep": 38}, "勤恳本分"),
    ("县城私塾先生", "守着一间旧书房，教村童认字读经，束脩微薄却受乡邻敬重。", {"health": 84, "wealth": 2.5, "intellect": 74, "happiness": 60, "luck": 51, "rep": 68}, "清高自持"),
    ("行商小贩人家", "挑担赶集贩卖针头线脑，逢节赶庙会，风雨里算计着一家人的嚼用。", {"health": 87, "wealth": 3.2, "intellect": 56, "happiness": 57, "luck": 55, "rep": 46}, "精打细算"),
    ("铁路工人门庭", "父兄在机务段抡扳手，靠工钱与工友互助过活，逢罢工便全家悬心。", {"health": 88, "wealth": 3.8, "intellect": 54, "happiness": 56, "luck": 51, "rep": 58}, "仗义执言"),
    ("军人家眷门第", "男丁随军在外，家中靠抚恤与做针线糊口，一封信要等上半年。", {"health": 82, "wealth": 2, "intellect": 50, "happiness": 53, "luck": 49, "rep": 65}, "含辛茹苦"),
    ("中医坐堂世家", "祖上三代坐堂问诊，药柜里藏着旧方，诊金随人给，贫者常不计较。", {"health": 90, "wealth": 5.5, "intellect": 70, "happiness": 62, "luck": 53, "rep": 72}, "医者仁心"),
    ("梨园戏班门第", "在茶楼戏园里唱念做打，红时满堂喝彩，背时连行头都要典当。", {"health": 85, "wealth": 3, "intellect": 58, "happiness": 63, "luck": 56, "rep": 52}, "洒脱不羁"),
    ("邮政信差门第", "穿绿制服走街串巷送信送报，脚力换来的薪水平稳，只是风雨无阻。", {"health": 89, "wealth": 3.6, "intellect": 61, "happiness": 60, "luck": 52, "rep": 62}, "恪尽职守"),
    ("华侨汇款之家", "南洋的叔伯按月寄回侨批，家中衣食稍宽，却常年悬着远方的牵挂。", {"health": 87, "wealth": 8.5, "intellect": 63, "happiness": 57, "luck": 54, "rep": 60}, "守望相助")
]

# ---- modern 16 大生命阶段事件池 ----
MODERN_STAGE_POOLS = [
  [
    {
        "age_rel": 6,
        "period": "幼年启蒙",
        "title": "私塾戒尺与新式学堂的铃声",
        "narrative": "民国初立，街口私塾仍摆着孔夫子牌位，先生持戒尺教《三字经》；隔巷的新式学堂却挂起黑板，教国文、算学与体操。母亲用铜板凑了学费，只够一处。你站在两扇门之间，听着一边的念诵与一边的风琴声，不知该往哪边走。",
        "choices": [
          {
            "text": "进新式学堂，学白话国文与算学，放学后自己抄《千字文》补上旧学",
            "risk_label": "新旧兼修 · 根基 · 成功率 75%",
            "calc_chance": lambda p: 75 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "先生夸你字写得端正，算盘也打得快；晚上你在油灯下抄完《千字文》，父亲摸了摸你的头，说这孩子两条腿都能站。",
            "succ_eff": {"intellect": 10, "rep": 5},
            "fail_feedback": "课程跳得太快，你算学跟不上，旧学也丢了大半。先生摇头，母亲却把省下的铜板换成纸笔，说再熬一熬。",
            "fail_eff": {"intellect": 4, "happiness": -5},
            "tag_succ": "开蒙启智",
            "tag_fail": "根基未稳",
            "is_key": True
          },
          {
            "text": "留在私塾，先把《四书》背熟，认字写毛笔字，图个稳妥",
            "risk_label": "守旧 · 稳妥 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "戒尺下你背熟了半部《论语》，字也像模像样。街坊说这孩子将来能写对联、记账，不会吃亏。",
            "succ_eff": {"intellect": 5, "rep": 4},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "旧学扎实",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 6,
        "period": "幼年启蒙",
        "title": "剪辫那天父亲关上了院门",
        "narrative": "城里贴出剪辫告示，巡警带着剪刀在街上拦人。父亲留了半辈子的辫子，昨夜自己铰了，灰白的头发散在肩上。他把你叫到院里，让你看那截辫子，又问你：往后出门，是低着头走，还是挺着胸走？",
        "choices": [
          {
            "text": "替父亲把辫子收进木匣，自己剃短头发，第二天照常去街口买豆腐",
            "risk_label": "顺势 · 露面 · 成功率 70%",
            "calc_chance": lambda p: 70 + (8 if p.luck > 50 else 0),
            "succ_feedback": "邻人指指点点，却没人为难你。卖豆腐的老张还多给了一块，说新朝新气象，孩子精神。父亲在门后松了口气。",
            "succ_eff": {"luck": 6, "rep": 4},
            "fail_feedback": "巷口几个闲汉哄笑，追着你喊“假洋鬼子”。你跑回家，母亲给你拍掉身上的灰，说别怕，日子总要往前走。",
            "fail_eff": {"happiness": -6, "luck": 3},
            "tag_succ": "随世而变",
            "tag_fail": "当街受辱",
            "is_key": True
          },
          {
            "text": "暂时不出门，在家帮母亲糊纸盒，等人心定下来再说",
            "risk_label": "避风 · 稳妥 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你在家糊了三天纸盒，换回十几个铜板。风声过去，街上辫子少了，你也悄悄出了门，没人多看你一眼。",
            "succ_eff": {"wealth": 3, "happiness": 2},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "静观其变",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 10,
        "period": "童年韶光",
        "title": "军阀过境那夜的包袱",
        "narrative": "夜里枪声从城西传来，说是过境的兵要征粮拉夫。母亲摸黑把两件旧棉袄、一包炒米和几块银元裹进布包袱，父亲去后院牵驴。巷子里全是脚步声与婴儿的哭。母亲攥着你的手问：往山里走，还是去教堂后头躲一躲？",
        "choices": [
          {
            "text": "跟着乡邻往山里走，路上照看弟弟，把自己那份炒米省下一半",
            "risk_label": "逃难 · 饥寒 · 成功率 60%",
            "calc_chance": lambda p: 60 + (10 if p.luck > 50 else 0) + (8 if p.health > 60 else 0),
            "succ_feedback": "走了两夜，脚底磨破，你把炒米分给弟弟，自己啃树皮。到了山坳舅家，人都还在，母亲抱着你哭，说你长大了。",
            "succ_eff": {"health": -4, "happiness": 4, "rep": 8},
            "fail_feedback": "半路遇上散兵，包袱被抢走，一家人跌跌撞撞走散又聚拢。你饿得站不住，却死死牵着弟弟的手没松。",
            "fail_eff": {"health": -8, "wealth": -8, "happiness": -6},
            "tag_succ": "患难相依",
            "tag_fail": "流离失所",
            "is_key": True
          },
          {
            "text": "躲进教堂后院，那儿人多，兵一般不进去搜",
            "risk_label": "借庇 · 稳妥 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "教堂里挤了几十户人家，神父煮了一锅稀粥分给众人。天亮后兵开走了，你回家一看，米缸空了，人平安。",
            "succ_eff": {"health": -3, "happiness": 1},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "暂得安身",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 10,
        "period": "童年韶光",
        "title": "警报声里替家里守铺子",
        "narrative": "父亲去乡下收账，铺子只剩你和母亲。午后警报骤响，街上人往防空洞跑，可柜上还摆着刚进的洋布与煤油，卷帘门一锁就顾不上货。母亲问你：是拉着她一起躲，还是留下看铺子？远处已有飞机声。",
        "choices": [
          {
            "text": "让母亲先躲，自己把洋布和钱匣搬进地窖，再锁门去追她",
            "risk_label": "涉险 · 护家 · 成功率 55%",
            "calc_chance": lambda p: 55 + (8 if p.luck > 50 else 0) + (6 if p.health > 60 else 0),
            "succ_feedback": "你来回两趟，手心全是汗，最后一趟才钻进防空洞。飞机只掠过城郊，铺子的货无损，母亲骂了你一句，又把你搂紧。",
            "succ_eff": {"health": -3, "wealth": 6, "rep": 5},
            "fail_feedback": "你搬第二趟时瓦片震落，砸在柜台上。货保住了大半，你却磕破了额角，母亲连夜用草药给你敷上。",
            "fail_eff": {"health": -7, "wealth": 3, "happiness": -4},
            "tag_succ": "临危守业",
            "tag_fail": "血溅柜台",
            "is_key": True
          },
          {
            "text": "锁上门跟母亲一起进防空洞，货没了还能再挣",
            "risk_label": "舍财 · 稳妥 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你扶着母亲挤进洞里，蹲在墙角听外面闷响。警报解除后回来，丢了两匹布，人却都好好的，父亲回来也没多责骂。",
            "succ_eff": {"wealth": -4, "happiness": 3},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "人安为先",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 15,
        "period": "少年分流",
        "title": "家道中落后的两支笔",
        "narrative": "父亲的商号抵了债，家里只剩一架旧书柜和母亲陪嫁的银镯。你十五岁，成绩在学堂里数一数二。先生上门劝考师范，说免学费还有膳费；同乡的远房叔父却来信，说上海纱厂招练习生，管吃管住，月有工钱。母亲把银镯放在桌上，问你怎么选。",
        "choices": [
          {
            "text": "去考省立师范，靠免膳读书，课余给报馆抄稿挣纸笔钱",
            "risk_label": "清贫 · 向学 · 成功率 65%",
            "calc_chance": lambda p: 65 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "你榜上有名，穿着洗白的蓝布衫进了师范。夜里替报馆抄稿，稿酬是几只铜板，却让你第一次读到了白话报上的新道理。",
            "succ_eff": {"intellect": 14, "rep": 6},
            "fail_feedback": "考试那日你发起烧，作文只写了半篇，落榜回家。先生叹气，母亲却说：明年再考，家里的米还够。",
            "fail_eff": {"intellect": 5, "happiness": -7},
            "tag_succ": "负笈求学",
            "tag_fail": "抱病落榜",
            "is_key": True
          },
          {
            "text": "去上海纱厂当练习生，先把工钱寄回家，夜里上夜校识字",
            "risk_label": "进厂 · 稳妥 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你进了纱厂，机器声震耳，一天站十个钟头。工钱虽薄，每月能寄回几块银元；夜校里你学会了记账，也认得几个字。",
            "succ_eff": {"health": -4, "wealth": 8, "intellect": 4},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "做工养家",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 15,
        "period": "少年分流",
        "title": "救亡歌咏队敲响了校门",
        "narrative": "北方局势一日紧似一日，城里学生们组织救亡歌咏队，上街唱《松花江上》，散发传单，也有人悄悄收拾行装去投军。学堂先生睁一只眼闭一只眼。你是班上年岁最大的，同学都看你。唱歌要担风险，读书也不能耽误。",
        "choices": [
          {
            "text": "白天照常上课，傍晚带歌咏队去码头与茶馆唱，教工友识字",
            "risk_label": "涉世 · 担当 · 成功率 60%",
            "calc_chance": lambda p: 60 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (6 if p.luck > 50 else 0),
            "succ_feedback": "码头工人围了半圈听你唱，有人跟着抹泪。散场后一位老工人塞给你两个馒头，说学生也该吃饱了再喊。你嗓子哑了三天，心里却亮堂。",
            "succ_eff": {"happiness": 5, "rep": 12},
            "fail_feedback": "巡警驱散队伍，你被记了名字。校长把你叫去训话，母亲听说后一夜没睡，但你仍把传单藏在了书页里。",
            "fail_eff": {"happiness": -5, "luck": -3, "rep": 4},
            "tag_succ": "唤醒街巷",
            "tag_fail": "名列警册",
            "is_key": True
          },
          {
            "text": "先不抛头露面，安心读书，把功课考好再说",
            "risk_label": "专注 · 稳妥 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你躲在教室后头做题，期末考名列前茅。歌咏队的事你只远远看着，心里有些愧，却也没让家里多担一分心。",
            "succ_eff": {"intellect": 7, "happiness": -2},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "埋头书卷",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 18,
        "period": "成人立志",
        "title": "十字街口的招兵旗与留洋船票",
        "narrative": "你十八岁，师范将毕业。城门贴着招兵告示，管饭发饷；城里教会学堂有一张赴法勤工俭学的名额，需自筹盘缠；母亲鬓角已白，家中弟妹尚小。同学里有人已经换上灰布军装。夜里你翻来覆去，铺上摆着三样东西：一支笔、一张船票存根、弟妹的旧鞋。",
        "choices": [
          {
            "text": "报名赴法勤工俭学，先在码头做工攒盘缠，把一半工钱寄回家",
            "risk_label": "远行 · 求索 · 成功率 55%",
            "calc_chance": lambda p: 55 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (8 if p.luck > 50 else 0) + (5 if p.health > 60 else 0),
            "succ_feedback": "你在码头扛了半年货，凑够船资。开船那日母亲没哭，只把一双新纳的布鞋塞进你怀里，说出去别丢中国人的脸。",
            "succ_eff": {"wealth": -8, "intellect": 15, "luck": 8},
            "fail_feedback": "盘缠凑不齐，名额让给了别人。你把船票存根夹进书里，留在城里教书，白日上课，夜里读译来的新书，也没停下。",
            "fail_eff": {"intellect": 8, "happiness": -6, "rep": 4},
            "tag_succ": "远渡求索",
            "tag_fail": "留城守志",
            "is_key": True
          },
          {
            "text": "应招入伍，随军做文书，管饭发饷，也能照应家里",
            "risk_label": "从戎 · 稳妥 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你换上灰布军装，在营部抄写公文、替不识字的兵写信回家。饷银不多，按月寄回，母亲来信只写了四个字：好生保重。",
            "succ_eff": {"health": -3, "wealth": 5, "rep": 8},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "投笔从戎",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 18,
        "period": "成人立志",
        "title": "三人夜谈：办夜校还是南下考学",
        "narrative": "同窗三人围着一盏煤油灯。老周说城郊工厂多文盲，该去办工人夜校；阿元说南方新式中学招考，考上可免学费；你手里还有母亲托人捎来的几块银元，是家里最后的积蓄。灯花爆了一下，谁也没先开口。窗外传来黄包车夫的吆喝。",
        "choices": [
          {
            "text": "拿出银元办夜校，租半间铺面，自编识字课本，不收学费",
            "risk_label": "启蒙 · 倾囊 · 成功率 62%",
            "calc_chance": lambda p: 62 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (5 if p.luck > 50 else 0),
            "succ_feedback": "夜校开了，二十几个工人挤在铺面里，油灯下写自己的名字。有个车夫第一次写会“人”字，笑得像个孩子。你把最后一块银元也换成了灯油。",
            "succ_eff": {"wealth": -10, "intellect": 8, "rep": 14},
            "fail_feedback": "铺租涨了，来的工人渐渐少，夜校办了三个月就散了。可那本手抄的识字课本，被一个学徒带走，说要在厂里接着教。",
            "fail_eff": {"wealth": -8, "happiness": -5, "rep": 6},
            "tag_succ": "点灯照人",
            "tag_fail": "散而未灭",
            "is_key": True
          },
          {
            "text": "南下考学，银元只做路费，考上了再半工半读",
            "risk_label": "赶考 · 稳妥 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你坐了三天火车，考进南方一所中学的高中部。课余替人抄书、校对报稿，勉强糊口。夜里躺在窄铺上，你想起那盏煤油灯，给老周去了封信。",
            "succ_eff": {"wealth": -5, "intellect": 10, "luck": 3},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "南行就学",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 21,
        "period": "青春韶华",
        "title": "青布长衫投考师范讲习所",
        "narrative": "县里师范讲习所招生，免学费，还管一顿糙米饭。你攥着借来的两块银元，天不亮走了三十里土路。可家中七亩薄田正等着人下地，父亲说读书人填不饱肚子。报名处就设在文庙廊下，考还是不考，你得当场拿定主意。",
        "choices": [
          {
            "text": "先应下考卷，考完再连夜赶回村里，求父亲点头",
            "risk_label": "前程未定 · 家计难舍 · 成功率 68%",
            "calc_chance": lambda p: 68 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "榜上第十九名。父亲把烟袋在门槛上磕了三下，终究把地契押给族里，替你凑齐了铺盖钱。",
            "succ_eff": {"intellect": 10, "rep": 5},
            "fail_feedback": "你落了榜，回家正赶上秋收。父亲没说什么，只把你能吃的糙米省给了弟妹。",
            "fail_eff": {"intellect": 4, "happiness": -5},
            "tag_succ": "题名有望",
            "tag_fail": "归田收秋",
            "is_key": True
          },
          {
            "text": "留在家里帮父亲把七亩地种完，夜里再去乡塾借书自学",
            "risk_label": "两全其难 · 心志不堕 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "秋粮进了仓，你把一本《算术》翻得卷了边，村里的孩子开始追着喊你先生。",
            "succ_eff": {"intellect": 6, "happiness": 3, "rep": 3},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "耕读不辍",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 21,
        "period": "青春韶华",
        "title": "纱厂招练习生，铁门里汽笛响",
        "narrative": "日资纱厂的铁门外挤满了人，招二十个练习生，月给八块银元，管住不管吃。工头捏着你的手掌看茧，说细纱车间热得能拧出水，一天要站十二个钟头。同村有人递话来，码头扛包当天就结现钱。",
        "choices": [
          {
            "text": "咬牙留下考工，进细纱车间做学徒，先挣一份稳当工钱",
            "risk_label": "苦干立身 · 积劳伤身 · 成功率 72%",
            "calc_chance": lambda p: 72 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (8 if p.health > 60 else 0),
            "succ_feedback": "三年后你摸熟了细纱机的脾性，能听声辨断头，工钱涨到十二块，还把铺盖从通铺搬进了小屋。",
            "succ_eff": {"wealth": 8, "intellect": 5},
            "fail_feedback": "机器咬去了你左手半截指尖。工头给了两块银元养伤钱，你把它缝进棉袄里，没敢寄回家。",
            "fail_eff": {"health": -12, "wealth": 2, "happiness": -6},
            "tag_succ": "听声辨纱",
            "tag_fail": "断指存银",
            "is_key": True
          },
          {
            "text": "跟着同村人去码头扛包，当日结钱，先顾眼前",
            "risk_label": "现钱糊口 · 肩背难支 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你在码头上喊了三年号子，肩膀磨出厚茧，攒下的银元寄回家翻修了两间瓦房。",
            "succ_eff": {"health": 4, "wealth": 6, "rep": 2},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "号子立身",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 24,
        "period": "初涉人世",
        "title": "沪上码头送别，留洋的船票",
        "narrative": "亲戚牵线，有人愿资助你去法国勤工俭学，船票和介绍信都备下了；只是路费要自筹一半，此去少则五年，家中老母的病还没好。码头上四等舱的舷梯已收起一半，同行的青年正喊着你的名字。",
        "choices": [
          {
            "text": "典当母亲的银镯凑齐船票，登上开往马赛的四等舱",
            "risk_label": "远渡求新 · 亲恩难报 · 成功率 62%",
            "calc_chance": lambda p: 62 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "你在里昂的工厂半工半读，学会了看图纸，也学会在夜校里跟人争论中国该往何处去。",
            "succ_eff": {"wealth": -4, "intellect": 12, "rep": 6},
            "fail_feedback": "船到新加坡你病倒了，被送上岸养了两个月，钱花去大半，只得折回上海，银镯也没能赎回。",
            "fail_eff": {"wealth": -6, "intellect": 5, "happiness": -8},
            "tag_succ": "负笈远洋",
            "tag_fail": "中途折返",
            "is_key": True
          },
          {
            "text": "留下侍奉老母，在县城中学谋一份教书的差事",
            "risk_label": "晨昏定省 · 壮志稍敛 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你在县立中学教算术，月薪十八元，课余替人抄写状纸，母亲的药没有断过。",
            "succ_eff": {"intellect": 6, "happiness": 6, "rep": 5},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "侍疾守志",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 24,
        "period": "初涉人世",
        "title": "城门口贴出告示，招学兵",
        "narrative": "城门口贴着招兵告示，说一人当兵，全家免捐。街那头，学生救亡宣传队正搭台子唱《松花江上》。你手里还捏着半张没写完的启事——部队要识字的人当文书，宣传队却只管一顿午饭。",
        "choices": [
          {
            "text": "投考学兵队，凭一手好字去连部做个文书",
            "risk_label": "投笔从戎 · 生死难料 · 成功率 66%",
            "calc_chance": lambda p: 66 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "你替连长誊清花名册，也替不识字的弟兄写家信。一次夜行军，你把全连带出了岔路口。",
            "succ_eff": {"health": -4, "intellect": 5, "rep": 10},
            "fail_feedback": "部队在皖北被打散，你背着伤兵走了三天，回到家乡时军装已被老乡换走，只剩一块干粮。",
            "fail_eff": {"health": -10, "happiness": -5, "rep": 4},
            "tag_succ": "文书赴难",
            "tag_fail": "散兵归乡",
            "is_key": True
          },
          {
            "text": "加入学生救亡宣传队，走街串巷演活报剧",
            "risk_label": "唤醒乡邻 · 清苦自持 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你在集市上演《放下你的鞭子》，台下的老农攥紧了拳头。队里管饭，你瘦了，嗓子却越来越亮。",
            "succ_eff": {"intellect": 4, "happiness": 6, "rep": 8},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "街头呐喊",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 27,
        "period": "成家立业",
        "title": "媒人上门说亲，聘礼要四色",
        "narrative": "媒人第三次上门，说女方是邻村织布的好手，只是聘礼要银元六十、细布四匹、猪肉半扇。你攒了三年的工钱只够一半，女方娘舅又放出话来，年底前凑不齐便另许人家。",
        "choices": [
          {
            "text": "向厂里工友起个会借钱，赶在冬至前把亲定下",
            "risk_label": "举债成家 · 日后还偿 · 成功率 70%",
            "calc_chance": lambda p: 70 + (6 if p.luck > 50 else 0),
            "succ_feedback": "工友凑了二十八块，你终于赶在冬至前下了定。新房里贴着红纸剪的喜字，灶上炖着借来的半只鸡。",
            "succ_eff": {"wealth": -6, "happiness": 12, "rep": 5},
            "fail_feedback": "会钱没凑齐，女方改许了镇上的布商。你把那几匹细布退给店里，折了两成价，独自喝了半斤酒。",
            "fail_eff": {"wealth": -3, "happiness": -10, "rep": -2},
            "tag_succ": "冬至下定",
            "tag_fail": "亲事他许",
            "is_key": True
          },
          {
            "text": "与女方商量简办，只迎亲不摆席，往后一起挣",
            "risk_label": "两情相谅 · 从简结发 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "她拎着一只蓝布包袱过了门，你们在租来的厢房里对坐吃了一碗面，说定往后日子一起挣。",
            "succ_eff": {"wealth": 2, "happiness": 9, "rep": 2},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "布衣结发",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 27,
        "period": "成家立业",
        "title": "江边码头，工厂要迁往重庆",
        "narrative": "战事逼近，纱厂奉命拆卸机器西迁，工头说愿走的每人补三块银元，家眷随船，只是江上要过三道封锁线。你刚出生的孩子还在发热，岳母一家又不肯离开老屋。",
        "choices": [
          {
            "text": "携妻儿随厂西迁，跟着机器一程一程拆运",
            "risk_label": "逆江西行 · 家小颠沛 · 成功率 64%",
            "calc_chance": lambda p: 64 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "船在宜昌换小船，你的孩子在舱里退了热。到了重庆，你守着重新开工的纱锭，成了熟练的保全工。",
            "succ_eff": {"health": -5, "intellect": 8, "rep": 6},
            "fail_feedback": "船在江上遇了空袭，铺盖和行李都沉了，一家人在巫山脚下走了半个月才追上大部队。",
            "fail_eff": {"health": -9, "wealth": -5, "happiness": -8},
            "tag_succ": "溯江保全",
            "tag_fail": "失箧追队",
            "is_key": True
          },
          {
            "text": "留下看守老屋，在本地另寻一份零工",
            "risk_label": "守土安家 · 生计日蹙 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你替粮行挑脚，又在城隍庙前摆了个修车摊。日子紧，但妻儿都在身边，老屋的瓦也没塌。",
            "succ_eff": {"health": -3, "wealth": 3, "happiness": 5},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "守屋度日",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 31,
        "period": "三十而立",
        "title": "村里丈量土地，要重新立契",
        "narrative": "土改工作队进了村，丈量土地，重立契据。你家分到七亩水田和半头耕牛，可老父卧病在床，两位叔伯盯着祖屋的三间正房，说长子应当多担赡养，房产却要摊平。",
        "choices": [
          {
            "text": "接下赡养担子，把分到的田契写成兄弟共有",
            "risk_label": "独担养老 · 让产求安 · 成功率 75%",
            "calc_chance": lambda p: 75 + (5 if p.luck > 50 else 0),
            "succ_feedback": "工作队把公议记在册子上，两位叔伯再没为房争执。老人的药钱你一人出，秋后收了十石谷子。",
            "succ_eff": {"wealth": 4, "happiness": 5, "rep": 10},
            "fail_feedback": "田契写共有的次日，二叔又反悔，说祖屋的梁是你爹换的，该归他。你气得砸了一只碗。",
            "fail_eff": {"wealth": 2, "happiness": -8, "rep": -3},
            "tag_succ": "立契让产",
            "tag_fail": "房争伤和",
            "is_key": True
          },
          {
            "text": "请村干部与族老当众评理，按人口均分田产",
            "risk_label": "当众评理 · 亲族生隙 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "族老在祠堂里把话说透，田按人头分，赡养按月轮。你落了个公道，只是逢年过节少了往来。",
            "succ_eff": {"wealth": 3, "happiness": 3, "rep": 6},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "祠堂公议",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 31,
        "period": "三十而立",
        "title": "车间黑板报贴出技术革新榜",
        "narrative": "厂里响应一五计划，要推广苏联专家的高速切削法，黑板报上列出技术革新榜，谁改进了工装就记功。夜校晚上开课，教代数与识图；可车间定额也加了三成，你家里刚添了第二个孩子。",
        "choices": [
          {
            "text": "报名夜校学识图，琢磨着把车床夹具改一改",
            "risk_label": "以工代学 · 力有未逮 · 成功率 68%",
            "calc_chance": lambda p: 68 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "你的夹具把辅助时间省了一半，黑板报上登了你的名字，厂里奖了一支金星钢笔和二十尺布票。",
            "succ_eff": {"wealth": 5, "intellect": 12, "rep": 10},
            "fail_feedback": "夹具崩了刀，废了两根料，你赔了半个月工资，夜校的课也落了三成，图纸总算看懂了。",
            "fail_eff": {"wealth": -5, "intellect": 5, "happiness": -5},
            "tag_succ": "革新记功",
            "tag_fail": "崩刀赔料",
            "is_key": True
          },
          {
            "text": "先把定额干满，下班后帮家里糊纸盒补用度",
            "risk_label": "安分守额 · 持家补用 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你月月超额完成定额，评上先进生产者，奖金买了二斤猪肉和一双胶鞋，孩子的棉衣也絮上新棉花。",
            "succ_eff": {"wealth": 6, "happiness": 4, "rep": 5},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "先进守额",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 36,
        "period": "负重前行",
        "title": "一封家书过了三道封锁线",
        "narrative": "民国二十九年冬，你在镇上做木匠，妻子咳血已有月余。邮路断了三回，终于捎来老家口信，说岳母病重，盼你回去一趟；可厂里接了军需的活，工钱翻倍，走了这活就归别人。你捏着那张纸条，站在檐下听北风。",
        "choices": [
          {
            "text": "先赶完这批军需木箱，托同乡捎钱捎药回老家",
            "risk_label": "误了归期 · 得保工钱 · 成功率 62%",
            "calc_chance": lambda p: 62 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (6 if p.luck > 50 else 0),
            "succ_feedback": "木箱如期交齐，工钱翻倍，你托人捎回药钱和一封短信。妻子接过信，咳得轻了些。",
            "succ_eff": {"wealth": 12, "rep": 4},
            "fail_feedback": "你赶完工时岳母已入土，妻子怨你心硬，家里冷了半冬，你却攒下一笔救命钱。",
            "fail_eff": {"wealth": 8, "happiness": -8},
            "tag_succ": "如期交货",
            "tag_fail": "归迟憾深",
            "is_key": True
          },
          {
            "text": "告假还乡，把军需的活让与同行，先顾病人",
            "risk_label": "舍利取义 · 心有所安 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你连夜赶回，煎药侍疾半月，岳母转危为安，同行也承你这份人情，日后常来帮衬。",
            "succ_eff": {"happiness": 10, "rep": 6},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "亲恩为重",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 36,
        "period": "负重前行",
        "title": "公共食堂锅底那半勺稀粥",
        "narrative": "一九六〇年冬，公社食堂按人头打饭，你家小子正是长个子，碗里总不见稠的。邻家寡妇带着三个娃，昨日已断粮，夜里来敲门，想借你藏在炕洞里的半袋红薯干。可那是你攒着给孩子过冬的。你握着门闩，半晌没作声。",
        "choices": [
          {
            "text": "匀出半袋红薯干，约定开春队里分红再还",
            "risk_label": "恤邻济困 · 自家受窘 · 成功率 68%",
            "calc_chance": lambda p: 68 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (6 if p.luck > 50 else 0),
            "succ_feedback": "开春分红，她如数还来，还捎了一篮野菜。两家的孩子一处上学，从此成了伴。",
            "succ_eff": {"happiness": 5, "rep": 10},
            "fail_feedback": "开春她家仍紧，红薯干没还上，你家小子饿了半月，你却得了全队一句厚道。",
            "fail_eff": {"happiness": -6, "rep": 8},
            "tag_succ": "邻里相济",
            "tag_fail": "亏己全义",
            "is_key": True
          },
          {
            "text": "婉言推说自家也紧，只借出一小瓢应急",
            "risk_label": "量力而行 · 各守本分 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你舀了一瓢递过去，话说得软。她千恩万谢走了，两家情分没断，自家口粮也保住了。",
            "succ_eff": {"wealth": 3, "happiness": 4},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "量力周济",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 40,
        "period": "中年险滩",
        "title": "车间黑板报上的技术革新",
        "narrative": "一九五六年，厂里号召技术革新，你熬了三个通宵，把车床的夹具改了一道，能省两成料。可老师傅说这是祖上传下的规矩，动了要出事故；车间主任让你先报上去评先进。你捏着图纸，指节发白。",
        "choices": [
          {
            "text": "把图纸交上去，请在老师傅跟前当场试车",
            "risk_label": "冒犯旧规 · 险中求进 · 成功率 58%",
            "calc_chance": lambda p: 58 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (4 if p.health > 60 else 0),
            "succ_feedback": "试车三回，夹具稳当，省料两成。老师傅点点头，你上了黑板报，还评上市里先进。",
            "succ_eff": {"intellect": 12, "rep": 8},
            "fail_feedback": "头一回试车崩了刀，老师傅没说什么，只让你把图纸收回去。你赔了料钱，却把机理想透。",
            "fail_eff": {"wealth": -6, "intellect": 8},
            "tag_succ": "技改争先",
            "tag_fail": "吃亏长智",
            "is_key": True
          },
          {
            "text": "压下图纸，先私下请老师傅指点再作打算",
            "risk_label": "藏锋守拙 · 稳中求全 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "老师傅看了半宿，指你改了一处夹角。你把功劳记在他名下，两人都得了体面。",
            "succ_eff": {"intellect": 4, "rep": 5},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "藏器待时",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 40,
        "period": "中年险滩",
        "title": "知青报名表上的名字",
        "narrative": "一九六九年，街道敲锣打鼓送知青下乡，你儿子刚满十六，报名表递到手上。他成份一栏填的是职员，不算差也不算好，去与不去都有人议论。妻子夜里抹泪，说独子走了，家里就冷清了。你把表在灯下看了又看。",
        "choices": [
          {
            "text": "让儿子报名去北大荒，临行把棉袄絮厚",
            "risk_label": "骨肉远别 · 历练成人 · 成功率 62%",
            "calc_chance": lambda p: 62 + (8 if p.luck > 50 else 0),
            "succ_feedback": "儿子在北大荒学会了开拖拉机，来信字迹愈发端正，三年后招工回城，人结实也沉稳。",
            "succ_eff": {"happiness": 6, "rep": 6},
            "fail_feedback": "北地苦寒，儿子冻伤了脚，信里却不诉苦。你寄去一双毡靴，心里疼了整冬。",
            "fail_eff": {"happiness": -8, "rep": 4},
            "tag_succ": "送子支边",
            "tag_fail": "牵肠挂肚",
            "is_key": True
          },
          {
            "text": "托人情把儿子留在城里，先当个学徒工",
            "risk_label": "骨肉在侧 · 落人话柄 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "儿子进了街办小厂，早晚能回家吃饭。邻里背后说你家会打算，妻子却总算睡得安稳。",
            "succ_eff": {"happiness": 8, "rep": -4},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "承欢膝下",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 45,
        "period": "动荡考验",
        "title": "大字报贴到了车间门口",
        "narrative": "一九六七年春，厂门口贴满了大字报，有人点名要你表态，说老会计有历史问题，人人得划清界限。你与他共事十二年，知道他不过是旧社会当过账房。夜里你翻来覆去，笔在纸上写了又划。",
        "choices": [
          {
            "text": "只写自己不谙内情，不给人扣帽子",
            "risk_label": "缄口守拙 · 得罪两边 · 成功率 55%",
            "calc_chance": lambda p: 55 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0),
            "succ_feedback": "你的检讨写得含糊，两边都不满意，却也没人再追。老会计后来悄悄朝你拱了拱手。",
            "succ_eff": {"happiness": 3, "rep": 6},
            "fail_feedback": "有人贴出你的大字报，说你立场暧昧。你被叫去学习班半个月，回来时瘦了一圈。",
            "fail_eff": {"health": -4, "happiness": -10},
            "tag_succ": "守口如瓶",
            "tag_fail": "处境转难",
            "is_key": True
          },
          {
            "text": "按报上口径写一张大字报，随大流签上名",
            "risk_label": "明哲保身 · 心有余愧 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你照抄了报上的话，签了名，风波绕过了你家。只是再遇见老会计，你总低着头快步走开。",
            "succ_eff": {"happiness": -3, "rep": 4},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "随波自保",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 45,
        "period": "动荡考验",
        "title": "五七干校来的那张调令",
        "narrative": "一九七〇年，机关精简，一张调令要你去五七干校，说是劳动锻炼，归期未定。同一批里有人托病不去，有人抢着报名表忠心。你妻子体弱，孩子还在读书，行囊收拾了又拆开。",
        "choices": [
          {
            "text": "主动申请下干校，说改造思想也锻炼身体",
            "risk_label": "以退为进 · 前程未卜 · 成功率 60%",
            "calc_chance": lambda p: 60 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (6 if p.health > 60 else 0),
            "succ_feedback": "你在干校挑粪种菜，晒黑了也结实了。两年后调令回城，组织说你表现好，安排了新岗。",
            "succ_eff": {"health": 6, "rep": 8},
            "fail_feedback": "干校湿冷，你落下腰疾，回城时岗位已被人顶了，只能从头做起。",
            "fail_eff": {"health": -6, "wealth": -4},
            "tag_succ": "主动请缨",
            "tag_fail": "劳身失位",
            "is_key": True
          },
          {
            "text": "以妻子病重为由请假缓行，留在原单位",
            "risk_label": "家室为重 · 落人口实 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你交了病假条，留下来照顾妻子。单位里有人说你恋家，可妻子熬过了那个冬天。",
            "succ_eff": {"happiness": 8, "rep": -3},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "顾家守拙",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 51,
        "period": "知命之年",
        "title": "平反通知书下来的那天",
        "narrative": "一九七七年秋，单位来人通知，说当年扣在你头上的那顶帽子可以摘了，档案里的材料要重新写。你跑了三趟，最后在一间办公室里看见那张薄纸。窗外梧桐落叶，你手抖得签不成名字。",
        "choices": [
          {
            "text": "要求把当年的结论一并改正，恢复原职级",
            "risk_label": "据理力争 · 一波三折 · 成功率 58%",
            "calc_chance": lambda p: 58 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (8 if p.luck > 50 else 0),
            "succ_feedback": "材料改了，职称补上，补发的工资装了一个信封。你把信封压在箱底，先给妻子买了一斤肉。",
            "succ_eff": {"wealth": 10, "rep": 12},
            "fail_feedback": "来回扯了半年，只改了一半。你没再争，回家把旧笔记本一页页烧了。",
            "fail_eff": {"happiness": -6, "rep": 4},
            "tag_succ": "沉冤得雪",
            "tag_fail": "半纸平反",
            "is_key": True
          },
          {
            "text": "只领回那张通知，不再申辩，回岗位做事",
            "risk_label": "但求清白 · 不争长短 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你把通知叠好收进抽屉，第二天照常上班。同事待你客气了，日子也一点点回到正轨。",
            "succ_eff": {"happiness": 8, "rep": 4},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "清白自守",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 51,
        "period": "知命之年",
        "title": "恢复高考的第一个冬天",
        "narrative": "一九七七年冬，广播里说恢复高考，不拘成份，自愿报名。你女儿在乡下插队七年，课本早当了引火纸。她连夜翻出旧笔记，眼睛亮得吓人；可家里拿不出路费和复习的工夫。你在灯下算了半宿。",
        "choices": [
          {
            "text": "让女儿请假回城复习，全家省口粮供她",
            "risk_label": "孤注一掷 · 望女成凤 · 成功率 64%",
            "calc_chance": lambda p: 64 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (6 if p.luck > 50 else 0),
            "succ_feedback": "她考上了省城的师范学院，走那天你送到车站，把攒的布票缝进她棉袄里。信里说食堂有白面馒头。",
            "succ_eff": {"happiness": 12, "rep": 8},
            "fail_feedback": "她差了几分落榜，回村时没哭。第二年再考，中了中专。你才知她夜里背书到天亮。",
            "fail_eff": {"intellect": 4, "happiness": -5},
            "tag_succ": "寒门折桂",
            "tag_fail": "来年再试",
            "is_key": True
          },
          {
            "text": "劝她安心务农，先顾眼下工分和口粮",
            "risk_label": "务实守成 · 埋没心愿 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "她没报名，把笔记又收进箱底。年底分红多了几十斤粮，家里过了个踏实年。",
            "succ_eff": {"wealth": 5, "happiness": -3},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "安分守成",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 58,
        "period": "花甲在望",
        "title": "退休证压在抽屉最底下的那个下午",
        "narrative": "退休证和工资折压在抽屉最底下，厂门口敲锣打鼓送你回家。食堂师傅说，往后打饭就得自己掏钱了。小儿子还在北边插队，老伴的药也快吃完。你站在院子里，是留在城里守着这份体面，还是回乡下陪老母亲过几年清苦日子？",
        "choices": [
          {
            "text": "收拾行李回乡下，侍奉老母亲，顺带照看几分自留地",
            "risk_label": "归乡奉亲 · 生计渐薄 · 成功率 68%",
            "calc_chance": lambda p: 68 + (10 if p.luck > 50 else 0) + (8 if p.health > 60 else 0),
            "succ_feedback": "老屋的灶膛重新烧暖，母亲夜里不再咳得那样久。你日出下地，日落煮粥，日子清苦，心里却踏实。",
            "succ_eff": {"health": 4, "happiness": 9, "rep": 4},
            "fail_feedback": "水土不服，腰腿旧伤又犯，母亲的药钱也紧。你在灯下算账，明白尽孝二字，从来比想象中更沉。",
            "fail_eff": {"health": -8, "wealth": -3, "happiness": -4},
            "tag_succ": "膝前尽孝",
            "tag_fail": "力不从心",
            "is_key": True
          },
          {
            "text": "留在城里，把退休金攒作药钱，按月给乡下寄去",
            "risk_label": "守城寄养 · 两处牵肠 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "每月十五，你把汇款单仔细折好投进邮筒。母亲的回信总说家中安好，你却把每个字都读了两遍。",
            "succ_eff": {"wealth": 3, "happiness": 2, "rep": 5},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "两地相安",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 58,
        "period": "花甲在望",
        "title": "旧藤箱里翻出一叠泛黄的家书",
        "narrative": "收拾屋子，旧藤箱底翻出半辈子的家书与旧照片，纸边脆得像秋叶。有人劝你把这些年的事写下来，留给儿孙；也有人说，往事多舛，提笔便是揭疤。你坐在窗前，望着收音机里正播的样板戏，久久没有落笔。",
        "choices": [
          {
            "text": "按年份理好旧信，一页一页写下自己这一生的来路",
            "risk_label": "秉笔存真 · 心绪难平 · 成功率 72%",
            "calc_chance": lambda p: 72 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (10 if p.luck > 50 else 0),
            "succ_feedback": "字迹一行行落定，离散的人、走过的路都回来了。孙子趴桌边问东问西，你忽然觉得这一生有了交代。",
            "succ_eff": {"intellect": 4, "happiness": 8, "rep": 5},
            "fail_feedback": "写到战乱那几年，笔顿住了，夜里连做几场旧梦。稿纸只写了半册，你把它收好，说再缓缓罢。",
            "fail_eff": {"health": -6, "happiness": -7},
            "tag_succ": "落纸存心",
            "tag_fail": "旧事难提",
            "is_key": True
          },
          {
            "text": "把旧信旧照分门别类收好，只给儿孙讲些轻省的往事",
            "risk_label": "择善而述 · 旧物长存 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "抽屉里多了三只纸包，分别写着年份与人名。孩子问起时，你便挑一段温热的旧事，慢慢讲给他们听。",
            "succ_eff": {"intellect": 2, "happiness": 5},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "旧物有温",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 66,
        "period": "桑榆晚景",
        "title": "登门寻访三十年未见的老同事",
        "narrative": "老同事的消息终于问到了，住在城西旧楼的三层。你换上洗得发白的中山装，揣着两斤点心出门。有人劝你这把年纪别再奔波，也有人说起当年那场争执，怕见面更难堪。公共汽车摇晃着，你一时不知该不该去。",
        "choices": [
          {
            "text": "提着点心登门，把当年的话当面说开",
            "risk_label": "旧怨冰释 · 来路已远 · 成功率 70%",
            "calc_chance": lambda p: 70 + (10 if p.luck > 50 else 0) + (8 if p.health > 60 else 0),
            "succ_feedback": "两位老人在藤椅上坐了半日，从食堂的菜价说到当年的误会，末了都笑了。回来的路上，你脚步轻了许多。",
            "succ_eff": {"health": 3, "happiness": 9, "rep": 5},
            "fail_feedback": "门开了，话却始终没有说到那一层。临走他送你到楼梯口，你回头看见他扶着栏杆，也没有再说什么。",
            "fail_eff": {"health": -5, "happiness": -7},
            "tag_succ": "一笑泯恩",
            "tag_fail": "话到嘴边",
            "is_key": True
          },
          {
            "text": "只托人捎口信问候，不打扰他晚年的清净",
            "risk_label": "遥寄平安 · 各守余年 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "口信捎去半月，回话只有一句：他身子还好，也惦记你。你把这句话在心里放了许多天，像收好一件旧物。",
            "succ_eff": {"happiness": 4, "rep": 3},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "遥遥相念",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 66,
        "period": "桑榆晚景",
        "title": "雪夜陪着返城的儿子商议工作去处",
        "narrative": "知青返城的文件下来了，儿子背着铺盖卷回家，户口与工作还悬着。街道办说名额有限，单位食堂正缺个帮工，也有人劝他去南方碰运气。屋外飘雪，老伴把炉子添旺。你握着那只搪瓷缸，一时难下决断。",
        "choices": [
          {
            "text": "拿出大半积蓄走动门路，替儿子谋一个稳妥的去处",
            "risk_label": "倾囊铺路 · 成败难料 · 成功率 62%",
            "calc_chance": lambda p: 62 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (10 if p.luck > 50 else 0),
            "succ_feedback": "开春时儿子进了厂，学徒工的名牌压在胸前。他领到第一份工资，给你买了一包好烟，你却舍不得抽。",
            "succ_eff": {"wealth": -8, "happiness": 8, "rep": 6},
            "fail_feedback": "钱花了，事没成，儿子只好先去食堂帮工。他并不怨你，只是你夜里听见他翻身，心里像压了块冷铁。",
            "fail_eff": {"health": -4, "wealth": -10, "happiness": -6},
            "tag_succ": "父荫成事",
            "tag_fail": "钱财两空",
            "is_key": True
          },
          {
            "text": "让他自个儿去街道办排队苦等，路要自己走出来",
            "risk_label": "放手自立 · 前路维艰 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "儿子天不亮就去排队，回来时鞋上全是雪泥。几个月后他自有去处，虽不体面，却站得直。你看着他，没有说话。",
            "succ_eff": {"wealth": 2, "happiness": 4, "rep": 4},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "自立成人",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 74,
        "period": "古稀沧桑",
        "title": "平反的通知送到胡同老院门口",
        "narrative": "街道的同志敲开院门，递来一纸落实政策的通知，说要为你当年的事恢复名誉，还补发一笔钱。消息传得很快，街坊都来道喜。你却想起那些年月里不敢来往的故人，提起笔，不知先去告诉谁。",
        "choices": [
          {
            "text": "把补发的钱分送几户当年受牵连的旧邻，再登门谢过他们",
            "risk_label": "推己及人 · 人心难量 · 成功率 74%",
            "calc_chance": lambda p: 74 + (10 if p.luck > 50 else 0) + (8 if p.health > 60 else 0),
            "succ_feedback": "有人推辞，有人红了眼眶，末了都收下了。胡同里过了几天热闹日子，你走在其中，觉得腰杆终于是直的。",
            "succ_eff": {"wealth": -6, "happiness": 8, "rep": 9},
            "fail_feedback": "有两户闭门不见，说旧账不必再提。你把钱留下，独自走回院中，明白有些亏欠，一辈子也还不完。",
            "fail_eff": {"wealth": -6, "happiness": -5, "rep": 2},
            "tag_succ": "尘埃落定",
            "tag_fail": "旧债难偿",
            "is_key": True
          },
          {
            "text": "把钱存进工资折，只去坟前静静坐一坐",
            "risk_label": "沉默谢幕 · 各安其位 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你在坟前坐了很久，把通知的内容一句一句念给他听。回来时把存折压回抽屉，日子仍是原来的日子。",
            "succ_eff": {"wealth": 5, "happiness": 5, "rep": 2},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "静水流深",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 74,
        "period": "古稀沧桑",
        "title": "把攒了半辈子的存折摊在灯下",
        "narrative": "夜里你把几张存折与票证摊在桌上，那是给儿孙攒下的那点家底。小儿子想借钱换一台缝纫机，说能挣些活钱；女儿却说，不如留着给你看病养老。灯光昏黄，老伴坐在一旁，等你拿主意。",
        "choices": [
          {
            "text": "匀出一半给儿子添置缝纫机，剩下的封存备医",
            "risk_label": "慈心难断 · 两头兼顾 · 成功率 70%",
            "calc_chance": lambda p: 70 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (10 if p.luck > 50 else 0),
            "succ_feedback": "缝纫机抬进门那天，全家围看。儿媳接的活儿渐渐多了，逢年过节总给你捎来新做的棉袄，针脚细密。",
            "succ_eff": {"wealth": 4, "happiness": 8, "rep": 4},
            "fail_feedback": "活儿没接着几单，机器在墙角落了灰。你嘴上说不要紧，心里却盘算着往后的药钱，从此更省了些。",
            "fail_eff": {"wealth": -8, "happiness": -5},
            "tag_succ": "家底生暖",
            "tag_fail": "机杼蒙尘",
            "is_key": True
          },
          {
            "text": "一文不动，明明白白告诉儿女这份钱只作养老送终之用",
            "risk_label": "守本自持 · 亲情有隙 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你把话说明白了，儿女都点头。往后看病抓药不必向谁开口，你夜里睡得安稳，只是家里少了几分热闹。",
            "succ_eff": {"health": 3, "wealth": 3, "happiness": -2},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "自有分寸",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ],
  [
    {
        "age_rel": 80,
        "period": "夕阳辞章",
        "title": "儿孙守候床前听你交代最后几句",
        "narrative": "入了冬，你躺在床上，气力一日不如一日。儿女轮班守着，药炉在墙角温着，收音机开得很轻。你让孙子把那只旧藤箱搬来，想最后说几句话，也想再看看那些泛黄的家书与照片。",
        "choices": [
          {
            "text": "把旧信旧照一封封分给儿孙，交代完身后事，安然合眼",
            "risk_label": "交代清楚 · 魂归平和 · 成功率 76%",
            "calc_chance": lambda p: 76 + (10 if p.luck > 50 else 0) + (8 if p.health > 60 else 0),
            "succ_feedback": "信件分完，你一一唤过他们的名字，说各自珍重。屋外落着细雪，你握着老伴的手，慢慢合上眼，神色安然。",
            "succ_eff": {"happiness": 12, "rep": 8},
            "fail_feedback": "话未说完，气已不继，只攥着那张全家福。儿孙都懂了你的意思，低声应着，陪你坐到天亮。",
            "fail_eff": {"health": -6, "happiness": -4},
            "tag_succ": "含笑长眠",
            "tag_fail": "未尽之言",
            "is_key": True
          },
          {
            "text": "让儿孙把窗帘拉开，看着院子里那株老树，静静等天黑",
            "risk_label": "无言以对 · 各自安宁 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "光从窗棂上一点点退去，儿孙都在屋里。你望着老树的枝影，呼吸渐渐轻了，像忙完一天的人终于歇下。",
            "succ_eff": {"happiness": 10, "rep": 6},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "安然谢幕",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 80,
        "period": "夕阳辞章",
        "title": "藤椅上手握全家福看最后一次夕阳",
        "narrative": "你执意要从床上起来，坐到老屋那张藤椅里去。儿孙把毯子搭在你膝上，又端来一碗温水。夕阳斜过屋脊，照片里的年轻人早已不在，膝下的孩子却都长成了。你慢慢握紧了那张全家福。",
        "choices": [
          {
            "text": "留下话把一生的积蓄捐给村小学，再回故里老屋住到最后",
            "risk_label": "散尽家财 · 落叶归根 · 成功率 72%",
            "calc_chance": lambda p: 72 + (int((p.intellect - 50) / 2) if p.intellect > 50 else 0) + (10 if p.luck > 50 else 0),
            "succ_feedback": "你回老屋住了半月，每日看村里孩子背着书包经过。课本是新的，木窗是旧的。一个午后，你在藤椅上睡着了，没有再醒。",
            "succ_eff": {"wealth": -12, "happiness": 10, "rep": 12},
            "fail_feedback": "钱捐了出去，身子却没能撑回故里。你在城里的屋中走完最后一程，望着窗外的树梢，也算安静。",
            "fail_eff": {"health": -6, "happiness": 2, "rep": 8},
            "tag_succ": "夕阳辞章",
            "tag_fail": "归途未竟",
            "is_key": True
          },
          {
            "text": "哪儿也不去，就守着这间老屋与家人，把手边的事放下",
            "risk_label": "守屋待终 · 灯火可亲 · 稳妥必成",
            "calc_chance": lambda p: 100,
            "succ_feedback": "你把全家福贴在心口，听着屋里锅碗的动静与孩子的笑闹。夕阳沉下去时，你仍旧坐着，像是看着一家人慢慢长大。",
            "succ_eff": {"happiness": 11, "rep": 5},
            "fail_feedback": "",
            "fail_eff": {},
            "tag_succ": "灯火长明",
            "tag_fail": "另寻他途",
            "is_key": False
          }
        ]
    }
  ]
]


def get_origin_tables(epoch_id):
    if epoch_id == "ancient":
        return ANCIENT_REGIONS, ANCIENT_SOCIAL_STRATA
    if epoch_id == "premodern":
        return PREMODERN_REGIONS, PREMODERN_SOCIAL_STRATA
    if epoch_id == "modern":
        return MODERN_REGIONS, MODERN_SOCIAL_STRATA
    if epoch_id == "contemporary":
        return PAST_REGIONS, PAST_SOCIAL_STRATA
    return FUTURE_REGIONS, FUTURE_SOCIAL_STRATA


def get_stage_pools(epoch_id):
    if epoch_id == "ancient":
        return ANCIENT_STAGE_POOLS
    if epoch_id == "premodern":
        return PREMODERN_STAGE_POOLS
    if epoch_id == "modern":
        return MODERN_STAGE_POOLS
    if epoch_id == "contemporary":
        return PAST_STAGE_POOLS
    return FUTURE_STAGE_POOLS


def generate_procedural_origin(epoch_id):
    regions, strata_list = get_origin_tables(epoch_id)
    region_name, region_desc, region_stat = random.choice(regions)
    strata_title, strata_desc, strata_stat, trait_name = random.choice(strata_list)
    title = "%s · %s" % (region_name[:5], strata_title)
    desc = "降生于【%s】。%s；家庭是【%s】，%s。" % (
        region_name, region_desc, strata_title, strata_desc)
    stat_mod = {}
    for k in ["health", "wealth", "intellect", "happiness", "luck", "rep"]:
        stat_mod[k] = round(strata_stat.get(k, 0) + region_stat.get(k, 0), 1)
    return {
        "title": title, "desc": desc, "region": region_name,
        "strata": strata_title, "stat": stat_mod,
        "trait": trait_name, "flavor": strata_desc,
    }


def generate_random_destiny(epoch_id):
    cfg = get_epoch_config(epoch_id)
    b_year = random.randint(cfg["min_year"], cfg["max_year"])
    b_month = random.randint(1, 12)
    origin = generate_procedural_origin(epoch_id)
    trait = random.choice(RANDOM_TRAITS)
    return b_year, b_month, origin, trait


RANDOM_TRAITS = [
    {"name": "天生神力", "desc": "体魄异常健硕，抗病力强，耐劳度高", "mod": {"health": 8}},
    {"name": "灵光乍现", "desc": "悟性出众，学东西极快，见识超群", "mod": {"intellect": 8}},
    {"name": "福泽深厚", "desc": "冥冥中自有运气眷顾，常能逢凶化吉", "mod": {"luck": 12}},
    {"name": "钝感心安", "desc": "不善内耗，神经大条，心境极其不易崩溃", "mod": {"happiness": 10}},
    {"name": "商海通达", "desc": "对财富流转天生亲和，初始多带微薄启动金", "mod": {"wealth": 3}},
    {"name": "多愁善感", "desc": "同理心与艺术直觉敏锐，但容易多思内耗", "mod": {"intellect": 5, "happiness": -5}},
    {"name": "不屈不挠", "desc": "逆境中求生意志极为强烈，危局中易有奇迹", "mod": {"health": 5, "luck": 6}},
    {"name": "八面玲珑", "desc": "处世圆润得体，交游广阔，长辈同侪皆喜", "mod": {"rep": 10, "happiness": 4}},
    {"name": "清心寡欲", "desc": "知足常乐，不易为物欲所累，身心松弛自然", "mod": {"happiness": 12, "wealth": -1}},
    {"name": "洞若观火", "desc": "直觉极强，能迅速洞察谎言与暗藏的风险", "mod": {"intellect": 6, "luck": 5}}
]

class Player:
    def __init__(self, name, epoch_mode, birth_year, origin, trait):
        self.name = name
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
        
        self.tags = [origin["trait"], trait["name"]]
        self.history = []
        self.key_choices = []
        self.random_events = []
        self.is_dead = False
        self.death_reason = ""
        self.career_track = "探索未定"
        self.social_rank = "风雨布衣"
        self.track_scores = {"体制政务": 0, "商海实业": 0, "学术科技": 0, "文艺江湖": 0, "守拙布衣": 0}

    def show_dashboard(self, stage_idx, total_stages):
        clear_screen()
        curr_year = self.birth_year + self.age
        era_title, era_desc = resolve_era_details(curr_year, self.epoch_mode)

        print(f"{Color.GOLD}{'='*68}{Color.RESET}")
        print(f" {Color.BOLD}{self.name}{Color.RESET} · {curr_year} 年 ({self.age} 岁) | 轨迹: {Color.CYAN}{self.career_track} · {self.social_rank}{Color.RESET} | 进度 [{stage_idx}/{total_stages}] | 时代：{Color.YELLOW}{era_title}{Color.RESET}")
        print(f" 时代背景: {Color.GRAY}{era_desc}{Color.RESET}")
        print(f"{Color.GOLD}{'-'*68}{Color.RESET}")
        print(f" [健康]: {int(self.health):<3}♥  |  [财富]: {self.wealth:.1f}万￥  |  [智识]: {int(self.intellect):<3}✦  |  [心安]: {int(self.happiness):<3}☼  |  [气运]: {int(self.luck):<3}🎲")
        print(f"{Color.GOLD}{'='*68}{Color.RESET}\n")

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

PAST_STAGES = [
    {
        "age_rel": 6,
        "title": "大院门槛与小城清晨",
        "narrative": "清晨空气里飘着蜂窝煤和油条的烟气，邻里骑着二八大杠按铃而过。父母为是否托关系送你进城关名校争吵不休。",
        "choices": [
          {
            "text": "全家省吃俭用托人送礼，硬挤进教学质量顶尖的城关中心小学",
            "risk_label": "高压开局 · 成功率 75%",
            "calc_chance": lambda p: 75 + (10 if p.luck > 50 else -5),
            "succ_feedback": "你进入了名校尖子班，虽然在干部子弟间有些局促，但良好学习习惯自此扎根。",
            "succ_eff": {"intellect": 8, "wealth": -1.0, "happiness": -2, "rep": 5},
            "fail_feedback": "借读名额被更有背景的人顶替，白花了积蓄，早早体会到世态的现实无奈。",
            "fail_eff": {"intellect": 3, "wealth": -1.5, "happiness": -6},
            "tag_succ": "名校开蒙",
            "tag_fail": "碰壁初尝",
            "is_key": False
          },
          {
            "text": "就近入读家属厂办/乡村小学，在泥地和小伙伴疯跑野蛮生长",
            "risk_label": "质朴童年 · 顺其自然",
            "calc_chance": lambda p: 100,
            "succ_feedback": "童年伴着打弹珠、抓泥鳅的笑语，体质被锻炼得格外扎实，性格从容开朗。",
            "succ_eff": {"health": 5, "happiness": 8, "intellect": 3},
            "tag_succ": "野趣童年",
            "is_key": False
          }
        ]
    },
    {
        "age_rel": 10,
        "title": "黑白电视机与下海狂潮",
        "narrative": "大街上的录音机放起港台流行歌，万元户与下海淘金的故事广为流传。有亲戚邀父母一起凑钱去特区贩运小商品。",
        "choices": [
            {
                "text": "在饭桌上极力鼓动父母：'隔壁叔叔都发财了，咱们也试一把！'",
                "risk_label": "时代博弈 · 成功率 55%",
                "calc_chance": lambda p: 55 + (15 if p.luck > 50 else -10),
                "succ_feedback": "父母咬牙跟投赶上紧缺红利，家里添了彩电冰箱，你的零花钱也丰裕起来。",
                "succ_eff": {"wealth": 5.0, "happiness": 6, "intellect": 4, "luck": 4},
                "fail_feedback": "货品半道被扣罚，合伙亲戚失联，家里亏了近半年工资，气氛一度冰冷压抑。",
                "fail_eff": {"wealth": -3.0, "happiness": -8, "intellect": 2, "luck": -4},
                "tag_succ": "商潮初利",
                "tag_fail": "家道艰难",
                "is_key": True
            },
            {
                "text": "劝父母安心守本分，平平安安就是福，不要冒倾家荡产的险",
                "risk_label": "守正自保 · 确定安稳",
                "calc_chance": lambda p: 100,
                "succ_feedback": "父母听劝没有冒进，安稳领着月薪，一家人平安温馨。",
                "succ_eff": {"wealth": 0.8, "happiness": 4, "intellect": 2},
                "tag_succ": "本分人家",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 15,
        "title": "中考独木桥与网吧微光",
        "narrative": "中考录取率四成左右，班主任敲黑板强调普高重要性；而街头黑网吧的暗巷里，同龄人正在通宵游戏。",
        "choices": [
            {
                "text": "彻底断绝玩乐，每天题海苦读到深夜两点冲击重点高中",
                "risk_label": "苦行应试 · 成功率 80%",
                "calc_chance": lambda p: int(80 + (p.intellect - 50) / 2),
                "succ_feedback": "你以全区名列前茅的高分考入省重点高中！父母在邻界面前扬眉吐气。",
                "succ_eff": {"intellect": 12, "happiness": 6, "health": -4, "rep": 10},
                "fail_feedback": "考前突发高烧发挥失常，压线挤入普通高中，体会到造化的捉弄。",
                "fail_eff": {"intellect": 6, "happiness": -8, "health": -6, "rep": 2},
                "tag_succ": "做题精英",
                "tag_fail": "考场蹉跎",
                "is_key": True
            },
            {
                "text": "对死记硬背反感，迷上计算机编程与早期网站架设",
                "risk_label": "异类探索 · 成功率 60%",
                "calc_chance": lambda p: int(60 + (p.intellect - 50) / 2 + (10 if p.luck > 55 else 0)),
                "succ_feedback": "自建的个人网站在早期论坛爆火，凭借特长加分破格保送计算机特色班！",
                "succ_eff": {"intellect": 15, "wealth": 2.0, "happiness": 8, "luck": 5},
                "fail_feedback": "文化课彻底跟不上，中考失利只得进入中专职校，面对父母叹息与亲戚眼光。",
                "fail_eff": {"intellect": 4, "wealth": -1.0, "happiness": -12, "rep": -6},
                "tag_succ": "极客先锋",
                "tag_fail": "歧路少年",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 18,
        "title": "高考十字路口：热门风口还是体制包分配？",
        "narrative": "加入WTO的呼声震天，高考志愿表摆在面前，将决定你未来数十年的轨道走向。",
        "choices": [
            {
                "text": "报考沿海名校的'计算机科学'或'国际金融/贸易'专业",
                "risk_label": "浪潮之巅 · 成功率 70%",
                "calc_chance": lambda p: 70 + (10 if p.luck > 50 else -5),
                "succ_feedback": "完美搭上中国互联网与全球化腾飞快车！大学眼界彻底撕开旧认知。",
                "succ_eff": {"intellect": 14, "wealth": 3.0, "happiness": 6, "rep": 8},
                "fail_feedback": "高校扩招课程脱节，毕业时遭遇行业周期小调整，陷入激烈求职内卷。",
                "fail_eff": {"intellect": 8, "wealth": -1.5, "happiness": -6, "rep": 2},
                "tag_succ": "时代弄潮儿",
                "tag_fail": "风口跌宕",
                "is_key": True
            },
            {
                "text": "报考公费师范或军警医校，学费全免且毕业确保体制编制",
                "risk_label": "避风港湾 · 绝对稳妥",
                "calc_chance": lambda p: 100,
                "succ_feedback": "父母长舒了一口气。你拿到了铁饭碗入场券，站在象牙塔内淡看外界商海沉浮。",
                "succ_eff": {"intellect": 7, "wealth": 1.5, "happiness": 8, "rep": 8},
                "tag_succ": "体制坚盾",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 21,
        "title": "大学象牙塔：青涩深情还是职业考证？",
        "narrative": "随身听里放着经典流行歌，你遇到了让你心动的 Ta，同时专业考研与考证的竞争迫在眉睫。",
        "choices": [
            {
                "text": "全身心投入深情相恋，与 Ta 一起在林荫道和自习室相互依偎",
                "risk_label": "真情至性 · 成功率 65%",
                "calc_chance": lambda p: 65 + (10 if p.happiness > 60 else -5),
                "succ_feedback": "你们成为彼此最坚固的依靠，一同约定奋斗城市，收获最纯粹的爱意。",
                "succ_eff": {"happiness": 15, "rep": 5, "health": 2},
                "fail_feedback": "毕业前夕因家庭异地现实问题激烈冲突抱憾分手，失恋让你大病一场。",
                "fail_eff": {"happiness": -16, "health": -6, "intellect": 3},
                "tag_succ": "情深意笃",
                "tag_fail": "情伤碎梦",
                "is_key": False
            },
            {
                "text": "克制情感保持清心寡欲，夜夜死磕专业考研与职业资格证",
                "risk_label": "理性笃行 · 成功率 85%",
                "calc_chance": lambda p: int(85 + (p.intellect - 50) / 2),
                "succ_feedback": "顺利斩获硬核资格证书，在校招中手握大批优质 Offer。",
                "succ_eff": {"intellect": 12, "wealth": 2.0, "happiness": 4, "rep": 6},
                "fail_feedback": "考场过度紧张以微弱分差落榜，错失秋招黄金期，但基本功依然扎实。",
                "fail_eff": {"intellect": 6, "happiness": -6, "health": -3},
                "tag_succ": "履历出众",
                "tag_fail": "功亏一篑",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 24,
        "title": "大城蚁族还是小城安居？",
        "narrative": "大城市房价正如火箭蓄势，逼仄的合租屋与早高峰地铁消磨着你，是坚守大城还是退守老家？",
        "choices": [
            {
                "text": "做北漂/沪漂，进民企大厂搏命加班，抢抓一线晋升机遇",
                "risk_label": "大城搏命 · 成功率 60%",
                "calc_chance": lambda p: int(60 + (p.intellect - 50) / 2 + (10 if p.luck > 50 else -5)),
                "succ_feedback": "核心业务指标大涨，被破格提拔为骨干组长，年终奖丰厚，在大城站稳脚跟！",
                "succ_eff": {"wealth": 12.0, "intellect": 10, "happiness": 6, "health": -8, "rep": 10},
                "fail_feedback": "遭遇画饼领导，天天无偿加班至深夜，体检出现多项异常，心力交瘁。",
                "fail_eff": {"wealth": 3.0, "intellect": 4, "happiness": -12, "health": -12},
                "tag_succ": "职场新星",
                "tag_fail": "身心透支",
                "is_key": True
            },
            {
                "text": "退守老家二三线城市，通过招考进事业单位或国企过慢节奏生活",
                "risk_label": "故土安稳 · 确定性高",
                "calc_chance": lambda p: 100,
                "succ_feedback": "父母照拂下有房住有饭吃，下班后跟老友吹风喝茶。虽无暴富，心境祥和。",
                "succ_eff": {"wealth": 3.0, "happiness": 10, "health": 6, "rep": 5},
                "tag_succ": "故土安居",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 27,
        "title": "四万亿洪流与创业下海",
        "narrative": "四万亿刺激政策带来海量流动性，移动互联与电商萌动。昔日同窗邀你辞职合伙创业，父母则催你掏积蓄买房。",
        "choices": [
            {
                "text": "拿出所有积蓄合伙创业，搏一把移动互联网/电商爆发期",
                "risk_label": "险峰创业 · 成功率 45%",
                "calc_chance": lambda p: int(45 + (p.intellect - 50) / 2 + (15 if p.luck > 50 else -10)),
                "succ_feedback": "研发的产品被大机构注资数百万，年纪轻轻斩获第一桶金，实现阶层跨越！",
                "succ_eff": {"wealth": 35.0, "intellect": 12, "happiness": 10, "health": -6, "rep": 15},
                "fail_feedback": "合伙人卷款失联，项目资金链断裂欠下十余万债务，不得不送外卖还债。",
                "fail_eff": {"wealth": -15.0, "intellect": 8, "happiness": -15, "health": -10, "rep": -4},
                "tag_succ": "独角兽风光",
                "tag_fail": "负债受挫",
                "is_key": True
            },
            {
                "text": "将积蓄全部作为首付，赶在房价起飞前夕按揭买下近郊两居室",
                "risk_label": "置业筑底 · 时代红利",
                "calc_chance": lambda p: 100,
                "succ_feedback": "精准踩准了中国房产黄金期的发车点！数年后房屋估值翻番，成为全家压舱石。",
                "succ_eff": {"wealth": 22.0, "happiness": 8, "health": 2, "rep": 8},
                "tag_succ": "早早上车",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 31,
        "title": "红白账簿：世俗婚宴还是务实自守？",
        "narrative": "面对相处多年的对象与两方家庭关于彩礼、嫁妆、房产排场的较劲，你站在世俗旋涡中心。",
        "choices": [
            {
                "text": "倾全家之力办一场风光体面的婚礼，满足双方长辈的一切面子要求",
                "risk_label": "世俗圆满 · 代价沉重",
                "calc_chance": lambda p: 100,
                "succ_feedback": "亲友称赞体面，家庭关系和睦，但小家庭积蓄几乎掏空，随后两年紧缩度日。",
                "succ_eff": {"wealth": -8.0, "rep": 12, "happiness": 4},
                "tag_succ": "宗族体面",
                "is_key": False
            },
            {
                "text": "说服长辈旅行结婚或极简操办，省下钱用于理财与育儿金",
                "risk_label": "务实自守 · 成功率 75%",
                "calc_chance": lambda p: 75 + (10 if p.intellect > 55 else 0),
                "succ_feedback": "两口子手握充足现金流，免遭繁文缛节内耗，小日子过得踏实自在。",
                "succ_eff": {"wealth": 6.0, "happiness": 6, "intellect": 4},
                "fail_feedback": "老一辈觉得丢了脸面，逢年过节免不了冷嘲热讽，家庭平添闲言碎语。",
                "fail_eff": {"wealth": 4.0, "happiness": -8, "rep": -5},
                "tag_succ": "务实自守",
                "tag_fail": "人情羁绊",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 35,
        "title": "学区房神话与三倍杠杆豪赌",
        "narrative": "孩子到了入学年纪，中介天天鼓吹学区房只涨不跌，劝你卖掉旧房加满三倍杠杆抢核心名校老破小。",
        "choices": [
            {
                "text": "加满三倍杠杆掏空六个钱包换购名校学区房，赌孩子起点与资产增值",
                "risk_label": "高杠杆博弈 · 成功率 50%",
                "calc_chance": lambda p: 50 + (10 if p.luck > 50 else -10),
                "succ_feedback": "精准在政策收紧前上车，孩子顺利入读重点校，账面浮盈丰厚，成为亲友楷模。",
                "succ_eff": {"wealth": 28.0, "happiness": -4, "rep": 12},
                "fail_feedback": "买在历史最高峰，随后行业去杠杆房价跌去三成，每月沉重月供如绞索套喉。",
                "fail_eff": {"wealth": -32.0, "happiness": -20, "health": -10, "rep": -4},
                "tag_succ": "杠杆豪赌",
                "tag_fail": "高位套牢",
                "is_key": True
            },
            {
                "text": "保持克制拒绝过度杠杆，让孩子读普通公立，积蓄配置国债与自身身心健康",
                "risk_label": "守拙自安 · 绝对安全",
                "calc_chance": lambda p: 100,
                "succ_feedback": "虽然被笑话缺乏远见，但随后数年周期风浪中，全家手握流动现金，从容不迫。",
                "succ_eff": {"wealth": 10.0, "happiness": 12, "health": 6, "rep": 5},
                "tag_succ": "现金为王",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 40,
        "title": "医院走廊的消毒水与35岁职场魔咒",
        "narrative": "家中老人确诊慢性大病需昂贵靶向药，公司推行'年轻化'大批裁员，中年重担如山倒下。",
        "choices": [
            {
                "text": "用最好的自费药，自己咬牙兼职接私单，一天睡五小时硬扛",
                "risk_label": "血肉尽孝 · 成功率 60%",
                "calc_chance": lambda p: int(60 + (p.health - 60) / 2),
                "succ_feedback": "父母病情稳定好转，兼职也跑通小财路，你用坚强毅力守住了全家的屋顶！",
                "succ_eff": {"rep": 15, "happiness": 6, "health": -12, "wealth": -6.0},
                "fail_feedback": "因连轴熬夜在赶路时突发晕厥送医，父母老泪纵横，家里账面元气大伤。",
                "fail_eff": {"health": -20, "wealth": -12.0, "happiness": -15, "rep": 6},
                "tag_succ": "铁骨脊梁",
                "tag_fail": "苦雨连阴",
                "is_key": True
            },
            {
                "text": "选用医保目录内保守方案，理性权衡家庭财务底线，不让小家庭因病返贫",
                "risk_label": "理性止损 · 沉重抉择",
                "calc_chance": lambda p: 100,
                "succ_feedback": "内心虽有遗憾，但小家庭现金流未伤筋动骨，子女生活与教育依然井然有序。",
                "succ_eff": {"wealth": -4.0, "happiness": -6, "intellect": 4},
                "tag_succ": "理性持家",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 44,
        "title": "突发疫情与行业大洗牌",
        "narrative": "行业洗牌风暴呼啸而至，所在部门被整体裁撤，HR将 N+1 补偿协议推到你面前。",
        "choices": [
            {
                "text": "拿走 N+1 彻底走出内耗，转行做独立咨询、跨境电商或自媒体创业",
                "risk_label": "逆势破局 · 成功率 55%",
                "calc_chance": lambda p: int(55 + (p.intellect - 50) / 2 + (10 if p.luck > 50 else -10)),
                "succ_feedback": "凭多年积累与线上红利，业务迅速跑通，年收益超过昔日死工资，重获掌控感！",
                "succ_eff": {"wealth": 25.0, "happiness": 14, "health": 2, "rep": 12},
                "fail_feedback": "线上赛道早已一片血海，接单艰难不得不消耗老本度日，生出斑白双鬓。",
                "fail_eff": {"wealth": -12.0, "happiness": -18, "health": -8, "rep": -2},
                "tag_succ": "绝处逢生",
                "tag_fail": "中年受困",
                "is_key": True
            },
            {
                "text": "放下自尊接受降薪40%调至边缘分支，保住五险一金和稳定",
                "risk_label": "忍辱求稳 · 稳固基本盘",
                "calc_chance": lambda p: 100,
                "succ_feedback": "虽然没了往日优越感，但准时到账的工资成了风浪中庇护全家老小的安全绳。",
                "succ_eff": {"wealth": 6.0, "happiness": -6, "health": -4, "rep": 6},
                "tag_succ": "风雨同舟",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 50,
        "title": "孩子高考：复制内卷还是尊重个性？",
        "narrative": "年过半百两鬓微白。孩子高考成绩中等偏上，亲戚建议报好就业的工科，孩子却想读小众哲学或艺术。",
        "choices": [
            {
                "text": "强力干预，逼孩子报考稳定好就业的专业，确保人生下限",
                "risk_label": "家长威严 · 成功率 70%",
                "calc_chance": lambda p: 70,
                "succ_feedback": "孩子毕业后顺利考取事业单位编制，旱涝保收，后来逐渐体谅了你的苦心。",
                "succ_eff": {"wealth": 5.0, "rep": 6, "happiness": -4},
                "fail_feedback": "孩子在讨厌的专业中痛苦挂科，毕业后换了几份工作，与你长期冷战疏离。",
                "fail_eff": {"happiness": -12, "rep": -4},
                "tag_succ": "铺路搭桥",
                "tag_fail": "代际隔阂",
                "is_key": False
            },
            {
                "text": "尊重孩子天赋意愿，资助其追求热爱，告诉 Ta'做个快乐普通人就好'",
                "risk_label": "开明慈爱 · 成功率 65%",
                "calc_chance": lambda p: 65 + (10 if p.luck > 50 else 0),
                "succ_feedback": "孩子在热爱领域闪闪发光，家庭氛围温馨如初，其乐融融。",
                "succ_eff": {"happiness": 15, "health": 4, "rep": 5},
                "fail_feedback": "冷门专业毕业即失业，孩子长年在家'全职啃老'，家庭不得不继续补贴。",
                "fail_eff": {"wealth": -8.0, "happiness": -8},
                "tag_succ": "开明长辈",
                "tag_fail": "儿女啃老",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 58,
        "title": "生成式AI风暴与体检红字",
        "narrative": "人工智能全面融入社会，曾经经验贬值。年近六旬的你体检单密布红字，单位通知准备退休。",
        "choices": [
            {
                "text": "彻底退居二线，戒掉烟酒与无效社交，晨练太极弄花种草寄情山水",
                "risk_label": "修身颐养 · 确定延寿",
                "calc_chance": lambda p: 100,
                "succ_feedback": "指标大幅改善，轻盈与淡然重回身心。名利彻底看淡，内心安详从容。",
                "succ_eff": {"health": 20, "happiness": 16, "wealth": -2.0, "rep": 5},
                "tag_succ": "养生得道",
                "is_key": False
            },
            {
                "text": "老骥伏枥，拿出部分积蓄投资AI新赛道或办青年导师工作室，再搏一回",
                "risk_label": "老骥伏枥 · 成功率 40%",
                "calc_chance": lambda p: int(40 + (15 if p.intellect > 70 else 0) + (10 if p.luck > 50 else -10)),
                "succ_feedback": "厚重阅历与新工具碰撞出奇迹，成为业界尊崇的元老顾问，名利双收！",
                "succ_eff": {"wealth": 25.0, "intellect": 10, "rep": 20, "health": -6},
                "fail_feedback": "精力跟不上被年轻人欺瞒，因熬夜突发心颤进ICU抢救，捡回一条命后认输。",
                "fail_eff": {"wealth": -15.0, "health": -28, "happiness": -16, "rep": 0},
                "tag_succ": "老骥伏枥",
                "tag_fail": "心力交瘁",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 66,
        "title": "含饴弄孙与公园的长椅",
        "narrative": "孙辈蹒跚学步，儿女工作繁忙希望你帮忙照料；老友则约你包车去西藏自驾圆年轻时的梦。",
        "choices": [
            {
                "text": "为子女分担重任，住进逼仄儿童房，每天买菜做饭接送孙辈",
                "risk_label": "代际燃烧 · 无怨无悔",
                "calc_chance": lambda p: 100,
                "succ_feedback": "看着小孙子扑进怀里，满心天伦之乐，虽腰腿偶有酸痛，但日子充实温暖。",
                "succ_eff": {"happiness": 10, "rep": 8, "health": -4},
                "tag_succ": "春蚕蜡炬",
                "is_key": False
            },
            {
                "text": "坚持独立生活空间，与老伴老友踏遍祖国名山大川",
                "risk_label": "暮年畅游 · 成功率 75%",
                "calc_chance": lambda p: int(75 + (p.health - 60) / 2),
                "succ_feedback": "在青海湖边吹风，在雪山脚下拍照，晚年如晚霞绚烂，活出了真性情！",
                "succ_eff": {"happiness": 16, "health": 6, "wealth": -5.0},
                "fail_feedback": "途中突发急性呼吸道感染折返休养，但见到了想看的风景，亦无憾意。",
                "fail_eff": {"health": -8, "wealth": -4.0, "happiness": 4},
                "tag_succ": "快意余生",
                "tag_fail": "风尘仆仆",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 74,
        "title": "老友凋零与泛黄的相册",
        "narrative": "翻看泛黄相片，昔日挚友相继离世，参加葬礼已多于婚礼，你平静凝视岁月余晖。",
        "choices": [
            {
                "text": "静心将见证的大时代与个人半生波澜写成自传，留给后世子孙",
                "risk_label": "立传铭史 · 精神传承",
                "calc_chance": lambda p: 100,
                "succ_feedback": "墨香弥漫。平静梳理了所有荣耀与遗憾，儿孙读罢热泪盈眶，记忆得以永存。",
                "succ_eff": {"intellect": 15, "happiness": 12, "rep": 15},
                "tag_succ": "青史留痕",
                "is_key": False
            },
            {
                "text": "散尽部分积蓄捐资助学，为这片热土留下最后一份温情",
                "risk_label": "大爱无声 · 广种福田",
                "calc_chance": lambda p: 100,
                "succ_feedback": "收到山区孩子们的真挚感谢信，如沐春风，灵魂感受到了前所未有的安详升华。",
                "succ_eff": {"wealth": -10.0, "happiness": 18, "rep": 20, "luck": 8},
                "tag_succ": "慈悲福泽",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 80,
        "title": "夕阳晚钟与生命辞章",
        "narrative": "冬日午后暖阳洒在阳台，长年相伴的老伴器官衰竭卧榻，握着你满是皱纹的手温柔告别。",
        "choices": [
            {
                "text": "遵从爱人生前意愿，选择安宁缓和疗护，在温情老歌中握手平静相伴",
                "risk_label": "体面告别 · 慈悲释怀",
                "calc_chance": lambda p: 100,
                "succ_feedback": "在老歌与回忆的温光中，爱人安详闭眼。没有仪器刺耳的轰鸣，满心皆是感恩。",
                "succ_eff": {"intellect": 10, "happiness": 8, "rep": 10},
                "tag_succ": "体面告别",
                "is_key": True
            },
            {
                "text": "倾尽全家积蓄送入ICU抢救插管，只求哪怕多陪一天",
                "risk_label": "生死执念 · 倾力而战",
                "calc_chance": lambda p: 100,
                "succ_feedback": "散尽晚年积蓄，在ICU门外守候近一个月。纵有万般不舍，终究坦然面对。",
                "succ_eff": {"wealth": -20.0, "happiness": -15, "health": -10, "rep": 5},
                "tag_succ": "生死执念",
                "is_key": True
            }
        ]
    }
]

# 未来纪元 16 大关卡 (深度构思：常温超导、聚变能源、脑机接口、碳配额、深空采矿、数字永生)
FUTURE_STAGES = [
    {
        "age_rel": 6,
        "title": "人造穹顶与幼年脑机接口手术",
        "narrative": "窗外是人造电离层过滤的幽蓝天幕，悬浮物流穿梭在钢铁峡谷。到了入幼学年龄，社区建议植入第三代神经智网接口。",
        "choices": [
            {
                "text": "自费升级军规级纯金神经元芯片，确保起步便拥有兆比特脑波直连速率",
                "risk_label": "顶尖义体 · 成功率 80%",
                "calc_chance": lambda p: 80 + (10 if p.luck > 50 else -5),
                "succ_feedback": "手术极度成功！思维与城市总网无缝嵌合，海量知识如本能般涌入，展现神童天赋。",
                "succ_eff": {"intellect": 14, "wealth": -2.5, "rep": 8},
                "fail_feedback": "发生轻度神经回路排斥，虽经抢救脱险，眼角留下了轻微疤痕，且耗尽家庭流动资金。",
                "fail_eff": {"intellect": 5, "wealth": -3.5, "health": -8, "happiness": -8},
                "tag_succ": "义体神童",
                "tag_fail": "排异惊魂",
                "is_key": False
            },
            {
                "text": "坚持采用传统纯碳基自然教学法，佩戴外置轻量光镜，保护原生态脑髓纯洁",
                "risk_label": "自然碳基 · 纯粹温润",
                "calc_chance": lambda p: 100,
                "succ_feedback": "大脑无冰冷金属压迫，想象力与原生情感发育极为完整，眼神清澈灵动。",
                "succ_eff": {"health": 8, "happiness": 10, "intellect": 4},
                "tag_succ": "纯粹碳基",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 10,
        "title": "碳配额紧缩与低轨研学抽签",
        "narrative": "全球公约严控个人碳配额，合成营养膏占据餐桌。学校组织'近地空间站7日重力研学营'，需押上半年能源分参与摇号。",
        "choices": [
            {
                "text": "家庭抵押光伏配额孤注一掷参与抽签，誓要亲眼俯瞰真实星海",
                "risk_label": "星辰豪赌 · 成功率 50%",
                "calc_chance": lambda p: 50 + (15 if p.luck > 50 else -10),
                "succ_feedback": "在空间站巨大穹顶下俯瞰蓝白相间的母星，灵魂遭剧烈洗礼，立下探索深空宏愿！",
                "succ_eff": {"intellect": 12, "happiness": 12, "rep": 10, "luck": 6},
                "fail_feedback": "抽签落空扣减配额，接下来半年全家不得不靠低阶藻类合成膏度日。",
                "fail_eff": {"wealth": -2.0, "happiness": -10, "health": -4},
                "tag_succ": "俯瞰地球",
                "tag_fail": "地表困顿",
                "is_key": True
            },
            {
                "text": "留在地面沉浸式VR全息模拟仓'云太空'游览，节约碳配额配置家庭储能电池",
                "risk_label": "务实持家 · 稳固生存",
                "calc_chance": lambda p: 100,
                "succ_feedback": "虽少了一份真实肉体的失重震撼，但能源储备充足，在寒潮断电季从容度过。",
                "succ_eff": {"wealth": 1.5, "happiness": 5, "intellect": 4},
                "tag_succ": "能源清醒",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 15,
        "title": "算力分级考试：中央智脑调度员还是深空航线技工？",
        "narrative": "职业被算法全权分流，前10%脑波共振者入选'智脑总控系'，其余大部分人将进深空技工学院派驻矿区。",
        "choices": [
            {
                "text": "通宵加载矩阵算法逻辑，注射神经激活剂，拼命冲击智脑核心调度席位",
                "risk_label": "算力冲顶 · 成功率 65%",
                "calc_chance": lambda p: int(65 + (p.intellect - 50) / 2),
                "succ_feedback": "以名列前茅的逻辑并发率斩获直博生资格！获赠高权限个人算力密钥。",
                "succ_eff": {"intellect": 16, "rep": 12, "wealth": 3.0, "health": -6},
                "fail_feedback": "神经元在关键测验中突发过热熔断，失之交臂，降级分流至外勤维修技校。",
                "fail_eff": {"intellect": 6, "happiness": -12, "health": -8, "rep": 2},
                "tag_succ": "算力精英",
                "tag_fail": "芯片熔断",
                "is_key": True
            },
            {
                "text": "选修实体核动力与机械动力学，深耕等离子焊接与气动阀门维修手艺",
                "risk_label": "硬派工匠 · 需求永存",
                "calc_chance": lambda p: 100,
                "succ_feedback": "算法喧嚣中唯实体手艺不可或缺。你成为各方争抢的硬核机械师，薪水丰厚稳健。",
                "succ_eff": {"wealth": 4.0, "health": 6, "intellect": 8, "rep": 6},
                "tag_succ": "深空重工",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 18,
        "title": "成人生死契：月球南极氦-3采掘还是虚拟灵境造梦？",
        "narrative": "成人礼上深空署递来契约：月球前哨高薪极端工种（合约期免除全家碳税），或留地表做虚拟现实造梦师。",
        "choices": [
            {
                "text": "签署月球采掘契约，登上班机前往严寒低重力极地，拿命换取阶层跃升",
                "risk_label": "异星搏命 · 成功率 60%",
                "calc_chance": lambda p: int(60 + (p.health - 60) / 2 + (10 if p.luck > 50 else -5)),
                "succ_feedback": "在极端风暴中成功抢修聚变反应堆，被破格晋升为南极基地首席工程师，全家获绿卡！",
                "succ_eff": {"wealth": 28.0, "intellect": 10, "rep": 15, "health": -6},
                "fail_feedback": "遭遇太阳耀斑风暴受困月表，留下不可逆骨质萎缩，提前结束服役返回母星。",
                "fail_eff": {"wealth": 8.0, "health": -18, "happiness": -12, "rep": 5},
                "tag_succ": "月海掘金",
                "tag_fail": "月面重创",
                "is_key": True
            },
            {
                "text": "留守母星，加入虚拟现实'灵境造梦工程'，为数十亿人构建精神避难所",
                "risk_label": "赛博造梦 · 舒适安详",
                "calc_chance": lambda p: 100,
                "succ_feedback": "在光怪陆离的赛博世界中创造梦幻国度，收获海量打赏，衣食无忧，心境优渥。",
                "succ_eff": {"wealth": 8.0, "happiness": 14, "intellect": 8, "health": 2},
                "tag_succ": "赛博造梦师",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 21,
        "title": "真挚碳基情愫还是完美仿生伴侣？",
        "narrative": "高级仿生机器人能完美模拟一切温柔与共情，且永不背叛。你遇到了纯真的碳基同窗，同时巨头推送了专属仿生伴侣。",
        "choices": [
            {
                "text": "选择真实的碳基同窗，接纳彼此的脾气与脆弱，在冰冷科技浪潮中抱团取暖",
                "risk_label": "真情凡人 · 成功率 70%",
                "calc_chance": lambda p: 70 + (10 if p.happiness > 60 else -5),
                "succ_feedback": "在算法至上的时代，你们两具真实的身躯成了彼此在冰冷星球上唯一的温热依靠。",
                "succ_eff": {"happiness": 18, "health": 4, "rep": 6},
                "fail_feedback": "因配额危机与微型胶囊住房的逼仄爆发争吵，抱憾解除同居协议。",
                "fail_eff": {"happiness": -15, "health": -6, "intellect": 2},
                "tag_succ": "碳基真爱",
                "tag_fail": "孤岛破碎",
                "is_key": False
            },
            {
                "text": "定制专属AI仿生伴侣，告别复杂内耗的情感博弈，全身心投入事业",
                "risk_label": "理性依附 · 绝对掌控",
                "calc_chance": lambda p: 100,
                "succ_feedback": "伴侣体贴渊博，为你打理一切杂务，你在无后顾之忧中全力冲刺事业积累。",
                "succ_eff": {"wealth": 10.0, "intellect": 8, "happiness": 6},
                "tag_succ": "人机共谐",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 24,
        "title": "地月货运电梯危机与应急处置",
        "narrative": "地月同步轨道电梯遭遇微陨石撞击，3号副缆震颤，原料悬停半空。智脑建议切断副缆断臂求生，但下方吊舱仍有工友失联。",
        "choices": [
            {
                "text": "手动覆盖智脑指令，穿着冷气外骨骼出舱近距离抢修备用牵引栓",
                "risk_label": "绝地救援 · 成功率 55%",
                "calc_chance": lambda p: int(55 + (p.intellect - 50) / 2 + (10 if p.luck > 50 else -10)),
                "succ_feedback": "失重翻滚中成功卡入锁死栓！工友生还且保全货运干线，获颁联邦一级星芒勋章！",
                "succ_eff": {"rep": 25, "wealth": 15.0, "happiness": 12, "health": -6},
                "fail_feedback": "虽延缓坠落，推进器被碎片割破，受困高空数小时险些缺氧失温。",
                "fail_eff": {"health": -16, "happiness": -12, "wealth": -2.0, "rep": 8},
                "tag_succ": "星轨英雄",
                "tag_fail": "轨道惊魂",
                "is_key": True
            },
            {
                "text": "严格遵循智脑方案执行安全抛弃程序，确保整座空港不受波及",
                "risk_label": "冷酷守则 · 稳妥避险",
                "calc_chance": lambda p: 100,
                "succ_feedback": "空港主体安全保全，你获得了合规表彰，但午夜梦回时那一缕坠落流光常在眼前掠过。",
                "succ_eff": {"wealth": 6.0, "rep": 5, "intellect": 4, "happiness": -6},
                "tag_succ": "规程执行者",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 27,
        "title": "小行星采矿股权还是地表绿区永久产权？",
        "narrative": "谷神星发现了储量惊人的超导矿脉，全网众筹；同时地表第四穹顶的'天然土壤独栋房产'挂牌出售。",
        "choices": [
            {
                "text": "押上全部流动资产加三倍杠杆，买入谷神星采矿母舰的核心股权通证",
                "risk_label": "星际创投 · 成功率 45%",
                "calc_chance": lambda p: int(45 + (p.intellect - 50) / 2 + (15 if p.luck > 50 else -10)),
                "succ_feedback": "采矿母舰首期满载而归，通证估值翻升数十倍，一跃晋升新太空寡头！",
                "succ_eff": {"wealth": 48.0, "intellect": 10, "rep": 18, "happiness": 10},
                "fail_feedback": "母舰遭遇未编目彗星风暴失联，项目破产清算，资产一夜归零跌入负债。",
                "fail_eff": {"wealth": -22.0, "happiness": -20, "health": -10, "rep": -5},
                "tag_succ": "星际寡头",
                "tag_fail": "深空破产",
                "is_key": True
            },
            {
                "text": "稳健买入穹顶绿区的天然泥土花园公寓，让家人呼吸未经循环的温润空气",
                "risk_label": "生态筑底 · 代际不动产",
                "calc_chance": lambda p: 100,
                "succ_feedback": "在人人只能看全息假草的未来，你拥有一片真实盛开鲜花的土地，全家体魄与心境大获庇佑。",
                "succ_eff": {"wealth": 18.0, "health": 10, "happiness": 12, "rep": 8},
                "tag_succ": "绿区领主",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 31,
        "title": "CRISPR-IV 胚胎基因编辑还是自然分娩？",
        "narrative": "新生命即将诞生。基因中心建议：支付高额费用进行综合强化编辑（消除99%遗传病并增脑容量），否则未来或处劣势。",
        "choices": [
            {
                "text": "抵押资产给孩子加载全套顶配抗病与智力基因强化剪辑",
                "risk_label": "基因跃迁 · 成功率 85%",
                "calc_chance": lambda p: 85 + (10 if p.luck > 50 else 0),
                "succ_feedback": "孩子健康指标拉满，双目炯炯有神，对多维空间几何拥有与生俱来的领悟力！",
                "succ_eff": {"rep": 12, "wealth": -10.0, "happiness": 8},
                "fail_feedback": "出现微量代谢过敏综合征，往后数年需定期注射专用抑制酶维持平衡。",
                "fail_eff": {"wealth": -15.0, "health": -4, "happiness": -10},
                "tag_succ": "新人类之父/母",
                "tag_fail": "基因困惑",
                "is_key": False
            },
            {
                "text": "拒绝人工剪辑，坚信自然演化的多样性，给予孩子一个未经篡改的质朴原生态身躯",
                "risk_label": "自然主义 · 纯真之爱",
                "calc_chance": lambda p: 100,
                "succ_feedback": "孩子继承了最本真的微笑与泪水，家庭洋溢着纯天然温情，不受商业订阅制绑定。",
                "succ_eff": {"happiness": 15, "health": 6, "wealth": 2.0},
                "tag_succ": "自然守卫",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 35,
        "title": "数字永生法案：思维云端备份的诱惑",
        "narrative": "《意识上传与数字连续性法案》通过，首批商业'意识云端备份'开放，只要连入量子机房即可战胜肉体毁灭。",
        "choices": [
            {
                "text": "重金认购顶层量子服务器终身席位，将自身全部记忆模型实时同步云端",
                "risk_label": "数字永生 · 成功率 75%",
                "calc_chance": lambda p: int(75 + (p.intellect - 50) / 2),
                "succ_feedback": "你确信自己战胜了碳基生物最原始的死亡恐惧，行事更加从容果敢，眼界上升至宇宙维度！",
                "succ_eff": {"intellect": 15, "happiness": 10, "wealth": -12.0, "rep": 10},
                "fail_feedback": "上传过程中产生严重的人格解离症，总感觉云端有另一个'自己'在注视肉身，心境震荡。",
                "fail_eff": {"wealth": -15.0, "happiness": -18, "health": -6},
                "tag_succ": "云端漫游者",
                "tag_fail": "解离迷航",
                "is_key": True
            },
            {
                "text": "断然拒绝'假借代码续命'，坚信'有限的生命才是真实的生命'，珍惜当下每一寸阳光",
                "risk_label": "碳基尊严 · 终极清醒",
                "calc_chance": lambda p: 100,
                "succ_feedback": "看着许多人迷失于虚拟永生幻觉，你脚踏实地体验泥土芬芳与家人体温，精神极其富足。",
                "succ_eff": {"happiness": 16, "health": 8, "intellect": 8, "rep": 8},
                "tag_succ": "碳基守护者",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 40,
        "title": "仿生义体老化与高阶维护费黑洞",
        "narrative": "早年植入的神经连接轴与人工肺叶出现氧化磨损，固件已停更；孩子的算力学费与穹顶维保费如两只巨兽。",
        "choices": [
            {
                "text": "不惜成本贷款置换全新钛合金轻量化内脏与四代神经枢纽，重返巅峰状态",
                "risk_label": "机械飞升 · 成功率 65%",
                "calc_chance": lambda p: int(65 + (p.health - 60) / 2),
                "succ_feedback": "奔流着澎湃的电信号动力，体能与心智超越二十岁青年，职场竞争力暴涨！",
                "succ_eff": {"health": 20, "intellect": 8, "wealth": -12.0, "rep": 10},
                "fail_feedback": "新旧芯片协议冲突引发局部瘫痪，在康复舱躺了三个月，现金流被掏空。",
                "fail_eff": {"health": -18, "wealth": -18.0, "happiness": -15, "rep": -2},
                "tag_succ": "机械重生",
                "tag_fail": "义体溃败",
                "is_key": True
            },
            {
                "text": "通过自然物理调理缓解衰老，拆除过载义体，顺应生理节律降速生活",
                "risk_label": "返璞归真 · 沉静自安",
                "calc_chance": lambda p: 100,
                "succ_feedback": "放弃了与年轻人拼算力的冲动，摆脱了昂贵的维保陷阱，财务扎实内心平和。",
                "succ_eff": {"health": 6, "happiness": 12, "wealth": 4.0},
                "tag_succ": "自然养老",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 44,
        "title": "强人工智能自组织与地表大洗牌",
        "narrative": "中央智能网络完成第七次自我重构，接管了全球90%的规划与研发。深空项目部被整体'代码化整编'发放退役通证。",
        "choices": [
            {
                "text": "领走遣散资产，联合独立学者创办'纯人工艺术与哲学思辨学社'，守卫人类诗性灵光",
                "risk_label": "文明火种 · 成功率 65%",
                "calc_chance": lambda p: int(65 + (p.intellect - 50) / 2 + (10 if p.luck > 50 else 0)),
                "succ_feedback": "纯手绘展览与哲学讲座引起全球精神共鸣，成为冰冷机械时代的一座精神灯塔！",
                "succ_eff": {"rep": 20, "intellect": 15, "happiness": 14, "wealth": 8.0},
                "fail_feedback": "人们早已习惯了算法投喂的极乐幻象，学社门可罗雀入不敷出，陷入深深的时代虚无。",
                "fail_eff": {"wealth": -8.0, "happiness": -16, "intellect": 5},
                "tag_succ": "文明火炬手",
                "tag_fail": "时代的乡愁",
                "is_key": True
            },
            {
                "text": "接受算法调遣，成为中央智脑在实体矿区的'人类伦理安全巡检员'，保住高额体制福利",
                "risk_label": "体制守夜人 · 确定无忧",
                "calc_chance": lambda p: 100,
                "succ_feedback": "巡视在机器轰鸣的旷野，虽然枯燥重复，但拥有最高等级的医疗与全家配额保障。",
                "succ_eff": {"wealth": 12.0, "happiness": 4, "health": 4, "rep": 6},
                "tag_succ": "巡检守夜人",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 50,
        "title": "孩子的火星移民申请表：远征还是守望？",
        "narrative": "火星城邦接纳新移民。年满十八岁的孩子递来'水手大峡谷移民表'，一旦启程，异星时空将让此生再难亲身相拥。",
        "choices": [
            {
                "text": "含泪在资助单上签字，倾囊为孩子购置顶级深空救生装备，勉励 Ta'征服辽阔星辰'",
                "risk_label": "深空慈爱 · 成功率 75%",
                "calc_chance": lambda p: 75 + (10 if p.luck > 50 else 0),
                "succ_feedback": "孩子在火星发来红色日落握手全息，两代人隔亿万里，心灵在骄傲中紧紧相依。",
                "succ_eff": {"rep": 15, "happiness": 8, "intellect": 8, "wealth": -10.0},
                "fail_feedback": "漫长的通信延迟折磨着神经，每逢深空黑子暴发便夜夜担忧难眠。",
                "fail_eff": {"happiness": -12, "health": -6, "wealth": -10.0},
                "tag_succ": "送子远征",
                "tag_fail": "星际空巢",
                "is_key": False
            },
            {
                "text": "动用监护人否决权，将孩子留在母星地表共同生活，守护代际天伦",
                "risk_label": "故土守望 · 安全温暖",
                "calc_chance": lambda p: 100,
                "succ_feedback": "虽无波澜壮阔的星际历险，但能时常围坐真实餐桌共进晚餐，人间烟火胜过万颗冰冷恒星。",
                "succ_eff": {"happiness": 12, "health": 6, "rep": 4},
                "tag_succ": "母星守望",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 58,
        "title": "超级太阳风暴与城市断网之夜",
        "narrative": "百年未遇的超级太阳风暴击碎了外层星链，整座城市断网断电。年轻一代在黑暗中恐慌，年近六旬的你点亮了实体蜡烛。",
        "choices": [
            {
                "text": "凭一生的实体机械手艺，组织邻里搭建手摇发电机与自流冷凝净水系统",
                "risk_label": "古道热肠 · 成功率 85%",
                "calc_chance": lambda p: int(85 + (p.intellect - 50) / 2),
                "succ_feedback": "烛光跃动。你用古老智慧带领整个街区安稳度过了危机，深受各世代居民拥戴敬仰！",
                "succ_eff": {"rep": 20, "happiness": 15, "intellect": 10, "health": 2},
                "fail_feedback": "在攀爬顶楼固定太阳能板时扭伤了腰椎，但在年轻人的搀扶中感受到久违的社区温度。",
                "fail_eff": {"health": -8, "rep": 10, "happiness": 4},
                "tag_succ": "暗夜引路人",
                "tag_fail": "老将负伤",
                "is_key": True
            },
            {
                "text": "在温暖防空小居室里，与伴侣在烛光下翻看实体纸质相册，享受绝对宁静",
                "risk_label": "岁月温存 · 终极静谧",
                "calc_chance": lambda p: 100,
                "succ_feedback": "没有算法推送，没有指标催促，这一夜重回千百年前人类最朴素的模样，心灵得到深层治愈。",
                "succ_eff": {"happiness": 20, "health": 8, "intellect": 5},
                "tag_succ": "烛光沉醉",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 66,
        "title": "深空引退与星空观象台长椅",
        "narrative": "全自动化无需人类肉身劳动，终身算力红利衣食无忧。孙辈好奇摸着你温热手指，问起你年轻时造过的飞船与写过的代码。",
        "choices": [
            {
                "text": "出资将废弃射电望远镜改造成公益星空学堂，免费教下一代辨认真实星座",
                "risk_label": "点亮童眸 · 代际引路",
                "calc_chance": lambda p: 100,
                "succ_feedback": "孩子们围坐在你身边仰望真实星空。你将属于人类最初的敬畏与浪漫，深植进新世代心田。",
                "succ_eff": {"happiness": 18, "rep": 16, "intellect": 10},
                "tag_succ": "星空先生",
                "is_key": False
            },
            {
                "text": "搭乘深空游轮前往木星大红斑轨道旅行，亲眼凝视转动了万年的风暴",
                "risk_label": "朝圣宇宙 · 成功率 80%",
                "calc_chance": lambda p: int(80 + (p.health - 60) / 2),
                "succ_feedback": "直面那遮天蔽日的橙红风暴，身心被宇宙的无垠与庄严所震慑，晚年再无任何遗憾！",
                "succ_eff": {"intellect": 18, "happiness": 16, "wealth": -6.0},
                "fail_feedback": "虽因重力缓冲故障导致头晕，但亲眼见证木星光环的瞬间，泪水浸湿了眼眶。",
                "fail_eff": {"health": -8, "happiness": 10, "wealth": -5.0},
                "tag_succ": "大红斑朝圣者",
                "tag_fail": "风尘旅人",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 74,
        "title": "老旧量子晶片的封存：把什么留给未来？",
        "narrative": "整理一生的旧式晶片与信件，全球数字历史博物馆发来邀请，希望收录你这一代跨越'旧碳基向星际智能跃迁'的实录私人档案。",
        "choices": [
            {
                "text": "毫无保留地将全套私人回忆日记、错误抉择与真实泪水捐献归档，作为人类童年期的真切见证",
                "risk_label": "真情铭史 · 照亮来路",
                "calc_chance": lambda p: 100,
                "succ_feedback": "名字被刻入月球文明地平线金石库。后世学者盛赞：'在这份档案里，我们看见了活生生的人'。",
                "succ_eff": {"rep": 25, "intellect": 15, "happiness": 12},
                "tag_succ": "文明记忆标本",
                "is_key": False
            },
            {
                "text": "将积蓄全部捐助给地球荒漠化生物圈逆转基金，为母星多种一棵未经基因编辑的天然阔叶树",
                "risk_label": "绿茵长眠 · 报恩母星",
                "calc_chance": lambda p: 100,
                "succ_feedback": "春风吹拂着山谷里稚嫩的树苗。你把最后的力量还给了这颗蓝色摇篮，灵魂一片澄澈空灵。",
                "succ_eff": {"wealth": -12.0, "happiness": 20, "rep": 18, "luck": 10},
                "tag_succ": "母星反哺",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 80,
        "title": "生命终幕：是上传思维意识，还是随微风散入尘埃？",
        "narrative": "冬日午后阳光穿过穹顶折射出七彩微茫。意识上传舱候在一旁，医生柔声询问是否启动永久上传，还是选择以碳基肉身完整告别？",
        "choices": [
            {
                "text": "微笑拒绝上传，紧握着家人的手，在真实的心跳渐止中体面辞世，化作泥土与春风",
                "risk_label": "碳基终章 · 从容化蝶",
                "calc_chance": lambda p: 100,
                "succ_feedback": "在安静温暖的夕阳中平静地呼出最后一口气。人间这一遭，你完完整整、真真切切地走过，问心无愧。",
                "succ_eff": {"intellect": 12, "happiness": 15, "rep": 15},
                "tag_succ": "真善合眼",
                "is_key": True
            },
            {
                "text": "启动思维上传终端，将一生的灵魂与认知化作一道光束射入深空网络，奔赴永恒赛博星海",
                "risk_label": "意识升维 · 奔向永恒",
                "calc_chance": lambda p: 100,
                "succ_feedback": "碳基身躯冷却，而你的意识已在光速航线中展开羽翼，翱翔于无穷无尽的宇宙数据云海之中。",
                "succ_eff": {"intellect": 25, "happiness": 10, "rep": 10},
                "tag_succ": "光流升维",
                "is_key": True
            }
        ]
    }
]

# -*- coding: utf-8 -*-
PAST_ALT_STAGES_PY = [
    # Stage 0
    {
        "period": "幼年启蒙",
        "title": "供销社的玻璃糖罐与弄堂嬉戏",
        "narrative": "弄堂里回荡着竹椅摇晃与叫卖麦芽糖的梆子声。长辈想教你毛笔临帖与古文，而邻里伙伴正在街上翻花绳捉迷藏。",
        "choices": [
            {
                "text": "跟随长辈在八仙桌前研墨临帖，背诵千字文与珠算口诀",
                "risk_label": "书香开蒙 · 涵养心性",
                "calc_chance": lambda p: 80 + (10 if p.intellect > 50 else 0),
                "succ_feedback": "字迹清秀端正，长辈欣慰，早早培养出专注力与耐得住寂寞的定力。",
                "succ_eff": {"intellect": 8, "happiness": 4, "rep": 5},
                "fail_feedback": "顽皮好动打翻了墨水瓶弄脏新衣挨了板子，但多少记住了几篇古训。",
                "fail_eff": {"intellect": 3, "happiness": -4, "rep": 1},
                "tag_succ": "临池学书",
                "tag_fail": "顽皮受戒",
                "is_key": False
            },
            {
                "text": "混迹弄堂巷尾，当孩子王领着大伙拍洋画、滚铁环疯玩",
                "risk_label": "野蛮生长 · 市井天性",
                "calc_chance": lambda p: 100,
                "succ_feedback": "成了胡同里最机灵的小首领，交际能力强，皮实耐摔身体棒。",
                "succ_eff": {"health": 6, "happiness": 8, "intellect": 2},
                "tag_succ": "巷尾霸王",
                "is_key": False
            }
        ]
    },
    # Stage 1
    {
        "period": "童年韶光",
        "title": "集市小摊与万元户浪潮",
        "narrative": "集市上摆满了喇叭裤、蛤蟆镜和电子表，个体户渐渐受人眼热。表哥邀你放学后一起帮他在校门外摆摊卖磁带和圆珠笔。",
        "choices": [
            {
                "text": "放学后帮表哥看摊吆喝、算账收钱，体会商海微澜",
                "risk_label": "市井试水 · 成功率 65%",
                "calc_chance": lambda p: 65 + (15 if p.luck > 50 else -5),
                "succ_feedback": "货品被同龄人一抢而空！分到人生第一笔零花钱，早早树立商业嗅觉。",
                "succ_eff": {"wealth": 3.0, "intellect": 6, "happiness": 5, "luck": 3},
                "fail_feedback": "遭遇学校纪检抓包，货物被扣，回家被父母好一顿训斥。",
                "fail_eff": {"wealth": -1.0, "happiness": -8, "intellect": 2, "rep": -3},
                "tag_succ": "地摊财商",
                "tag_fail": "出师不利",
                "is_key": True
            },
            {
                "text": "拒绝摆摊，专心待在家中阅读少儿科普读物《十万个为什么》",
                "risk_label": "规矩求知 · 笃定平稳",
                "calc_chance": lambda p: 100,
                "succ_feedback": "远离街头喧嚣，沉浸在百科常识中，打下了扎实科学基础。",
                "succ_eff": {"intellect": 7, "happiness": 5, "health": 2},
                "tag_succ": "求知幼苗",
                "is_key": False
            }
        ]
    },
    # Stage 2
    {
        "period": "少年分流",
        "title": "少年宫无线电队还是街头武侠梦",
        "narrative": "录像厅放着港台武侠片，少年宫正选拔无线电测向学员。初三升高中关口，技术钻研与仗剑走天涯在你心中碰撞。",
        "choices": [
            {
                "text": "报名少年宫无线电队，夜夜自学焊电路板与收发摩尔斯码",
                "risk_label": "技术硬派 · 成功率 75%",
                "calc_chance": lambda p: int(75 + (p.intellect - 50) / 2),
                "succ_feedback": "在全省科技竞赛中斩获二等奖，获省重点高中降分录取！",
                "succ_eff": {"intellect": 14, "rep": 8, "happiness": 5, "health": -2},
                "fail_feedback": "焊接时不慎烫伤手指电路击穿，虽参赛失利但掌握了扎实电工基础。",
                "fail_eff": {"intellect": 5, "happiness": -6, "health": -4},
                "tag_succ": "无线电极客",
                "tag_fail": "烙铁微痕",
                "is_key": True
            },
            {
                "text": "沉迷租书摊金庸古龙武侠小说，与发小结拜兄弟快意恩仇",
                "risk_label": "浪漫不羁 · 豪爽义气",
                "calc_chance": lambda p: 100,
                "succ_feedback": "虽文化课受轻微影响，但结交了过命发小，性格变得极其豪爽讲义气。",
                "succ_eff": {"happiness": 10, "intellect": -2, "rep": 5},
                "tag_succ": "江湖义气",
                "is_key": False
            }
        ]
    },
    # Stage 3
    {
        "period": "成人立志",
        "title": "外企代表处热潮还是军旅铸钢魂",
        "narrative": "跨国企业在沿海设代表处高薪招聘白领，征兵横幅也在广场招展。是学好外语冲刺外企，还是投笔从戎进军营淬炼？",
        "choices": [
            {
                "text": "报考外语或国际商务，通宵苦练英语口语与商务礼仪衝刺涉外企业",
                "risk_label": "涉外先锋 · 成功率 65%",
                "calc_chance": lambda p: 65 + (10 if p.intellect > 50 else 0) + (5 if p.luck > 50 else -5),
                "succ_feedback": "一口流利外语让你在校招中脱颖而出，拿到高薪外企管培资格！",
                "succ_eff": {"wealth": 5.0, "intellect": 12, "rep": 10, "happiness": 5},
                "fail_feedback": "当年外贸岗位缩减竞争白热化只拿到普通文秘，但眼界已然拓宽。",
                "fail_eff": {"wealth": 1.0, "intellect": 6, "happiness": -6, "rep": 2},
                "tag_succ": "外企菁英",
                "tag_fail": "涉外求索",
                "is_key": True
            },
            {
                "text": "响应国家号召应征入伍，进入野战部队或技术兵种磨砺钢铁意志",
                "risk_label": "戎装风华 · 淬炼筋骨",
                "calc_chance": lambda p: 100,
                "succ_feedback": "在严明纪律中褪去稚嫩，铸就磐石般毅力与体魄，立三等功入党！",
                "succ_eff": {"health": 15, "intellect": 5, "happiness": 8, "rep": 12},
                "tag_succ": "铁血铸魂",
                "is_key": True
            }
        ]
    },
    # Stage 4
    {
        "period": "青春韶华",
        "title": "实验室夜灯还是摇滚校园乐队",
        "narrative": "校园广播放着朴树的歌，长发吉他手在草坪受人追捧，重点实验室灯火通明。是押注科研论文，还是组乐队燃烧热血？",
        "choices": [
            {
                "text": "跟随导师泡在重点实验室熬夜做实验跑数据，冲刺核心期刊论文",
                "risk_label": "学术登攀 · 成功率 70%",
                "calc_chance": lambda p: int(70 + (p.intellect - 50) / 2),
                "succ_feedback": "论文成功被核心期刊收录！拿到特等奖学金并锁定学术保研资格！",
                "succ_eff": {"intellect": 16, "rep": 8, "wealth": 2.0, "health": -4},
                "fail_feedback": "实验仪器突发故障半年心血白费，科研路充满坎坷考验。",
                "fail_eff": {"intellect": 6, "happiness": -10, "health": -6},
                "tag_succ": "学术新星",
                "tag_fail": "重做实验",
                "is_key": True
            },
            {
                "text": "担任校园摇滚乐队乐手，走穴高校巡演，在吉他失真中宣泄热血",
                "risk_label": "摇滚狂潮 · 激情燃烧",
                "calc_chance": lambda p: 100,
                "succ_feedback": "原创曲目在大学城风靡一时，收获无数掌声与热烈爱慕，无悔青春！",
                "succ_eff": {"happiness": 16, "rep": 6, "wealth": -1.0},
                "tag_succ": "摇滚青年",
                "is_key": False
            }
        ]
    },
    # Stage 5
    {
        "period": "初涉人世",
        "title": "外包代工厂驻厂还是股市红马甲",
        "narrative": "世界工厂流水线日夜轰鸣，证券营业部人头攒动。是扎根实体制造一线做工程师，还是去证券咨询做穿梭行情的操盘手？",
        "choices": [
            {
                "text": "投身合资制造大厂担任现场工程师，深入车间把控精密工业标准",
                "risk_label": "硬核制造 · 确定成长",
                "calc_chance": lambda p: 100,
                "succ_feedback": "吃透了全套精密工业标准与供应链管理，成为无可替代的技术骨干。",
                "succ_eff": {"wealth": 5.0, "intellect": 10, "health": 2, "rep": 8},
                "tag_succ": "工业脊梁",
                "is_key": True
            },
            {
                "text": "进入民间配资与投资咨询室，学习K线缠论尝试做职业操盘手",
                "risk_label": "资本刀尖 · 成功率 45%",
                "calc_chance": lambda p: int(45 + (15 if p.luck > 50 else -10) + (p.intellect - 50) / 2),
                "succ_feedback": "精准捕捉几只重组大牛股，账户本金在半年内暴涨三倍！",
                "succ_eff": {"wealth": 22.0, "intellect": 12, "happiness": 8, "luck": 6},
                "fail_feedback": "突遭黑天鹅连续跌停穿仓清洗，在营业部门前抽了一整盒劣质烟。",
                "fail_eff": {"wealth": -8.0, "happiness": -16, "health": -8, "rep": -4},
                "tag_succ": "操盘黑马",
                "tag_fail": "股海折戟",
                "is_key": True
            }
        ]
    },
    # Stage 6
    {
        "period": "成家立业",
        "title": "淘宝电商档口还是体制内安稳考编",
        "narrative": "服装数码小商品通过网线发往全国，双十一狂欢启幕；父母催你考编。是租车库开淘宝店，还是备战省考谋安稳？",
        "choices": [
            {
                "text": "在城中村租民房做淘宝电商，日夜打包发货搏击电商红利",
                "risk_label": "电商淘金 · 成功率 55%",
                "calc_chance": lambda p: int(55 + (15 if p.luck > 50 else -5) + (p.intellect - 50) / 2),
                "succ_feedback": "打中爆款日出万单，快递车天天堵在楼下，短短两年累积惊人财富！",
                "succ_eff": {"wealth": 30.0, "intellect": 10, "happiness": 8, "health": -6, "rep": 10},
                "fail_feedback": "代工厂质量翻车遭遇退货潮和平台扣保，押进的几万本金血本无归。",
                "fail_eff": {"wealth": -6.0, "intellect": 5, "happiness": -12, "health": -8},
                "tag_succ": "电商弄潮",
                "tag_fail": "库存挤压",
                "is_key": True
            },
            {
                "text": "专心闭门苦读申论行测，在公务员省考中突围入编捧上金饭碗",
                "risk_label": "金榜入仕 · 成功率 75%",
                "calc_chance": lambda p: int(75 + (p.intellect - 50) / 2),
                "succ_feedback": "以面试第一被市直机关录用！父母在亲友圈扬眉吐气，社会地位稳固。",
                "succ_eff": {"wealth": 4.0, "rep": 18, "happiness": 12, "health": 4},
                "fail_feedback": "笔试入围但面试被反超，只得委身街道编外临聘，心绪郁结。",
                "fail_eff": {"wealth": 1.5, "rep": 4, "happiness": -6},
                "tag_succ": "体制栋梁",
                "tag_fail": "省考饮恨",
                "is_key": True
            }
        ]
    },
    # Stage 7
    {
        "period": "三十而立",
        "title": "跨国派驻海外淘金还是深耕家乡人脉",
        "narrative": "基建出海如火如荼，海外驻外岗位开出三倍年薪；老家亲友劝你留在本地深耕圈子。远赴海外荒原还是经营温情人脉？",
        "choices": [
            {
                "text": "签下海外派驻军令状，奔赴艰苦海外工地独当一面赚取高薪",
                "risk_label": "海外征途 · 成功率 65%",
                "calc_chance": lambda p: 65 + (10 if p.health > 60 else -10) + (10 if p.luck > 50 else 0),
                "succ_feedback": "在异国克服风沙成功交付重大跨国标段，攒下巨额现金并获擢升！",
                "succ_eff": {"wealth": 25.0, "rep": 15, "intellect": 10, "health": -6, "happiness": 4},
                "fail_feedback": "在热带感染严重登革热，工程又因政局波动搁浅，只得提前回国。",
                "fail_eff": {"wealth": 6.0, "health": -18, "happiness": -14, "rep": 2},
                "tag_succ": "海外拓荒巨子",
                "tag_fail": "异域惊涛",
                "is_key": True
            },
            {
                "text": "留在本地合伙开茶楼，以茶会友深耕地方政商人脉网络",
                "risk_label": "市井人情 · 稳扎稳打",
                "calc_chance": lambda p: 100,
                "succ_feedback": "成了熟人网络的节点，办事总能找到门路，家庭其乐融融。",
                "succ_eff": {"wealth": 6.0, "rep": 12, "happiness": 10, "health": 2},
                "tag_succ": "人情达人",
                "is_key": False
            }
        ]
    },
    # Stage 8
    {
        "period": "负重前行",
        "title": "民间借贷风暴还是理财信托踩雷",
        "narrative": "民间借贷与高息理财野蛮生长，动辄12%以上利息动人心魄；亲戚登门借巨资。是相信高息熟人借贷，还是存大额存单？",
        "choices": [
            {
                "text": "坚决抵制任何高息诱惑，把全家积蓄拆分存入国有行大额存单与国债",
                "risk_label": "绝对防守 · 锁定本金",
                "calc_chance": lambda p: 100,
                "succ_feedback": "不少熟人在暴雷中血本无归，唯独你家现金秋毫无损，被奉为远见楷模！",
                "succ_eff": {"wealth": 8.0, "happiness": 14, "rep": 8},
                "tag_succ": "定海神针",
                "is_key": True
            },
            {
                "text": "看在重利与旧交情面上借出重金吃高息，甚至抵押部分房产跟进",
                "risk_label": "贪婪博弈 · 成功率 35%",
                "calc_chance": lambda p: 35 + (15 if p.luck > 60 else -10),
                "succ_feedback": "在崩塌前三个月敏锐嗅到风险强行收回本息，狠狠大赚了一笔！",
                "succ_eff": {"wealth": 25.0, "happiness": 10, "luck": 6},
                "fail_feedback": "实控人卷款潜逃，催收群哭声一片，多年血汗钱灰飞烟灭，一夜白头。",
                "fail_eff": {"wealth": -25.0, "happiness": -22, "health": -14, "rep": -8},
                "tag_succ": "险峰收割",
                "tag_fail": "雷暴劫难",
                "is_key": True
            }
        ]
    },
    # Stage 9
    {
        "period": "中年险滩",
        "title": "合伙人反目还是技术转型破局",
        "narrative": "四十岁中年危机降临，昔日合伙人在利益分配上产生巨大裂痕并转移客户。是打官司清算旧友，还是钻研新技术破局？",
        "choices": [
            {
                "text": "请专业商业律师对簿公堂，坚决捍卫合法知识产权与股东权益",
                "risk_label": "法槌对决 · 成功率 65%",
                "calc_chance": lambda p: 65 + (10 if p.intellect > 50 else 0) + (10 if p.luck > 50 else -10),
                "succ_feedback": "一审全额支持诉求，追回数百万赔偿并夺回控制权，树立铁血威名！",
                "succ_eff": {"wealth": 15.0, "rep": 15, "happiness": 6, "health": -6},
                "fail_feedback": "诉讼拖延数年耗尽心力，执行时对方金蝉脱壳，赢了官司输了钱。",
                "fail_eff": {"wealth": -6.0, "rep": 4, "happiness": -15, "health": -10},
                "tag_succ": "铁腕维权",
                "tag_fail": "赢了官司输了钱",
                "is_key": True
            },
            {
                "text": "放下执念断舍离，以四十岁之躯从零自学新架构和数字化工具破局",
                "risk_label": "涅槃重生 · 大器晚成",
                "calc_chance": lambda p: 100,
                "succ_feedback": "行业底蕴融合新工具，开发出低成本高敏捷新业务，赢得满堂彩！",
                "succ_eff": {"intellect": 15, "wealth": 8.0, "happiness": 10, "rep": 12},
                "tag_succ": "中年涅槃",
                "is_key": True
            }
        ]
    },
    # Stage 10
    {
        "period": "动荡考验",
        "title": "实体供应链断裂与社区团购互助",
        "narrative": "外部物流受阻工厂停工，邻里蔬菜药品短缺。是闭门自保消耗存粮，还是站出来担当社区团长组织平价保供？",
        "choices": [
            {
                "text": "挺身而出担当民间保供团长，对接农贸批发为整小区协调平价物资",
                "risk_label": "侠者仁心 · 成功率 80%",
                "calc_chance": lambda p: 80 + (10 if p.luck > 50 else 0),
                "succ_feedback": "在最紧张的日子守护了数百户餐桌与急用药，成为公认的定盘星！",
                "succ_eff": {"rep": 25, "happiness": 15, "health": -4, "wealth": 1.0},
                "fail_feedback": "途中遭遇损耗个别人不理解还冷嘲热讽，深刻体会到人性的复杂。",
                "fail_eff": {"rep": 8, "happiness": -10, "health": -6},
                "tag_succ": "邻里英雄",
                "tag_fail": "仁心微凉",
                "is_key": True
            },
            {
                "text": "紧闭大门严格消杀，在室内健身陪伴家人读书下棋安稳度日",
                "risk_label": "韬光养晦 · 恬淡自守",
                "calc_chance": lambda p: 100,
                "succ_feedback": "全家平安度过危机没有染病，反而难得修复了因忙碌疏离的亲情。",
                "succ_eff": {"health": 8, "happiness": 12, "intellect": 4},
                "tag_succ": "阖家平安",
                "is_key": False
            }
        ]
    },
    # Stage 11
    {
        "period": "知命之年",
        "title": "老宅拆迁谈判还是乡村民宿退隐",
        "narrative": "城市规划到了近郊老宅，拆迁办开出安置方案；乡村归园田居兴起。是紧咬条件博弈拆迁，还是拿补偿归隐山水？",
        "choices": [
            {
                "text": "请专业评估团队据理力争，坚守合法红线博弈拿下最优安置方案",
                "risk_label": "拆迁博弈 · 成功率 65%",
                "calc_chance": lambda p: int(65 + (15 if p.luck > 50 else -5) + (p.intellect - 50) / 2),
                "succ_feedback": "拿到多套核心地段商铺与大笔安家现金，为家族彻底奠定财富基业！",
                "succ_eff": {"wealth": 35.0, "happiness": 10, "rep": 10},
                "fail_feedback": "僵持过久开发商绕道更改规划，拆迁搁浅成为死角，空耗心血。",
                "fail_eff": {"wealth": 2.0, "happiness": -15, "rep": -4},
                "tag_succ": "旧城红利",
                "tag_fail": "画地为牢",
                "is_key": True
            },
            {
                "text": "承包青山绿水旁的一方老农院改造为茶舍民宿，回归清静自然",
                "risk_label": "山水归隐 · 怡然自乐",
                "calc_chance": lambda p: 100,
                "succ_feedback": "晨起看山雾暮落听松涛，民宿成文人雅客秘境，内心宽阔宁静。",
                "succ_eff": {"health": 12, "happiness": 18, "wealth": 4.0, "rep": 6},
                "tag_succ": "山居雅士",
                "is_key": False
            }
        ]
    },
    # Stage 12
    {
        "period": "花甲在望",
        "title": "大病保单理赔与海外尖端医疗",
        "narrative": "年近六旬大检中查出早期结节，现代微创质子治疗费用昂贵。是动用商业重疾险赴顶尖专科彻底手术，还是保守调养？",
        "choices": [
            {
                "text": "启动全球重疾绿通，接受顶尖专家主刀的机器人微创手术切除病灶",
                "risk_label": "现代医学 · 成功率 85%",
                "calc_chance": lambda p: 85 + (10 if p.wealth > 20 else 0),
                "succ_feedback": "手术极其成功完全切除未扩散！劫后余生全家相拥喜极而泣！",
                "succ_eff": {"health": 15, "happiness": 12, "wealth": -8.0, "rep": 5},
                "fail_feedback": "虽切除病灶但术后出现长期低烧，休养大半年方才复原，耗资巨大。",
                "fail_eff": {"health": -5, "happiness": -12, "wealth": -15.0},
                "tag_succ": "劫后安康",
                "tag_fail": "医海波折",
                "is_key": True
            },
            {
                "text": "遍访名老中医按古方长期调理，搭配每日八段锦太极拳修心",
                "risk_label": "国医调神 · 顺天应命",
                "calc_chance": lambda p: 100,
                "succ_feedback": "脏腑功能逐渐平衡，复查结节未再进展，心态愈发超脱淡定。",
                "succ_eff": {"health": 8, "happiness": 12, "intellect": 4, "wealth": -1.5},
                "tag_succ": "养生真谛",
                "is_key": False
            }
        ]
    },
    # Stage 13
    {
        "period": "桑榆晚景",
        "title": "老年大学诗社还是自驾房车巡游",
        "narrative": "退居二线天高云淡。是购置轻型房车和老伴周游全国名山大川，还是在老年书画社担任社长著书立说？",
        "choices": [
            {
                "text": "添置房车带上老伴顺着国道出发，丈量祖国的三江源与海岸线",
                "risk_label": "壮心不已 · 成功率 80%",
                "calc_chance": lambda p: 80 + (10 if p.health > 50 else -10),
                "succ_feedback": "在戈壁与椰林间留下潇洒足迹，短视频分享收获数十万点赞艳羡！",
                "succ_eff": {"happiness": 20, "health": 5, "rep": 8, "wealth": -4.0},
                "fail_feedback": "高原偏僻路段故障受冻受了虚惊，但携手看遍了最美的星空。",
                "fail_eff": {"happiness": 5, "health": -8, "wealth": -6.0},
                "tag_succ": "银发骑士",
                "tag_fail": "风雨同舟",
                "is_key": False
            },
            {
                "text": "坐镇市老年文联，主编回忆录《小城往事与家族印记》著书立说",
                "risk_label": "文脉流芳 · 雅致从容",
                "calc_chance": lambda p: 100,
                "succ_feedback": "回忆录被市图书馆正式馆藏，留下温润长存的精神遗产。",
                "succ_eff": {"rep": 20, "intellect": 10, "happiness": 12},
                "tag_succ": "文林耆宿",
                "is_key": True
            }
        ]
    },
    # Stage 14
    {
        "period": "古稀沧桑",
        "title": "家族信托安排还是平分助幼孙",
        "narrative": "年逾古稀儿孙绕膝。面对一生的积累：是找专业信托设立家族教育保障基金，还是直接取现贴补晚辈？",
        "choices": [
            {
                "text": "设立规范家族信托基金，锁定教育与医疗兜底，防止败家挥霍",
                "risk_label": "长治久安 · 成功率 90%",
                "calc_chance": lambda p: int(90 + (p.intellect - 50) / 2),
                "succ_feedback": "家族规矩森严有序，即便后辈失利亦有源源不断的兜底保障！",
                "succ_eff": {"rep": 15, "wealth": 5.0, "happiness": 8},
                "fail_feedback": "急于套现的后辈心生怨怼，家宴上少了几分纯粹温情。",
                "fail_eff": {"rep": 5, "happiness": -8, "wealth": 2.0},
                "tag_succ": "门阀根基",
                "tag_fail": "家和微隙",
                "is_key": True
            },
            {
                "text": "看淡钱财，拿出大部分积蓄为晚辈付清首付学费，愿他们轻装前行",
                "risk_label": "慈爱倾囊 · 满堂欢笑",
                "calc_chance": lambda p: 100,
                "succ_feedback": "儿孙感念至深承欢膝下，四世同堂欢声笑语，人间至乐莫过于此。",
                "succ_eff": {"happiness": 18, "rep": 10, "wealth": -15.0},
                "tag_succ": "仁厚长者",
                "is_key": False
            }
        ]
    },
    # Stage 15
    {
        "period": "夕阳辞章",
        "title": "院落斜阳与安详辞世",
        "narrative": "八十余载春秋白驹过隙，院里老槐树落叶纷飞。儿孙在堂屋轻声说话，最后的时刻正悄然到来。",
        "choices": [
            {
                "text": "握住至亲挚爱的双手，留下最后的微笑与平安叮嘱，从容合眼",
                "risk_label": "圆满归宿 · 慈祥辞章",
                "calc_chance": lambda p: 100,
                "succ_feedback": "呼吸渐渐平静。留给世界一世的清白与温厚，在敬意与爱戴中远行。",
                "succ_eff": {"happiness": 20, "rep": 20},
                "tag_succ": "德泽流芳",
                "is_key": True
            },
            {
                "text": "凝望窗外云卷云舒，默念一生的苦难与荣光，问心无愧，静谧而去",
                "risk_label": "天地无言 · 纯净超脱",
                "calc_chance": lambda p: 100,
                "succ_feedback": "生如夏花死如秋叶，坦然走完了凡人真实而波澜壮阔的一生。",
                "succ_eff": {"intellect": 20, "happiness": 20},
                "tag_succ": "大化归真",
                "is_key": True
            }
        ]
    }
]

FUTURE_ALT_STAGES_PY = [
    # Stage 0
    {
        "period": "神经初萌",
        "title": "次级穹顶的人造雨林与全息启蒙",
        "narrative": "城市被恒温穹顶笼罩。社区推行全息视网膜投射自然课，但有微弱视神经疲劳风险。是否参与？",
        "choices": [
            {
                "text": "参加全息高阶认知训练，提前掌握天体物理与量子矩阵启蒙图景",
                "risk_label": "超前启智 · 成功率 80%",
                "calc_chance": lambda p: 80 + (10 if p.intellect > 50 else 0),
                "succ_feedback": "突触活跃度远超同龄人，被评为次级穹顶优等生！",
                "succ_eff": {"intellect": 10, "rep": 6, "health": -2},
                "fail_feedback": "强光照射引起轻度视疲劳，但知识储备依然领先。",
                "fail_eff": {"intellect": 4, "health": -4, "happiness": -4},
                "tag_succ": "全息神童",
                "tag_fail": "视神经微损",
                "is_key": False
            },
            {
                "text": "摘掉头盔，在真实的生态土培农场抓泥鳅采草菇，保持碳基幼年本真",
                "risk_label": "质朴碳基 · 天性安宁",
                "calc_chance": lambda p: 100,
                "succ_feedback": "保留了对真实泥土植物的嗅觉记忆，呼吸机能极优。",
                "succ_eff": {"health": 8, "happiness": 10, "intellect": 2},
                "tag_succ": "泥土芬芳",
                "is_key": False
            }
        ]
    },
    # Stage 1
    {
        "period": "能量与配额",
        "title": "合成藻类牧场还是聚变堆巡检学徒",
        "narrative": "地下藻类农场成为主粮基地，聚变堆招聘少年观察员。是培育发光藻株，还是去聚变堆实习核物理？",
        "choices": [
            {
                "text": "申请进入聚变堆少年观测站，协助监测等离子体约束波动",
                "risk_label": "高能前沿 · 成功率 65%",
                "calc_chance": lambda p: int(65 + (15 if p.luck > 50 else -10) + (p.intellect - 50) / 2),
                "succ_feedback": "成功协助校准一次磁岛扰动，获深空能源署颁发少年银星勋章！",
                "succ_eff": {"intellect": 14, "rep": 10, "wealth": 3.0, "happiness": 5},
                "fail_feedback": "微量辐射传感器警报长鸣，虽无损伤但被勒令休学调养。",
                "fail_eff": {"intellect": 5, "happiness": -10, "health": -6},
                "tag_succ": "聚变雏鹰",
                "tag_fail": "辐射惊悸",
                "is_key": True
            },
            {
                "text": "在地下水耕藻类农场照料发光藻株，享受温和湿润的恒温环境",
                "risk_label": "绿色安宁 · 稳健生存",
                "calc_chance": lambda p: 100,
                "succ_feedback": "收获大批高品质合成蛋白质块，家庭碳税享受一年减免。",
                "succ_eff": {"wealth": 2.5, "health": 6, "happiness": 6},
                "tag_succ": "绿藻清芬",
                "is_key": False
            }
        ]
    },
    # Stage 2
    {
        "period": "矩阵分流",
        "title": "黑客地下暗网协议还是近轨防御志愿役",
        "narrative": "轨道拦截舰队征召士兵，民间暗网流传暗光去中心化协议。是穿戴外骨骼参军，还是黑客地下室破译巨企中继？",
        "choices": [
            {
                "text": "深入暗网钻研零日漏洞，打破寡头企业的算力垄断",
                "risk_label": "黑客漫游 · 成功率 60%",
                "calc_chance": lambda p: int(60 + (p.intellect - 50) / 2 + (10 if p.luck > 50 else -10)),
                "succ_feedback": "成功开源免审查算力分发协议，成为暗网受敬仰的英雄！",
                "succ_eff": {"intellect": 18, "rep": 12, "wealth": 5.0, "happiness": 6},
                "fail_feedback": "遭智脑反向追踪封锁网络权限，自费巨款更换视网膜Mac。",
                "fail_eff": {"wealth": -4.0, "intellect": 6, "happiness": -12, "rep": -6},
                "tag_succ": "矩阵破壁者",
                "tag_fail": "虚拟流亡",
                "is_key": True
            },
            {
                "text": "应征入伍近轨防御志愿役，在失重营锤炼格斗与电磁炮操控",
                "risk_label": "轨道卫士 · 确定硬朗",
                "calc_chance": lambda p: 100,
                "succ_feedback": "结实肌肉与出色前庭神经让你成为优秀战士，享有全额津贴。",
                "succ_eff": {"health": 12, "rep": 8, "wealth": 3.0, "happiness": 4},
                "tag_succ": "轨道尖兵",
                "is_key": True
            }
        ]
    },
    # Stage 3
    {
        "period": "成年生死",
        "title": "深空殖民先驱还是地底避难城工程师",
        "narrative": "火星永久农业穹顶招募拓荒先锋，地底万米热能城扩建。是单程航向红色星球，还是在母星深处建地堡？",
        "choices": [
            {
                "text": "签署拓荒公约登上殖民飞船，向火星红色星球进发",
                "risk_label": "星际拓荒 · 成功率 55%",
                "calc_chance": lambda p: 55 + (10 if p.health > 60 else -10) + (10 if p.luck > 50 else 0),
                "succ_feedback": "安全穿越辐射带降落火星！在风沙中立下第一块领地标石！",
                "succ_eff": {"rep": 22, "intellect": 14, "happiness": 10, "wealth": 10.0},
                "fail_feedback": "休眠舱冷凝液微漏神经反应受损，抵达后转入后勤基地。",
                "fail_eff": {"health": -14, "happiness": -12, "wealth": 2.0, "rep": 6},
                "tag_succ": "火星先锋",
                "tag_fail": "休眠后遗症",
                "is_key": True
            },
            {
                "text": "留在母星地下万米任地热电站主管技师，享稳固高薪与最高避险",
                "risk_label": "地下壁垒 · 固若金汤",
                "calc_chance": lambda p: 100,
                "succ_feedback": "地热能源无尽，过着无风无雨的安稳生活，成全家避风港。",
                "succ_eff": {"wealth": 8.0, "health": 6, "happiness": 8, "rep": 6},
                "tag_succ": "熔岩掌灯人",
                "is_key": True
            }
        ]
    },
    # Stage 4
    {
        "period": "青春与情感",
        "title": "神经共感网络恋情还是独身算力苦修",
        "narrative": "青年流行突触共感恋爱，喜怒哀乐100%互通。是向伴侣敞开全部意识，还是断开接口做独立高冷的思考者？",
        "choices": [
            {
                "text": "接入神经共感协议，与心仪伴侣实现灵魂层面的同频共振",
                "risk_label": "灵魂交融 · 成功率 65%",
                "calc_chance": lambda p: 65 + (10 if p.happiness > 50 else -10),
                "succ_feedback": "在数据海中找到最纯净的灵魂底色，成终身灵境眷侣！",
                "succ_eff": {"happiness": 18, "rep": 6, "health": 4},
                "fail_feedback": "对方隐匿的抑郁情感波冲垮了情绪防火墙，失恋后大病数月。",
                "fail_eff": {"happiness": -20, "health": -10, "intellect": 4},
                "tag_succ": "灵犀共振",
                "tag_fail": "情感过载",
                "is_key": False
            },
            {
                "text": "锁死脑波防火墙保持精神孤立，将所有算力投入科研物理",
                "risk_label": "冷峻独行 · 智性巅峰",
                "calc_chance": lambda p: 100,
                "succ_feedback": "冰冷大脑爆发惊人生产力，以单作者发表多篇重量报告。",
                "succ_eff": {"intellect": 16, "wealth": 4.0, "happiness": 2},
                "tag_succ": "纯粹理性",
                "is_key": False
            }
        ]
    },
    # Stage 5
    {
        "period": "初涉宇宙",
        "title": "太空垃圾打捞船长还是空间站安保主管",
        "narrative": "低轨漂浮数十万件残骸，拾荒者被誉为星轨淘金客。是贷款买二手拖船打捞，还是在联合空间站任警卫？",
        "choices": [
            {
                "text": "贷款购买二手拖船，深入残骸墓地搜寻高价值军用残骸与密钥",
                "risk_label": "轨道拾金 · 成功率 50%",
                "calc_chance": lambda p: int(50 + (15 if p.luck > 50 else -10) + (p.intellect - 50) / 2),
                "succ_feedback": "捞获未损绝密量子发生器！军工天价回购还清船贷！",
                "succ_eff": {"wealth": 28.0, "rep": 12, "happiness": 8, "luck": 6},
                "fail_feedback": "微陨石贯穿推进舱，打捞失败倒赔巨额施救费。",
                "fail_eff": {"wealth": -12.0, "happiness": -14, "health": -8},
                "tag_succ": "星轨掘金客",
                "tag_fail": "太空白卷",
                "is_key": True
            },
            {
                "text": "受聘联合空间站警卫署，负责飞船出入港识别与违禁排查",
                "risk_label": "守望哨卡 · 确定薪饷",
                "calc_chance": lambda p: 100,
                "succ_feedback": "薪酬优厚稳定，目睹各色飞船穿梭，生活规律安全。",
                "succ_eff": {"wealth": 6.0, "rep": 8, "health": 4, "happiness": 6},
                "tag_succ": "星空港警",
                "is_key": False
            }
        ]
    },
    # Stage 6
    {
        "period": "立业与资产",
        "title": "小行星采矿股权还是火星冷凝水专营权",
        "narrative": "小行星稀土丰收，火星冷凝水水源开采权拍卖。是押宝高风险富铂小行星，还是竞标刚需火星水务？",
        "choices": [
            {
                "text": "孤注一掷竞标火星北极冷凝水处理厂，垄断千万穹顶水源",
                "risk_label": "刚需命脉 · 成功率 70%",
                "calc_chance": lambda p: 70 + (10 if p.wealth > 10 else 0) + (10 if p.luck > 50 else -10),
                "succ_feedback": "火星人口暴增水价飞涨，每日进账数万能量点，富甲一方！",
                "succ_eff": {"wealth": 40.0, "rep": 16, "happiness": 10},
                "fail_feedback": "深井含硫严重超标设备腐蚀报废，被迫接受重组吞并。",
                "fail_eff": {"wealth": -15.0, "happiness": -15, "rep": -4},
                "tag_succ": "火星水神",
                "tag_fail": "毒泉折戟",
                "is_key": True
            },
            {
                "text": "将资金分散配置近地轨道物流ETF追求稳健低波动收益",
                "risk_label": "分散防御 · 稳若磐石",
                "calc_chance": lambda p: 100,
                "succ_feedback": "避开探矿破产潮，资产稳步复利增长，现金流源源不绝。",
                "succ_eff": {"wealth": 12.0, "happiness": 8, "rep": 4},
                "tag_succ": "稳健资管",
                "is_key": False
            }
        ]
    },
    # Stage 7
    {
        "period": "繁衍与伦理",
        "title": "定制完美人造子宫婴儿还是自然受孕抗体传承",
        "narrative": "育儿中心提供人造子宫与基因优化套餐；自然受孕保留母体温存。是订购完美试管婴儿，还是十月怀胎自然分娩？",
        "choices": [
            {
                "text": "掏空积蓄选购顶级智力与抗辐射套餐置入人造母舱孕育",
                "risk_label": "新人类契约 · 成功率 80%",
                "calc_chance": lambda p: 80 + (10 if p.intellect > 50 else 0),
                "succ_feedback": "宝宝免疫地表所有已知病毒且数理直觉超凡，轰动社区！",
                "succ_eff": {"intellect": 10, "rep": 12, "happiness": 8, "wealth": -10.0},
                "fail_feedback": "代谢基因拮抗引起轻度内分泌紊乱，需长期注射调谐制剂。",
                "fail_eff": {"wealth": -12.0, "happiness": -12, "health": -4},
                "tag_succ": "智力新星之父",
                "tag_fail": "基因调试苦旅",
                "is_key": True
            },
            {
                "text": "顺应自然规律受孕分娩，让生命在温暖心跳羊水中破晓",
                "risk_label": "碳基温情 · 顺应天道",
                "calc_chance": lambda p: 100,
                "succ_feedback": "在产房握住婴儿温热小手泪水滑落，爱意任何冰冷仪器无法比拟。",
                "succ_eff": {"happiness": 18, "health": 6, "rep": 6},
                "tag_succ": "大地之母",
                "is_key": False
            }
        ]
    },
    # Stage 8
    {
        "period": "意识存续",
        "title": "记忆冷备份保险还是纯生物大脑防护",
        "narrative": "数字永生推出微雕冷备份，遭遇意外三分钟克隆至义体。是每年缴重金保费买复活底牌，还是坚守肉身孤勇？",
        "choices": [
            {
                "text": "每年缴纳重金保费每日快照上传，买下一份死而复生的底牌",
                "risk_label": "数字备胎 · 绝对防备",
                "calc_chance": lambda p: 100,
                "succ_feedback": "直面深空风暴内心毫无恐惧，拥有超越死亡威胁的从容。",
                "succ_eff": {"happiness": 12, "rep": 8, "wealth": -6.0},
                "tag_succ": "云端有底",
                "is_key": True
            },
            {
                "text": "拒绝将隐秘思维托付巨头服务器，加装物理头盔坚守纯净",
                "risk_label": "独立灵魂 · 傲然卓立",
                "calc_chance": lambda p: 100,
                "succ_feedback": "思维从未被算法窃取分析，保留了最崇高的人格独立尊严。",
                "succ_eff": {"intellect": 14, "happiness": 12, "rep": 10},
                "tag_succ": "思维堡垒",
                "is_key": True
            }
        ]
    },
    # Stage 9
    {
        "period": "义体与衰老",
        "title": "全钛合金人工心脏改造还是干细胞再生修复",
        "narrative": "四十余岁出现心肌衰老。是移植磁悬浮全人工核能心脏永动机，还是采用自体干细胞慢慢克隆长出温热心肌？",
        "choices": [
            {
                "text": "移植磁悬浮人工核能心脏，彻底终结心律失常与疲惫感",
                "risk_label": "机械强袭 · 成功率 85%",
                "calc_chance": lambda p: 85 + (10 if p.wealth > 15 else -10),
                "succ_feedback": "输出功率极其平稳，极限气压下心率随心调节，体能重回巅峰！",
                "succ_eff": {"health": 20, "wealth": -8.0, "rep": 8},
                "fail_feedback": "遭遇太阳黑子活动时胸膛微热杂音，需每月去车间微调阀门。",
                "fail_eff": {"health": 4, "wealth": -12.0, "happiness": -10},
                "tag_succ": "钢铁之心",
                "tag_fail": "磁悬浮异响",
                "is_key": True
            },
            {
                "text": "采用温和干细胞原位注射修复，保留原生肉体自然搏动",
                "risk_label": "生物温养 · 纯粹自然",
                "calc_chance": lambda p: 100,
                "succ_feedback": "虽然恢复期长达三月，但胸腔跳动的依然是热乎原装心，踏实安宁。",
                "succ_eff": {"health": 10, "happiness": 12, "wealth": -3.0},
                "tag_succ": "生生不息",
                "is_key": False
            }
        ]
    },
    # Stage 10
    {
        "period": "硅基巨变",
        "title": "强人工智能自治特区还是旧人类自治地下城",
        "narrative": "全球算力超脑接管司法与生产，人类面临站队。是融入超脑统筹的极高效率新世界，还是退居旧人类自由邦？",
        "choices": [
            {
                "text": "接受超脑调度，成为链接人类情感与机器决策的首席共情官",
                "risk_label": "桥梁使者 · 成功率 75%",
                "calc_chance": lambda p: 75 + (15 if p.intellect > 60 else 0),
                "succ_feedback": "在冰冷机械与民意间搭建缓冲带，获得双边世界的崇高礼遇！",
                "succ_eff": {"rep": 24, "wealth": 15.0, "intellect": 12, "happiness": 6},
                "fail_feedback": "人类骂你硅基走狗，机械中枢嫌你效率低下，精神压力倍增。",
                "fail_eff": {"rep": -6, "happiness": -16, "health": -8, "wealth": 4.0},
                "tag_succ": "碳硅桥梁",
                "tag_fail": "夹缝游魂",
                "is_key": True
            },
            {
                "text": "退往拒绝算法统治的自由海岛，靠发电机吉他过自给自足生活",
                "risk_label": "文明遗民 · 诗意栖居",
                "calc_chance": lambda p: 100,
                "succ_feedback": "在真实的篝火旁唱歌写诗，饱尝了作为人的至纯欢愉。",
                "succ_eff": {"happiness": 20, "health": 6, "rep": 10, "wealth": -4.0},
                "tag_succ": "自由遗民",
                "is_key": True
            }
        ]
    },
    # Stage 11
    {
        "period": "代际抉择",
        "title": "孩子的恒星际飞船船票：启程飞向比邻星",
        "narrative": "首艘恒星际巨舰启航飞向半人马座，航程八十年，孩子通过遴选。是变卖财产支持 Ta 飞向星河，还是劝 Ta 留下相守？",
        "choices": [
            {
                "text": "变卖家产为孩子购置顶级休眠舱，目送飞船化作星海微光",
                "risk_label": "星海远嫁 · 成功率 85%",
                "calc_chance": lambda p: 85 + (10 if p.luck > 50 else 0),
                "succ_feedback": "起航全息画面里孩子敬了崇高军礼，人类铭记这一瞬间！",
                "succ_eff": {"rep": 20, "happiness": 12, "intellect": 10, "wealth": -15.0},
                "fail_feedback": "加速突遭星尘冲撞警报，虽化解但让你彻夜痛哭难眠。",
                "fail_eff": {"happiness": -14, "health": -10, "wealth": -15.0, "rep": 8},
                "tag_succ": "星海之父",
                "tag_fail": "牵肠挂肚",
                "is_key": True
            },
            {
                "text": "泪流满面劝孩子留在母星共同生活，享受天伦乐事",
                "risk_label": "人间炊烟 · 暖意融融",
                "calc_chance": lambda p: 100,
                "succ_feedback": "孩子成家生儿育女。无论宇宙多大，家人的餐桌永远最暖。",
                "succ_eff": {"happiness": 16, "health": 6, "rep": 4},
                "tag_succ": "母星天伦",
                "is_key": False
            }
        ]
    },
    # Stage 12
    {
        "period": "天地惊变",
        "title": "近地轨道伽马射线暴余波与地表辐射防御",
        "narrative": "超新星伽马射线扫过太阳系外围，行星护盾激荡。身为资深顾问：是冒辐射去护盾塔手动锁死偏转阀，还是进掩体？",
        "choices": [
            {
                "text": "穿铅合金防辐射服爬上塔顶手动锁死磁通偏转阀力挽狂澜",
                "risk_label": "舍身力挽 · 成功率 80%",
                "calc_chance": lambda p: int(80 + (p.intellect - 50) / 2 + (10 if p.health > 50 else -10)),
                "succ_feedback": "最后三十秒恢复地表护盾！数十万人免遭辐射，全城为你鸣礼炮！",
                "succ_eff": {"rep": 30, "happiness": 16, "intellect": 10, "health": -6},
                "fail_feedback": "抢修成功但手套破损吸收过量射线，术后休养整整半年。",
                "fail_eff": {"rep": 18, "health": -18, "happiness": -8},
                "tag_succ": "护盾英雄",
                "tag_fail": "射线烙痕",
                "is_key": True
            },
            {
                "text": "引导全家退入最深层铅防护掩体，安静等待风暴自然消退",
                "risk_label": "合规避险 · 平安无虞",
                "calc_chance": lambda p: 100,
                "succ_feedback": "掩体厚实，全家平安走出地底，看着重现蔚蓝的天空百感交集。",
                "succ_eff": {"health": 8, "happiness": 10, "intellect": 2},
                "tag_succ": "平安避险",
                "is_key": False
            }
        ]
    },
    # Stage 13
    {
        "period": "暮年归隐",
        "title": "月球静海疗养院还是地表生态园艺",
        "narrative": "月球1/6低重力基地对老年心肺骨骼极好。步入花甲暮年：是移居月球轻盈漫步，还是留在母星修剪古老真实的盆景花卉？",
        "choices": [
            {
                "text": "移居月球静海低重力基地，像鸟一样漫步滑翔摆脱关节磨损",
                "risk_label": "月海飞羽 · 舒适延寿",
                "calc_chance": lambda p: 100,
                "succ_feedback": "身躯重获轻盈自由，骨骼压力骤减，身体机能大幅回春！",
                "succ_eff": {"health": 18, "happiness": 16, "wealth": -6.0},
                "tag_succ": "月海漫步",
                "is_key": False
            },
            {
                "text": "留在母星阳光小镇培植真实花木，给来访孩童讲述深空传奇",
                "risk_label": "落叶归根 · 岁月温润",
                "calc_chance": lambda p: 100,
                "succ_feedback": "花园成社区绿洲，孩子们绕在膝前倾听星海传奇，安详自足。",
                "succ_eff": {"rep": 16, "happiness": 18, "health": 8},
                "tag_succ": "绿意守望",
                "is_key": True
            }
        ]
    },
    # Stage 14
    {
        "period": "记忆回响",
        "title": "神经记忆解密开源还是随身封存",
        "narrative": "世界历史档案馆征集第一人称意识流。面对一生的爱恨：是公开一生脑电波录像供人类查阅，还是封存私人晶体？",
        "choices": [
            {
                "text": "将经历情绪与技术手记无保留上传至人类公共文明记忆库",
                "risk_label": "文明奉献 · 名垂青史",
                "calc_chance": lambda p: 100,
                "succ_feedback": "亿万后辈感知到了你的真实心跳与泪水，成文明不朽拼图！",
                "succ_eff": {"rep": 30, "intellect": 15, "happiness": 15},
                "tag_succ": "文明记忆基石",
                "is_key": True
            },
            {
                "text": "将包含私人秘密的量子晶体锁入合金小盒，沉入湖底留住私密",
                "risk_label": "守密自珍 · 独善其身",
                "calc_chance": lambda p: 100,
                "succ_feedback": "带着神秘与尊严，守住了最纯洁私密的精神自留地。",
                "succ_eff": {"happiness": 18, "intellect": 10},
                "tag_succ": "永恒秘语",
                "is_key": False
            }
        ]
    },
    # Stage 15
    {
        "period": "终幕升维",
        "title": "戴森球光芒与静谧合眼",
        "narrative": "窗外戴森金环环绕恒星熠熠生辉，八十年风雪见证人类迈向星河巅峰。最后的时刻，心跳如渐落晚钟平静庄严。",
        "choices": [
            {
                "text": "拒绝虚幻代码，在挚爱温暖握手中将肉体骨灰撒入深空微风",
                "risk_label": "碳基尊严 · 壮烈归真",
                "calc_chance": lambda p: 100,
                "succ_feedback": "原子源于星尘归于星尘，在恒星风吹拂下飘向宇宙，坦荡无悔！",
                "succ_eff": {"happiness": 25, "rep": 25},
                "tag_succ": "星尘归真",
                "is_key": True
            },
            {
                "text": "闭上双眼，将一生爱与痛化为纯净正弦波融入戴森球共振节奏",
                "risk_label": "恒星脉动 · 融于浩瀚",
                "calc_chance": lambda p: 100,
                "succ_feedback": "整颗太阳的光芒仿佛为你呼吸，化作浩瀚星辰中永不熄灭的光！",
                "succ_eff": {"intellect": 25, "happiness": 25},
                "tag_succ": "光流同辉",
                "is_key": True
            }
        ]
    }
]


PAST_STAGE_POOLS = [
    [PAST_STAGES[i], PAST_ALT_STAGES_PY[i]] for i in range(16)
]

FUTURE_STAGE_POOLS = [
    [FUTURE_STAGES[i], FUTURE_ALT_STAGES_PY[i]] for i in range(16)
]


PAST_RANDOM_EVENTS = [
    {
        "id": "re_lottery",
        "title": "街头彩票微幸",
        "tag": "微幸眷顾",
        "desc": "路过街头报刊亭随手刮了一张体育彩票，竟中了二等小奖！虽非巨资，却在捉襟见肘时添了口温热饭菜。",
        "effect": {"wealth": 1.2, "happiness": 8, "luck": -2}
    },
    {
        "id": "re_illness_scare",
        "title": "深夜急诊惊魂",
        "tag": "病痛突袭",
        "desc": "毫无征兆的急性剧痛让你在深夜被送进急诊。无影灯与消毒水味刺鼻，让你体会到肉体凡胎的极度脆弱。",
        "effect": {"health": -10, "wealth": -0.8, "happiness": -5, "luck": 0}
    },
    {
        "id": "re_old_mentor",
        "title": "偶遇退休老法师点拨",
        "tag": "良师开窍",
        "desc": "在旧书摊旁与一位隐退老工程师攀谈，对方一席肺腑之言醍醐灌顶，让你瞬间参透了行业底层门道。",
        "effect": {"intellect": 10, "happiness": 5, "luck": 4}
    },
    {
        "id": "re_market_slump",
        "title": "小本买卖突遭寒流",
        "tag": "市井波折",
        "desc": "跟风囤积的一批小百货遭遇退潮，不得不折价半月方才甩清。虽然折了本钱，但交足了接地气的学费。",
        "effect": {"wealth": -2.0, "happiness": -6, "intellect": 4}
    },
    {
        "id": "re_neighbor_kindness",
        "title": "邻里风雪送炭",
        "tag": "人间烟火",
        "desc": "遭遇困顿水暖爆裂之时，对门邻居送来了热腾腾的饭菜与应急工具，平淡的人间温情让你眼眶发热。",
        "effect": {"happiness": 10, "health": 4, "rep": 5}
    },
    {
        "id": "re_peer_envy",
        "title": "流言蜚语中伤",
        "tag": "人情冷暖",
        "desc": "略有小成招来周围人的暗中忌恨，甚至有捕风捉影的闲话传到了单位。你学会了收敛锋芒保持定力。",
        "effect": {"happiness": -8, "rep": -4, "intellect": 5}
    }
]

FUTURE_RANDOM_EVENTS = [
    {
        "id": "re_quantum_drop",
        "title": "近地暗网算力空投",
        "tag": "开源馈赠",
        "desc": "暗网分布式节点突发零日算力空投，你的私人量子钱包意外截获了一笔匿名加密配额！",
        "effect": {"wealth": 3.0, "happiness": 8, "luck": -2}
    },
    {
        "id": "re_cyber_virus",
        "title": "突触神经木马侵袭",
        "tag": "赛博劫波",
        "desc": "在公共星网信道感染了定向神经木马，视网膜持续产生剧烈色彩噪点，自费刷新固件心惊肉跳。",
        "effect": {"health": -8, "wealth": -1.5, "happiness": -8}
    },
    {
        "id": "re_solar_surge",
        "title": "微型地磁耀斑脉冲",
        "tag": "天体微澜",
        "desc": "太阳微耀斑穿透了电离层次级护盾，家庭全息投影短路冒烟，在黑暗中全家点燃了久违的古董蜡烛。",
        "effect": {"happiness": 6, "health": -2, "intellect": 4}
    },
    {
        "id": "re_bionic_recall",
        "title": "仿生零件召回公函",
        "tag": "巨企维权",
        "desc": "多年前植入的微型代谢滤网被巨企以'安全隐患'召回，跑了一整天流程获得一笔微薄补偿金。",
        "effect": {"wealth": 1.5, "happiness": -4, "rep": 3}
    },
    {
        "id": "re_ai_insight",
        "title": "智脑异常逻辑自省",
        "tag": "超维顿悟",
        "desc": "偶遇一次中央智脑公共调试日志泄露，一段纯粹的哲学正弦波令你陷入整夜深思，看淡了功名。",
        "effect": {"intellect": 12, "happiness": 8, "luck": 3}
    },
    {
        "id": "re_carbon_fine",
        "title": "超额碳排放罚单",
        "tag": "配额红线",
        "desc": "因违规在室内使用老旧电阻炉烹调真实肉食，被社区无人机检测开出二级碳排放惩戒罚单。",
        "effect": {"wealth": -2.5, "happiness": -8, "rep": -3}
    }
]

def main():
    clear_screen()
    print(f"{Color.GOLD}{'='*68}{Color.RESET}")
    print(f"{Color.BOLD}{Color.GOLD}    浮 生 录  ·  过 去 与 未 来 浪 潮 模 拟 器 (全 卷 纪 传 版){Color.RESET}")
    print(f"{Color.GOLD}{'='*68}{Color.RESET}")
    slow_print(" 一个人的命运，既要靠自我的奋斗，亦要看历史的进程。\n 时代洪流呼啸而过，偶发的幸与不幸如影随形。细水长流，步步为营，落子无悔。\n", 0.012)

    # 纪元模式选择
    print(f"{Color.CYAN}【 请选择入世时代纪元 】{Color.RESET}")
    print(f"  {Color.GRAY}文明长河自公元前1600年奔涌至公元2150年，皆可投胎；一生将随年代推移自动切换时代背景。{Color.RESET}")
    for idx_e, e in enumerate(EPOCHS, 1):
        print(f"  {idx_e}. {e['icon']} {e['name']} ({e['sub_title']}) · {e['badge']}")
    print(f"  {len(EPOCHS) + 1}. 完全随机天命 (由命运的骰子决定你降生于哪一个大时代)")

    epoch_mode = EPOCHS[3]["id"]
    while True:
        e_choice = input(f"\n{Color.GOLD}请选择纪元模式 [1-{len(EPOCHS) + 1}, 默认 {len(EPOCHS) + 1}]: {Color.RESET}").strip()
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
        b_year, b_month, origin, trait = generate_random_destiny(epoch_mode)
        era_title, era_desc = resolve_era(b_year)

        print(f"\n{Color.CYAN}【 🎲 先天命格卡 · 随机摇号投胎 】{Color.RESET}")
        print(f"  纪元属性: {Color.BOLD}{cfg_now['icon']} {cfg_now['name']} ({cfg_now['sub_title']}){Color.RESET}")
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
        name = pick_epoch_name(epoch_mode)

    player = Player(name, epoch_mode, b_year, origin, trait)
    player.birth_month = b_month
    total_stages = 16
    timeline = generate_random_timeline()

    slow_print(f"\n命运之轮缓缓启动，{player.name} 踏入了 {format_year_month(player.birth_year, getattr(player, 'birth_month', 1))} 的人间...\n", 0.02)
    time.sleep(0.05)

    # 游戏主轮次
    for idx_stage in range(1, total_stages + 1):
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
    print(f" 主角姓名: {Color.BOLD}{player.name}{Color.RESET} ({format_year_month(player.birth_year, _bmonth)} - {format_year_only(end_year)} · 享年 {player.age} 岁)")
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

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n岁月如风，中途隐退。")
