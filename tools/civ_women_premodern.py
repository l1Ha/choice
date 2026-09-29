# -*- coding: utf-8 -*-
# 《浮生录》宋韵明清 · 女性专属处境事件（主角为女性时附加进入候选池）

EPOCH_ID = "premodern"

WOMEN_EVENTS = [
    {
        "stage": 2,
        "period": "少年分流",
        "title": "绣绷与账本同摆在灯下",
        "narrative": "你十四岁，家在县前开着间茶铺，父亲赊欠簿上的数总对不齐。母亲把一方绣绷浆好递来，说女儿家针线是立身的本分；父亲却把你的算盘拨得噼啪响，让你替他誊清欠户名录。窗外汴河夜船摇过，母亲的呼吸就在耳后。",
        "choices": [
            {
                "text": "白日随母亲学挑绣，夜里就灯替父亲誊写赊欠簿",
                "risk": "灯下掌算 · 心志渐明",
                "chance": {"base": 66, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                "succ_fb": "半年后你能报出各户欠账，父亲把茶铺流水交你经手，说女娃的算盘也拨得响。",
                "fail_fb": "你错记一笔赊账，赔了几句闲话，却由此懂得了银钱的轻重，账本再没离过手。",
                "succ_eff": {"intellect": 10, "wealth": 5.0, "rep": 4},
                "fail_eff": {"intellect": 6, "happiness": -5, "wealth": -3.0},
                "tag_succ": "掌算立身",
                "tag_fail": "误记账目",
                "is_key": True
            },
            {
                "text": "收了算盘，随母亲一针一线学绣，闲时只翻两页账本",
                "risk": "坐守绣绷 · 女红渐精",
                "chance": {"base": 100},
                "succ_fb": "你的针脚平整，一方帕子换了半升米，夜里照旧把账本上的字认全，母亲看你时眼里有光。",
                "succ_eff": {"wealth": 4.0, "happiness": 6, "intellect": 3},
                "tag_succ": "女红初成",
                "is_key": False
            }
        ]
    },
    {
        "stage": 3,
        "period": "成人立志",
        "title": "媒人踏破门槛，绣坊也在等你回话",
        "narrative": "你十八岁，媒婆第三回上门，说的是绸缎铺少东家，聘礼不薄。你却在瓦舍见过一位女医当街诊脉，也在绣坊见绣娘自己养家。母亲说嫁人最稳当，父亲放下茶碗，只问你一句：你自己拿什么主意？檐下燕子正衔泥。",
        "choices": [
            {
                "text": "婉辞这门亲事，投绣坊拜师，从劈线描样学起，自己挣口饭食",
                "risk": "弃嫁从艺 · 立身有术",
                "chance": {"base": 58, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                "succ_fb": "三年后你绣的百子帐被绸缎庄高价收走，绣坊留你作师傅，媒人再来时，你已能自己开口。",
                "fail_fb": "你手慢赶不出工期，被扣了工钱，只得回家；可那一双描样的好眼力，从此再没还给谁。",
                "succ_eff": {"intellect": 10, "wealth": 9.0, "rep": 8},
                "fail_eff": {"happiness": -6, "wealth": -4.0, "intellect": 5},
                "tag_succ": "绣坊立身",
                "tag_fail": "失工存艺",
                "is_key": True
            },
            {
                "text": "依父母之命受聘定亲，安心备办嫁妆，学管家认亲戚",
                "risk": "顺亲守礼 · 安稳有靠",
                "chance": {"base": 100},
                "succ_fb": "六礼按序走完，你随母亲学掌中馈、认族中亲眷，出嫁那日妆奁齐整，心里并不慌。",
                "succ_eff": {"rep": 6, "wealth": 5.0, "happiness": 5},
                "tag_succ": "六礼既定",
                "is_key": False
            }
        ]
    },
    {
        "stage": 4,
        "period": "青春韶华",
        "title": "花轿三日，婆婆递来一串铜钥匙",
        "narrative": "你二十岁，过门第三日，婆婆把一串黄铜钥匙放进你手心，说米缸、酱缸、后院的鸡鸭从此归你。丈夫常随漕船走货，一年在家不足两月。族中妯娌都拿眼盯着你，这串钥匙能开米柜，也能开临街那间空铺面。",
        "choices": [
            {
                "text": "接下钥匙，先清米盐账目，再把临街铺面收拾出来做点营生",
                "risk": "抛头露面 · 掌铺理事",
                "chance": {"base": 64, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                "succ_fb": "你把铺面盘成针线布头小铺，进出账目清楚，婆婆在外人前头一回夸你，妯娌也收了口。",
                "fail_fb": "头一季进货看走了眼，压了半柜子货，你赔上压箱底的嫁资，却认得了布行的规矩。",
                "succ_eff": {"wealth": 12.0, "intellect": 6, "rep": 6},
                "fail_eff": {"wealth": -7.0, "happiness": -6, "intellect": 6},
                "tag_succ": "柜台立信",
                "tag_fail": "初出受欺",
                "is_key": True
            },
            {
                "text": "只管家中中馈，节俭度日，凡事请婆婆示下",
                "risk": "侍疾守内 · 恭谨无失",
                "chance": {"base": 100},
                "succ_fb": "你把一家吃穿用度料理得齐齐整整，婆媳相安，日子虽无大进项，也没叫人挑出错处。",
                "succ_eff": {"happiness": 7, "rep": 6, "wealth": 3.0},
                "tag_succ": "中馈无失",
                "is_key": False
            }
        ]
    },
    {
        "stage": 5,
        "period": "初涉人世",
        "title": "产房添丁，账上却添一笔亏空",
        "narrative": "你二十四岁，头胎生了个女儿。婆婆脸色淡了三分，说下一胎再求儿子，转身把雇乳母的钱压下。你自己奶孩子，夜里睡不足，白日还得盯着灶头与铺面。丈夫捎信回来说外头周转不开，问你嫁妆里的银镯能否先当出去。",
        "choices": [
            {
                "text": "当掉银镯救急，自己哺乳兼管账，把铺面典期往后延一延",
                "risk": "忍身理事 · 撑持门户",
                "chance": {"base": 60, "int_div": 2, "luck_bonus": 0, "health_bonus": 2},
                "succ_fb": "开春生意回暖，丈夫赎回镯子还添了一对，婆婆见你撑得住家，待你与女儿都亲厚了。",
                "fail_fb": "你熬得气血两亏，孩子也跟着病了一场，铺面终究典了出去；可这家离了你也转不动。",
                "succ_eff": {"wealth": 9.0, "rep": 8, "happiness": 5},
                "fail_eff": {"health": -8, "wealth": -9.0, "happiness": -6},
                "tag_succ": "撑持门户",
                "tag_fail": "熬损识家",
                "is_key": True
            },
            {
                "text": "辞了铺面，专心育儿侍奉婆婆，银镯原封不动留着",
                "risk": "安身养息 · 蓄力待时",
                "chance": {"base": 100},
                "succ_fb": "家中吃用紧了些，你却把孩子与婆婆都照料妥帖，丈夫归家见家宅安稳，心里感念。",
                "succ_eff": {"happiness": 8, "health": 5, "rep": 4},
                "tag_succ": "养息蓄力",
                "is_key": False
            }
        ]
    },
    {
        "stage": 6,
        "period": "成家立业",
        "title": "旧绣坊待盘，你在巷口挂招牌",
        "narrative": "你二十八岁，攒下一笔银钱。原先雇你的绣坊要盘出去，老师傅劝你接手，说有几位旧姊妹肯跟来帮工。可接手要押金，还得请牙行作保、给里正递帖子。丈夫说风险太大，不如把钱留着给儿子将来读书赴考。",
        "choices": [
            {
                "text": "接下绣坊，招旧姊妹帮工，自己描样验货、跑绸缎庄接单",
                "risk": "自立字号 · 担险兴业",
                "chance": {"base": 56, "int_div": 2, "luck_bonus": 4, "health_bonus": 0},
                "succ_fb": "你的绣坊接上绸缎庄的常年活计，四季有单，几位绣娘跟着你吃饭，里正也肯为你作保。",
                "fail_fb": "一单大活被牙行压价，你贴了工钱，绣坊勉强撑着；但你的针法与名号进了城里人的口。",
                "succ_eff": {"wealth": 20.0, "rep": 12, "intellect": 6},
                "fail_eff": {"wealth": -12.0, "happiness": -7, "rep": 5},
                "tag_succ": "招牌立起",
                "tag_fail": "赔工留名",
                "is_key": True
            },
            {
                "text": "不接绣坊，在家设灯课子，教儿子与邻童识字",
                "risk": "督子读书 · 静守本分",
                "chance": {"base": 100},
                "succ_fb": "你白日做针线，夜里教儿子读《千字文》，邻家也送孩子来，束脩虽薄，母子灯下相伴却安稳。",
                "succ_eff": {"intellect": 8, "rep": 6, "happiness": 6},
                "tag_succ": "课子灯前",
                "is_key": False
            }
        ]
    },
    {
        "stage": 7,
        "period": "三十而立",
        "title": "夫行两年无音信，族中议你田产",
        "narrative": "你三十二岁，丈夫随商队北上贩丝，两年没有音信。族中叔伯说妇道人家管不了田产铺面，劝你把陪嫁的三十亩水田并给长房代管，年底分你几石租米。田契就压在妆匣底下，儿子在灯下描红，尚不知家中风波。",
        "choices": [
            {
                "text": "不交田契，自己下乡对租续约，请里正与老账房当面作证",
                "risk": "下乡对租 · 独当门户",
                "chance": {"base": 56, "int_div": 2, "luck_bonus": 4, "health_bonus": 0},
                "succ_fb": "你带着老账房挨户对租，佃户见你清楚明白都肯认你，族叔没了话，你头一回上了族中议事的席。",
                "fail_fb": "族中拦你在祠堂外，几亩租米仍被长房代收；你把契纸贴身收好，等一个说法，也等一个人。",
                "succ_eff": {"wealth": 16.0, "rep": 10, "intellect": 6},
                "fail_eff": {"wealth": -9.0, "happiness": -8, "rep": 4},
                "tag_succ": "契纸在手",
                "tag_fail": "忍待时机",
                "is_key": True
            },
            {
                "text": "让长房代管田产，自己带孩子在城中支个茶摊糊口",
                "risk": "托付族亲 · 退让求安",
                "chance": {"base": 100},
                "succ_fb": "茶摊生意虽小，你与孩子衣食有着，族中也不再为难你，只当你是不争的人。",
                "succ_eff": {"happiness": 6, "wealth": 5.0, "rep": 3},
                "tag_succ": "退守自养",
                "is_key": False
            }
        ]
    },
    {
        "stage": 9,
        "period": "中年险滩",
        "title": "灵幡未撤，族伯已上门算产",
        "narrative": "你四十岁，丈夫病故，棺木刚下葬。族伯带着中人上门，说你无子承嗣，铺面宅子该归族中，只给你一间偏屋养老。你膝下有个十四岁的女儿，另有过继来的六岁侄儿。夜里你翻出房契与丈夫留下的欠条，油灯一直亮到天明。",
        "choices": [
            {
                "text": "抱过继子去县衙立契，请讼师写文书，把房产记在嗣子名下",
                "risk": "争产抗族 · 立契保家",
                "chance": {"base": 50, "int_div": 2, "luck_bonus": 6, "health_bonus": 0},
                "succ_fb": "县衙批了文书，房产归嗣子，你以主母身份代管到他成人，族伯当众下不来台，门户却立住了。",
                "fail_fb": "讼师收了钱不肯尽力，族伯又买通中人，你只保住半间铺面；从那日起，你认得了官文书的轻重。",
                "succ_eff": {"rep": 12, "wealth": 14.0, "intellect": 8},
                "fail_eff": {"wealth": -10.0, "happiness": -9, "intellect": 6},
                "tag_succ": "立契保产",
                "tag_fail": "失产知律",
                "is_key": True
            },
            {
                "text": "立志守节不再嫁，闭门纺绩教女，把家事让出一半求安稳",
                "risk": "守节抚孤 · 退让求安",
                "chance": {"base": 100},
                "succ_fb": "你不与人争，闭门纺绩，女儿学得一手好针线；族中见你安分，不再步步紧逼，家业到底薄了些。",
                "succ_eff": {"happiness": 5, "health": 3, "rep": 8, "wealth": -3.0},
                "tag_succ": "纺绩守门",
                "is_key": False
            }
        ]
    },
    {
        "stage": 12,
        "period": "花甲在望",
        "title": "五十八岁，族中请你主祭修谱",
        "narrative": "你五十八岁，儿子已成家，铺面交媳妇打理。族中重修族谱，请你坐堂，说你一生守住了门户，又带出几房人手艺。修谱先生搁笔问：媳妇名讳、孙女名讳要不要上谱？你手边针线篓里，压着一本记了三十年的家训旧稿。",
        "choices": [
            {
                "text": "口述掌家心得，把持家账目针法写入家训，请先生把媳女名讳一并上谱",
                "risk": "传艺立训 · 家风有继",
                "chance": {"base": 66, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                "succ_fb": "家训写成三十二条，媳妇与孙女的名讳赫然在谱；你教孙女描样记账，说女子手中既要有针，也要有算盘。",
                "fail_fb": "先生摇头说妇人之言不宜入谱，族人议论纷纷，你只把家训抄在自家账本背页；可那句话已教进孙女心里。",
                "succ_eff": {"rep": 14, "intellect": 8, "happiness": 8},
                "fail_eff": {"rep": 3, "happiness": -6, "intellect": 6},
                "tag_succ": "家训入谱",
                "tag_fail": "私录传心",
                "is_key": True
            },
            {
                "text": "谢过族中，只把绣法与账本私下传给媳妇孙女，不争谱上一笔",
                "risk": "传艺于内 · 不争虚名",
                "chance": {"base": 100},
                "succ_fb": "媳妇的针脚越来越像你，孙女的算盘也拨得清脆，你坐在檐下看她们，觉得有些东西不必写在纸上。",
                "succ_eff": {"happiness": 10, "rep": 6, "intellect": 4},
                "tag_succ": "檐下传艺",
                "is_key": False
            }
        ]
    }
]
