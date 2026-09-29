# -*- coding: utf-8 -*-
"""文明五大纪元专属突发随机事件库。

每个纪元 8 个具象微观随机事件，彻底杜绝先秦古人抽到“体育彩票”、宋明百姓碰到“股票”等时代错位。
数值范围规范：
  health, intellect, happiness, luck, rep: -15 .. +15
  wealth: -5.0 .. +5.0 (各纪元在结算时自动附加各自时代货币单位)
"""

RANDOM_EVENT_POOLS = {
    "ancient": [
        {
            "id": "ancient_re_jade",
            "title": "山涧偶拾古玉",
            "tag": "古玉通灵",
            "desc": "山行避雨，在溪涧泥沙中偶拾得一枚温润古玉。虽无印款，质地却极通透，暗合吉兆。",
            "effect": {"wealth": 1.2, "happiness": 8, "luck": 4}
        },
        {
            "id": "ancient_re_monk",
            "title": "古刹隐僧问道",
            "tag": "心源豁然",
            "desc": "古道暮色中遇一云游老僧，席地饮凉茶数巡，数语直指心源，使你久郁的心结豁然开朗。",
            "effect": {"happiness": 12, "intellect": 6, "luck": 2}
        },
        {
            "id": "ancient_re_flood",
            "title": "连雨山洪浸屋",
            "tag": "水患维艰",
            "desc": "夏秋连旬暴雨，后山泥流漫入土屋，积谷受潮，梁柱亦有倾斜，不得不耗费钱粮修葺。",
            "effect": {"wealth": -1.0, "health": -4, "happiness": -6}
        },
        {
            "id": "ancient_re_cure",
            "title": "游方草医良方",
            "tag": "逢医愈疾",
            "desc": "路遇背负青囊的游方草医，赠以一剂熬透的驱寒草药，陈年风湿暗疾竟大见舒缓。",
            "effect": {"health": 12, "happiness": 6, "intellect": 2}
        },
        {
            "id": "ancient_re_elder",
            "title": "里正公推保举",
            "tag": "乡党誉重",
            "desc": "乡里宗族耆老在公堂上赞你操行笃厚、守礼慎行，县衙公文上特予记名表彰。",
            "effect": {"rep": 10, "happiness": 6, "luck": 3}
        },
        {
            "id": "ancient_re_bandit_alarm",
            "title": "戍烽边警虚惊",
            "tag": "惊弓之险",
            "desc": "山关烽火骤起，夜半鸡犬不宁，村民皆裹粮避入深山，三日后探知方知是巡哨虚惊。",
            "effect": {"health": -6, "happiness": -8, "wealth": -0.5}
        },
        {
            "id": "ancient_re_bronze",
            "title": "市集低纳残铜",
            "tag": "古铭生辉",
            "desc": "在城邑墟市角落以几斗粟米购得数件锈蚀铜器，归家磨洗竟辨出商周铭文，引来雅士重金求借观。",
            "effect": {"wealth": 2.0, "intellect": 8, "rep": 5}
        },
        {
            "id": "ancient_re_bountiful",
            "title": "风调雨顺丰稔",
            "tag": "五谷丰登",
            "desc": "一年四时风调雨顺，租田菽粟齐熟，所纳官粮外尚有赢余，邻里共饮春酒。",
            "effect": {"wealth": 1.5, "happiness": 10, "health": 4}
        }
    ],

    "premodern": [
        {
            "id": "premodern_re_rubbing",
            "title": "旧肆偶得前朝残拓",
            "tag": "墨海得珍",
            "desc": "瓦舍书肆尘封角落翻得一卷苏黄法帖残拓，墨香沉郁，细加摩挲，笔意大有进益。",
            "effect": {"intellect": 10, "happiness": 6, "rep": 4}
        },
        {
            "id": "premodern_re_flood_granary",
            "title": "梅雨湿仓霉丝",
            "tag": "梅雨蚀利",
            "desc": "江南连月梅雨淫霏不绝，仓底生潮，数匹上好贡缎发霉斑蚀，亏了当季行利。",
            "effect": {"wealth": -1.5, "happiness": -8, "health": -2}
        },
        {
            "id": "premodern_re_tea_meeting",
            "title": "山馆品茗结清交",
            "tag": "茗社良朋",
            "desc": "游山遇雨暂避茶肆，同一商号掌柜煮泉斗茶，对方深赏你品行，引荐了通达路子。",
            "effect": {"intellect": 6, "wealth": 1.5, "luck": 4}
        },
        {
            "id": "premodern_re_theft",
            "title": "柜坊夜失细软",
            "tag": "夜警失金",
            "desc": "市镇遭宵小潜入，铺前藏银与细软账册被翻箱倒柜，所幸借据藏于夹壁，仅折了零银。",
            "effect": {"wealth": -1.8, "happiness": -10, "luck": -3}
        },
        {
            "id": "premodern_re_clan_aid",
            "title": "宗族义田分惠",
            "tag": "宗族庇荫",
            "desc": "族中义庄按岁分发胙肉与冬谷，长房感念你平素谦谨，格外添拨了半口良田收益。",
            "effect": {"wealth": 1.6, "happiness": 8, "rep": 6}
        },
        {
            "id": "premodern_re_epidemic",
            "title": "时疫避凶逢吉",
            "tag": "积善避瘟",
            "desc": "城中突发热症时疫，你谨守草方洁舍闭门深居，全家皆得安宁，反以余药济贫积了阴骘。",
            "effect": {"health": 6, "happiness": 8, "rep": 8, "luck": 4}
        },
        {
            "id": "premodern_re_ticket",
            "title": "钱庄票号分息",
            "tag": "票号利丰",
            "desc": "旧年寄存晋陕票号的闲银，逢着外贸大顺岁，东家特发加息两厘，平添一份喜钱。",
            "effect": {"wealth": 2.5, "happiness": 6, "luck": 2}
        },
        {
            "id": "premodern_re_street_fire",
            "title": "市巷回禄之灾",
            "tag": "劫后余生",
            "desc": "邻家失慎走水，火借风势延烧数丈，奋力搬运只保得身家无虞，房屋微损需整葺。",
            "effect": {"wealth": -1.2, "health": -5, "happiness": -8}
        }
    ],

    "modern": [
        {
            "id": "modern_re_foreign_letter",
            "title": "邮差送达海外侨批",
            "tag": "天涯侨批",
            "desc": "南洋远亲历尽艰难寄回一封泛黄的侨批与银汇，虽经数道邮路折损，终在燃眉之际解了全家饥荒。",
            "effect": {"wealth": 3.0, "happiness": 12, "luck": 4}
        },
        {
            "id": "modern_re_night_study",
            "title": "夜校烛光与借阅新书",
            "tag": "灯下求真",
            "desc": "工友从省城带回一本翻烂的《大众哲学》与工业图解，两人在油灯下轮流抄录至天明。",
            "effect": {"intellect": 12, "happiness": 8, "rep": 4}
        },
        {
            "id": "modern_re_curfew",
            "title": "警笛骤响的惊悸之夜",
            "tag": "乱世惊弓",
            "desc": "戒严巡逻的哨子与皮靴声在弄堂回响，全家屏息熄灯躲在阁楼，心悬半宿，惊魂甫定。",
            "effect": {"health": -4, "happiness": -10, "luck": -2}
        },
        {
            "id": "modern_re_ration_coupon",
            "title": "合作社拾遗物归原主",
            "tag": "诚恪扬名",
            "desc": "在粮站排队时拾得遗落的布票与购粮簿，多方寻访归还失主，厂里特开黑板报通报嘉奖。",
            "effect": {"rep": 12, "happiness": 10, "luck": 3}
        },
        {
            "id": "modern_re_train_delay",
            "title": "蒸汽火车大误点",
            "tag": "羁旅同舟",
            "desc": "运煤车皮脱轨导致客车困在荒野道岔整整两日，干粮断顿，幸与同车乘客分饮凉水共渡难关。",
            "effect": {"health": -6, "happiness": -6, "intellect": 4}
        },
        {
            "id": "modern_re_invention",
            "title": "车间边角料巧改农具",
            "tag": "格物巧手",
            "desc": "利用厂区淘汰的报废角钢，自制了一把轻便好用的滚珠深耕犁，在农忙支农中大获赞誉。",
            "effect": {"intellect": 8, "rep": 8, "happiness": 6}
        },
        {
            "id": "modern_re_frozen_pipeline",
            "title": "严冬水管冻裂与邻里抢险",
            "tag": "风雪同心",
            "desc": "零下二十度寒潮冻裂总管道，大家在冰水里抢险排涝，虽受了风寒，工友却送来热姜汤。",
            "effect": {"health": -4, "happiness": 6, "rep": 6}
        },
        {
            "id": "modern_re_bonus",
            "title": "节约革新标兵津贴",
            "tag": "立功受奖",
            "desc": "提出的降耗小革新在全车间推广，月底大会受到表扬，并领到一张簇新的洗脸盆兑换券与小额奖励。",
            "effect": {"wealth": 1.5, "rep": 10, "happiness": 8}
        }
    ],

    "contemporary": [
        {
            "id": "contemporary_re_lottery",
            "title": "街头彩票微幸",
            "tag": "微幸眷顾",
            "desc": "路过街头报刊亭随手刮了一张体育彩票，竟中了二等小奖！虽非巨资，却在捉襟见肘时添了口温热饭菜。",
            "effect": {"wealth": 2.0, "happiness": 8, "luck": -2}
        },
        {
            "id": "contemporary_re_illness_scare",
            "title": "深夜急诊惊魂",
            "tag": "疾痛惊魂",
            "desc": "深夜高烧突发呼吸急促，被救护车紧急送医折腾了一整夜。输液到天明虽脱险，医药费却花了半月薪资。",
            "effect": {"health": -10, "wealth": -2.0, "happiness": -6}
        },
        {
            "id": "contemporary_re_friend_scam",
            "title": "老友借贷失联",
            "tag": "信义落空",
            "desc": "昔日挚友以资金周转为名求借一笔周转金，承诺数月即还。不料半年后微信拉黑人去楼空，令人心寒彻骨。",
            "effect": {"wealth": -3.5, "happiness": -12, "rep": -2}
        },
        {
            "id": "contemporary_re_mentor",
            "title": "贵人偶指迷津",
            "tag": "高人指路",
            "desc": "行业沙龙散场后，偶遇一位退休的前辈行尊。对方就着茶水三言两语点破你职业天花板，令你茅塞顿开。",
            "effect": {"intellect": 10, "happiness": 6, "rep": 4}
        },
        {
            "id": "contemporary_re_stock_bubble",
            "title": "跟风理财踩雷",
            "tag": "折戟商海",
            "desc": "轻信朋友推荐的理财新产品，遭遇行情闪崩与赎回冻结，辛苦攒下的活钱平白打了水漂。",
            "effect": {"wealth": -4.0, "happiness": -10, "luck": -4}
        },
        {
            "id": "contemporary_re_overtime_crash",
            "title": "连续通宵身体亮红灯",
            "tag": "透支预警",
            "desc": "为了赶项目进度连续通宵加班一周，清晨心悸晕眩几乎倒在工位，不得不自费购买昂贵保健品调理。",
            "effect": {"health": -12, "happiness": -6, "wealth": -1.0}
        },
        {
            "id": "contemporary_re_viral",
            "title": "随手自媒体微火一把",
            "tag": "浮名微光",
            "desc": "下班途中随手拍摄的生活感悟视频竟然在短视频平台小火出圈，收到不少读者鼓励与微薄流量收益。",
            "effect": {"rep": 8, "wealth": 1.5, "happiness": 10}
        },
        {
            "id": "contemporary_re_rent_hike",
            "title": "房东突击涨租逼迁",
            "tag": "居无定所",
            "desc": "租约未满房东突然宣布涨租三成，不得不顶着严寒连夜打包行李四处找房搬家，筋疲力竭。",
            "effect": {"wealth": -1.8, "happiness": -12, "health": -4}
        }
    ],

    "future": [
        {
            "id": "future_re_neural_glitch",
            "title": "神经脉冲震荡",
            "tag": "神经震颤",
            "desc": "人造电离穹顶遭遇强太阳风暴微扰，脑机接口神经信号出现短暂延迟反冲，视网膜全息界面频频雪花乱闪。",
            "effect": {"health": -8, "happiness": -6, "intellect": -2}
        },
        {
            "id": "future_re_quantum_airdrop",
            "title": "暗网算力盲盒空投",
            "tag": "天降算力",
            "desc": "由于早期参与过开源超导协议的节点维护，突然收到去中心化自治组织空投的一笔高阶加密算力配额！",
            "effect": {"wealth": 4.0, "luck": 4, "happiness": 8}
        },
        {
            "id": "future_re_synth_recall",
            "title": "二阶仿生器官例行召回",
            "tag": "义体维保",
            "desc": "收到生物义体制造商的通函，左臂的人工神经束存在隐患需入舱返厂检修，自费垫付了昂贵的保外调试费。",
            "effect": {"wealth": -2.5, "health": 4, "happiness": -6}
        },
        {
            "id": "future_re_deep_mentor",
            "title": "深空先驱的遗留日志",
            "tag": "星尘启蒙",
            "desc": "在小行星采矿站的公共数据库中翻阅到一段未加密的深空拓荒者私人音频，其宏阔深邃的宇宙观深深震撼了你。",
            "effect": {"intellect": 12, "happiness": 10, "rep": 5}
        },
        {
            "id": "future_re_carbon_fine",
            "title": "超额碳排二级罚单",
            "tag": "配额红线",
            "desc": "因违规在室内使用老旧电阻炉烹调真实肉食，被社区无人机检测开出二级碳排放惩戒罚单。",
            "effect": {"wealth": -2.5, "happiness": -8, "rep": -3}
        },
        {
            "id": "future_re_cosmic_ray",
            "title": "近轨高能辐射透射警报",
            "tag": "射线惊险",
            "desc": "空间站磁盾例行充能时遭遇微陨石擦碰，微量宇宙射线穿透舱壁，全员在辐射舱静置排毒并注射防辐射血清。",
            "effect": {"health": -6, "wealth": -1.5, "happiness": -4}
        },
        {
            "id": "future_re_seed_cultivar",
            "title": "水耕舱培育出稀有变异甘薯",
            "tag": "拓荒丰获",
            "desc": "在受控重力培养槽中培育出抗辐射高糖新株系，被火星拓荒科研所按专利高价收购。",
            "effect": {"wealth": 3.5, "intellect": 8, "happiness": 8}
        },
        {
            "id": "future_re_ai_glitch",
            "title": "生活伴侣强AI逻辑循环死锁",
            "tag": "硅基感伤",
            "desc": "家中的管家级合成仿生人突然遭遇感情悖论逻辑死锁，不得不花费两日时间重置核心模型并丢失了一部分温馨记忆。",
            "effect": {"happiness": -10, "wealth": -1.0, "intellect": 4}
        }
    ]
}
