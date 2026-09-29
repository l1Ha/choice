#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
浮生录 (Lifepath) · 命令行文字人生模拟器（时代风云与随机天命版）
通过一次次不可逆的真实抉择、时代浪潮沉浮与命运掷骰，走完大时代下的一生。
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

def slow_print(text, delay=0.015, newline=True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        print()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# 时代大浪潮背景
ERA_TIMELINE = {
    1975: ("文革晚期与初苏", "物质匮乏凭票供应，广播里播放样板戏，民间暗潮涌动，期盼春天的微光。"),
    1982: ("改革春风与倒爷潮", "包产到户在全国推行，沿海小商品市场萌动，喇叭裤与流行乐在青年中风靡。"),
    1988: ("物价闯关与商海涌动", "价格双轨制松动，民间现抢购狂潮，第一批敢下海倒货者开始斩获第一桶金。"),
    1992: ("南方谈话与全民下海", "春天的故事响彻神州，大批体制内干部与知识分子下海经商，海南与特区迎淘金潮。"),
    1998: ("国企改革与下岗大潮", "体制重组阵痛蔓延，千百万工人直面下岗转型，大街小巷回荡着'重头再来'的歌声。"),
    2001: ("加入WTO与世界工厂", "中国正式入世，沿海外贸如火如荼，农民工进城与中国制造出海掀起巨澜。"),
    2008: ("北京奥运与四万亿投资", "鸟巢烟花璀璨，四万亿基建落地，高铁全面延伸，房地产迎来狂飙十年。"),
    2014: ("移动互联与大众创业", "智能手机全面普及，移动支付改变日常，'大众创业、万众创新'催生风口狂热。"),
    2020: ("突发疫情与行业洗牌", "教培、地产、大厂相继迎收缩调整，考公热潮席卷，社会回归安全与稳健。"),
    2026: ("AI时代与老龄化纵深", "人工智能接管日常智力工作，老龄化加速，面对不确定性的未来，人们探索心安之道。")
}

# 随机家庭底色池
RANDOM_ORIGINS = [
    {
        "title": "三线内陆国企职工家庭",
        "desc": "父母在大型国营机械厂当技术工，住在大院。看似安稳平实，实则深藏体制改革巨澜。",
        "stat": {"health": 90, "wealth": 2.5, "intellect": 52, "happiness": 65, "luck": 50, "rep": 45},
        "trait": "大院情怀"
    },
    {
        "title": "黄土丘陵偏远农村",
        "desc": "祖辈世代躬耕于贫瘠农田。父母起早贪黑，唯一执念就是供你'读书跳出农门'。",
        "stat": {"health": 94, "wealth": 0.3, "intellect": 48, "happiness": 55, "luck": 52, "rep": 35},
        "trait": "野草劲骨"
    },
    {
        "title": "省城中学/大学教师家庭",
        "desc": "家里有一整面墙的藏书与学术期刊，家教严谨体面，重视修养但期待甚高。",
        "stat": {"health": 84, "wealth": 6.0, "intellect: ": 65, "happiness": 58, "luck": 54, "rep": 55},
        "trait": "书香灵慧"
    },
    {
        "title": "沿海敢闯个体户",
        "desc": "父母最早一批摆摊贩卖布匹电器，常年火车奔波，从小在算盘和现金堆中长大。",
        "stat": {"health": 88, "wealth": 12.0, "intellect": 54, "happiness": 60, "luck": 58, "rep": 48},
        "trait": "市井嗅觉"
    },
    {
        "title": "单亲下岗缝纫女工家庭",
        "desc": "母亲一个人在路边支缝纫机踩踏板养活全家，很小就知道生活毫无退路。",
        "stat": {"health": 86, "wealth": 0.8, "intellect": 53, "happiness": 50, "luck": 45, "rep": 38},
        "trait": "早慧逆境"
    }
]

# 先天词条
RANDOM_TRAITS = [
    {"name": "天生神力", "desc": "体魄异常健硕，抗病力强", "mod": {"health": 8}},
    {"name": "灵光乍现", "desc": "悟性出众，学东西极快", "mod": {"intellect": 8}},
    {"name": "福泽深厚", "desc": "常能逢凶化吉，气运加身", "mod": {"luck": 12}},
    {"name": "钝感心安", "desc": "神经大条，不易被焦虑击垮", "mod": {"happiness": 10}},
    {"name": "商海通达", "desc": "自小对数字敏感，带微薄本金", "mod": {"wealth": 3.0}}
]

# 强随机偶发突发事件
RANDOM_EVENTS = [
    {
        "title": "街头彩票小奖",
        "desc": "路过街头报亭顺手刮了张福利彩票，竟中了二等奖！虽非巨资，却解了燃眉之急。",
        "effect": {"wealth": 1.5, "happiness": 8, "luck": -2}
    },
    {
        "title": "深夜急性腹痛入院",
        "desc": "突发急性阑尾炎被救护车连夜拉走，冰冷手术台上深刻体会到健康的脆弱与可贵。",
        "effect": {"health": -10, "wealth": -0.8, "happiness": -6, "luck": 0}
    },
    {
        "title": "同窗借贷失联",
        "desc": "昔日老友声称周转困难向你借走一笔钱，数月后电话空号微信拉黑，体会人间冷暖。",
        "effect": {"wealth": -2.0, "happiness": -9, "intellect": 4, "luck": -2}
    },
    {
        "title": "贵人偶然提携",
        "desc": "偶然的业务相遇，一位德高望重的业内长辈对你的真诚大加赞许，指点迷津并赠予引荐。",
        "effect": {"intellect": 8, "happiness": 6, "rep": 10, "luck": 5}
    }
]

class Player:
    def __init__(self, name, birth_year, origin, trait):
        self.name = name
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

    def show_dashboard(self):
        curr_year = self.birth_year + self.age
        # 匹配时代
        era_keys = sorted(ERA_TIMELINE.keys(), reverse=True)
        era_title, _ = ERA_TIMELINE.get(self.birth_year, ("时代", ""))
        for y in era_keys:
            if curr_year >= y:
                era_title, _ = ERA_TIMELINE[y]
                break
                
        w_str = f"{self.wealth:.1f}万" if self.wealth >= 0 else f"负债{abs(self.wealth):.1f}万"
        print(f"\n{Color.BG_DARK}{Color.GOLD} 📅 {curr_year}年 · {self.age}岁 ({era_title}) | 👤 {self.name} | 健康: {int(self.health)} | 财富: {w_str} | 心智: {int(self.intellect)} | 气运: {int(self.luck)} {Color.RESET}\n")

# 时代剧本大关卡（带胜率检定与掷骰）
EPOCH_STAGES = [
    {
        "age_rel": 9,
        "title": "工厂汽笛与商品潮涌",
        "narrative": "时代正急速转向，小商贩与承包户遍地开花。\n父母在犹豫是否打破铁饭碗、承包小门面或停薪留职，家庭面临关键抉择。",
        "choices": [
            {
                "text": "力劝父母：'下海闯荡，抓住商品消费爆发的时代风口！'",
                "risk_label": "高风险 · 时代博弈",
                "calc_chance": lambda p: 50 + (15 if p.luck > 50 else -10),
                "succ_feedback": "【掷骰大胜！】父母承包的门店踩中消费热潮，家庭资产暴翻数倍！",
                "fail_feedback": "【掷骰失利】因经验不足遭遇货源骗局，积蓄赔光，父母艰难打零工还债。",
                "succ_eff": {"wealth": 12.0, "happiness": 8, "intellect": 5, "luck": 5},
                "fail_eff": {"wealth": -5.0, "happiness": -12, "intellect": 3, "luck": -5},
                "tag_succ": "踩中风口",
                "tag_fail": "早尝败绩",
                "is_key": True
            },
            {
                "text": "劝导父母求稳为上，保住铁饭碗与医保，安稳供孩子读书",
                "risk_label": "保守求稳 · 确定回报",
                "calc_chance": lambda p: 100,
                "succ_feedback": "家庭虽无暴富，但清贫安稳，每天有热汤热饭，你在宁静中完成童年学业。",
                "succ_eff": {"wealth": 1.5, "happiness": 5, "intellect": 3, "luck": 0},
                "tag_succ": "守正持重",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 15,
        "title": "中考分流与网吧浪潮",
        "narrative": "互联网正以野火之势蔓延，街头网吧与网游大火。\n中考只有一半人能升入高中，班主任敲着黑板严厉训诫。",
        "choices": [
            {
                "text": "断绝诱惑，每天题海苦读到凌晨两点，誓要考入省重点高中",
                "risk_label": "苦行应试 · 成功率80%",
                "calc_chance": lambda p: 80 + int((p.intellect - 50) / 2),
                "succ_feedback": "【应试拔筹】以全区前30名优异成绩考入省重点中学！全家扬眉吐气。",
                "fail_feedback": "【临场意外】考场突发急性胃痛发挥失常，压线进入普通中学，尝到无常滋味。",
                "succ_eff": {"intellect": 12, "happiness": 6, "health": -4, "rep": 10},
                "fail_eff": {"intellect": 6, "happiness": -8, "health": -6, "rep": 0},
                "tag_succ": "做题精英",
                "tag_fail": "考场蹉跎",
                "is_key": True
            },
            {
                "text": "对死记硬背厌烦，自学编程制作个人网站，视代码为未来钥匙",
                "risk_label": "异类先锋 · 成功率60%",
                "calc_chance": lambda p: 60 + int((p.intellect - 50) / 2) + (10 if p.luck > 55 else 0),
                "succ_feedback": "【极客奇迹】个人网站爆火，获计算机特长加分保送重点班，踏上技术快车道！",
                "fail_feedback": "【落选歧路】学业彻底荒废，未能考上普通高中，只得入读职专，饱受白眼。",
                "succ_eff": {"intellect": 16, "wealth": 3.0, "happiness": 10, "luck": 5},
                "fail_eff": {"intellect": 4, "wealth": -1.0, "happiness": -12, "rep": -6},
                "tag_succ": "极客先锋",
                "tag_fail": "歧途少年",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 18,
        "title": "入世浪潮与高考志愿博弈",
        "narrative": "入世与全球化全面铺开，外贸、金融、软件成为炙手可热的词汇。\n高考成绩出炉，两张截然不同的人生轨迹摆在眼前。",
        "choices": [
            {
                "text": "豪赌时代热门：报考沿海名校的'计算机科学'或'国际外贸金融'",
                "risk_label": "风口浪尖 · 潜力巨大",
                "calc_chance": lambda p: 70 + (10 if p.luck > 50 else -5),
                "succ_feedback": "【乘风而上】完美踩中中国互联网与全球化黄金二十年通道，眼界彻底跃升！",
                "fail_feedback": "【周期调整】扩招与泡沫叠加，毕业时面临惨烈内卷，在逼仄合租房中苦苦挣扎。",
                "succ_eff": {"intellect": 15, "wealth": 6.0, "happiness": 8, "rep": 10},
                "fail_eff": {"intellect": 8, "wealth": -2.0, "happiness": -6, "rep": 2},
                "tag_succ": "时代弄潮儿",
                "tag_fail": "风口折翼",
                "is_key": True
            },
            {
                "text": "选择本地公费师范或军警医校，毕业即享编制，安稳笃定",
                "risk_label": "安稳航道 · 绝对稳固",
                "calc_chance": lambda p: 100,
                "succ_feedback": "父母长舒口气。你免除学费并分配编制，冷眼看着外界商海起伏。",
                "succ_eff": {"intellect": 7, "wealth": 2.0, "happiness": 8, "rep": 8},
                "tag_succ": "体制坚盾",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 25,
        "title": "四万亿与创业/职场大博弈",
        "narrative": "大城市房价躁动，四万亿基建落地，到处都是狂飙的野心与财富神话。\n你手头有了点积蓄，站在了打工沉淀还是下海创业的关口。",
        "choices": [
            {
                "text": "辞职合伙创办移动互联网电商工作室，生死一线搏高倍回报",
                "risk_label": "创业豪赌 · 成功率45%",
                "calc_chance": lambda p: 45 + int((p.intellect - 50) / 2) + (15 if p.luck > 50 else -10),
                "succ_feedback": "【创业大成】产品火爆获得数百万风投资金，年纪轻轻实现资产跃升！",
                "fail_feedback": "【创业爆雷】合伙人理念不合撤资跑路，欠下债务，靠吃泡面借钱咬牙硬撑。",
                "succ_eff": {"wealth": 35.0, "intellect": 14, "happiness": 10, "health": -8, "rep": 15},
                "fail_eff": {"wealth": -16.0, "intellect": 8, "happiness": -15, "health": -10, "rep": -4},
                "tag_succ": "初创奇迹",
                "tag_fail": "创业受挫",
                "is_key": True
            },
            {
                "text": "进入头部大厂或国企稳步晋升，咬牙在房价起飞前夕付清首付",
                "risk_label": "稳健筑底 · 资产增值",
                "calc_chance": lambda p: 100,
                "succ_feedback": "【资产沉淀】抓住房价上涨前的最后一班车，房子数年后增值，成为坚实底气。",
                "succ_eff": {"wealth": 20.0, "happiness": 6, "health": 2, "rep": 8},
                "tag_succ": "稳健置业",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 34,
        "title": "杠杆狂欢下的资产抉择",
        "narrative": "理财借贷狂欢，学区房被炒至天价。家庭面临资产配置与杠杆的终极考验。",
        "choices": [
            {
                "text": "掏空两代人钱包并抵押贷款，高位上车千万核心学区房",
                "risk_label": "高杠杆搏击 · 成功率50%",
                "calc_chance": lambda p: 50 + (10 if p.luck > 50 else -10),
                "succ_feedback": "【顺风获利】精准抢在政策封门前锁定学位与资产暴涨，世俗眼里的赢家。",
                "fail_feedback": "【高位接盘】买在历史最高点，随后房价腰斩断崖，巨额月供成沉重绞索。",
                "succ_eff": {"wealth": 28.0, "happiness": -4, "rep": 12},
                "fail_eff": {"wealth": -32.0, "happiness": -20, "health": -10, "rep": -5},
                "tag_succ": "杠杆得胜",
                "tag_fail": "高位套牢",
                "is_key": True
            },
            {
                "text": "保持绝对清醒，拒绝高杠杆，配置大额存单与自身健康，从容生活",
                "risk_label": "守拙避险 · 绝对安全",
                "calc_chance": lambda p: 100,
                "succ_feedback": "亲友笑你胆小，但在随后暴雷潮与去产能中，唯有你现金流充沛从容。",
                "succ_eff": {"wealth": 10.0, "happiness": 12, "health": 6, "rep": 6},
                "tag_succ": "现金为王",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 43,
        "title": "降本增效与中年夹缝",
        "narrative": "经济周期遭遇调整，大厂优化裁员潮来袭。父母老人医药费与孩子教育开销如大山。",
        "choices": [
            {
                "text": "拿走N+1赔偿，利用多年深厚行业经验转行做独立顾问/出海",
                "risk_label": "逆境突围 · 成功率55%",
                "calc_chance": lambda p: 55 + int((p.intellect - 50) / 2) + (10 if p.luck > 50 else -10),
                "succ_feedback": "【逆风翻盘】凭借口碑与硬核能力，首年咨询费远超以往总包，赢得时间自由！",
                "fail_feedback": "【市场惨淡】赛道极度内卷接单艰难，消耗存款补贴家用，失眠白发丛生。",
                "succ_eff": {"wealth": 22.0, "happiness": 15, "health": 2, "rep": 15},
                "fail_eff": {"wealth": -12.0, "happiness": -16, "health": -8, "rep": -2},
                "tag_succ": "绝处逢生",
                "tag_fail": "中年窘迫",
                "is_key": True
            },
            {
                "text": "放下身段委曲求全，接受降薪40%调至边缘支撑岗位，保住五险一金",
                "risk_label": "忍辱负重 · 守护全家",
                "calc_chance": lambda p: 100,
                "succ_feedback": "虽被踩碎尊严，但收入未断，你用沉默坚韧的肩膀托住了全家风雨飘摇的屋顶。",
                "succ_eff": {"wealth": 6.0, "happiness": -6, "health": -4, "rep": 8},
                "tag_succ": "家庭脊梁",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 56,
        "title": "AI风暴与健康保卫战",
        "narrative": "人工智能重塑各行各业，体检报告上一堆箭头红字，老友群中开始传来心梗讣告。",
        "choices": [
            {
                "text": "彻底退居二线放权，每日慢跑太极，戒烟断酒，寄情山水书法",
                "risk_label": "静心修身 · 确定延寿",
                "calc_chance": lambda p: 100,
                "succ_feedback": "健康指标逆转，平和轻盈重回身心。名利彻底看淡，内心一片澄澈。",
                "succ_eff": {"health": 20, "happiness": 15, "wealth": -2.0, "rep": 4},
                "tag_succ": "养生得道",
                "is_key": False
            },
            {
                "text": "不服老，趁着AI新风口再投私房钱创立导师孵化室，誓证自我",
                "risk_label": "老骥伏枥 · 成功率40%",
                "calc_chance": lambda p: 40 + (15 if p.intellect > 70 else 0) + (10 if p.luck > 50 else -10),
                "succ_feedback": "【教父封神】沉淀的智慧与AI工具碰撞出奇迹，成为业界尊崇的元老！",
                "fail_feedback": "【身心溃败】精力不济被后辈算计，连续熬夜突发心房颤动住进急诊抢救。",
                "succ_eff": {"wealth": 24.0, "intellect": 10, "rep": 20, "health": -8},
                "fail_eff": {"wealth": -14.0, "health": -28, "happiness": -15, "rep": 0},
                "tag_succ": "老骥伏枥",
                "tag_fail": "心力交瘁",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 78,
        "title": "夕阳晚钟与生命辞章",
        "narrative": "冬日暖阳洒在阳台，长年相伴的老伴器官衰竭卧榻，握着你满是皱纹的手温柔告别。",
        "choices": [
            {
                "text": "遵从爱人生前意愿，选择安宁疗护，握着手在平静温情中陪伴最后一程",
                "risk_label": "体面告别 · 慈悲释怀",
                "calc_chance": lambda p: 100,
                "succ_feedback": "在老歌与回忆的温光中，爱人安详闭眼。没有仪器刺耳的轰鸣，满心皆是感恩。",
                "succ_eff": {"intellect": 8, "happiness": 6, "rep": 10},
                "tag_succ": "体面告别",
                "is_key": True
            },
            {
                "text": "倾尽全家积蓄送入ICU抢救插管，只求哪怕多陪一天",
                "risk_label": "生死执念 · 倾力而战",
                "calc_chance": lambda p: 100,
                "succ_feedback": "散尽晚年积蓄，在ICU门外守候近一个月。纵有万般不舍，终究坦然面对。",
                "succ_eff": {"wealth": -20.0, "happiness": -14, "health": -10, "rep": 5},
                "tag_succ": "生死执念",
                "is_key": True
            }
        ]
    }
]

def generate_random_destiny():
    birth_years = [1976, 1982, 1988, 1994]
    b_year = random.choice(birth_years)
    origin = random.choice(RANDOM_ORIGINS)
    trait = random.choice(RANDOM_TRAITS)
    return b_year, origin, trait

def main():
    clear_screen()
    print(f"{Color.GOLD}{'='*64}{Color.RESET}")
    print(f"{Color.BOLD}{Color.GOLD}      浮 生 录  ·  时 代 风 云 与 随 机 天 命 模 拟 器{Color.RESET}")
    print(f"{Color.GOLD}{'='*64}{Color.RESET}")
    slow_print(" 人生既有个人的苦心奋斗，更有时代风浪的无情洗礼与天命掷骰。\n", 0.02)

    # 随机天命投胎抽卡机制
    while True:
        b_year, origin, trait = generate_random_destiny()
        era_title, era_desc = ERA_TIMELINE.get(b_year, ("时代初晓", ""))
        
        print(f"{Color.CYAN}【 🎲 天命投胎卡号抽取中... 】{Color.RESET}")
        print(f"  出生年代: {Color.YELLOW}{b_year} 年 · {era_title}{Color.RESET}")
        print(f"  时代缩影: {Color.GRAY}{era_desc}{Color.RESET}")
        print(f"  出生家庭: {Color.BOLD}{origin['title']}{Color.RESET}")
        print(f"  门第机缘: {origin['desc']}")
        print(f"  先天特质: {Color.PURPLE}[{trait['name']}] - {trait['desc']}{Color.RESET}\n")

        cmd = input(f"{Color.GOLD}按回车接受此命格进入人间，或输入 r 重新摇号投胎: {Color.RESET}").strip().lower()
        if cmd != 'r':
            break
        print(f"\n{Color.GRAY}重新祈求天命...{Color.RESET}\n")
        time.sleep(0.5)

    name = input(f"\n{Color.CYAN}请输入入世姓名 (留空随机): {Color.RESET}").strip()
    if not name:
        name = random.choice(["陈远", "林栖", "陆明舟", "沈清弦", "许念安", "周子墨", "顾长风", "宋平"])

    player = Player(name, b_year, origin, trait)
    slow_print(f"\n命运落笔：{player.name}，生于 {player.birth_year} 年。漫漫长路，由此启程。\n", 0.02)
    time.sleep(1)

    # 阶段推演
    for stage in EPOCH_STAGES:
        if player.health <= 15:
            player.death_reason = "积劳成疾，在时代长风中过早抱憾离世"
            break

        player.age = stage["age_rel"]
        curr_year = player.birth_year + player.age

        player.show_dashboard()

        # 随机突发事件触发机制 (35% 几率)
        if random.random() < 0.35:
            re = random.choice(RANDOM_EVENTS)
            print(f"{Color.PURPLE}【 🎲 命运无常 · 偶发事件 】{re['title']}{Color.RESET}")
            print(f"  {Color.GRAY}{re['desc']}{Color.RESET}")
            
            # 作用效果
            eff = re["effect"]
            player.wealth = round(player.wealth + eff.get("wealth", 0), 1)
            player.health = max(10, min(100, player.health + eff.get("health", 0)))
            player.happiness = max(10, min(100, player.happiness + eff.get("happiness", 0)))
            player.intellect = max(20, min(100, player.intellect + eff.get("intellect", 0)))
            player.luck = max(10, min(100, player.luck + eff.get("luck", 0)))
            player.random_events.append((curr_year, player.age, re["title"]))
            time.sleep(1)

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

        # 属性更新
        player.health = max(0, min(100, player.health + eff.get("health", 0)))
        player.wealth = round(player.wealth + eff.get("wealth", 0), 1)
        player.intellect = max(0, min(100, player.intellect + eff.get("intellect", 0)))
        player.happiness = max(0, min(100, player.happiness + eff.get("happiness", 0)))
        player.luck = max(0, min(100, player.luck + eff.get("luck", 0)))
        player.reputation = max(0, min(100, player.reputation + eff.get("rep", 0)))

        if tag and tag not in player.tags:
            player.tags.append(tag)

        # 记录
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
        if chosen.get("is_key"):
            player.key_choices.append(record)

        if chance < 100:
            print(f"\n{Color.PURPLE}🎲 命运掷骰：出目 {roll} / 胜率基线 {chance}%  ➔  {'★ 顺遂如愿' if is_success else '✕ 天不遂人'}{Color.RESET}")
        print(f"{Color.GREEN}抉择回响：{Color.RESET}{fb}")
        time.sleep(1.2)

    if not player.death_reason:
        player.death_reason = "寿终正寝，与世长安"

    # 打印终局人生总结
    render_terminal_ending(player)

def render_terminal_ending(player):
    clear_screen()
    end_year = player.birth_year + player.age
    print(f"\n{Color.GOLD}{'='*64}{Color.RESET}")
    print(f"{Color.BOLD}{Color.GOLD}      《 浮 生 录 · 人 物 一 生 终 局 记 与 时 代 回 响 》{Color.RESET}")
    print(f"{Color.GOLD}{'='*64}{Color.RESET}\n")

    print(f" 主角姓名: {Color.BOLD}{player.name}{Color.RESET} ({player.birth_year} - {end_year} · 享年 {player.age} 岁)")
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

    # 评价原型
    if player.wealth >= 40 and player.happiness >= 55:
        archetype = "时代弄潮翁 · 功成身退"
        epitaph = "你踩准了时代每一朵最具生机的浪花，既饱览了财富的壮阔，又未曾迷失于物欲的深壑。落子无悔。"
    elif player.wealth >= 25 and player.happiness < 45:
        archetype = "负重攀登者 · 时代苦行僧"
        epitaph = "在狂飙的城市化与债务大山中，你用肩膀扛起了几代人的体面，却在深夜加班室里耗尽了青春的灵气。"
    elif player.happiness >= 70 and player.wealth < 20:
        archetype = "旷达布衣 · 自在散人"
        epitaph = "世人慌慌张张图碎银几两，而你早早参透了内卷的荒诞。向青山借得满怀清风，胸中自安然。"
    elif player.intellect >= 75:
        archetype = "清醒明哲者 · 孤峰观澜"
        epitaph = "你以澄澈的智识洞穿了时代周期演进的规律，在浮华中冷眼旁观。懂得了历史，因而深怀悲悯。"
    elif player.age < 50:
        archetype = "断弦流星 · 孤勇悲歌"
        epitaph = "生命弦绷得太紧，你在烈火中疾驰，走得太急太烈。人间热闹非凡，而你已悄然化作尘埃。"
    else:
        archetype = "人间守望者 · 平凡的伟力"
        epitaph = "没有成为站在风口的神话，亦未沦为时代的叹息。尽职岗位，尽心家庭，平凡而坚韧地走完了真诚的一生。"

    print(f"\n{Color.CYAN}【 宿命评定与墓志铭 】{Color.RESET}")
    print(f"  终极称号: {Color.BOLD}{Color.GOLD}《{archetype}》{Color.RESET}")
    print(f"  墓志铭  : {Color.ITALIC}“{epitaph}”{Color.RESET}")

    print(f"\n{Color.CYAN}【 时代坐标回响 】{Color.RESET}")
    print(f"  {player.name}降生于 {player.birth_year} 年（{player.origin['title']}）。")
    print(f"  这一生恰逢共和国历史上最磅礴的现代化转型：从改革发端、国企下岗阵痛、入世腾飞、")
    print(f"  到四万亿房产狂飙、移动互联风口与AI大潮。所有的个人拼搏，皆深刻映照着时代的风速。")

    print(f"\n{Color.CYAN}【 关键命运分水岭（掷骰与实录） 】{Color.RESET}")
    for idx, kc in enumerate(player.key_choices, 1):
        chance_str = f"出目 {kc['roll']} / 胜率 {kc['chance']}%" if kc['chance'] < 100 else "确定性契约"
        status_str = f"{Color.GREEN}顺遂{Color.RESET}" if kc['is_success'] else f"{Color.RED}受挫{Color.RESET}"
        print(f"  {idx}. [{kc['year']}年 · {kc['age']}岁] {kc['title']} ({chance_str} ➔ {status_str})")
        print(f"     决策: {Color.YELLOW}{kc['choice_text']}{Color.RESET}")
        print(f"     回响: {Color.GRAY}{kc['feedback']}{Color.RESET}")

    print(f"\n{Color.GOLD}{'='*64}{Color.RESET}")
    print(f"{Color.DIM}大浪淘沙，唯心自守。愿你在人间的每一程都无怨无悔。{Color.RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n岁月如风，中途隐退。")
