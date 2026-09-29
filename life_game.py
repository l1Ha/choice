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
PAST_ORIGINS = [
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
    }
]

# 未来家庭背景池
FUTURE_ORIGINS = [
    {
        "title": "近地轨道空港维护工家庭",
        "desc": "父母是低轨道空间站聚变管路维修工，常年处于微重力环境。蜂巢胶囊居住区，盼望攒够地表绿区永久居住权。",
        "flavor": "在透过观察舷窗俯瞰蓝色地球与低沉机械轰鸣中长大，对辽阔星空与狭窄生存有着双重直觉",
        "stat": {"health": 86, "wealth": 4.5, "intellect": 62, "happiness": 54, "luck": 52, "rep": 48},
        "trait": "真空坚毅"
    },
    {
        "title": "次级穹顶边缘生态农场",
        "desc": "在受控人造光与水培架间长大，父母躬耕于藻类蛋白工厂，虽然远离核心算力区，但保持了纯天然食物的质朴。",
        "flavor": "在人造紫外灯与水培滴灌的声音中成长，渴望挣脱穹顶过滤网，亲眼看看真正未经净化的暴雨",
        "stat": {"health": 95, "wealth": 1.5, "intellect": 50, "happiness": 66, "luck": 50, "rep": 40},
        "trait": "大地复归"
    },
    {
        "title": "跨国巨企算力中继基层职员",
        "desc": "父母为中央神经网络提供日常标记与清理，生活被密密麻麻的指标与义体维护费绑死，自幼植入基础教学芯片。",
        "flavor": "在全息霓虹与代码流的光影中长大，早早见识了数字永生者的傲慢与底层义体磨损的焦糊味",
        "stat": {"health": 82, "wealth": 9.0, "intellect": 68, "happiness": 50, "luck": 55, "rep": 52},
        "trait": "数据感知"
    },
    {
        "title": "地下自由频段游民家庭",
        "desc": "父母是未接入官方脑机中央网络的旧人类守望者，藏身于旧城地下防空洞，靠维修古董电子仪器与私密通信为生。",
        "flavor": "在充满松香焊锡味与旧书本的防空洞里长大，珍惜不被算法监控的纯粹思想与手写文字",
        "stat": {"health": 88, "wealth": 3.0, "intellect": 64, "happiness": 58, "luck": 60, "rep": 36},
        "trait": "断网自守"
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

# 过去偶发突发事件
PAST_RANDOM_EVENTS = [
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

# 未来偶发突发事件
FUTURE_RANDOM_EVENTS = [
    {
        "title": "神经脉冲微频震荡",
        "desc": "公共数据总线遭受微型电磁风暴，脑机神经元短路导致剧烈偏头痛，深感机械改造的健康忧虑。",
        "effect": {"health": -8, "wealth": -1.0, "happiness": -6, "luck": -1}
    },
    {
        "title": "匿名算力空投",
        "desc": "暗网开源基金会向你的冷钱包误转了一笔高纯度量子通证，小发一笔横财。",
        "effect": {"wealth": 3.5, "happiness": 10, "luck": 3}
    },
    {
        "title": "仿生合成蛋白污染事件",
        "desc": "长期订购的人造合成肉检测出未申报的合成酵母毒素，全家连夜注射排毒血清。",
        "effect": {"health": -10, "wealth": -1.5, "happiness": -8, "intellect": 4}
    },
    {
        "title": "星际退役老兵指点",
        "desc": "在空港旧货维修区，一位从火星轨道退役的老轮机长教了你一手被淘汰但极度可靠的冷电弧修复秘籍。",
        "effect": {"intellect": 10, "happiness": 6, "rep": 8, "luck": 4}
    },
    {
        "title": "超额碳排放罚单",
        "desc": "旧式供暖器排热超标触发街区环境算法巡检，全家当月被扣除两个等级的清洁水配额。",
        "effect": {"wealth": -2.0, "happiness": -7, "luck": -2}
    }
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

    def show_dashboard(self, stage_idx, total_stages):
        clear_screen()
        curr_year = self.birth_year + self.age
        timeline = PAST_TIMELINE if self.epoch_mode == "past" else FUTURE_TIMELINE
        era_key = max([y for y in timeline if curr_year >= y], default=self.birth_year)
        era_title, era_desc = timeline.get(era_key, ("时代演进", "历史的年轮悄然流转..."))

        print(f"{Color.GOLD}{'='*68}{Color.RESET}")
        print(f" {Color.BOLD}{self.name}{Color.RESET} · {curr_year} 年 ({self.age} 岁) | 进度 [{stage_idx}/{total_stages}] | 时代：{Color.YELLOW}{era_title}{Color.RESET}")
        print(f" 时代背景: {Color.GRAY}{era_desc}{Color.RESET}")
        print(f"{Color.GOLD}{'-'*68}{Color.RESET}")
        print(f" [健康]: {int(self.health):<3}♥  |  [财富]: {self.wealth:.1f}万￥  |  [智识]: {int(self.intellect):<3}✦  |  [心安]: {int(self.happiness):<3}☼  |  [气运]: {int(self.luck):<3}🎲")
        print(f"{Color.GOLD}{'='*68}{Color.RESET}\n")

# 过去纪元 16 大关卡
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
        birth_years = [1976, 1982, 1988, 1994]
        origin = random.choice(PAST_ORIGINS)
    else:
        birth_years = [2042, 2048, 2054, 2060]
        origin = random.choice(FUTURE_ORIGINS)
    
    b_year = random.choice(birth_years)
    trait = random.choice(RANDOM_TRAITS)
    return b_year, origin, trait

def main():
    clear_screen()
    print(f"{Color.GOLD}{'='*68}{Color.RESET}")
    print(f"{Color.BOLD}{Color.GOLD}    浮 生 录  ·  过 去 与 未 来 浪 潮 模 拟 器 (全 卷 纪 传 版){Color.RESET}")
    print(f"{Color.GOLD}{'='*68}{Color.RESET}")
    slow_print(" 一个人的命运，既要靠自我的奋斗，亦要看历史的进程。\n 时代洪流呼啸而过，偶发的幸与不幸如影随形。细水长流，步步为营，落子无悔。\n", 0.012)

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
        timeline = PAST_TIMELINE if epoch_mode == "past" else FUTURE_TIMELINE
        era_title, era_desc = timeline.get(b_year, ("时代初晓", ""))
        
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
        time.sleep(0.3)

    default_names = ["林栖", "陈远", "沈清弦", "陆明舟", "许念安", "周子墨", "星野", "艾柯", "顾长风"]
    name = input(f"\n{Color.CYAN}请输入入世姓名 (留空随机): {Color.RESET}").strip()
    if not name:
        name = random.choice(default_names)

    player = Player(name, epoch_mode, b_year, origin, trait)
    active_stages = PAST_STAGES if epoch_mode == "past" else FUTURE_STAGES
    total_stages = len(active_stages)

    slow_print(f"\n命运之轮缓缓启动，{player.name} 踏入了 {player.birth_year} 年的人间...\n", 0.02)
    time.sleep(0.8)

    # 游戏主轮次
    for idx_stage, stage in enumerate(active_stages, 1):
        if player.health <= 12:
            player.death_reason = "积劳成疾，在时代长风中过早抱憾离世"
            break

        player.age = stage["age_rel"]
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

        input(f"\n{Color.GRAY}按回车继续步入岁月下一程...{Color.RESET}")
        time.sleep(0.4)

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
