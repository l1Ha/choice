# -*- coding: utf-8 -*-
# 《浮生录》宋韵明清（公元960年~1911年）人生阶段 0-3

STAGES = [
    [   # 阶段 0 幼年启蒙（5-7岁）
        {
            "period": "幼年启蒙",
            "title": "塾师授三字经，村塾开蒙第一课",
            "narrative": "你年方六岁，父亲提着一方腊肉，领你拜入村塾。塾师姓陈，案上摆着戒尺和一册翻旧的《三字经》，窗外传来邻家舂米的闷响。同窗开蒙都先背这千字，背不出便要在掌心上挨三下。父亲临走只留一句话：家中只供得起一个读书人，你要想清楚。",
            "choices": [
                {
                    "text": "端坐案前逐字跟读，把“人之初”背得滚瓜烂熟，再请塾师圈点",
                    "risk": "勤勉 · 稳妥",
                    "chance": {"base": 75, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                    "succ_fb": "半月后你已能整段背诵，塾师用朱笔在你书页上画了个圈，父亲听说后多要了一碗米酒。",
                    "fail_fb": "你张口结舌，掌心挨了戒尺，回家抱着书箱坐到油灯下，倒把“性本善”记了个牢。",
                    "succ_eff": {"intellect": 10, "rep": 5},
                    "fail_eff": {"intellect": 4, "happiness": -5},
                    "tag_succ": "初通文墨", "tag_fail": "涩口难言",
                    "is_key": True
                },
                {
                    "text": "只顾看窗外货郎的糖人和拨浪鼓，把书页翻得哗哗响",
                    "risk": "贪玩 · 无伤",
                    "chance": {"base": 100},
                    "succ_fb": "一日自在，你尝了半块麦芽糖，也记住了货郎吆喝的调子，夜里竟把它当童谣哼给弟弟听。",
                    "succ_eff": {"happiness": 8, "luck": 3},
                    "tag_succ": "顽童一乐",
                    "is_key": False
                }
            ]
        },
        {
            "period": "幼年启蒙",
            "title": "上元庙会，随母亲看社戏傀儡",
            "narrative": "上元夜，镇上搭起灯棚，母亲用粗布巾裹着你挤进人堆。台上傀儡正演《劈山救母》，锣鼓一响，满街都是卖糖炒栗子和面人的吆喝。父亲给的几枚铜钱还揣在你怀里，母亲却攥紧你的手，说散场前要赶回去给祖母熬药。",
            "choices": [
                {
                    "text": "挣开母亲的手，钻到台前去摸那傀儡的丝线，看它如何抬手",
                    "risk": "好奇 · 冒险",
                    "chance": {"base": 70, "int_div": 0, "luck_bonus": 5, "health_bonus": 0},
                    "succ_fb": "你挤到台角，看清老艺人十指翻飞，回家用竹片和烂布头扎了个小傀儡，逗得祖母咳着也笑了。",
                    "fail_fb": "人潮一涌你跌在青石板上，膝盖磕出淤青，回家被母亲数落，却记住了那句唱词。",
                    "succ_eff": {"happiness": 8, "intellect": 4},
                    "fail_eff": {"health": -4, "happiness": 3},
                    "tag_succ": "眼明手巧", "tag_fail": "跌撞有得",
                    "is_key": False
                },
                {
                    "text": "陪母亲守在药炉边，把庙会听来的故事讲给祖母听",
                    "risk": "孝顺 · 安稳",
                    "chance": {"base": 100},
                    "succ_fb": "祖母听得合眼微笑，赏你一枚磨得发亮的旧铜钱，母亲看你的眼神也柔和了几分。",
                    "succ_eff": {"happiness": 6, "rep": 4},
                    "tag_succ": "膝下承欢",
                    "is_key": False
                }
            ]
        }
    ],

    [   # 阶段 1 童年韶光（9-11岁）
        {
            "period": "童年韶光",
            "title": "随父兄入商号，学记账打算盘",
            "narrative": "镇上的米行兼卖布匹，你十岁那年被父亲领进后柜。掌柜姓吴，先让你磨墨誊账，再把一把旧算盘推过来，珠子被前头学徒摸得发亮。门外有交子铺的伙计来兑钱，柜上银钱出出进进。兄长小声提醒你：账目错一笔，一年工钱都赔不起。",
            "choices": [
                {
                    "text": "每日临一遍账簿，把算盘口诀背熟，宁可晚睡也要对清当日进出",
                    "risk": "勤恳 · 立身",
                    "chance": {"base": 72, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                    "succ_fb": "一季下来你算珠不乱，吴掌柜当众把一本小账交你管，还添了两文月钱。",
                    "fail_fb": "你错记了两笔布价，被罚跪在柜台后重抄账本，手指发酸，却把珠算口诀记死了。",
                    "succ_eff": {"intellect": 10, "wealth": 6.0, "rep": 5},
                    "fail_eff": {"happiness": -6, "intellect": 5},
                    "tag_succ": "心中有账", "tag_fail": "错中学乖",
                    "is_key": True
                },
                {
                    "text": "陪东家少爷斗蛐蛐，替他跑腿买糖糕，图个清闲热闹",
                    "risk": "随和 · 无争",
                    "chance": {"base": 100},
                    "succ_fb": "你与少爷混熟了，常有零嘴分润，也从他口里听来不少城里商号的闲话门道。",
                    "succ_eff": {"happiness": 7, "luck": 3},
                    "tag_succ": "街头人缘",
                    "is_key": False
                }
            ]
        },
        {
            "period": "童年韶光",
            "title": "村中拳师设场，授你扎马步习射",
            "narrative": "村西的打谷场上，一位走镖回乡的老拳师摆开场子，教孩子们扎马步、拉硬弓。弓是竹胎牛筋的，拉满时手臂发抖。同来的孩童多熬不住，跑去看瓦舍说书。拳师眯眼看你，说学武先学忍痛，你若怕苦，趁早回家挑水。",
            "choices": [
                {
                    "text": "咬牙扎稳马步，日日拉弓百次，手心磨破也不肯先收势",
                    "risk": "坚忍 · 强身",
                    "chance": {"base": 65, "int_div": 0, "luck_bonus": 0, "health_bonus": 8},
                    "succ_fb": "两月后你一箭射中草人咽喉，拳师点头收你入正式弟子行列，村人见了都称你有股狠劲。",
                    "fail_fb": "你拉伤了肩，被拳师按在药酒里揉搓，疼得直咧嘴，却把弓步的架势记进了骨头。",
                    "succ_eff": {"health": 10, "rep": 5, "intellect": 3},
                    "fail_eff": {"health": -4, "happiness": -4, "intellect": 3},
                    "tag_succ": "筋骨渐壮", "tag_fail": "带伤知法",
                    "is_key": False
                },
                {
                    "text": "只学几路防身招式，余下时辰去瓦舍听人说书",
                    "risk": "取巧 · 安稳",
                    "chance": {"base": 100},
                    "succ_fb": "你学了三招护身，又听了几回《三国》故事，回家讲给玩伴听，颇受欢迎。",
                    "succ_eff": {"health": 4, "happiness": 6},
                    "tag_succ": "粗通拳脚",
                    "is_key": False
                }
            ]
        }
    ],

    [   # 阶段 2 少年分流（14-16岁）
        {
            "period": "少年分流",
            "title": "县试将近，你提篮赴童子试",
            "narrative": "县衙前贴出考期，你十四岁，父亲翻出压箱底的青布长衫，又托人寻廪生作保。考棚里一人一桌，墨臭混着汗味，试题出自四书。邻座少年进场时被搜出夹带，当场逐出，围观的人指指点点。父亲只说了一句：若考不中，明年就得下田或入铺。",
            "choices": [
                {
                    "text": "闭门苦读经义，把历年考题逐篇揣摩，孤注一掷赴考",
                    "risk": "拼搏 · 险中",
                    "chance": {"base": 55, "int_div": 2, "luck_bonus": 5, "health_bonus": 0},
                    "succ_fb": "榜上你的名字列在末等，虽未中秀才，县学先生却记住了你，愿留你在塾中帮教蒙童。",
                    "fail_fb": "卷上文章写偏了题，你落榜归家，父亲没骂你，只把一盏灯留到深夜，让你自己想明白。",
                    "succ_eff": {"intellect": 12, "rep": 8},
                    "fail_eff": {"intellect": 6, "happiness": -8},
                    "tag_succ": "榜上有名", "tag_fail": "落榜知耻",
                    "is_key": True
                },
                {
                    "text": "与乡邻结伴同行，只求稳妥应考，考完便回家帮忙收麦",
                    "risk": "平稳 · 务实",
                    "chance": {"base": 100},
                    "succ_fb": "你规规矩矩考完，回来赶上割麦，父亲看你惜力气又肯下力，心里踏实了几分。",
                    "succ_eff": {"happiness": 5, "intellect": 4, "wealth": 3.0},
                    "tag_succ": "安分守拙",
                    "is_key": False
                }
            ]
        },
        {
            "period": "少年分流",
            "title": "家道中落，父亲欲送你投师学艺",
            "narrative": "家里为祖母治病借了印子钱，父亲把几亩薄田抵了出去。饭桌上他沉默半晌，说读书这条道恐怕走不通了，城里木匠铺正收学徒，三年出师，管饭不给工钱。你床头还压着读了一半的《千字文》，油灯芯烧得只剩一点亮，窗外雨敲着瓦。",
            "choices": [
                {
                    "text": "次日便去木匠铺叩头拜师，从拉大锯、刨木料学起，三年不悔",
                    "risk": "务实 · 立身",
                    "chance": {"base": 78, "int_div": 0, "luck_bonus": 0, "health_bonus": 5},
                    "succ_fb": "师父见你手稳心细，半年便许你上刨台，说这门手艺饿不死人，你也第一次挣回自己的工钱。",
                    "fail_fb": "你刨坏了东家的门板，赔了半月工钱，师父骂你手笨，你却把那道木纹记了一辈子。",
                    "succ_eff": {"health": 5, "wealth": 8.0, "rep": 5},
                    "fail_eff": {"wealth": -4.0, "happiness": -6, "intellect": 4},
                    "tag_succ": "一技在手", "tag_fail": "赔钱长艺",
                    "is_key": True
                },
                {
                    "text": "白天替人挑水打短工，夜里就着残灯把旧书再读一遍",
                    "risk": "倔强 · 苦撑",
                    "chance": {"base": 45, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                    "succ_fb": "塾中先生听说你夜读不辍，让你白日抄书换米，你竟又摸回了笔墨生计。",
                    "fail_fb": "连熬几夜你病倒了，草药钱花去大半积蓄，书到底没能接着读下去。",
                    "succ_eff": {"intellect": 10, "rep": 6},
                    "fail_eff": {"health": -10, "wealth": -6.0, "intellect": 5},
                    "tag_succ": "灯下不辍", "tag_fail": "贫病折志",
                    "is_key": False
                }
            ]
        }
    ],

    [   # 阶段 3 成人立志（17-19岁）
        {
            "period": "成人立志",
            "title": "晋商票号招学徒，你随乡人入号",
            "narrative": "镇上几位老西儿回乡招人，说票号要在南边开分庄，收识字的少年学汇兑。你十七岁，能写会算，正合他们眼缘。号中规矩极严：白日算银、誊写汇票，夜里还要习字，三年不得私留一文钱。同乡有人劝你留下守几亩田，安稳一生。",
            "choices": [
                {
                    "text": "入号立契，苦练珠算与汇券笔法，随掌柜远行分庄见世面",
                    "risk": "远行 · 搏业",
                    "chance": {"base": 60, "int_div": 2, "luck_bonus": 6, "health_bonus": 0},
                    "succ_fb": "三年后你已能独当一面，一封汇票在你笔下分毫不差，掌柜许你跟着走南闯北，见识了白银的斤两。",
                    "fail_fb": "分庄遇上官府封号查账，你被扣了半年工钱，虽失了财，却学会了如何与官面周旋。",
                    "succ_eff": {"intellect": 8, "wealth": 18.0, "rep": 8},
                    "fail_eff": {"wealth": -8.0, "happiness": -6, "intellect": 6},
                    "tag_succ": "汇通四方", "tag_fail": "折银长识",
                    "is_key": True
                },
                {
                    "text": "留在本号打杂，替老掌柜抄信记账，静观行情再作打算",
                    "risk": "守成 · 观望",
                    "chance": {"base": 100},
                    "succ_fb": "你在总号站住了脚，识得银钱往来的门道，虽未出门，也攒下了一份踏实名声。",
                    "succ_eff": {"intellect": 6, "wealth": 8.0, "rep": 4},
                    "tag_succ": "稳坐总号",
                    "is_key": False
                }
            ]
        },
        {
            "period": "成人立志",
            "title": "粤海开市，十三行招记账伙计",
            "narrative": "海禁稍有松弛，广州城外十三行的商馆又热闹起来。有行商到内地招识字伙计，管账、验货、招呼番客。你十九岁，正想立一番事业，族中长辈却摇头：与番人打交道，弄不好便倾家荡产，还落个通番的名声。行商给的工钱，是你眼下活计的三倍。",
            "choices": [
                {
                    "text": "应招南下，学说几句番话，替行商验货记账，摸清海上货价",
                    "risk": "闯荡 · 逐利",
                    "chance": {"base": 58, "int_div": 2, "luck_bonus": 8, "health_bonus": 0},
                    "succ_fb": "你记清了茶叶与生丝的行情，一季下来分得花红，行商许你独自押货看仓，眼界大开。",
                    "fail_fb": "一船货物遇上风浪延误，你被扣了月钱，还替人赔了亏空，好在学明白了海船的凶险。",
                    "succ_eff": {"wealth": 25.0, "intellect": 8, "luck": 5},
                    "fail_eff": {"wealth": -12.0, "happiness": -7, "intellect": 5},
                    "tag_succ": "行商起家", "tag_fail": "亏空识险",
                    "is_key": True
                },
                {
                    "text": "谢过行商，留在乡中守着祖业，农闲时教几个蒙童识字",
                    "risk": "安分 · 守拙",
                    "chance": {"base": 100},
                    "succ_fb": "你守着几亩田与一屋旧书，日子清淡却无风波，乡邻都称你是个稳妥后生。",
                    "succ_eff": {"happiness": 8, "rep": 6, "wealth": 4.0},
                    "tag_succ": "耕读传家",
                    "is_key": False
                }
            ]
        }
    ]
]
