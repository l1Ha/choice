# -*- coding: utf-8 -*-
# 《浮生录》人生阶段数据 · 先秦汉唐 · 阶段 4-7

STAGES = [
    [  # 阶段 4 青春韶华 (20-22岁)
        {
            "period": "青春韶华",
            "title": "县廷征召，试为刀笔小吏",
            "narrative": "乡啬夫传话过来，县廷缺一名书佐，要识字的年轻人前去应试。你案头摊着几卷残简，父亲却盼你留在家中照看田亩与年迈的祖母。同里已有人在县衙当差，衣冠整齐，说话也硬气。去试，或许能踏上吏途；不去，家中秋收便少一双手。",
            "choices": [
                {
                    "text": "收拾好简牍笔墨，天明便去县廷报名应考书佐",
                    "risk": "求名有路 · 失家劳力",
                    "chance": {"base": 65, "int_div": 2, "luck_bonus": 3, "health_bonus": 0},
                    "succ_fb": "主吏考你书算，见你小篆工整，当场录为书佐，递来一枚竹简作凭信。",
                    "fail_fb": "你小篆尚可，算数却慢，主吏摇头让你回去，祖母的汤药钱仍无着落。",
                    "succ_eff": {"intellect": 8, "rep": 6, "wealth": 3},
                    "fail_eff": {"intellect": 3, "happiness": -5},
                    "tag_succ": "刀笔初试",
                    "tag_fail": "铩羽而归",
                    "is_key": True
                },
                {
                    "text": "先留在家中操持农事，夜里就着豆灯自读律令",
                    "risk": "守家尽责 · 缓图后计",
                    "chance": {"base": 100},
                    "succ_fb": "你白日扶犁，夜里诵律，乡邻都称你稳重，来日征召必先念及你。",
                    "succ_eff": {"happiness": 5, "rep": 4, "intellect": 4},
                    "tag_succ": "耕读自守",
                    "is_key": False
                }
            ]
        },
        {
            "period": "青春韶华",
            "title": "负笈远游，拜入名师门下",
            "narrative": "听说郡中有位老儒开门授徒，讲《春秋》与律令，弟子多被州府辟用。你背着一箱旧简走了三日，可拜师需奉束脩，家中只凑出一匹粗帛。同舍生多是豪族子弟，衣冠整齐，谈笑间已互称表字。留下，或可博一个出身；折返，则这三日脚程白费。",
            "choices": [
                {
                    "text": "情愿奉上一匹粗帛，甘居下座替师门抄书抵束脩",
                    "risk": "虚心求教 · 以劳补拙",
                    "chance": {"base": 70, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                    "succ_fb": "老儒见你抄录细密无误，留你居下舍，命你专掌经卷，同门也来借问。",
                    "fail_fb": "抄错三处经文，被罚立在庭中背诵，粗帛已收，颜面也丢了半截。",
                    "succ_eff": {"intellect": 10, "rep": 5},
                    "fail_eff": {"intellect": 4, "happiness": -6},
                    "tag_succ": "师门垂青",
                    "tag_fail": "当庭受责",
                    "is_key": True
                },
                {
                    "text": "不拜师门，只在市旁赁屋替旅人代写书信契券",
                    "risk": "自谋生计 · 学无常师",
                    "chance": {"base": 100},
                    "succ_fb": "你替旅人写家书、替乡邻写契券，铜钱虽少，识字的名声却传开了。",
                    "succ_eff": {"wealth": 5, "rep": 3, "happiness": 3},
                    "tag_succ": "市井笔耕",
                    "is_key": False
                }
            ]
        }
    ],
    [  # 阶段 5 初涉人世 (23-25岁)
        {
            "period": "初涉人世",
            "title": "边郡征戍，登烽燧望狼烟",
            "narrative": "县里张榜，北边烽燧缺戍卒，去者免一岁赋，归来可叙功受爵。你新婚未久，妻子腹中已有身孕。里正说，边地苦寒，胡骑时来劫掠，也有人一去三年杳无音信。应征，或能凭军功脱去布衣；不去，则要纳钱代役，家中粟米本就见底。",
            "choices": [
                {
                    "text": "应征北上，把自己的姓名报入戍卒名册，随队出发",
                    "risk": "军功可期 · 生死难卜",
                    "chance": {"base": 55, "int_div": 2, "luck_bonus": 4, "health_bonus": 4},
                    "succ_fb": "你随队登燧瞭望，一日烽火骤起，你率先举炬示警，都尉记你一功。",
                    "fail_fb": "深秋一场疫病，同伍倒了三人，你虽活下来，归期又拖了半年。",
                    "succ_eff": {"rep": 8, "health": 3, "wealth": 6},
                    "fail_eff": {"health": -10, "happiness": -8, "wealth": 3},
                    "tag_succ": "烽燧立功",
                    "tag_fail": "边地病归",
                    "is_key": True
                },
                {
                    "text": "留在乡里，替戍边之人纳粟代役并代为照料其家",
                    "risk": "破财免行 · 结好乡邻",
                    "chance": {"base": 100},
                    "succ_fb": "你典卖半亩薄田完纳代役钱，乡邻念你信义，常来帮你收割。",
                    "succ_eff": {"rep": 6, "wealth": -8, "happiness": 4},
                    "tag_succ": "信义乡里",
                    "is_key": False
                }
            ]
        },
        {
            "period": "初涉人世",
            "title": "随商队西行，贩缯帛于关市",
            "narrative": "姑臧来的商队缺一个记账的伙计，说走一趟河西，缯帛换回玉与苜蓿，利可数倍。妻子不愿你远行，族中长辈却想借你探探关市行情。此行要过边关，路上有盗匪，也有盘查的关吏。若得利，家业可起；若折本，连聘礼的欠账都还不上。",
            "choices": [
                {
                    "text": "随队西行，一路上替商主记账、验货、押运缯帛",
                    "risk": "重利远行 · 关山险阻",
                    "chance": {"base": 60, "int_div": 2, "luck_bonus": 4, "health_bonus": 3},
                    "succ_fb": "你在关市议价得当，缯帛脱手极快，商主分你两匹绢，另许下次同行。",
                    "fail_fb": "半途遇盗，货物折了大半，商主未责你，你却分文未得，还病了一场。",
                    "succ_eff": {"wealth": 18, "intellect": 6, "rep": 4},
                    "fail_eff": {"wealth": -12, "health": -6, "happiness": -5},
                    "tag_succ": "关市获利",
                    "tag_fail": "折货空归",
                    "is_key": True
                },
                {
                    "text": "不涉远途，只在县邑集市之间做些零碎转贩生意",
                    "risk": "小本经营 · 稳中求进",
                    "chance": {"base": 100},
                    "succ_fb": "你收乡下的布、卖城里的盐，薄利细攒，一年下来也添了两只健牛。",
                    "succ_eff": {"wealth": 7, "happiness": 3},
                    "tag_succ": "小贩积财",
                    "is_key": False
                }
            ]
        }
    ],
    [  # 阶段 6 成家立业 (26-29岁)
        {
            "period": "成家立业",
            "title": "纳采问名，聘礼尚差一筹",
            "narrative": "你与邻县女子相看已定，媒人来回奔走，只差最后一道纳征。女方家说，聘礼不论厚薄，只求体面；可你清点家中，粟不足十石，布只两匹。族兄劝你借债备礼，以免失了脸面；也有人劝你据实相告，莫为一时风光耗尽来年的种粮。",
            "choices": [
                {
                    "text": "向族兄借贷，也要备齐聘礼风风光光地纳征",
                    "risk": "顾全颜面 · 负债成婚",
                    "chance": {"base": 72, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                    "succ_fb": "女方家见礼数周全，欣然许婚，乡里都说这门亲事体面，你也得了个贤内助。",
                    "fail_fb": "债主催得紧，婚后第一年你常为还钱奔忙，妻子虽无怨言，你心里不好受。",
                    "succ_eff": {"happiness": 12, "rep": 6, "wealth": -10},
                    "fail_eff": {"happiness": 4, "wealth": -16, "rep": 2},
                    "tag_succ": "六礼告成",
                    "tag_fail": "婚成债重",
                    "is_key": True
                },
                {
                    "text": "据实相告，以自家织的两匹布和十石粟为礼",
                    "risk": "坦诚量力 · 平淡成礼",
                    "chance": {"base": 100},
                    "succ_fb": "女方父母见你诚实持重，反赞你可靠，婚事从简而办，两家都无怨言。",
                    "succ_eff": {"happiness": 9, "rep": 4},
                    "tag_succ": "布粟为聘",
                    "is_key": False
                }
            ]
        },
        {
            "period": "成家立业",
            "title": "族中分家，一卷薄田起争执",
            "narrative": "父亲过世，族老主持析产。兄长的儿子多、人口重，主张按口分田；你只一房妻小，按理可分较肥的近水田。族老却劝你顾全兄弟情面，先让一步。争，或可多得几亩活命田；让，则要在族中落个谦让的名声。可来年春耕，种子和耕牛都等着用钱。",
            "choices": [
                {
                    "text": "据理力争，务必请族老依据律令与旧契当众明断",
                    "risk": "寸土必争 · 伤了手足",
                    "chance": {"base": 68, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                    "succ_fb": "族老翻出旧契，判你分得近水田两段，秋收丰足，妻子终于展颜。",
                    "fail_fb": "兄长当众骂你刻薄，田虽多争半亩，族中却许久不与你往来。",
                    "succ_eff": {"wealth": 12, "rep": 4, "happiness": -3},
                    "fail_eff": {"wealth": 5, "rep": -8, "happiness": -8},
                    "tag_succ": "依法得田",
                    "tag_fail": "析产失和",
                    "is_key": True
                },
                {
                    "text": "主动让出近水肥田，另择坡地并多要农具",
                    "risk": "谦让全亲 · 另图桑麻",
                    "chance": {"base": 100},
                    "succ_fb": "你让了好田却得全套农具与耕牛，坡地种桑养蚕，来年另有一份进项。",
                    "succ_eff": {"rep": 8, "happiness": 6, "wealth": -3},
                    "tag_succ": "让田得牛",
                    "is_key": False
                }
            ]
        }
    ],
    [  # 阶段 7 三十而立 (30-33岁)
        {
            "period": "三十而立",
            "title": "郡国举荐，孝廉之名在望",
            "narrative": "郡守下教，要举一名孝廉入京对策，乡里议论纷纷，数你的孝行与文书最好。可另一家是本地豪族的子弟，门生故吏众多，已暗中打点。郡中主吏暗示，你若肯送些土物，事便可成。举，则一生仕途由此起；不举，则数年耕读尽付流水。",
            "choices": [
                {
                    "text": "备下薄礼拜访郡中主吏，请其在郡守面前美言",
                    "risk": "通融求举 · 名节有损",
                    "chance": {"base": 58, "int_div": 2, "luck_bonus": 4, "health_bonus": 0},
                    "succ_fb": "郡守果以你为孝廉，车马入京对策，你第一次望见宫阙的飞檐。",
                    "fail_fb": "主吏收了礼却不认账，豪族子弟得举，你反落下结交吏胥的话柄。",
                    "succ_eff": {"rep": 10, "intellect": 6, "wealth": -5},
                    "fail_eff": {"rep": -10, "happiness": -8, "wealth": -8},
                    "tag_succ": "举为孝廉",
                    "tag_fail": "求举见欺",
                    "is_key": True
                },
                {
                    "text": "不送一物，只把历年劝农赈济的簿册呈给郡守",
                    "risk": "以实自荐 · 静候公论",
                    "chance": {"base": 100},
                    "succ_fb": "郡守翻阅簿册，见你历年赈济灾民条条有据，叹你朴实，将你列入备选。",
                    "succ_eff": {"rep": 7, "intellect": 4, "happiness": 4},
                    "tag_succ": "簿册自明",
                    "is_key": False
                }
            ]
        },
        {
            "period": "三十而立",
            "title": "岁大饥，流民叩门求一斗粟",
            "narrative": "连月大旱，邻郡流民成群过境，篷车停在里门外。你家仓中尚存粟三十石，是来年春耕与全家口粮。里正说，郡府令各户出粟赈济，可事后未必补偿；也有人说，此时开仓能结下四方人望，来日或有大用。妻子抱着幼子，望着你的脸不说话。",
            "choices": [
                {
                    "text": "开仓出粟十石赈济流民，并邀壮者留下垦荒",
                    "risk": "散粟结众 · 来年恐饥",
                    "chance": {"base": 70, "int_div": 2, "luck_bonus": 3, "health_bonus": 0},
                    "succ_fb": "流民感你恩义，数十壮者留下替你开垦荒坡，里中皆称你有长者之风。",
                    "fail_fb": "流民一哄而散，粟去了大半，来年春耕你只得向族兄借种。",
                    "succ_eff": {"rep": 12, "happiness": 6, "wealth": -10},
                    "fail_eff": {"wealth": -16, "happiness": -6, "rep": 3},
                    "tag_succ": "散粟得众",
                    "tag_fail": "粟尽人散",
                    "is_key": True
                },
                {
                    "text": "只在门外施粥三日，其余时候闭门护住自家粮种",
                    "risk": "量力施惠 · 先保家门",
                    "chance": {"base": 100},
                    "succ_fb": "你施粥三日全了情面，又保住大半粮种，春耕未误，一家安然。",
                    "succ_eff": {"wealth": 2, "rep": 3, "happiness": 2},
                    "tag_succ": "施粥护仓",
                    "is_key": False
                }
            ]
        }
    ]
]
