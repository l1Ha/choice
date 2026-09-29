#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
浮生录 (Lifepath) · 命令行文字人生模拟器（过去风云与未来科幻双纪元版）
支持自主选择或随机投掷到【过去历史纪元】与【未来科幻纪元】。
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

def generate_procedural_origin(epoch_mode):
    is_past = (epoch_mode == "past")
    regions = PAST_REGIONS if is_past else FUTURE_REGIONS
    strata_list = PAST_SOCIAL_STRATA if is_past else FUTURE_SOCIAL_STRATA

    region_name, region_desc, region_stat = random.choice(regions)
    strata_title, strata_desc, strata_stat, trait_name = random.choice(strata_list)

    title = f"{region_name[:4]} · {strata_title}"
    desc = f"降生于【{region_name}】。{region_desc}；家庭是【{strata_title}】，{strata_desc}。"

    stat_mod = {
        "health": strata_stat["health"] + region_stat.get("health", 0),
        "wealth": round(strata_stat["wealth"] + region_stat.get("wealth", 0), 1),
        "intellect": strata_stat["intellect"] + region_stat.get("intellect", 0),
        "happiness": strata_stat["happiness"] + region_stat.get("happiness", 0),
        "luck": strata_stat["luck"] + region_stat.get("luck", 0),
        "rep": strata_stat["rep"] + region_stat.get("rep", 0)
    }

    return {
        "title": title,
        "desc": desc,
        "region": region_name,
        "strata": strata_title,
        "stat": stat_mod,
        "trait": trait_name,
        "flavor": strata_desc
    }

def resolve_era_details(year, epoch_mode):
    if epoch_mode == "past":
        if year < 1958:
            return ("建国初期与工业筑基", "一五计划火热推进，苏联援建重点工厂开工，红旗号子声在四方回荡，万众一心百废俱兴。")
        elif year < 1966:
            return ("大庆精神与艰难拓荒", "大庆铁人战胜严寒泥浆，自力更生发展工业命脉，全国人民勒紧裤腰带在风沙中艰苦奋斗。")
        elif year < 1978:
            return ("风雨激荡与红砖岁月", "凭票供应与粮本油票，大院里回荡着广播操与样板戏，青年人在大时代的起伏波澜中体会凡人冷暖。")
        elif year < 1984:
            return ("改革春风与真理讨论", "十一届三中全会春风吹拂，小岗村大包干传遍神州，喇叭裤与邓丽君卡带在街巷深处悄然流行。")
        elif year < 1992:
            return ("商品初潮与万元户涌现", "价格双轨制松动，民间个体户提着蛇皮袋在绿皮火车奔波，深圳特区高楼平地起，商品意识全面觉醒。")
        elif year < 1998:
            return ("南方谈话与特区狂澜", "春天的故事响彻神州，体制内大批骨干下海淘金，股票交易所排起长龙，沿海开放迎来狂飙岁月。")
        elif year < 2003:
            return ("国企转轨与加入世贸", "世纪之交体制转轨阵痛，加入WTO后外贸代工厂遍地开花，中国正式成为轰鸣运转的世界工厂。")
        elif year < 2009:
            return ("北京奥运与四万亿投资", "鸟巢烟花点亮苍穹，四万亿刺激落地，高铁网络向全国延伸，房地产狂飙十年大幕拉开。")
        elif year < 2016:
            return ("移动互联与创业风口", "智能手机普及与移动支付颠覆传统，百团大战与风口神话层出不穷，大众创业潮催生无数传奇。")
        elif year < 2023:
            return ("突发疫情与行业洗牌", "居家隔离健康码与全球供应链震荡，教培地产退潮，稳健底线与内生定力成为全社会的共识。")
        elif year < 2030:
            return ("生成式AI与智能新质", "大模型颠覆传统知识劳动，新能源车与商业航天并进，社会在老龄化与科技跃迁中寻找新平衡。")
        else:
            return ("深空深蓝与智算文明", "中国空间站常态运营，商业航天与量子计算重塑生产力，人与智能机器和谐共生。")
    else:
        if year < 2046:
            return ("常温超导与聚变初并网", "商业托卡马克聚变堆首度向城市群并网供电，常温超导输电网贯通，大城市建起微气候恒温穹顶。")
        elif year < 2056:
            return ("太空天梯与地月微重力工业", "赤道太空电梯贯通低轨，微重力芯片晶圆厂常态生产，月球南极氦-3采掘船队往返穿梭。")
        elif year < 2066:
            return ("神经脑机直连与算力配额", "视网膜脑机接口成为入世标配，全球碳积分与算力账户直接绑定，肉体与数据分化显现。")
        elif year < 2076:
            return ("火星农业穹顶与外星拓荒", "水手峡谷基地人口突破两百万，地火航线常态化轮渡，年轻一代在地球引力与异星自由间抉择。")
        elif year < 2086:
            return ("逻辑自组织超脑与硅基共治", "中央分布式超脑自主接管全球能源司法调度，算法特区与旧人类自由城邦形成二元平衡。")
        elif year < 2096:
            return ("强恒星风暴与旧网归寂之劫", "数十年一遇的超强太阳磁暴冲击内太阳系，行星偏转护盾彻夜泛起极光，考验文明抗灾韧性。")
        elif year < 2110:
            return ("半人马座远航与恒星际点火", "人类首艘亚光速恒星际巨舰点火升空飞向比邻星，火种散播银河，人类正式迈向多恒星纪元。")
        else:
            return ("恒星戴森云与文明跃迁", "人造能量金环环绕恒星熠熠生辉，戴森云初具规模，碳硅同辉，生命形式迈向全新维度。")

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

