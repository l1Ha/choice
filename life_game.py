#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
浮生录 (Lifepath) · 命令行文字人生模拟器（平滑沉浸与时代长卷版）
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

def slow_print(text, delay=0.012, newline=True):
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
    2015: ("移动互联与大众创业", "智能手机全面普及，移动支付改变日常，'大众创业、万众创新'催生风口狂热。"),
    2020: ("突发疫情与行业洗牌", "教培、地产、大厂相继迎收缩调整，考公热潮席卷，社会回归安全与稳健。"),
    2028: ("AI时代与老龄化纵深", "人工智能接管日常智力工作，老龄化加速，面对不确定性的未来，人们探索心安之道。")
}

# 随机家庭底色池
RANDOM_ORIGINS = [
    {
        "title": "三线内陆国企职工家庭",
        "desc": "父母在大型国营机械厂当技术工，住在大院。看似安稳平实，实则深藏体制改革巨澜。",
        "flavor": "在红砖家属楼与工厂汽笛声中度过童年，习惯了集体生活的温情与拘谨",
        "stat": {"health": 90, "wealth": 2.5, "intellect": 52, "happiness": 65, "luck": 50, "rep": 45},
        "trait": "大院情怀"
    },
    {
        "title": "黄土丘陵偏远农村",
        "desc": "祖辈世代躬耕于贫瘠农田。父母起早贪黑，唯一执念就是供你'读书跳出农门'。",
        "flavor": "童年总伴随割麦打场的热浪与对县城楼房的遥望，早早就知晓生活需步步淌血",
        "stat": {"health": 94, "wealth": 0.3, "intellect": 48, "happiness": 55, "luck": 52, "rep": 35},
        "trait": "野草劲骨"
    },
    {
        "title": "省城中学/大学教师家庭",
        "desc": "家里有一整面墙的藏书与学术期刊，家教严谨体面，重视修养但期待甚高。",
        "flavor": "在省城机关与教工宿舍的书卷香中长大，骨子里带着几分清高，见识敏锐",
        "stat": {"health": 84, "wealth": 6.0, "intellect": 65, "happiness": 58, "luck": 54, "rep": 55},
        "trait": "书香灵慧"
    },
    {
        "title": "沿海敢闯个体户",
        "desc": "父母最早一批摆摊贩卖布匹电器，常年火车奔波，从小在算盘和现金堆中长大。",
        "flavor": "自幼耳濡目染商贾交易与博弈，深知市场经济的残酷与暴利，敢于在风口下重注",
        "stat": {"health": 88, "wealth": 12.0, "intellect": 54, "happiness": 60, "luck": 58, "rep": 48},
        "trait": "市井嗅觉"
    },
    {
        "title": "单亲下岗缝纫女工家庭",
        "desc": "母亲一个人在路边支缝纫机踩踏板养活全家，很小就知道生活毫无退路。",
        "flavor": "在弄堂路灯下看着母亲踩缝纫机的背影长大，早熟懂事，对逆境格外警觉坚忍",
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
        "effect": {"wealth": 1.2, "happiness": 8, "luck": -2}
    },
    {
        "title": "深夜急诊惊魂",
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
    },
    {
        "title": "大盘剧烈震荡",
        "desc": "股市行情躁动，跟风买入遭遇跌停割肉，深刻铭记风险敬畏心。",
        "effect": {"wealth": -3.0, "happiness": -8, "intellect": 5, "luck": -3}
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

    def show_dashboard(self, current_stage_idx, total_stages):
        curr_year = self.birth_year + self.age
        era_keys = sorted(ERA_TIMELINE.keys(), reverse=True)
        era_title, _ = ERA_TIMELINE.get(self.birth_year, ("时代", ""))
        for y in era_keys:
            if curr_year >= y:
                era_title, _ = ERA_TIMELINE[y]
                break
                
        w_str = f"{self.wealth:.1f}万" if self.wealth >= 0 else f"负债{abs(self.wealth):.1f}万"
        print(f"\n{Color.BG_DARK}{Color.GOLD} 📅 {curr_year}年 · {self.age}岁 ({era_title}) [{current_stage_idx}/{total_stages}] | 👤 {self.name} | 健康: {int(self.health)} | 财富: {w_str} | 心智: {int(self.intellect)} | 气运: {int(self.luck)} {Color.RESET}\n")

# 16个更平滑细腻的宏大时代关卡
EPOCH_STAGES = [
    {
        "age_rel": 6,
        "title": "大院门槛与小城清晨",
        "narrative": "清晨空气中飘着蜂窝煤和油条的烟气，到了入小学的年纪，父母在为借读名校还是就近上学争论不休。",
        "choices": [
            {
                "text": "省吃俭用托人送礼，硬挤进教学质量顶尖的城关中心小学",
                "risk_label": "高压开局 · 成功率75%",
                "calc_chance": lambda p: 75 + (10 if p.luck > 50 else -5),
                "succ_feedback": "【判定成功】进入名校尖子班，奠定了极其扎实规整的学习习惯。",
                "fail_feedback": "【名额被顶】借读名额被顶替，白花人情积蓄，更早看清世态现实。",
                "succ_eff": {"intellect": 8, "wealth": -1.0, "rep": 5},
                "fail_eff": {"intellect": 3, "wealth": -1.5, "happiness": -6},
                "tag_succ": "名校开蒙",
                "tag_fail": "碰壁初尝",
                "is_key": False
            },
            {
                "text": "就近入读厂办或村小，在泥巴地和伙伴无拘无束疯跑长大",
                "risk_label": "质朴童年 · 顺其自然",
                "calc_chance": lambda p: 100,
                "succ_feedback": "每天打弹珠捉泥鳅，身子骨极其结实，性格乐观豁达。",
                "succ_eff": {"health": 5, "happiness": 8, "intellect": 3},
                "tag_succ": "野趣童年",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 10,
        "title": "工厂汽笛与商品潮涌",
        "narrative": "时代正急速转向，录音机放起港台歌曲，下海经商的传闻满天飞。亲戚邀约父母合伙去南方跑货。",
        "choices": [
            {
                "text": "力劝父母：'下海闯荡，抓住商品消费爆发的时代风口！'",
                "risk_label": "高风险 · 时代博弈",
                "calc_chance": lambda p: 55 + (15 if p.luck > 50 else -10),
                "succ_feedback": "【掷骰大胜！】父母承包的小摊位踩中消费热潮，家庭资产暴翻数倍！",
                "fail_feedback": "【掷骰失利】因经验不足遭遇货源骗局，积蓄赔光，父母艰难打零工还债。",
                "succ_eff": {"wealth": 6.0, "happiness": 6, "intellect": 4, "luck": 4},
                "fail_eff": {"wealth": -3.0, "happiness": -8, "intellect": 2, "luck": -4},
                "tag_succ": "商潮初利",
                "tag_fail": "早尝败绩",
                "is_key": True
            },
            {
                "text": "劝导父母求稳为上，保住铁饭碗与医保，安稳过日子",
                "risk_label": "保守求稳 · 确定回报",
                "calc_chance": lambda p: 100,
                "succ_feedback": "家庭虽无暴富，但清贫安稳，每天有热汤热饭，你在宁静中完成童年学业。",
                "succ_eff": {"wealth": 0.8, "happiness": 4, "intellect": 2},
                "tag_succ": "守正持重",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 15,
        "title": "中考分流与网吧浪潮",
        "narrative": "互联网正以野火之势蔓延，街头黑网吧与网游大火。中考只有四成多能考上高中，淘汰近在咫尺。",
        "choices": [
            {
                "text": "断绝诱惑拔掉网线，每天题海苦读到凌晨两点，誓考重点高中",
                "risk_label": "苦行应试 · 成功率80%",
                "calc_chance": lambda p: 80 + int((p.intellect - 50) / 2),
                "succ_feedback": "【应试拔筹】以全区前30名优异成绩考入省重点中学！全家扬眉吐气。",
                "fail_feedback": "【临场意外】考场突发急性胃痛发挥失常，压线进入普通高中，尝到无常滋味。",
                "succ_eff": {"intellect": 12, "happiness": 6, "health": -4, "rep": 10},
                "fail_eff": {"intellect": 6, "happiness": -8, "health": -6, "rep": 2},
                "tag_succ": "做题精英",
                "tag_fail": "考场蹉跎",
                "is_key": True
            },
            {
                "text": "自学编程与制作网站，将计算机技术视作未来的黄金钥匙",
                "risk_label": "异类先锋 · 成功率60%",
                "calc_chance": lambda p: 60 + int((p.intellect - 50) / 2) + (10 if p.luck > 55 else 0),
                "succ_feedback": "【极客奇迹】个人网站爆火，获计算机特长加分保送重点班，踏上技术快车道！",
                "fail_feedback": "【落选歧路】学业彻底荒废，未能考上普通高中，只得入读职专，饱受白眼。",
                "succ_eff": {"intellect": 15, "wealth": 2.0, "happiness": 8, "luck": 5},
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
        "narrative": "入世与全球化全面铺开，外贸、金融、软件成为炙手可热的词汇。两张截然不同的人生轨迹摆在眼前。",
        "choices": [
            {
                "text": "报考沿海名校的'计算机科学'或'国际外贸金融'热门专业",
                "risk_label": "风口浪尖 · 成功率70%",
                "calc_chance": lambda p: 70 + (10 if p.luck > 50 else -5),
                "succ_feedback": "【乘风而上】完美踩中中国互联网与全球化黄金二十年通道，眼界彻底跃升！",
                "fail_feedback": "【周期调整】扩招与泡沫叠加，毕业时面临惨烈内卷，在逼仄合租房中苦苦挣扎。",
                "succ_eff": {"intellect": 14, "wealth": 3.0, "happiness": 6, "rep": 8},
                "fail_eff": {"intellect": 8, "wealth": -1.5, "happiness": -6, "rep": 2},
                "tag_succ": "时代弄潮儿",
                "tag_fail": "风口折翼",
                "is_key": True
            },
            {
                "text": "选择本地公费师范或军警医校，毕业即享编制，安稳笃定",
                "risk_label": "安稳航道 · 绝对稳固",
                "calc_chance": lambda p: 100,
                "succ_feedback": "父母长舒口气。你免除学费并分配编制，冷眼看着外界商海起伏。",
                "succ_eff": {"intellect": 7, "wealth": 1.5, "happiness": 8, "rep": 8},
                "tag_succ": "体制坚盾",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 21,
        "title": "大学时光：考研考证还是青涩爱恋？",
        "narrative": "大学校园里栀子花开，遇到了心仪的人，同时考研升学与找工作的现实压力接踵而至。",
        "choices": [
            {
                "text": "全力以赴相濡以沫的爱恋，与 Ta 一同约定奋斗的城市",
                "risk_label": "至情至性 · 成功率65%",
                "calc_chance": lambda p: 65 + (10 if p.happiness > 60 else -5),
                "succ_feedback": "【琴瑟和鸣】两人互相支撑收获纯粹爱情，成了彼此最坚韧的后盾。",
                "fail_feedback": "【异地分离】毕业季在现实压力前痛哭分手，大病一场。",
                "succ_eff": {"happiness": 15, "rep": 5, "health": 2},
                "fail_eff": {"happiness": -16, "health": -6, "intellect": 3},
                "tag_succ": "情深意笃",
                "tag_fail": "情伤碎梦",
                "is_key": False
            },
            {
                "text": "清心寡欲克制情感，泡图书馆死磕专业考研与核心硬证书",
                "risk_label": "硬核履历 · 成功率85%",
                "calc_chance": lambda p: 85 + int((p.intellect - 50) / 2),
                "succ_feedback": "【名列前茅】顺利考上研究生或多张权威执照，求职简历金光闪闪。",
                "fail_feedback": "【偏门失利】因紧张几分之差遗憾落榜，但底子扎实。",
                "succ_eff": {"intellect": 12, "wealth": 2.0, "happiness": 4, "rep": 6},
                "fail_eff": {"intellect": 6, "happiness": -6, "health": -3},
                "tag_succ": "履历出众",
                "tag_fail": "功亏一篑",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 24,
        "title": "北京奥运前夜：大城市的蚁族还是小城归客？",
        "narrative": "奥运在即大城房价蠢蠢欲动，地下室的逼仄与拥挤地铁消磨着你，去留成为大拷问。",
        "choices": [
            {
                "text": "坚决留在大城市搏命加班，争夺业务核心骨干席位",
                "risk_label": "大城拼搏 · 成功率60%",
                "calc_chance": lambda p: 60 + int((p.intellect - 50) / 2) + (10 if p.luck > 50 else -5),
                "succ_feedback": "【初露锋芒】主导业务拿下亮眼业绩，升职加薪，站稳脚跟！",
                "fail_feedback": "【透支受挫】遭遇画饼领导无偿加班，身心俱疲体检异常。",
                "succ_eff": {"wealth": 12.0, "intellect": 10, "happiness": 6, "health": -8, "rep": 10},
                "fail_eff": {"wealth": 3.0, "intellect": 4, "happiness": -12, "health": -12},
                "tag_succ": "职场新星",
                "tag_fail": "身心透支",
                "is_key": True
            },
            {
                "text": "退守老家二三线城市进体制或国企，过安稳舒坦的慢生活",
                "risk_label": "故土安居 · 确定收益",
                "calc_chance": lambda p: 100,
                "succ_feedback": "有吃有住常伴父母身旁，虽无暴富机会，但身心极其祥和。",
                "succ_eff": {"wealth": 3.0, "happiness": 10, "health": 6, "rep": 5},
                "tag_succ": "故土安居",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 27,
        "title": "四万亿与创业/购房首班车",
        "narrative": "四万亿刺激政策带来海量资金，移动互联与电商如火如荼，是创业还是上车买房？",
        "choices": [
            {
                "text": "拿出所有积蓄合伙创业，搏一把移动互联网爆发红利",
                "risk_label": "创业豪赌 · 成功率45%",
                "calc_chance": lambda p: 45 + int((p.intellect - 50) / 2) + (15 if p.luck > 50 else -10),
                "succ_feedback": "【创业大捷】拿到数百万元天使轮融资，年轻有为，资产跃升！",
                "fail_feedback": "【爆雷欠债】合伙人跑路项目断裂，欠下外债靠打零工艰苦还债。",
                "succ_eff": {"wealth": 35.0, "intellect": 12, "happiness": 10, "health": -6, "rep": 15},
                "fail_eff": {"wealth": -15.0, "intellect": 8, "happiness": -15, "health": -10, "rep": -4},
                "tag_succ": "独角兽奇迹",
                "tag_fail": "负债受挫",
                "is_key": True
            },
            {
                "text": "掏出全部积蓄做首付，赶在房价起飞前夕按揭买下两居室",
                "risk_label": "早早上车 · 资产增值",
                "calc_chance": lambda p: 100,
                "succ_feedback": "【踏中红利】踩准房产黄金爆发点，数年后翻倍，成最硬压舱石。",
                "succ_eff": {"wealth": 22.0, "happiness": 8, "health": 2, "rep": 8},
                "tag_succ": "早早上车",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 31,
        "title": "三十而立：婚姻与家庭抉择",
        "narrative": "两方家庭就彩礼、婚宴排场与积蓄配置互相博弈，你站在世俗的风口浪尖。",
        "choices": [
            {
                "text": "顺从长辈一切要求，倾尽积蓄办一场风风光光的隆重婚宴",
                "risk_label": "面子体面 · 代价不菲",
                "calc_chance": lambda p: 100,
                "succ_feedback": "亲友赞不绝口，家庭长辈满意，但小家庭积蓄几乎掏空需紧缩度日。",
                "succ_eff": {"wealth": -8.0, "rep": 12, "happiness": 4},
                "tag_succ": "宗族体面",
                "is_key": False
            },
            {
                "text": "力排众议旅行结婚或极简操办，省下钱用于理财与育儿金",
                "risk_label": "务实自主 · 成功率75%",
                "calc_chance": lambda p: 75 + (10 if p.intellect > 55 else 0),
                "succ_feedback": "【务实省心】避开婆媳纷争与借贷烦恼，小日子过得充实踏实。",
                "fail_feedback": "【长辈怨言】老一辈觉得丢了面子，数年内逢年过节常遭白眼指责。",
                "succ_eff": {"wealth": 6.0, "happiness": 6, "intellect": 4},
                "fail_eff": {"wealth": 4.0, "happiness": -8, "rep": -5},
                "tag_succ": "务实自守",
                "tag_fail": "人情嫌隙",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 35,
        "title": "杠杆狂欢下的千万学区房博弈",
        "narrative": "股市狂热、P2P理财遍地，学区房被炒上天价。中介极力劝你卖掉老房加三倍杠杆抢名校学区房。",
        "choices": [
            {
                "text": "加满杠杆掏空六个钱包，赌一把名校学区房与房价二次暴涨",
                "risk_label": "高杠杆搏击 · 成功率50%",
                "calc_chance": lambda p: 50 + (10 if p.luck > 50 else -10),
                "succ_feedback": "【顺风获利】精准在政策收紧前锁定理财收益与学位，世俗赢家。",
                "fail_feedback": "【高位套牢】买在历史最高点，随后房价腰斩，月供成为沉重绞索。",
                "succ_eff": {"wealth": 28.0, "happiness": -4, "rep": 12},
                "fail_eff": {"wealth": -32.0, "happiness": -20, "health": -10, "rep": -4},
                "tag_succ": "杠杆豪赌",
                "tag_fail": "高位套牢",
                "is_key": True
            },
            {
                "text": "保持清醒拒绝过度负债，读普通公立，积蓄配置国债与健康",
                "risk_label": "守拙避险 · 绝对安全",
                "calc_chance": lambda p: 100,
                "succ_feedback": "亲友笑你胆小，但在随后暴雷潮中，唯有你现金流充沛从容。",
                "succ_eff": {"wealth": 10.0, "happiness": 12, "health": 6, "rep": 5},
                "tag_succ": "现金为王",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 40,
        "title": "医院走廊的消毒水与35岁职场瓶颈",
        "narrative": "家中老人确诊慢性大病需长年进口药，单位推行年轻化战略，中年两头受挤。",
        "choices": [
            {
                "text": "不惜代价用最好自费药尽孝，自己通宵接单一天只睡五小时硬扛",
                "risk_label": "血肉尽孝 · 成功率60%",
                "calc_chance": lambda p: 60 + int((p.health - 60) / 2),
                "succ_feedback": "【吉人天相】老人病情平稳，接单跑通小财源，以坚毅守住了全家！",
                "fail_feedback": "【积劳成疾】疲劳晕厥送医，老人痛哭心疼，全家账面大受损伤。",
                "succ_eff": {"rep": 15, "happiness": 6, "health": -12, "wealth": -6.0},
                "fail_eff": {"health": -20, "wealth": -12.0, "happiness": -15, "rep": 6},
                "tag_succ": "铁骨脊梁",
                "tag_fail": "苦雨连阴",
                "is_key": True
            },
            {
                "text": "选用医保目录保守治疗方案，守住小家庭财务底线不因病返贫",
                "risk_label": "理性持家 · 沉重止损",
                "calc_chance": lambda p: 100,
                "succ_feedback": "虽有一丝愧疚，但守住了全家现金流，孩子教育与生活井井有条。",
                "succ_eff": {"wealth": -4.0, "happiness": -6, "intellect": 4},
                "tag_succ": "理性持家",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 44,
        "title": "疫情洗牌、大厂毕业与降本增效",
        "narrative": "突发疫情颠覆日常，健康码与大厂裁员纷至沓来。你的部门被裁撤，补偿协议摆在眼前。",
        "choices": [
            {
                "text": "拿走 N+1 走出内卷，转行做独立顾问、出海咨询或自媒体",
                "risk_label": "逆势破局 · 成功率55%",
                "calc_chance": lambda p: 55 + int((p.intellect - 50) / 2) + (10 if p.luck > 50 else -10),
                "succ_feedback": "【逆风翻盘】凭借深厚人脉与技能，首年收入超过往昔死工资，赢得自由！",
                "fail_feedback": "【竞争残酷】赛道极卷接单受阻，消耗存款补贴家用，失眠白发丛生。",
                "succ_eff": {"wealth": 25.0, "happiness": 14, "health": 2, "rep": 12},
                "fail_eff": {"wealth": -12.0, "happiness": -18, "health": -8, "rep": -2},
                "tag_succ": "绝处逢生",
                "tag_fail": "中年受困",
                "is_key": True
            },
            {
                "text": "放下身段接受降薪40%调至边缘分支，保住社保与稳定基本盘",
                "risk_label": "忍辱求稳 · 稳固基本盘",
                "calc_chance": lambda p: 100,
                "succ_feedback": "虽失光鲜，但风雨中每月准时到账的工资成了庇护全家的定海神针。",
                "succ_eff": {"wealth": 6.0, "happiness": -6, "health": -4, "rep": 6},
                "tag_succ": "风雨同舟",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 50,
        "title": "知命之年：孩子高考与代际传承",
        "narrative": "年过半百两鬓微白，孩子高考放榜想选小众冷门的艺术哲学，而亲戚劝选考公体制专业。",
        "choices": [
            {
                "text": "强势干预，逼孩子报考体制好就业专业，确保人生下限",
                "risk_label": "家长威严 · 成功率70%",
                "calc_chance": lambda p: 70,
                "succ_feedback": "【平稳上岸】孩子考取体制编制旱涝保收，日后也逐渐体会到你的苦心。",
                "fail_feedback": "【代际冰封】孩子在不喜欢的专业厌学挂科，与你长期陷入冷战疏离。",
                "succ_eff": {"wealth": 5.0, "rep": 6, "happiness": -4},
                "fail_eff": {"happiness": -12, "rep": -4},
                "tag_succ": "铺路搭桥",
                "tag_fail": "代际隔阂",
                "is_key": False
            },
            {
                "text": "全力资助孩子追求热爱，宽容表示'做个快乐普通人就好'",
                "risk_label": "开明放手 · 成功率65%",
                "calc_chance": lambda p: 65 + (10 if p.luck > 50 else 0),
                "succ_feedback": "【各得其乐】孩子在热爱领域闪闪发光，家庭氛围融洽温馨。",
                "fail_feedback": "【毕业碰壁】小众专业求职困难，在家做全职儿女，全家持续资助。",
                "succ_eff": {"happiness": 15, "health": 4, "rep": 5},
                "fail_eff": {"wealth": -8.0, "happiness": -8},
                "tag_succ": "开明长辈",
                "tag_fail": "儿女啃老",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 58,
        "title": "AI风暴与老龄化晨昏",
        "narrative": "人工智能全面重塑社会，经验快速贬值。体检红字密布，单位通知你准备退休。",
        "choices": [
            {
                "text": "顺应天时彻底退居二线，太极晨练、弄花种草，寄情山水",
                "risk_label": "修身颐养 · 确定延寿",
                "calc_chance": lambda p: 100,
                "succ_feedback": "指标大幅转好，轻盈与平和重回身心。名利彻底看淡，内心一片澄澈。",
                "succ_eff": {"health": 20, "happiness": 16, "wealth": -2.0, "rep": 5},
                "tag_succ": "养生得道",
                "is_key": False
            },
            {
                "text": "烈士暮年心未已，投资AI新赛道开办顾问工作室，誓证老将价值",
                "risk_label": "老骥伏枥 · 成功率40%",
                "calc_chance": lambda p: 40 + (15 if p.intellect > 70 else 0) + (10 if p.luck > 50 else -10),
                "succ_feedback": "【老当益壮】智慧与AI碰撞出火花，成为业界尊崇的元老，名利双收！",
                "fail_feedback": "【心力交瘁】精力不济受年轻人欺瞒，更因连夜突发房颤进ICU抢救。",
                "succ_eff": {"wealth": 25.0, "intellect": 10, "rep": 20, "health": -6},
                "fail_eff": {"wealth": -15.0, "health": -28, "happiness": -16, "rep": 0},
                "tag_succ": "老骥伏枥",
                "tag_fail": "心力交瘁",
                "is_key": True
            }
        ]
    },
    {
        "age_rel": 66,
        "title": "桑榆晚景：带孙弄草还是周游天下？",
        "narrative": "孙辈蹒跚学步，儿女工作繁重希望你协助带娃；老友们则策划自驾去西藏圆年轻时的梦。",
        "choices": [
            {
                "text": "为儿女分担重压住进儿童房，每天买菜接送带孙享受天伦",
                "risk_label": "代际奉献 · 无怨无悔",
                "calc_chance": lambda p: 100,
                "succ_feedback": "看着小孙辈扑进怀里，内心满溢着天伦暖意，生活充实温馨。",
                "succ_eff": {"happiness": 10, "rep": 8, "health": -4},
                "tag_succ": "春蚕蜡炬",
                "is_key": False
            },
            {
                "text": "坚持独立生活，与老伴结伴游山玩水，踏遍祖国名山大川",
                "risk_label": "暮年畅游 · 成功率75%",
                "calc_chance": lambda p: 75 + int((p.health - 60) / 2),
                "succ_feedback": "【快意余生】在雪山脚下拍照，晚霞绚烂夺目，活出了真性情！",
                "fail_feedback": "【水土不服】途中呼吸道感染提前折返，但见到了想看的风景亦无憾。",
                "succ_eff": {"happiness": 16, "health": 6, "wealth": -5.0},
                "fail_eff": {"health": -8, "wealth": -4.0, "happiness": 4},
                "tag_succ": "快意余生",
                "tag_fail": "风尘仆仆",
                "is_key": False
            }
        ]
    },
    {
        "age_rel": 74,
        "title": "古稀回眸：旧友凋零与泛黄相册",
        "narrative": "翻看泛黄旧照，昔日同窗挚友相继离世，参加葬礼的次数已远多于婚礼。",
        "choices": [
            {
                "text": "提笔撰写一生自传与家族大时代变迁实录，给后代留存记忆",
                "risk_label": "立传铭史 · 精神长存",
                "calc_chance": lambda p: 100,
                "succ_feedback": "墨香沉静，梳理了毕生荣耀与风霜，后人读罢泪目，精神得以传承。",
                "succ_eff": {"intellect": 15, "happiness": 12, "rep": 15},
                "tag_succ": "青史留痕",
                "is_key": False
            },
            {
                "text": "散尽部分积蓄捐资山区助学，为大地播洒最后一份温情善念",
                "risk_label": "广种福田 · 大爱无声",
                "calc_chance": lambda p: 100,
                "succ_feedback": "收到山区孩子的感谢信，心头如沐春风，灵魂升华至纯净境地。",
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

def generate_random_destiny():
    birth_years = [1976, 1982, 1988, 1994]
    b_year = random.choice(birth_years)
    origin = random.choice(RANDOM_ORIGINS)
    trait = random.choice(RANDOM_TRAITS)
    return b_year, origin, trait

def main():
    clear_screen()
    print(f"{Color.GOLD}{'='*68}{Color.RESET}")
    print(f"{Color.BOLD}{Color.GOLD}      浮 生 录  ·  时 代 风 云 与 随 机 天 命 模 拟 器 (全卷版){Color.RESET}")
    print(f"{Color.GOLD}{'='*68}{Color.RESET}")
    slow_print(" 人生既有个人的苦心奋斗，更有时代风浪的无情洗礼与天命掷骰。\n", 0.015)

    while True:
        b_year, origin, trait = generate_random_destiny()
        era_title, era_desc = ERA_TIMELINE.get(b_year, ("时代初晓", ""))
        
        print(f"{Color.CYAN}【 🎲 先天命格卡 · 随机摇号投胎 】{Color.RESET}")
        print(f"  出生年代: {Color.YELLOW}{b_year} 年 · {era_title}{Color.RESET}")
        print(f"  时代缩影: {Color.GRAY}{era_desc}{Color.RESET}")
        print(f"  出生家庭: {Color.BOLD}{origin['title']}{Color.RESET}")
        print(f"  门第机缘: {origin['desc']}")
        print(f"  先天特质: {Color.PURPLE}[{trait['name']}] - {trait['desc']}{Color.RESET}\n")

        cmd = input(f"{Color.GOLD}按回车接受此命格进入人间，或输入 r 重新摇号投胎: {Color.RESET}").strip().lower()
        if cmd != 'r':
            break
        print(f"\n{Color.GRAY}重新祈求天命...{Color.RESET}\n")
        time.sleep(0.4)

    name = input(f"\n{Color.CYAN}请输入入世姓名 (留空随机): {Color.RESET}").strip()
    if not name:
        name = random.choice(["陈远", "林栖", "陆明舟", "沈清弦", "许念安", "周子墨", "顾长风", "宋平", "赵文初", "唐立本"])

    player = Player(name, b_year, origin, trait)
    slow_print(f"\n命运落笔：{player.name}，生于 {player.birth_year} 年。漫漫长路，由此启程。\n", 0.015)
    time.sleep(0.8)

    total_stages = len(EPOCH_STAGES)
    for idx_stage, stage in enumerate(EPOCH_STAGES, 1):
        if player.health <= 12:
            player.death_reason = "积劳成疾，在时代长风中过早抱憾离世"
            break

        player.age = stage["age_rel"]
        curr_year = player.birth_year + player.age

        player.show_dashboard(idx_stage, total_stages)

        if random.random() < 0.32:
            re = random.choice(RANDOM_EVENTS)
            print(f"{Color.PURPLE}【 🎲 命运无常 · 偶发事件 】{re['title']}{Color.RESET}")
            print(f"  {Color.GRAY}{re['desc']}{Color.RESET}")
            
            eff = re["effect"]
            player.wealth = round(player.wealth + eff.get("wealth", 0), 1)
            player.health = max(10, min(100, player.health + eff.get("health", 0)))
            player.happiness = max(10, min(100, player.happiness + eff.get("happiness", 0)))
            player.intellect = max(20, min(100, player.intellect + eff.get("intellect", 0)))
            player.luck = max(10, min(100, player.luck + eff.get("luck", 0)))
            player.random_events.append((curr_year, player.age, re["title"]))
            time.sleep(0.6)

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
        if chosen.get("is_key"):
            player.key_choices.append(record)

        if chance < 100:
            print(f"\n{Color.PURPLE}🎲 命运掷骰：出目 {roll} / 胜率基线 {chance}%  ➔  {'★ 顺遂如愿' if is_success else '✕ 天不遂人'}{Color.RESET}")
        print(f"{Color.GREEN}抉择回响：{Color.RESET}{fb}")
        time.sleep(0.8)

    if not player.death_reason:
        player.death_reason = "寿终正寝，儿孙绕膝，在安详与温情中平静合眼"

    render_terminal_ending(player)

def render_terminal_ending(player):
    clear_screen()
    end_year = player.birth_year + player.age
    print(f"\n{Color.GOLD}{'='*68}{Color.RESET}")
    print(f"{Color.BOLD}{Color.GOLD}    《 浮 生 录 · 人 物 一 生 长 卷 纪 传 与 时 代 回 响 》{Color.RESET}")
    print(f"{Color.GOLD}{'='*68}{Color.RESET}\n")

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
