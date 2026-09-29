# -*- coding: utf-8 -*-
# 《浮生录》先秦汉唐 · 人生阶段 0-3

STAGES = [
    [   # 阶段 0 幼年启蒙 (5-7岁)
        {
            "period": "幼年启蒙",
            "title": "竹简刀笔间初识天下字",
            "narrative": "蒙学设在族中旧屋，先生以刀笔在竹简上刻字，命你逐字摹写。窗外井田里父兄正忙春耕，缺一个递水送饭的帮手。先生却道今日十简未成，不许归家。你握着刻刀，手心渐渐发汗。",
            "choices": [
                {
                    "text": "咬牙刻完十简，宁可饿着肚子也要让先生点头",
                    "risk": "寒窗苦读 · 稳妥积淀",
                    "chance": {"base": 75, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                    "succ_fb": "先生抚简称善，将你的名字写在学簿头一行，族中长辈闻讯，派人送来一块干肉。",
                    "fail_fb": "手指被刀笔磨破，简上字迹歪斜，先生叹你心浮，罚你明日再刻二十简。",
                    "succ_eff": {"intellect": 10, "rep": 5},
                    "fail_eff": {"intellect": 4, "happiness": -5},
                    "tag_succ": "刀笔初成",
                    "tag_fail": "手拙受罚",
                    "is_key": True
                },
                {
                    "text": "借口腹痛溜去田头，帮父兄递水送饭，趁隙偷听农事",
                    "risk": "亲近田垄 · 事功渐长",
                    "chance": {"base": 100},
                    "succ_fb": "父兄夸你懂事，教你辨认节气与土色，你把一句句农谚默默记在心里。",
                    "succ_eff": {"health": 6, "happiness": 6, "wealth": 2.0},
                    "tag_succ": "田垄情长",
                    "is_key": False
                }
            ]
        },
        {
            "period": "幼年启蒙",
            "title": "宗庙习礼初见尊卑",
            "narrative": "岁末祭祖，族中长者命你捧青铜小俎，立于阶下随众行礼。你腿脚酸麻，忽见邻家小儿在庙外招手，邀你去河边看新捕的鱼。长者目光沉沉扫来，俎中祭肉须捧到礼毕方止。",
            "choices": [
                {
                    "text": "屏息站定，把俎捧到礼毕，一步也不曾挪动",
                    "risk": "恪守宗法 · 沉稳有度",
                    "chance": {"base": 80, "int_div": 0, "luck_bonus": 0, "health_bonus": 0},
                    "succ_fb": "长者当众赞你知礼，把祭余的一块肉亲手分给你，道此子可教，将来可托付。",
                    "fail_fb": "你终究忍不住回头张望，被长者一眼看见，罚你跪在阶下，直到日头西沉。",
                    "succ_eff": {"rep": 8, "intellect": 4},
                    "fail_eff": {"rep": -5, "happiness": -6, "health": -3},
                    "tag_succ": "知礼守节",
                    "tag_fail": "失仪受罚",
                    "is_key": True
                },
                {
                    "text": "趁长者低头祝祷，悄悄溜出庙门去河边看鱼",
                    "risk": "任性贪玩 · 快意当前",
                    "chance": {"base": 100},
                    "succ_fb": "你摸到一尾滑鱼，笑得很大声，回家时衣襟尽湿，心头却痛快极了。",
                    "succ_eff": {"happiness": 10, "health": 4, "rep": -3},
                    "tag_succ": "童心未泯",
                    "is_key": False
                }
            ]
        }
    ],
    [   # 阶段 1 童年韶光 (9-11岁)
        {
            "period": "童年韶光",
            "title": "乡塾比试射御夺头筹",
            "narrative": "乡塾春日较艺，诸童须张弓射柳，胜者得先生一支刻字木牍。你用的弓是兄长旧物，弦已松软。同窗中有一人箭术极精，正笑你弓弱，先生却已击柝催令，众人列队上前。",
            "choices": [
                {
                    "text": "借力巧射，专瞄近处柳枝，稳中求胜不逞强",
                    "risk": "审时度势 · 巧取头筹",
                    "chance": {"base": 70, "int_div": 2, "luck_bonus": 3, "health_bonus": 0},
                    "succ_fb": "三箭两中，先生将木牍递到你手中，同窗们围上来要摸那支箭，眼里都是羡慕。",
                    "fail_fb": "弓弦忽然崩断，箭落在柳树根下，众人哄笑，你脸红到耳根，握弓的手发颤。",
                    "succ_eff": {"intellect": 6, "rep": 8, "health": 4},
                    "fail_eff": {"rep": -5, "happiness": -6, "health": -2},
                    "tag_succ": "箭无虚发",
                    "tag_fail": "弦断人笑",
                    "is_key": True
                },
                {
                    "text": "远远退开十步再射，赌自己臂力过人，一箭惊人",
                    "risk": "逞强好胜 · 意气用事",
                    "chance": {"base": 40, "int_div": 0, "luck_bonus": 0, "health_bonus": 3},
                    "succ_fb": "箭如流星穿柳而过，满塾哗然，连先生也捋须颔首，说你力气不小。",
                    "fail_fb": "臂力不济，箭软软坠地，你被同窗起了绰号，半月抬不起头来。",
                    "succ_eff": {"rep": 10, "health": 6, "happiness": 5},
                    "fail_eff": {"happiness": -8, "rep": -4, "health": -3},
                    "tag_succ": "一箭惊人",
                    "tag_fail": "力不从心",
                    "is_key": False
                }
            ]
        },
        {
            "period": "童年韶光",
            "title": "随父兄入市贩粟议价",
            "narrative": "秋收之后，父兄推车入市贩粟，命你看守钱袋并学着与买主议价。市中有掮客愿出高价全收，却要赊账至来年。族里正等这笔钱添置铁镰，你也想给自己买一册旧竹书。",
            "choices": [
                {
                    "text": "压价卖给散客，宁可多等半日也要现钱落袋",
                    "risk": "稳妥持家 · 细水长流",
                    "chance": {"base": 78, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                    "succ_fb": "粟卖得干净，钱袋沉实，父兄允你留下一枚小钱，你买回半册旧书。",
                    "fail_fb": "散客挑拣压价，日暮仍有半车粟，父兄沉沉叹息，你懊恼地收摊。",
                    "succ_eff": {"wealth": 8.0, "intellect": 5, "happiness": 4},
                    "fail_eff": {"wealth": -4.0, "happiness": -5},
                    "tag_succ": "粒粟皆金",
                    "tag_fail": "坐失良机",
                    "is_key": True
                },
                {
                    "text": "贪那高价，劝父兄赊给掮客，立下竹券为凭",
                    "risk": "放债图利 · 险中求财",
                    "chance": {"base": 50, "int_div": 0, "luck_bonus": 4, "health_bonus": 0},
                    "succ_fb": "掮客如约践诺，来年送来双倍粟钱，还引你认得几位往来行商。",
                    "fail_fb": "掮客一去无踪，竹券成了废简，家中当年缺了农具，你愧疚良久。",
                    "succ_eff": {"wealth": 14.0, "rep": 5, "luck": 3},
                    "fail_eff": {"wealth": -10.0, "happiness": -6},
                    "tag_succ": "券约得偿",
                    "tag_fail": "券成废简",
                    "is_key": False
                }
            ]
        }
    ],
    [   # 阶段 2 少年分流 (14-16岁)
        {
            "period": "少年分流",
            "title": "负笈远行千里求见名师",
            "narrative": "闻邻郡有位饱学先生开门授徒，讲论百家之说，士子往来如云。你欲负笈前往，然家中田亩将收，父母盼你留下帮工；路远盘缠不足，须卖掉母亲亲手织的一匹布。",
            "choices": [
                {
                    "text": "卖掉那匹布作盘缠，星夜启程，投帖拜入先生门下",
                    "risk": "负笈千里 · 孤注一掷",
                    "chance": {"base": 65, "int_div": 2, "luck_bonus": 4, "health_bonus": 0},
                    "succ_fb": "先生见你衣衫破旧而应答不俗，破例收你为徒，还赐半间草舍安身。",
                    "fail_fb": "先生门徒已满，你被拒之门外，盘缠耗尽，只好沿路乞食徒步归家。",
                    "succ_eff": {"intellect": 14, "rep": 6, "happiness": 5},
                    "fail_eff": {"intellect": 5, "wealth": -8.0, "happiness": -7},
                    "tag_succ": "得列门墙",
                    "tag_fail": "白走一遭",
                    "is_key": True
                },
                {
                    "text": "先留家中收完秋粮，再挑一担新粟去换书简自学",
                    "risk": "耕读两全 · 稳中有进",
                    "chance": {"base": 85, "int_div": 0, "luck_bonus": 0, "health_bonus": 0},
                    "succ_fb": "秋粮入仓，你换回几卷书简，夜里就着灶火抄读，字迹工整可观。",
                    "fail_fb": "白日劳碌，夜里读不上两行便困倒，书简在手边积了一层灰。",
                    "succ_eff": {"intellect": 8, "wealth": 4.0, "happiness": 3},
                    "fail_eff": {"intellect": 2, "happiness": -4},
                    "tag_succ": "耕读自持",
                    "tag_fail": "灯下倦读",
                    "is_key": False
                }
            ]
        },
        {
            "period": "少年分流",
            "title": "里正登门点选徭役",
            "narrative": "郡县征发徭役，里正捧名册登门，你已够岁数，须随众去修驰道、筑边城。同里有人愿出钱代役，只求顶你的名额；父母年迈，你亦想去外头见见世面。",
            "choices": [
                {
                    "text": "接下名册，随队上路，在役夫中多学一门手艺",
                    "risk": "应役远行 · 见闻渐广",
                    "chance": {"base": 72, "int_div": 2, "luck_bonus": 0, "health_bonus": 5},
                    "succ_fb": "你在工地上跟匠人学会夯土与量绳，还结识了一位识字的小吏。",
                    "fail_fb": "烈日之下水土不服，你病倒在工棚，被提前遣送回乡，一路颠簸。",
                    "succ_eff": {"health": 8, "intellect": 6, "rep": 5},
                    "fail_eff": {"health": -10, "happiness": -6, "rep": -3},
                    "tag_succ": "应役有成",
                    "tag_fail": "病卧工棚",
                    "is_key": True
                },
                {
                    "text": "收下那人的钱替家里添牛，自己躲过这趟徭役",
                    "risk": "以钱代役 · 安守家门",
                    "chance": {"base": 100},
                    "succ_fb": "家中添了一头小牛，秋耕省力不少，父母难得舒展了眉头。",
                    "succ_eff": {"wealth": 10.0, "happiness": 5},
                    "tag_succ": "以钱代役",
                    "is_key": False
                }
            ]
        }
    ],
    [   # 阶段 3 成人立志 (17-19岁)
        {
            "period": "成人立志",
            "title": "郡府征辟与边关募兵",
            "narrative": "郡府小吏来乡里访贤，言你若通经明法，可先充书佐；同时边关募兵，斩首有赏，立功可入行伍。两条路摆在眼前：一条稳而慢，一条险而快。父母只盼你平安，却也盼你出息。",
            "choices": [
                {
                    "text": "投身边关，执戈从军，凭军功博一个出身",
                    "risk": "投笔从戎 · 险中求贵",
                    "chance": {"base": 55, "int_div": 2, "luck_bonus": 5, "health_bonus": 4},
                    "succ_fb": "你随军破敌，斩获首级，校尉记你首功，授你什长之职，同伍皆服。",
                    "fail_fb": "初战即伤，你被抬回营帐，虽保住性命，却落下每逢阴雨便痛的旧疾。",
                    "succ_eff": {"rep": 15, "health": 6, "wealth": 8.0},
                    "fail_eff": {"health": -15, "rep": -4, "happiness": -6},
                    "tag_succ": "首功授职",
                    "tag_fail": "负伤而归",
                    "is_key": True
                },
                {
                    "text": "入郡府为书佐，掌文书簿册，在案牍间积累人望",
                    "risk": "案牍立身 · 稳进仕途",
                    "chance": {"base": 88, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                    "succ_fb": "你抄录文书从不出错，郡丞颇赏识，将你举荐给上官，前途渐明。",
                    "fail_fb": "一笔误抄惹出是非，你被罚俸半月，同僚也渐渐疏远了你。",
                    "succ_eff": {"intellect": 10, "rep": 10, "wealth": 6.0},
                    "fail_eff": {"rep": -6, "wealth": -3.0, "happiness": -5},
                    "tag_succ": "文牍见赏",
                    "tag_fail": "误抄见罚",
                    "is_key": False
                }
            ]
        },
        {
            "period": "成人立志",
            "title": "胡商车队过境邀你同行",
            "narrative": "一支胡商驼队过境歇脚，领头的胡商见你通晓数算、口齿伶俐，邀你随队西行贩运丝绸，许诺分你一份厚利。此去关山万里，归期难料；而家中正为你议亲，只待你点头。",
            "choices": [
                {
                    "text": "收拾行囊随商队西行，把命与运押在长路上",
                    "risk": "万里行商 · 富贵险求",
                    "chance": {"base": 50, "int_div": 2, "luck_bonus": 6, "health_bonus": 0},
                    "succ_fb": "驼队平安出关，你贩丝获利数倍，归来时乡人皆出门观看，啧啧称奇。",
                    "fail_fb": "途中遇劫，货物尽失，你徒步东归，瘦得父母几乎认不出你来。",
                    "succ_eff": {"wealth": 25.0, "rep": 8, "luck": 4},
                    "fail_eff": {"wealth": -18.0, "health": -8, "happiness": -8},
                    "tag_succ": "满载而归",
                    "tag_fail": "货失人还",
                    "is_key": True
                },
                {
                    "text": "留在乡里，用积蓄开一间小肆，收售乡邻杂物",
                    "risk": "守土小贾 · 安稳度日",
                    "chance": {"base": 100},
                    "succ_fb": "小肆开张，乡邻常来赊账却也常来照顾，日子过得安稳而有盈余。",
                    "succ_eff": {"wealth": 12.0, "happiness": 6, "rep": 3},
                    "tag_succ": "小肆安稳",
                    "is_key": False
                }
            ]
        }
    ]
]