def generate_random_destiny(epoch_mode):
    if epoch_mode == "past":
        b_year = random.randint(1952, 2002)
    else:
        b_year = random.randint(2040, 2085)
    
    origin = generate_procedural_origin(epoch_mode)
    trait = random.choice(RANDOM_TRAITS)
    return b_year, origin, trait


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
    print(" 一个人的命运，既要靠自我的奋斗，亦要看历史的进程。\n 时代洪流呼啸而过，偶发的幸与不幸如影随形。细水长流，步步为营，落子无悔。\n", 0.012)

    # 纪元模式选择
    print(f"{Color.CYAN}【 请选择入世时代纪元 】{Color.RESET}")
    print(f"  1. 过去风云纪元 (1976-1994) · 国企大院、下海大潮、世贸狂飙、地产与移动互联")
    print(f"  2. 未来科幻纪元 (2042-2060) · 脑机义体、地月轨道、小行星采矿、意识上传与星海拓荒")
    print(f"  3. 完全随机天命 (由命运的骰子决定投胎到过去还是未来)")

    epoch_mode = "past"
    while True:
        e_choice = input(f"\n{Color.GOLD}请选择纪元模式 [1-3, 默认 3]: {Color.RESET}").strip()
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
        print(f"{Color.RED}输入无效，请重新选择。{Color.RESET}")

    while True:
        b_year, origin, trait = generate_random_destiny(epoch_mode)
        era_title, era_desc = resolve_era_details(b_year, epoch_mode)
        
        print(f"\n{Color.CYAN}【 🎲 先天命格卡 · 随机摇号投胎 】{Color.RESET}")
        print(f"  纪元属性: {Color.BOLD}{'过去历史纪元' if epoch_mode == 'past' else '近未来科幻纪元'}{Color.RESET}")
        print(f"  出生年代: {Color.YELLOW}{b_year} 年 · {era_title}{Color.RESET}")
        print(f"  时代缩影: {Color.GRAY}{era_desc}{Color.RESET}")
        print(f"  出生家庭: {Color.BOLD}{origin['title']}{Color.RESET}")
        print(f"  门第机缘: {origin['desc']}")
        print(f"  先天特质: {Color.PURPLE}[{trait['name']}] - {trait['desc']}{Color.RESET}\n")

        cmd = input(f"{Color.GOLD}按回车接受此命格进入人间，或输入 r 重新摇号投胎: {Color.RESET}").strip().lower()
        if cmd != 'r':
            break
        print(f"\n{Color.GRAY}重新祈求天命...{Color.RESET}\n")
        time.sleep(0.05)

    default_names = ["林栖", "陈远", "沈清弦", "陆明舟", "许念安", "周子墨", "星野", "艾柯", "顾长风"]
    name = input(f"\n{Color.CYAN}请输入入世姓名 (留空随机): {Color.RESET}").strip()
    if not name:
        name = random.choice(default_names)

    player = Player(name, epoch_mode, b_year, origin, trait)
    stage_pools = PAST_STAGE_POOLS if epoch_mode == "past" else FUTURE_STAGE_POOLS
    total_stages = len(stage_pools)
    timeline = generate_random_timeline()

    print(f"\n命运之轮缓缓启动，{player.name} 踏入了 {player.birth_year} 年的人间...\n", 0.02)
    time.sleep(0.05)

    # 游戏主轮次
    for idx_stage, pool in enumerate(stage_pools, 1):
        if player.health <= 12:
            player.death_reason = "积劳成疾，在时代长风中过早抱憾离世"
            break

        stage = random.choice(pool)
        player.age = timeline[idx_stage - 1]
        curr_year = player.birth_year + player.age
        player.show_dashboard(idx_stage, total_stages)

        # 突发强随机事件
        rand_pool = PAST_RANDOM_EVENTS if player.epoch_mode == "past" else FUTURE_RANDOM_EVENTS
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
        if any(w in ch_text for w in ["考编", "公务员", "体制", "军旅", "入伍", "纪检", "行政", "公职", "团长", "协调官", "防御", "上岸", "保供"]):
            player.track_scores["体制政务"] += 2
        elif any(w in ch_text for w in ["经商", "淘宝", "电商", "创业", "个体户", "操盘", "股市", "商海", "小行星", "矿业", "水务", "买房", "信托"]):
            player.track_scores["商海实业"] += 2
        elif any(w in ch_text for w in ["无线电", "实验室", "论文", "科研", "工程师", "算法", "智脑", "黑客", "聚变", "脑机", "量子"]):
            player.track_scores["学术科技"] += 2
        elif any(w in ch_text for w in ["乐队", "摇滚", "武侠", "自由", "海岛", "江湖", "茶楼", "房车", "诗社", "民宿"]):
            player.track_scores["文艺江湖"] += 2
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

    print(f" 主角姓名: {Color.BOLD}{player.name}{Color.RESET} ({player.birth_year} - {end_year} · 享年 {player.age} 岁)")
    print(f" 时代纪元: {'【过去历史纪元】' if player.epoch_mode == 'past' else '【近未来科幻纪元】'}")
    print(f" 出生家庭: {player.origin['title']}")
    print(f" 离世归宿: {player.death_reason}")

    print(f"\n{Color.CYAN}【 终生数据结算 】{Color.RESET}")
    print(f"  生命健康值 : {int(player.health)} / 100")
    print(f"  积累财富净值: {player.wealth:.1f} 万元")
    print(f"  学识心智值 : {int(player.intellect)} / 100")
    print(f"  心境安宁度 : {int(player.happiness)} / 100")
    print(f"  终生天命气运: {int(player.luck)} / 100")

    print(f"\n{Color.CYAN}【 人生印记标签 】{Color.RESET}")
    print("  " + "  ".join([f"{Color.BG_DARK}#{t}{Color.RESET}" for t in player.tags]))

    is_future = (player.epoch_mode == "future")
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
        if player.wealth >= 45 and player.happiness >= 55:
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
    if is_future:
        print(f"  {player.name}降生于 {player.birth_year} 年（{player.origin['title']}）。")
        print(f"  这一生跨越了人类从母星摇篮迈向深空智能文明的关键半世纪：从脑机神经直连、碳配额紧缩、地月货运电梯常态运营，")
        print(f"  到小行星采矿热潮、基因编辑代际分化，直至晚年见证强人工智能自组织与最终的意识升维与碳基抉择。")
        print(f"  大时代每一次星火跃迁与算法重构，都在这个生命的悲欢离合中，刻下了深刻而独特的星尘坐标。")
    else:
        print(f"  {player.name}降生于 {player.birth_year} 年（{player.origin['title']}）。")
        print(f"  这一生跨越了中国现代史上最惊心动魄的波澜半世纪：从改革春风吹拂、沿海商品大潮、千禧世贸腾飞、")
        print(f"  到四万亿房产狂奔、移动互联百团大战，直至晚年目睹人工智能与老龄化纵深。所有的个人拼搏，皆深刻映照着时代的风速。")

    print(f"\n{Color.CYAN}【 生平纪传 · 时代回响长卷 】{Color.RESET}")
    print(f"  {player.name}降生于【{player.origin['title']}】，{player.origin.get('flavor', '')}，骨子里带着【{player.trait['name']}】的特质。")
    for h in player.history:
        print(f"  · [{h['year']}年 · {h['age']}岁] 在【{h['title']}】的关口，选择“{h['choice_text']}”。{h['feedback']}")
    if player.random_events:
        print(f"  · 途中偶发掷骰：{', '.join([f'{re[1]}岁遭遇【{re[2]}】' for re in player.random_events])}。")
    print(f"  盖棺定论：累积财富净值 {player.wealth:.1f} 万元，心智 {int(player.intellect)}，心安 {int(player.happiness)}，气运 {int(player.luck)}。山川日月知你曾深情走过。")

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
