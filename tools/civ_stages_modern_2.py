STAGES = [
    [   # 阶段 8 负重前行
        {
            "period": "负重前行",
            "title": "一封家书过了三道封锁线",
            "narrative": "民国二十九年冬，你在镇上做木匠，妻子咳血已有月余。邮路断了三回，终于捎来老家口信，说岳母病重，盼你回去一趟；可厂里接了军需的活，工钱翻倍，走了这活就归别人。你捏着那张纸条，站在檐下听北风。",
            "choices": [
                {
                    "text": "先赶完这批军需木箱，托同乡捎钱捎药回老家",
                    "risk": "误了归期 · 得保工钱",
                    "chance": {"base": 62, "int_div": 2, "luck_bonus": 6, "health_bonus": 0},
                    "succ_fb": "木箱如期交齐，工钱翻倍，你托人捎回药钱和一封短信。妻子接过信，咳得轻了些。",
                    "fail_fb": "你赶完工时岳母已入土，妻子怨你心硬，家里冷了半冬，你却攒下一笔救命钱。",
                    "succ_eff": {"wealth": 12, "rep": 4},
                    "fail_eff": {"happiness": -8, "wealth": 8},
                    "tag_succ": "如期交货", "tag_fail": "归迟憾深",
                    "is_key": True
                },
                {
                    "text": "告假还乡，把军需的活让与同行，先顾病人",
                    "risk": "舍利取义 · 心有所安",
                    "chance": {"base": 100},
                    "succ_fb": "你连夜赶回，煎药侍疾半月，岳母转危为安，同行也承你这份人情，日后常来帮衬。",
                    "succ_eff": {"happiness": 10, "rep": 6},
                    "tag_succ": "亲恩为重",
                    "is_key": False
                }
            ]
        },
        {
            "period": "负重前行",
            "title": "公共食堂锅底那半勺稀粥",
            "narrative": "一九六〇年冬，公社食堂按人头打饭，你家小子正是长个子，碗里总不见稠的。邻家寡妇带着三个娃，昨日已断粮，夜里来敲门，想借你藏在炕洞里的半袋红薯干。可那是你攒着给孩子过冬的。你握着门闩，半晌没作声。",
            "choices": [
                {
                    "text": "匀出半袋红薯干，约定开春队里分红再还",
                    "risk": "恤邻济困 · 自家受窘",
                    "chance": {"base": 68, "int_div": 2, "luck_bonus": 6, "health_bonus": 0},
                    "succ_fb": "开春分红，她如数还来，还捎了一篮野菜。两家的孩子一处上学，从此成了伴。",
                    "fail_fb": "开春她家仍紧，红薯干没还上，你家小子饿了半月，你却得了全队一句厚道。",
                    "succ_eff": {"rep": 10, "happiness": 5},
                    "fail_eff": {"happiness": -6, "rep": 8},
                    "tag_succ": "邻里相济", "tag_fail": "亏己全义",
                    "is_key": True
                },
                {
                    "text": "婉言推说自家也紧，只借出一小瓢应急",
                    "risk": "量力而行 · 各守本分",
                    "chance": {"base": 100},
                    "succ_fb": "你舀了一瓢递过去，话说得软。她千恩万谢走了，两家情分没断，自家口粮也保住了。",
                    "succ_eff": {"happiness": 4, "wealth": 3},
                    "tag_succ": "量力周济",
                    "is_key": False
                }
            ]
        }
    ],
    [   # 阶段 9 中年险滩
        {
            "period": "中年险滩",
            "title": "车间黑板报上的技术革新",
            "narrative": "一九五六年，厂里号召技术革新，你熬了三个通宵，把车床的夹具改了一道，能省两成料。可老师傅说这是祖上传下的规矩，动了要出事故；车间主任让你先报上去评先进。你捏着图纸，指节发白。",
            "choices": [
                {
                    "text": "把图纸交上去，请在老师傅跟前当场试车",
                    "risk": "冒犯旧规 · 险中求进",
                    "chance": {"base": 58, "int_div": 2, "luck_bonus": 0, "health_bonus": 4},
                    "succ_fb": "试车三回，夹具稳当，省料两成。老师傅点点头，你上了黑板报，还评上市里先进。",
                    "fail_fb": "头一回试车崩了刀，老师傅没说什么，只让你把图纸收回去。你赔了料钱，却把机理想透。",
                    "succ_eff": {"intellect": 12, "rep": 8},
                    "fail_eff": {"intellect": 8, "wealth": -6},
                    "tag_succ": "技改争先", "tag_fail": "吃亏长智",
                    "is_key": True
                },
                {
                    "text": "压下图纸，先私下请老师傅指点再作打算",
                    "risk": "藏锋守拙 · 稳中求全",
                    "chance": {"base": 100},
                    "succ_fb": "老师傅看了半宿，指你改了一处夹角。你把功劳记在他名下，两人都得了体面。",
                    "succ_eff": {"rep": 5, "intellect": 4},
                    "tag_succ": "藏器待时",
                    "is_key": False
                }
            ]
        },
        {
            "period": "中年险滩",
            "title": "知青报名表上的名字",
            "narrative": "一九六九年，街道敲锣打鼓送知青下乡，你儿子刚满十六，报名表递到手上。他成份一栏填的是职员，不算差也不算好，去与不去都有人议论。妻子夜里抹泪，说独子走了，家里就冷清了。你把表在灯下看了又看。",
            "choices": [
                {
                    "text": "让儿子报名去北大荒，临行把棉袄絮厚",
                    "risk": "骨肉远别 · 历练成人",
                    "chance": {"base": 62, "int_div": 0, "luck_bonus": 8, "health_bonus": 0},
                    "succ_fb": "儿子在北大荒学会了开拖拉机，来信字迹愈发端正，三年后招工回城，人结实也沉稳。",
                    "fail_fb": "北地苦寒，儿子冻伤了脚，信里却不诉苦。你寄去一双毡靴，心里疼了整冬。",
                    "succ_eff": {"happiness": 6, "rep": 6},
                    "fail_eff": {"happiness": -8, "rep": 4},
                    "tag_succ": "送子支边", "tag_fail": "牵肠挂肚",
                    "is_key": True
                },
                {
                    "text": "托人情把儿子留在城里，先当个学徒工",
                    "risk": "骨肉在侧 · 落人话柄",
                    "chance": {"base": 100},
                    "succ_fb": "儿子进了街办小厂，早晚能回家吃饭。邻里背后说你家会打算，妻子却总算睡得安稳。",
                    "succ_eff": {"happiness": 8, "rep": -4},
                    "tag_succ": "承欢膝下",
                    "is_key": False
                }
            ]
        }
    ],
    [   # 阶段 10 动荡考验
        {
            "period": "动荡考验",
            "title": "大字报贴到了车间门口",
            "narrative": "一九六七年春，厂门口贴满了大字报，有人点名要你表态，说老会计有历史问题，人人得划清界限。你与他共事十二年，知道他不过是旧社会当过账房。夜里你翻来覆去，笔在纸上写了又划。",
            "choices": [
                {
                    "text": "只写自己不谙内情，不给人扣帽子",
                    "risk": "缄口守拙 · 得罪两边",
                    "chance": {"base": 55, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                    "succ_fb": "你的检讨写得含糊，两边都不满意，却也没人再追。老会计后来悄悄朝你拱了拱手。",
                    "fail_fb": "有人贴出你的大字报，说你立场暧昧。你被叫去学习班半个月，回来时瘦了一圈。",
                    "succ_eff": {"rep": 6, "happiness": 3},
                    "fail_eff": {"happiness": -10, "health": -4},
                    "tag_succ": "守口如瓶", "tag_fail": "处境转难",
                    "is_key": True
                },
                {
                    "text": "按报上口径写一张大字报，随大流签上名",
                    "risk": "明哲保身 · 心有余愧",
                    "chance": {"base": 100},
                    "succ_fb": "你照抄了报上的话，签了名，风波绕过了你家。只是再遇见老会计，你总低着头快步走开。",
                    "succ_eff": {"happiness": -3, "rep": 4},
                    "tag_succ": "随波自保",
                    "is_key": False
                }
            ]
        },
        {
            "period": "动荡考验",
            "title": "五七干校来的那张调令",
            "narrative": "一九七〇年，机关精简，一张调令要你去五七干校，说是劳动锻炼，归期未定。同一批里有人托病不去，有人抢着报名表忠心。你妻子体弱，孩子还在读书，行囊收拾了又拆开。",
            "choices": [
                {
                    "text": "主动申请下干校，说改造思想也锻炼身体",
                    "risk": "以退为进 · 前程未卜",
                    "chance": {"base": 60, "int_div": 2, "luck_bonus": 0, "health_bonus": 6},
                    "succ_fb": "你在干校挑粪种菜，晒黑了也结实了。两年后调令回城，组织说你表现好，安排了新岗。",
                    "fail_fb": "干校湿冷，你落下腰疾，回城时岗位已被人顶了，只能从头做起。",
                    "succ_eff": {"health": 6, "rep": 8},
                    "fail_eff": {"health": -6, "wealth": -4},
                    "tag_succ": "主动请缨", "tag_fail": "劳身失位",
                    "is_key": True
                },
                {
                    "text": "以妻子病重为由请假缓行，留在原单位",
                    "risk": "家室为重 · 落人口实",
                    "chance": {"base": 100},
                    "succ_fb": "你交了病假条，留下来照顾妻子。单位里有人说你恋家，可妻子熬过了那个冬天。",
                    "succ_eff": {"happiness": 8, "rep": -3},
                    "tag_succ": "顾家守拙",
                    "is_key": False
                }
            ]
        }
    ],
    [   # 阶段 11 知命之年
        {
            "period": "知命之年",
            "title": "平反通知书下来的那天",
            "narrative": "一九七七年秋，单位来人通知，说当年扣在你头上的那顶帽子可以摘了，档案里的材料要重新写。你跑了三趟，最后在一间办公室里看见那张薄纸。窗外梧桐落叶，你手抖得签不成名字。",
            "choices": [
                {
                    "text": "要求把当年的结论一并改正，恢复原职级",
                    "risk": "据理力争 · 一波三折",
                    "chance": {"base": 58, "int_div": 2, "luck_bonus": 8, "health_bonus": 0},
                    "succ_fb": "材料改了，职称补上，补发的工资装了一个信封。你把信封压在箱底，先给妻子买了一斤肉。",
                    "fail_fb": "来回扯了半年，只改了一半。你没再争，回家把旧笔记本一页页烧了。",
                    "succ_eff": {"rep": 12, "wealth": 10},
                    "fail_eff": {"happiness": -6, "rep": 4},
                    "tag_succ": "沉冤得雪", "tag_fail": "半纸平反",
                    "is_key": True
                },
                {
                    "text": "只领回那张通知，不再申辩，回岗位做事",
                    "risk": "但求清白 · 不争长短",
                    "chance": {"base": 100},
                    "succ_fb": "你把通知叠好收进抽屉，第二天照常上班。同事待你客气了，日子也一点点回到正轨。",
                    "succ_eff": {"happiness": 8, "rep": 4},
                    "tag_succ": "清白自守",
                    "is_key": False
                }
            ]
        },
        {
            "period": "知命之年",
            "title": "恢复高考的第一个冬天",
            "narrative": "一九七七年冬，广播里说恢复高考，不拘成份，自愿报名。你女儿在乡下插队七年，课本早当了引火纸。她连夜翻出旧笔记，眼睛亮得吓人；可家里拿不出路费和复习的工夫。你在灯下算了半宿。",
            "choices": [
                {
                    "text": "让女儿请假回城复习，全家省口粮供她",
                    "risk": "孤注一掷 · 望女成凤",
                    "chance": {"base": 64, "int_div": 2, "luck_bonus": 6, "health_bonus": 0},
                    "succ_fb": "她考上了省城的师范学院，走那天你送到车站，把攒的布票缝进她棉袄里。信里说食堂有白面馒头。",
                    "fail_fb": "她差了几分落榜，回村时没哭。第二年再考，中了中专。你才知她夜里背书到天亮。",
                    "succ_eff": {"happiness": 12, "rep": 8},
                    "fail_eff": {"happiness": -5, "intellect": 4},
                    "tag_succ": "寒门折桂", "tag_fail": "来年再试",
                    "is_key": True
                },
                {
                    "text": "劝她安心务农，先顾眼下工分和口粮",
                    "risk": "务实守成 · 埋没心愿",
                    "chance": {"base": 100},
                    "succ_fb": "她没报名，把笔记又收进箱底。年底分红多了几十斤粮，家里过了个踏实年。",
                    "succ_eff": {"wealth": 5, "happiness": -3},
                    "tag_succ": "安分守成",
                    "is_key": False
                }
            ]
        }
    ]
]
