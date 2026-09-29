EPOCH_ID = "modern"

WOMEN_EVENTS = [
    {
        "stage": 2,
        "period": "少年分流",
        "title": "缠脚布解开的那一日",
        "narrative": "民国六年，镇上的女学堂挂出新匾，先生挨家劝女孩放脚剪发。母亲把缠脚布藏在箱底，说缠过的脚才嫁得出去。你十四岁了，能自己走三里土路去报名。",
        "choices": [
            {
                "text": "当着母亲解开缠脚布，剪去发辫，去女学堂报名识字",
                "risk": "众叛亲离 · 前程未卜",
                "chance": {"base": 65, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                "succ_fb": "先生给你一支铅笔，你在糙纸上写下自己的名字。放学路上脚还疼，可步子第一次由你自己迈。",
                "fail_fb": "母亲把你锁在灶房三天，字没认成几个。可缠脚布被你烧了，那双脚再没裹回去。",
                "succ_eff": {"intellect": 12, "rep": 4},
                "fail_eff": {"happiness": -6, "intellect": 4},
                "tag_succ": "开蒙识字",
                "tag_fail": "骨气未折",
                "is_key": True
            },
            {
                "text": "托城里亲戚进纱厂当童工，按月把铜板交回家里",
                "risk": "任劳任怨 · 自食其力",
                "chance": {"base": 100},
                "succ_fb": "你成了车间里最小的一个，日日站十二个钟头，月底把工钱攥出汗交给母亲。手粗了，米缸满了。",
                "succ_eff": {"wealth": 9, "health": -5, "happiness": -3},
                "tag_succ": "自食其力",
                "is_key": False
            }
        ]
    },
    {
        "stage": 3,
        "period": "成人立志",
        "title": "师范榜下，有人相看",
        "narrative": "县里女子师范贴出招生榜，不收学费还管膳宿，毕业能当教员。夜里媒人上门，说城南米行东家看中你，定了亲便不愁吃穿。母亲把两人的八字压在灯下。",
        "choices": [
            {
                "text": "先偷偷去投考女子师范，考中了再向家里开口",
                "risk": "先斩后奏 · 前路未定",
                "chance": {"base": 58, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                "succ_fb": "榜单上有你的名字。你抱着铺盖进校门，穿黑裙白衫，第一次听见女先生讲科学与人当自立。",
                "fail_fb": "差了几名落榜，家里已经收下聘礼。你哭着求母亲宽限一年，答应再考，母亲到底点了头。",
                "succ_eff": {"intellect": 14, "rep": 5, "happiness": 6},
                "fail_eff": {"happiness": -7, "rep": -3, "intellect": 4},
                "tag_succ": "榜上有名",
                "tag_fail": "一年之约",
                "is_key": True
            },
            {
                "text": "由着家里定下亲事，把聘礼省下来供弟弟念书",
                "risk": "顺亲安分 · 各得其所",
                "chance": {"base": 100},
                "succ_fb": "红烛下你拜了堂，丈夫待你平和。夜里你把师范的招生简章折好，夹进陪嫁的箱底。",
                "succ_eff": {"wealth": 10, "happiness": 3, "rep": 4},
                "tag_succ": "安分持家",
                "is_key": False
            }
        ]
    },
    {
        "stage": 4,
        "period": "青春韶华",
        "title": "救护棚前的那张桌",
        "narrative": "战事吃紧，红十字会来厂里招救护员，说上前线抬担架、缝绷带。同宿舍的秀兰报了名。母亲托人带信，叫你别去，家里正在替你说一门稳妥的亲事。",
        "choices": [
            {
                "text": "瞒着家里报名随救护队北上，学包扎、止血与抬担架",
                "risk": "生死难料 · 家书难递",
                "chance": {"base": 55, "int_div": 2, "luck_bonus": 0, "health_bonus": 6},
                "succ_fb": "你在炮声里学会用盐水洗伤口，也背得动半袋米。有个伤兵叫你一声同志，你记了一辈子。",
                "fail_fb": "路遇溃兵，队伍散了。你护送两个伤员绕回后方，瘦脱了形，却从没后悔走过这一趟。",
                "succ_eff": {"rep": 12, "health": 5, "intellect": 6},
                "fail_eff": {"health": -8, "rep": 6, "happiness": -4},
                "tag_succ": "临危受命",
                "tag_fail": "风尘仆仆",
                "is_key": True
            },
            {
                "text": "留在城里应下小学教员的差事，按月领薪养家",
                "risk": "执鞭立身 · 安分守己",
                "chance": {"base": 100},
                "succ_fb": "三十几个孩子齐声喊先生。薪米不厚，可每月发薪那天，你都能给母亲捎两块银元回去。",
                "succ_eff": {"rep": 8, "wealth": 6, "intellect": 5},
                "tag_succ": "执鞭立身",
                "is_key": False
            }
        ]
    },
    {
        "stage": 5,
        "period": "初涉人世",
        "title": "产假只批了四十五天",
        "narrative": "厂里催你回车间，说细纱岗缺人；婆婆说孩子还小，女人的本分在灶台边。产假只批四十五天，厂办托儿所一个月要两块银元，你的工钱刚够三块。",
        "choices": [
            {
                "text": "把孩子送进厂办托儿所，按期回车间保住岗位",
                "risk": "骨肉牵挂 · 饭碗要紧",
                "chance": {"base": 62, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                "succ_fb": "你白天挡车接线头，夜里给孩子喂奶。工段长在墙上记你满勤，工资袋上第一次印着你自己的名字。",
                "fail_fb": "孩子夜里发烧，你请假三天，岗位被调去看仓库。工钱少了，可你守住了做母亲的那份心。",
                "succ_eff": {"wealth": 8, "rep": 7, "happiness": 4},
                "fail_eff": {"happiness": -6, "wealth": -5, "rep": -3},
                "tag_succ": "双肩挑担",
                "tag_fail": "母职难舍",
                "is_key": True
            },
            {
                "text": "夜里去工人夜校识字，跟着先生学记账与算术",
                "risk": "灯下苦读 · 日久见功",
                "chance": {"base": 100},
                "succ_fb": "一年下来你认了两千字，能自己读厂里的通知。结业那天，先生把一支钢笔插在你衣襟上。",
                "succ_eff": {"intellect": 12, "rep": 5},
                "tag_succ": "勤学不辍",
                "is_key": False
            }
        ]
    },
    {
        "stage": 6,
        "period": "成家立业",
        "title": "黑板一侧写上你的名字",
        "narrative": "建国后厂里评先进生产者，要挑人去学新式细纱机。名单上有你，可要脱产去城里学三个月。丈夫在码头扛包，两个孩子要接送，婆婆说她只认得灶火不认得机器。",
        "choices": [
            {
                "text": "报名技术培训班，脱产三个月学细纱机维修",
                "risk": "两头难顾 · 技术在手",
                "chance": {"base": 60, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                "succ_fb": "结业考核你拿了第一，回厂当上技术员，工装口袋别着卡尺。机器一出毛病，女工们都来喊你。",
                "fail_fb": "头一个月孩子病了两回，你中途退学。回车间照旧挡车，可师傅教的每一句口诀你都记着。",
                "succ_eff": {"intellect": 12, "rep": 10, "wealth": 6},
                "fail_eff": {"happiness": -5, "intellect": 5, "rep": -2},
                "tag_succ": "技压群芳",
                "tag_fail": "半途折返",
                "is_key": True
            },
            {
                "text": "和丈夫商量好，家务轮着做，孩子轮着接送",
                "risk": "夫妻同心 · 家事分摊",
                "chance": {"base": 100},
                "succ_fb": "他笨手笨脚地学擀面，孩子笑作一团。街坊有闲话，说你家男人怕老婆，可你晚上能歇歇脚了。",
                "succ_eff": {"happiness": 8, "rep": 3, "health": 4},
                "tag_succ": "同担家事",
                "is_key": False
            }
        ]
    },
    {
        "stage": 7,
        "period": "三十而立",
        "title": "公社广播喊你去接生",
        "narrative": "公社要办卫生员训练班，学接生、认草药、打针。队长说你是妇女队长，最合适。可小女儿刚断奶，家里一摊事；队里记工分的旧章程又正惹人议论。",
        "choices": [
            {
                "text": "报名去县里学接生，背上药箱走遍十里八村",
                "risk": "夜路难行 · 人命关天",
                "chance": {"base": 64, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                "succ_fb": "头一回接生遇上难产，你守着产妇一整夜。鸡叫时孩子落地，那家人煮了两个荷包蛋，叫你恩人。",
                "fail_fb": "一次雪夜出诊，你滑进沟里扭了脚，药箱也摔开。可你还是爬到产妇家，只从此落了腿疼的毛病。",
                "succ_eff": {"rep": 14, "intellect": 8, "health": -3},
                "fail_eff": {"health": -8, "rep": 8, "happiness": -3},
                "tag_succ": "赤脚行医",
                "tag_fail": "雪夜失足",
                "is_key": True
            },
            {
                "text": "带头在队里争同工同酬，替妇女去评先进生产者",
                "risk": "得罪众人 · 出头招风",
                "chance": {"base": 55, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                "succ_fb": "记工分的老会计改了章程，妇女干一样的活记一样的分。你的照片贴上光荣榜，写着劳动模范。",
                "fail_fb": "有人背地里说你争强好胜，工分照旧少记两成。你没再吵，只把每天割的亩数记在小本上。",
                "succ_eff": {"rep": 12, "wealth": 6, "happiness": 5},
                "fail_eff": {"rep": -5, "happiness": -6},
                "tag_succ": "巾帼不让",
                "tag_fail": "人言可畏",
                "is_key": False
            }
        ]
    },
    {
        "stage": 9,
        "period": "中年险滩",
        "title": "锣鼓响时，去与留的抉择",
        "narrative": "运动来了，有人贴出大字报，说你出身不好、又讲过技术不要讲政治。文件下来，一批人要下放干校。丈夫劝你主动报名避风头，可你刚接手车间质检，走了这道关怕没人守。",
        "choices": [
            {
                "text": "主动报名下放干校，避过风头，保全一家老小",
                "risk": "前路茫茫 · 屈身求全",
                "chance": {"base": 72, "int_div": 0, "luck_bonus": 0, "health_bonus": 0},
                "succ_fb": "干校的田埂上你学会了插秧。清早收工，你还在纸上默写公差表。两年后调回城，手上的茧没白长。",
                "fail_fb": "下放第三年丈夫病倒，你两头奔波。回城时岗位没了，被安排去仓库点数，工龄却还是连着的。",
                "succ_eff": {"intellect": 8, "health": -4, "rep": -2},
                "fail_eff": {"health": -8, "happiness": -6, "wealth": -4},
                "tag_succ": "随遇而安",
                "tag_fail": "磋磨经年",
                "is_key": False
            },
            {
                "text": "坚持留在车间守住质检岗，任凭大字报贴满墙",
                "risk": "孤立无援 · 坚守到底",
                "chance": {"base": 45, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                "succ_fb": "你照旧每天量纱的支数，一笔笔记在本上。后来有人翻出那些记录，替厂里挡下一桩大事故。",
                "fail_fb": "你被停了职，扫了半年厕所。可每天路过车间，你还是忍不住朝纱锭的方向多看上一眼。",
                "succ_eff": {"rep": 10, "intellect": 8, "happiness": 4},
                "fail_eff": {"happiness": -8, "rep": -6, "health": -4},
                "tag_succ": "守岗如初",
                "tag_fail": "蒙尘不屈",
                "is_key": True
            }
        ]
    },
    {
        "stage": 12,
        "period": "花甲在望",
        "title": "冬夜里，等一张准考证",
        "narrative": "恢复高考的消息从广播里传出来，儿子翻出压箱底的课本。厂里要你办退休，说再干两年就该让位给年轻人。你摸着车间的机器，又看着灯下念书的儿子。",
        "choices": [
            {
                "text": "办了退休，白天带孙辈，夜里陪儿子复习功课",
                "risk": "含饴弄孙 · 灯下守望",
                "chance": {"base": 100},
                "succ_fb": "你守着一盏煤油灯，给儿子端热水、削铅笔。放榜那天他跑回家，喊妈我考上了，你手里的针线掉在地上。",
                "succ_eff": {"happiness": 14, "rep": 8},
                "tag_succ": "灯下守望",
                "is_key": False
            },
            {
                "text": "跟厂里说推迟退休，带出最后一批青年女工",
                "risk": "薪火相传 · 去留两难",
                "chance": {"base": 58, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                "succ_fb": "你手把手教她们摸纱的粗细，把三十年攒的笔记抄成一本。徒弟们送你一副手套，说师傅的活有人接了。",
                "fail_fb": "厂里终究没有批，退休手续照办。你把笔记留给最勤的那个姑娘，看她攥着本子红了眼眶。",
                "succ_eff": {"rep": 12, "intellect": 8, "happiness": 6},
                "fail_eff": {"happiness": -4, "rep": 4, "intellect": 3},
                "tag_succ": "薪火相传",
                "tag_fail": "交了班",
                "is_key": True
            }
        ]
    }
]
