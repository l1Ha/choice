REGIONS = [
    {"name": "关中秦川", "desc": "渭水两岸沃野千里，青铜农具初兴，军功爵下耕战并举，老秦人尚武重法。", "stat": {"health": 2, "rep": 1}},
    {"name": "齐鲁之邦", "desc": "洙泗之间儒风最盛，稷下论学、盐铁通商，士人抱竹简讲经，乡里重礼尚俭。", "stat": {"intellect": 3, "rep": 2}},
    {"name": "荆楚云梦", "desc": "江汉泽国水汽弥漫，稻作渔猎相济，漆器编钟见其工巧，楚人信巫好祀。", "stat": {"health": 1, "happiness": 2}},
    {"name": "江南会稽", "desc": "水乡稻熟鱼肥，越人断发文身，冶剑煮盐之利颇丰，商船沿江上下。", "stat": {"wealth": 2.0, "luck": 1}},
    {"name": "陇西凉州", "desc": "河西走廊胡商络绎，丝路驼铃与烽燧相望，边民自幼习骑射，风沙苦寒。", "stat": {"health": -1, "luck": 2}},
    {"name": "中原洛邑", "desc": "天下之中车马辐辏，诸侯会盟、百工聚居，市井喧嚣而礼法森严。", "stat": {"intellect": 2, "wealth": 1.0, "health": -1}},
    {"name": "燕赵之地", "desc": "北接胡狄铁马边关，慷慨悲歌多壮士游侠，冬日苦寒而民风刚烈。", "stat": {"health": 2, "rep": -1}},
    {"name": "巴蜀成都", "desc": "岷江冲积沃野，都江堰引水灌田，蜀锦漆器行销四方，山高路险少兵祸。", "stat": {"health": 1, "wealth": 2.5, "happiness": 2}},
]

STRATA = [
    {
        "title": "没落公族后裔",
        "desc": "祖上曾列诸侯之卿，如今封邑尽削，只剩旧宅与几捆竹简；仍守祭祀礼数，却要变卖青铜器度日。",
        "stat": {"health": 88, "wealth": 3.2, "intellect": 68, "happiness": 52, "luck": 49, "rep": 58},
        "trait": "守礼自持",
    },
    {
        "title": "老秦耕战农卒",
        "desc": "家在关中乡里，丁男按爵授田，农时扶犁、战时执戈；一纸军功文书便可改换门庭，故尚武不畏苦。",
        "stat": {"health": 92, "wealth": 0.8, "intellect": 50, "happiness": 55, "luck": 50, "rep": 40},
        "trait": "耐苦尚武",
    },
    {
        "title": "齐鲁经学儒士",
        "desc": "世居洙泗之滨，家中藏经书数箧，子弟自幼习礼诵诗；以讲学授徒为业，虽清贫却颇受乡里敬重。",
        "stat": {"health": 85, "wealth": 2.5, "intellect": 74, "happiness": 58, "luck": 52, "rep": 66},
        "trait": "温厚好古",
    },
    {
        "title": "临淄盐铁巨贾",
        "desc": "凭煮盐冶铁起家，车马奴婢成群，与官府往来密切；家中账册堆积，最怕朝廷一纸抑商之令。",
        "stat": {"health": 86, "wealth": 11.5, "intellect": 66, "happiness": 60, "luck": 56, "rep": 55},
        "trait": "精明豪爽",
    },
    {
        "title": "大唐西市胡商",
        "desc": "自粟特远来，在长安西市经营香料珠宝，通数种语言；虽家资丰厚，却始终被视为异乡客，常思故土。",
        "stat": {"health": 87, "wealth": 9.8, "intellect": 64, "happiness": 57, "luck": 58, "rep": 42},
        "trait": "机敏健谈",
    },
    {
        "title": "终南山采药隐士",
        "desc": "结庐终南山中，采药炼丹、观星著书，与樵夫野老为邻；不慕功名，只求清静长寿。",
        "stat": {"health": 94, "wealth": 0.6, "intellect": 70, "happiness": 66, "luck": 54, "rep": 62},
        "trait": "恬淡自适",
    },
    {
        "title": "太学博士门第",
        "desc": "父祖累世为太学博士，家学以经义为本，子弟须通一经方能入仕；门庭清贵而俸禄微薄。",
        "stat": {"health": 84, "wealth": 4.6, "intellect": 76, "happiness": 60, "luck": 51, "rep": 74},
        "trait": "端方守正",
    },
    {
        "title": "边郡戍卒之家",
        "desc": "父兄远戍烽燧，家中只有老母与幼弟，靠屯田薄收糊口；书信难通，年年盼望换防归乡的那一天。",
        "stat": {"health": 91, "wealth": 0.5, "intellect": 47, "happiness": 50, "luck": 48, "rep": 36},
        "trait": "坚忍寡言",
    },
    {
        "title": "织室匠户之家",
        "desc": "隶属官营织室，母女终年坐机杼前，织成锦帛尽数入官；手艺极精却身役难脱，只盼朝廷宽免匠籍。",
        "stat": {"health": 88, "wealth": 1.4, "intellect": 55, "happiness": 53, "luck": 52, "rep": 34},
        "trait": "灵巧安分",
    },
    {
        "title": "豪强庄园宾客",
        "desc": "寄身大姓庄园为宾客，耕其田、护其坞堡，得衣食与庇护；虽无户籍自由，却比编户安稳。",
        "stat": {"health": 90, "wealth": 7.6, "intellect": 58, "happiness": 56, "luck": 53, "rep": 60},
        "trait": "忠勇仗义",
    },
]
