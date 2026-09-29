# -*- coding: utf-8 -*-
# 《浮生录》先秦汉唐 · 女性专属处境事件（主角为女性时附加进入候选池）

EPOCH_ID = "ancient"

WOMEN_EVENTS = [
    {
        "stage": 2,
        "period": "少年分流",
        "title": "机杼声中偷听邻塾诵诗",
        "narrative": "母亲在堂屋织缣，你坐机前续麻，隔壁塾中传来童子诵《诗》之声。父亲说女儿家识得几个字便够，学得一手好织，才是他日出嫁的体面妆奁。塾师却隔着篱笆问你，可愿每日来抄半卷书。梭子在你手中一顿。",
        "choices": [
            {
                "text": "白日续麻织缣，夜里就一盏油灯借简抄书",
                "risk": "偷光识字 · 心志渐明",
                "chance": {"base": 62, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                "succ_fb": "塾师见你字迹端正，许你每旬借一卷竹简，母亲虽唠叨，却把灯油多添了一勺。",
                "fail_fb": "灯下久坐，天未亮便被唤去上机，手指发颤断了经线，被母亲罚跪织室半日。",
                "succ_eff": {"intellect": 10, "happiness": 4},
                "fail_eff": {"intellect": 4, "health": -4, "happiness": -5},
                "tag_succ": "偷光识字",
                "tag_fail": "断经受罚",
                "is_key": True
            },
            {
                "text": "收了心思，把一匹绢织得经纬匀密，做母亲的帮手",
                "risk": "坐守机杼 · 女红渐精",
                "chance": {"base": 100},
                "succ_fb": "那匹绢素净如霜，母亲拿在手里反复摩挲，说你已织得出嫁时压箱底的锦。",
                "succ_eff": {"wealth": 3.0, "happiness": 5, "health": 3},
                "tag_succ": "女红初成",
                "is_key": False
            }
        ]
    },
    {
        "stage": 3,
        "period": "成人立志",
        "title": "及笄绾发，医门与媒妁并至",
        "narrative": "你刚行过及笄礼，母亲为你绾发插笄。里中老医妪登门，说她年逾花甲，一身切脉施针的本事无人可传，愿收你为徒。同月媒人也踏破门槛，说城东某户愿以三牲六礼相聘。铜笄映着烛火，两条路都摆在眼前。",
        "choices": [
            {
                "text": "婉辞媒妁，负箧随老医妪认药施针，学一门立身本事",
                "risk": "弃嫁从医 · 立身有术",
                "chance": {"base": 58, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                "succ_fb": "三年后你能独诊妇科诸疾，乡里妇人夜半叩门求医，你背着药囊出诊，身后递来一盏灯。",
                "fail_fb": "乡人以女子行医为怪，寻医者寥寥，你只得替人接生、代煎汤药，勉强度日。",
                "succ_eff": {"intellect": 12, "rep": 8, "wealth": 2.0},
                "fail_eff": {"intellect": 6, "rep": -4, "happiness": -5},
                "tag_succ": "悬壶立身",
                "tag_fail": "见疑乡里",
                "is_key": True
            },
            {
                "text": "依父母之命受聘定亲，备办妆奁，安稳待嫁",
                "risk": "顺亲守礼 · 安稳有靠",
                "chance": {"base": 100},
                "succ_fb": "亲事议定，两家长辈往来如礼，母亲替你收好嫁衣，说这门亲事门当户对，你心下稍安。",
                "succ_eff": {"rep": 6, "wealth": 3.0, "happiness": 4},
                "tag_succ": "六礼既定",
                "is_key": False
            }
        ]
    },
    {
        "stage": 4,
        "period": "青春韶华",
        "title": "妆奁底层压着一册手抄账簿",
        "narrative": "出阁那日，母亲在妆奁底层压了一册手抄账簿与一柄铜尺，说掌家先要识数。夫家在西市开一间绢帛铺，婆婆久病卧床，夫君常随商队走丝路。铺面钥匙挂在门后，婆婆的汤药也在灶上温着，你须先择一头。",
        "choices": [
            {
                "text": "取下钥匙坐柜台，逐匹清点绢帛出入，学做坊市营生",
                "risk": "抛头露面 · 掌铺理事",
                "chance": {"base": 64, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                "succ_fb": "你分得清胡商压价的伎俩，一季下来账面盈余，铺中伙计改口称你一声东家娘子。",
                "fail_fb": "市井牙人欺你年轻妇道，以次充好骗去两匹上绢，婆婆闻讯在病榻上叹气。",
                "succ_eff": {"wealth": 8.0, "intellect": 6, "rep": 5},
                "fail_eff": {"wealth": -6.0, "happiness": -6, "rep": -3},
                "tag_succ": "柜台立信",
                "tag_fail": "初出受欺",
                "is_key": True
            },
            {
                "text": "闭门侍奉婆婆汤药，把内闱诸事料理得齐齐整整",
                "risk": "侍疾守内 · 恭谨无失",
                "chance": {"base": 100},
                "succ_fb": "婆婆病中握你的手，把腕上一只银镯褪下给你，说这个家往后有你，她放心。",
                "succ_eff": {"rep": 8, "happiness": 5, "health": 2},
                "tag_succ": "内闱称贤",
                "is_key": False
            }
        ]
    },
    {
        "stage": 5,
        "period": "初涉人世",
        "title": "产褥未起，账房已候在床边",
        "narrative": "你产后十日，尚在褥中，婆婆便催你起身理事，说家中米缸见底，佃户租粮未齐。夫君在外未归，书信也无。乳母劝你歇息养身，账房婆子却捧着旧账簿立在床边，只等你一句话。窗外新妇的婴儿正哭。",
        "choices": [
            {
                "text": "强撑起身，就着灯核账，遣人去佃户门上催租",
                "risk": "忍身理事 · 撑持门户",
                "chance": {"base": 60, "int_div": 2, "luck_bonus": 0, "health_bonus": 2},
                "succ_fb": "你查出账房私吞两石粟，当场换了人，佃户也补缴了新粮，米缸终于见了底下的新米。",
                "fail_fb": "你冒风出门催租，落下畏寒的病根，往后阴雨天便觉腰膝酸软，账也没催齐。",
                "succ_eff": {"wealth": 5.0, "rep": 6, "intellect": 5},
                "fail_eff": {"health": -10, "happiness": -5},
                "tag_succ": "撑持门户",
                "tag_fail": "落病催租",
                "is_key": True
            },
            {
                "text": "闭门养息满月，将家事暂托婆婆与乳母照看",
                "risk": "安身养息 · 蓄力待时",
                "chance": {"base": 100},
                "succ_fb": "满月后你气色转好，乳汁也足，婴儿白白胖胖，乳母笑说娘子这一个月没白躺。",
                "succ_eff": {"health": 10, "happiness": 6},
                "tag_succ": "养息蓄力",
                "is_key": False
            }
        ]
    },
    {
        "stage": 6,
        "period": "成家立业",
        "title": "三更机杼声里的织造字号",
        "narrative": "你织的锦在市中被胡商认作字号，一冬可换十数贯钱。夫君想添机雇工，把织坊做大，你却怕官家织室抽税、又怕荒了儿子的功课。灯下机杼未歇，儿子捧着《论语》立在机旁，等你听他背完这一章。",
        "choices": [
            {
                "text": "添置织机，雇几名织娘，自立一处织造字号",
                "risk": "扩机营商 · 与夫并立",
                "chance": {"base": 63, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                "succ_fb": "你的锦在坊市挂了名号，凉州胡商先付定金再来取货，家中仓房堆满了待染的生丝。",
                "fail_fb": "官家织室摊派急织，织娘昼夜赶工仍误了期限，赔了工钱，还落下苛待之名。",
                "succ_eff": {"wealth": 12.0, "rep": 6, "intellect": 4},
                "fail_eff": {"wealth": -8.0, "health": -5, "happiness": -6},
                "tag_succ": "织造立业",
                "tag_fail": "摊派折本",
                "is_key": True
            },
            {
                "text": "收敛机坊，亲自陪儿子读经，把指望放在他的前程上",
                "risk": "督子读书 · 静守本分",
                "chance": {"base": 100},
                "succ_fb": "儿子开卷能诵，塾师夸他聪敏，你在一旁补缀他的衣角，心里比织出锦还熨帖。",
                "succ_eff": {"intellect": 8, "happiness": 8, "rep": 3},
                "tag_succ": "课子有成",
                "is_key": False
            }
        ]
    },
    {
        "stage": 7,
        "period": "三十而立",
        "title": "夫君书信断在玉门关外",
        "narrative": "夫君随商队远赴凉州，去岁书信只到玉门便断。族中叔伯觊觎你家田产，说妇人不可为户主，要代管田契。县衙的均田文书上，尚缺一个当家人的画押。儿女尚幼，都仰头望着你，等你拿主意。",
        "choices": [
            {
                "text": "携田契亲赴县衙，依律自请为户主，把田亩一注明白",
                "risk": "对簿公堂 · 独当门户",
                "chance": {"base": 55, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                "succ_fb": "县吏验过契书，文书上写了你的名字，叔伯们拂袖而去，你抱着田契走出衙门，日头正好。",
                "fail_fb": "县吏含糊推诿，说妇人立户须有族中保结，叔伯扣着不画押，田契终究没能落定。",
                "succ_eff": {"rep": 10, "wealth": 6.0, "intellect": 6},
                "fail_eff": {"rep": -5, "happiness": -8, "wealth": -4.0},
                "tag_succ": "自立门户",
                "tag_fail": "为吏所阻",
                "is_key": True
            },
            {
                "text": "请族中长辈代管田产，只求母子安稳，少生争端",
                "risk": "托付族亲 · 退让求安",
                "chance": {"base": 100},
                "succ_fb": "叔伯代管田租，年年按时送来口粮，虽比往年少些，母子几人总算衣食无缺。",
                "succ_eff": {"happiness": 5, "wealth": 2.0, "rep": 2},
                "tag_succ": "退让求安",
                "is_key": False
            }
        ]
    },
    {
        "stage": 9,
        "period": "中年险滩",
        "title": "素衣未除，族人已议分产",
        "narrative": "夫君病故，灵前素衣未除，族中已有人上门议分家产，说寡母难守，不如过继一子承嗣，田宅另作处置。也有旧识托媒来问，愿娶你为继室，带你与儿女离开此地另寻安身。儿子的手一直攥着你的衣角。",
        "choices": [
            {
                "text": "立志守节抚孤，把田契铺账一一执定，不使家业外流",
                "risk": "守节抚孤 · 执契护产",
                "chance": {"base": 58, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                "succ_fb": "你请里正为证，把田宅写在自己与儿子名下，族人无话可说，儿子在你膝下安心读起了书。",
                "fail_fb": "族中以承嗣为由强分了两顷水田，你独力难争，夜里对着灵位坐了很久。",
                "succ_eff": {"rep": 10, "intellect": 6, "happiness": 4},
                "fail_eff": {"wealth": -10.0, "happiness": -10, "rep": -4},
                "tag_succ": "执契守家",
                "tag_fail": "寡母受欺",
                "is_key": True
            },
            {
                "text": "允了再嫁，携儿女随新夫迁居，另立一处门户",
                "risk": "再醮远去 · 另寻生路",
                "chance": {"base": 100},
                "succ_fb": "新夫待儿女不薄，你换了居处，重新支起织机，旧日的邻人只在梦里出现。",
                "succ_eff": {"happiness": 8, "health": 4, "rep": -5},
                "tag_succ": "再醮安身",
                "is_key": False
            }
        ]
    },
    {
        "stage": 12,
        "period": "花甲在望",
        "title": "白发主母灯前口授家训",
        "narrative": "你已是一家长辈，儿孙绕膝，孙女的婚事、儿媳的织坊都来请你定夺。案上那卷家训只写到一半，墨已研好。窗外孙女的机杼声断续传来。是趁天色尚明把织造诀窍与家训一并传下，还是先把田契铺账核清，替儿孙留下明白家底？",
        "choices": [
            {
                "text": "召集儿媳孙女于灯前，把织艺与家训一条条口授下去",
                "risk": "传艺立训 · 家风有继",
                "chance": {"base": 70, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                "succ_fb": "儿媳记下家训，孙女学会挑经断纬的诀窍，那卷家训抄成两份，一份压在机下，一份供在堂前。",
                "fail_fb": "孙女嫌织造劳苦，学了半月便放下梭子，你只得把诀窍写进家训，盼后人再拾起来。",
                "succ_eff": {"intellect": 8, "rep": 10, "happiness": 6},
                "fail_eff": {"happiness": -5, "rep": 3, "intellect": 4},
                "tag_succ": "传艺立训",
                "tag_fail": "后人不继",
                "is_key": True
            },
            {
                "text": "闭门把田契铺账逐一核清，写成一本明白账簿留给儿孙",
                "risk": "核产留账 · 家底分明",
                "chance": {"base": 100},
                "succ_fb": "账目一注明白，哪处田、哪间铺、欠何人多少，儿孙翻看便知，无人再敢含糊。",
                "succ_eff": {"wealth": 6.0, "intellect": 6, "rep": 5},
                "tag_succ": "账目分明",
                "is_key": False
            }
        ]
    }
]
