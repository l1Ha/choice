# -*- coding: utf-8 -*-
# 《浮生录》· 近代破晓（1912—1977）· 人生阶段 4-7
# 仅含一个模块级变量 STAGES，纯字面量，无导入、无函数。

STAGES = [
    [   # 阶段 4 青春韶华（20-22岁）
        {
            "period": "青春韶华",
            "title": "青布长衫投考师范讲习所",
            "narrative": "县里师范讲习所招生，免学费，还管一顿糙米饭。你攥着借来的两块银元，天不亮走了三十里土路。可家中七亩薄田正等着人下地，父亲说读书人填不饱肚子。报名处就设在文庙廊下，考还是不考，你得当场拿定主意。",
            "choices": [
                {
                    "text": "先应下考卷，考完再连夜赶回村里，求父亲点头",
                    "risk": "前程未定 · 家计难舍",
                    "chance": {"base": 68, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                    "succ_fb": "榜上第十九名。父亲把烟袋在门槛上磕了三下，终究把地契押给族里，替你凑齐了铺盖钱。",
                    "fail_fb": "你落了榜，回家正赶上秋收。父亲没说什么，只把你能吃的糙米省给了弟妹。",
                    "succ_eff": {"intellect": 10, "rep": 5},
                    "fail_eff": {"intellect": 4, "happiness": -5},
                    "tag_succ": "题名有望",
                    "tag_fail": "归田收秋",
                    "is_key": True
                },
                {
                    "text": "留在家里帮父亲把七亩地种完，夜里再去乡塾借书自学",
                    "risk": "两全其难 · 心志不堕",
                    "chance": {"base": 100},
                    "succ_fb": "秋粮进了仓，你把一本《算术》翻得卷了边，村里的孩子开始追着喊你先生。",
                    "succ_eff": {"intellect": 6, "happiness": 3, "rep": 3},
                    "tag_succ": "耕读不辍",
                    "is_key": False
                }
            ]
        },
        {
            "period": "青春韶华",
            "title": "纱厂招练习生，铁门里汽笛响",
            "narrative": "日资纱厂的铁门外挤满了人，招二十个练习生，月给八块银元，管住不管吃。工头捏着你的手掌看茧，说细纱车间热得能拧出水，一天要站十二个钟头。同村有人递话来，码头扛包当天就结现钱。",
            "choices": [
                {
                    "text": "咬牙留下考工，进细纱车间做学徒，先挣一份稳当工钱",
                    "risk": "苦干立身 · 积劳伤身",
                    "chance": {"base": 72, "int_div": 2, "luck_bonus": 0, "health_bonus": 8},
                    "succ_fb": "三年后你摸熟了细纱机的脾性，能听声辨断头，工钱涨到十二块，还把铺盖从通铺搬进了小屋。",
                    "fail_fb": "机器咬去了你左手半截指尖。工头给了两块银元养伤钱，你把它缝进棉袄里，没敢寄回家。",
                    "succ_eff": {"wealth": 8.0, "intellect": 5},
                    "fail_eff": {"health": -12, "wealth": 2.0, "happiness": -6},
                    "tag_succ": "听声辨纱",
                    "tag_fail": "断指存银",
                    "is_key": True
                },
                {
                    "text": "跟着同村人去码头扛包，当日结钱，先顾眼前",
                    "risk": "现钱糊口 · 肩背难支",
                    "chance": {"base": 100},
                    "succ_fb": "你在码头上喊了三年号子，肩膀磨出厚茧，攒下的银元寄回家翻修了两间瓦房。",
                    "succ_eff": {"health": 4, "wealth": 6.0, "rep": 2},
                    "tag_succ": "号子立身",
                    "is_key": False
                }
            ]
        }
    ],
    [   # 阶段 5 初涉人世（23-25岁）
        {
            "period": "初涉人世",
            "title": "沪上码头送别，留洋的船票",
            "narrative": "亲戚牵线，有人愿资助你去法国勤工俭学，船票和介绍信都备下了；只是路费要自筹一半，此去少则五年，家中老母的病还没好。码头上四等舱的舷梯已收起一半，同行的青年正喊着你的名字。",
            "choices": [
                {
                    "text": "典当母亲的银镯凑齐船票，登上开往马赛的四等舱",
                    "risk": "远渡求新 · 亲恩难报",
                    "chance": {"base": 62, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                    "succ_fb": "你在里昂的工厂半工半读，学会了看图纸，也学会在夜校里跟人争论中国该往何处去。",
                    "fail_fb": "船到新加坡你病倒了，被送上岸养了两个月，钱花去大半，只得折回上海，银镯也没能赎回。",
                    "succ_eff": {"intellect": 12, "rep": 6, "wealth": -4.0},
                    "fail_eff": {"intellect": 5, "happiness": -8, "wealth": -6.0},
                    "tag_succ": "负笈远洋",
                    "tag_fail": "中途折返",
                    "is_key": True
                },
                {
                    "text": "留下侍奉老母，在县城中学谋一份教书的差事",
                    "risk": "晨昏定省 · 壮志稍敛",
                    "chance": {"base": 100},
                    "succ_fb": "你在县立中学教算术，月薪十八元，课余替人抄写状纸，母亲的药没有断过。",
                    "succ_eff": {"intellect": 6, "happiness": 6, "rep": 5},
                    "tag_succ": "侍疾守志",
                    "is_key": False
                }
            ]
        },
        {
            "period": "初涉人世",
            "title": "城门口贴出告示，招学兵",
            "narrative": "城门口贴着招兵告示，说一人当兵，全家免捐。街那头，学生救亡宣传队正搭台子唱《松花江上》。你手里还捏着半张没写完的启事——部队要识字的人当文书，宣传队却只管一顿午饭。",
            "choices": [
                {
                    "text": "投考学兵队，凭一手好字去连部做个文书",
                    "risk": "投笔从戎 · 生死难料",
                    "chance": {"base": 66, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                    "succ_fb": "你替连长誊清花名册，也替不识字的弟兄写家信。一次夜行军，你把全连带出了岔路口。",
                    "fail_fb": "部队在皖北被打散，你背着伤兵走了三天，回到家乡时军装已被老乡换走，只剩一块干粮。",
                    "succ_eff": {"rep": 10, "intellect": 5, "health": -4},
                    "fail_eff": {"health": -10, "happiness": -5, "rep": 4},
                    "tag_succ": "文书赴难",
                    "tag_fail": "散兵归乡",
                    "is_key": True
                },
                {
                    "text": "加入学生救亡宣传队，走街串巷演活报剧",
                    "risk": "唤醒乡邻 · 清苦自持",
                    "chance": {"base": 100},
                    "succ_fb": "你在集市上演《放下你的鞭子》，台下的老农攥紧了拳头。队里管饭，你瘦了，嗓子却越来越亮。",
                    "succ_eff": {"rep": 8, "happiness": 6, "intellect": 4},
                    "tag_succ": "街头呐喊",
                    "is_key": False
                }
            ]
        }
    ],
    [   # 阶段 6 成家立业（26-29岁）
        {
            "period": "成家立业",
            "title": "媒人上门说亲，聘礼要四色",
            "narrative": "媒人第三次上门，说女方是邻村织布的好手，只是聘礼要银元六十、细布四匹、猪肉半扇。你攒了三年的工钱只够一半，女方娘舅又放出话来，年底前凑不齐便另许人家。",
            "choices": [
                {
                    "text": "向厂里工友起个会借钱，赶在冬至前把亲定下",
                    "risk": "举债成家 · 日后还偿",
                    "chance": {"base": 70, "int_div": 0, "luck_bonus": 6, "health_bonus": 0},
                    "succ_fb": "工友凑了二十八块，你终于赶在冬至前下了定。新房里贴着红纸剪的喜字，灶上炖着借来的半只鸡。",
                    "fail_fb": "会钱没凑齐，女方改许了镇上的布商。你把那几匹细布退给店里，折了两成价，独自喝了半斤酒。",
                    "succ_eff": {"happiness": 12, "rep": 5, "wealth": -6.0},
                    "fail_eff": {"happiness": -10, "wealth": -3.0, "rep": -2},
                    "tag_succ": "冬至下定",
                    "tag_fail": "亲事他许",
                    "is_key": True
                },
                {
                    "text": "与女方商量简办，只迎亲不摆席，往后一起挣",
                    "risk": "两情相谅 · 从简结发",
                    "chance": {"base": 100},
                    "succ_fb": "她拎着一只蓝布包袱过了门，你们在租来的厢房里对坐吃了一碗面，说定往后日子一起挣。",
                    "succ_eff": {"happiness": 9, "wealth": 2.0, "rep": 2},
                    "tag_succ": "布衣结发",
                    "is_key": False
                }
            ]
        },
        {
            "period": "成家立业",
            "title": "江边码头，工厂要迁往重庆",
            "narrative": "战事逼近，纱厂奉命拆卸机器西迁，工头说愿走的每人补三块银元，家眷随船，只是江上要过三道封锁线。你刚出生的孩子还在发热，岳母一家又不肯离开老屋。",
            "choices": [
                {
                    "text": "携妻儿随厂西迁，跟着机器一程一程拆运",
                    "risk": "逆江西行 · 家小颠沛",
                    "chance": {"base": 64, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                    "succ_fb": "船在宜昌换小船，你的孩子在舱里退了热。到了重庆，你守着重新开工的纱锭，成了熟练的保全工。",
                    "fail_fb": "船在江上遇了空袭，铺盖和行李都沉了，一家人在巫山脚下走了半个月才追上大部队。",
                    "succ_eff": {"intellect": 8, "rep": 6, "health": -5},
                    "fail_eff": {"health": -9, "happiness": -8, "wealth": -5.0},
                    "tag_succ": "溯江保全",
                    "tag_fail": "失箧追队",
                    "is_key": True
                },
                {
                    "text": "留下看守老屋，在本地另寻一份零工",
                    "risk": "守土安家 · 生计日蹙",
                    "chance": {"base": 100},
                    "succ_fb": "你替粮行挑脚，又在城隍庙前摆了个修车摊。日子紧，但妻儿都在身边，老屋的瓦也没塌。",
                    "succ_eff": {"happiness": 5, "wealth": 3.0, "health": -3},
                    "tag_succ": "守屋度日",
                    "is_key": False
                }
            ]
        }
    ],
    [   # 阶段 7 三十而立（30-33岁）
        {
            "period": "三十而立",
            "title": "村里丈量土地，要重新立契",
            "narrative": "土改工作队进了村，丈量土地，重立契据。你家分到七亩水田和半头耕牛，可老父卧病在床，两位叔伯盯着祖屋的三间正房，说长子应当多担赡养，房产却要摊平。",
            "choices": [
                {
                    "text": "接下赡养担子，把分到的田契写成兄弟共有",
                    "risk": "独担养老 · 让产求安",
                    "chance": {"base": 75, "int_div": 0, "luck_bonus": 5, "health_bonus": 0},
                    "succ_fb": "工作队把公议记在册子上，两位叔伯再没为房争执。老人的药钱你一人出，秋后收了十石谷子。",
                    "fail_fb": "田契写共有的次日，二叔又反悔，说祖屋的梁是你爹换的，该归他。你气得砸了一只碗。",
                    "succ_eff": {"rep": 10, "happiness": 5, "wealth": 4.0},
                    "fail_eff": {"happiness": -8, "rep": -3, "wealth": 2.0},
                    "tag_succ": "立契让产",
                    "tag_fail": "房争伤和",
                    "is_key": True
                },
                {
                    "text": "请村干部与族老当众评理，按人口均分田产",
                    "risk": "当众评理 · 亲族生隙",
                    "chance": {"base": 100},
                    "succ_fb": "族老在祠堂里把话说透，田按人头分，赡养按月轮。你落了个公道，只是逢年过节少了往来。",
                    "succ_eff": {"rep": 6, "happiness": 3, "wealth": 3.0},
                    "tag_succ": "祠堂公议",
                    "is_key": False
                }
            ]
        },
        {
            "period": "三十而立",
            "title": "车间黑板报贴出技术革新榜",
            "narrative": "厂里响应一五计划，要推广苏联专家的高速切削法，黑板报上列出技术革新榜，谁改进了工装就记功。夜校晚上开课，教代数与识图；可车间定额也加了三成，你家里刚添了第二个孩子。",
            "choices": [
                {
                    "text": "报名夜校学识图，琢磨着把车床夹具改一改",
                    "risk": "以工代学 · 力有未逮",
                    "chance": {"base": 68, "int_div": 2, "luck_bonus": 0, "health_bonus": 0},
                    "succ_fb": "你的夹具把辅助时间省了一半，黑板报上登了你的名字，厂里奖了一支金星钢笔和二十尺布票。",
                    "fail_fb": "夹具崩了刀，废了两根料，你赔了半个月工资，夜校的课也落了三成，图纸总算看懂了。",
                    "succ_eff": {"intellect": 12, "rep": 10, "wealth": 5.0},
                    "fail_eff": {"intellect": 5, "wealth": -5.0, "happiness": -5},
                    "tag_succ": "革新记功",
                    "tag_fail": "崩刀赔料",
                    "is_key": True
                },
                {
                    "text": "先把定额干满，下班后帮家里糊纸盒补用度",
                    "risk": "安分守额 · 持家补用",
                    "chance": {"base": 100},
                    "succ_fb": "你月月超额完成定额，评上先进生产者，奖金买了二斤猪肉和一双胶鞋，孩子的棉衣也絮上新棉花。",
                    "succ_eff": {"wealth": 6.0, "rep": 5, "happiness": 4},
                    "tag_succ": "先进守额",
                    "is_key": False
                }
            ]
        }
    ]
]
