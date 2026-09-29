REGIONS = [
    {"name": "汴京宣德门", "desc": "御街宽阔，瓦舍勾栏彻夜喧闹，酒楼茶坊林立，四方商旅云集，市井繁华。", "stat": {"health": 1, "wealth": 3.0, "rep": 2}},
    {"name": "江南姑苏", "desc": "水乡河道纵横，机户织坊林立，漕运码头帆樯相接，文风鼎盛，丝米富庶。", "stat": {"wealth": 3.5, "intellect": 2, "happiness": 1}},
    {"name": "泉州刺桐港", "desc": "市舶司设于此，蕃商海舶辐辏，香料珠宝云集，海风咸湿，通贸四海。", "stat": {"wealth": 4.0, "luck": 2, "rep": -1}},
    {"name": "徽州休宁", "desc": "山多田少，男子多出门行贾，宗族祠堂巍然，重儒重信，勤俭成风。", "stat": {"intellect": 3, "rep": 4}},
    {"name": "直隶顺天", "desc": "京师首善之地，官署林立，旗民杂居，街市规整，礼法森严。", "stat": {"rep": 3, "wealth": 1.5, "happiness": -1}},
    {"name": "天府成都", "desc": "沃野千里，茶馆戏台声声入耳，蜀锦名扬，百姓闲适安逸。", "stat": {"happiness": 3, "health": 1, "intellect": 1}},
    {"name": "山陕商道", "desc": "驼铃古道，晋商票号往来不绝，风沙扑面，商旅重诺守信。", "stat": {"wealth": 2.0, "luck": 1, "health": -1}},
    {"name": "广州十三行", "desc": "海禁之下独口通商，洋货行栈毗邻，商贾云集，银钱往来浩繁。", "stat": {"wealth": 5.0, "rep": -2, "luck": 1}},
]

STRATA = [
    {"title": "江南织造机户", "desc": "家中织机数张，日夜赶织绸缎，靠机户手艺营生，日子殷实却辛苦。", "stat": {"health": 86, "wealth": 6.5, "intellect": 58, "happiness": 58, "luck": 52, "rep": 55}, "trait": "勤巧持家"},
    {"title": "徽州儒商门第", "desc": "祖上经商起家，亦贾亦儒，家训以诚信为本，子弟须读书应试，光耀门楣。", "stat": {"health": 88, "wealth": 9.5, "intellect": 70, "happiness": 60, "luck": 54, "rep": 68}, "trait": "贾而好儒"},
    {"title": "钱塘书院耕读", "desc": "家有薄田数亩，耕读并重，父辈供子弟入书院受业，盼科举改换门庭。", "stat": {"health": 87, "wealth": 3.2, "intellect": 74, "happiness": 57, "luck": 50, "rep": 62}, "trait": "诗礼传家"},
    {"title": "泉州远洋海商", "desc": "家中有海船股份，货通南洋诸国，风浪里讨生活，富贵与凶险并存。", "stat": {"health": 84, "wealth": 11.0, "intellect": 62, "happiness": 56, "luck": 58, "rep": 60}, "trait": "敢闯重信"},
    {"title": "京畿旗人食禄", "desc": "隶于旗籍，按月支领钱粮，不必躬耕劳作，闲时遛鸟听戏，日子安稳。", "stat": {"health": 92, "wealth": 8.0, "intellect": 52, "happiness": 64, "luck": 56, "rep": 58}, "trait": "安闲守分"},
    {"title": "乡村私塾寒儒", "desc": "世代教蒙学为生，束脩微薄，家徒四壁却藏书满架，清高自守，颇受乡邻敬重。", "stat": {"health": 85, "wealth": 1.2, "intellect": 76, "happiness": 51, "luck": 49, "rep": 50}, "trait": "清贫守志"},
    {"title": "运河漕帮水手", "desc": "常年在漕船上搬运粮米，靠力气吃饭，讲义气，风餐露宿，结交帮中兄弟。", "stat": {"health": 90, "wealth": 2.4, "intellect": 49, "happiness": 53, "luck": 51, "rep": 44}, "trait": "义气耐劳"},
    {"title": "两淮盐引巨富", "desc": "持盐引行销数省，家资巨万，宅第连云，仆从成群，与官府往来密切。", "stat": {"health": 89, "wealth": 12.0, "intellect": 66, "happiness": 62, "luck": 57, "rep": 72}, "trait": "阔绰通权"},
    {"title": "晋商票号伙计", "desc": "在票号学徒出身，掌银钱汇兑，常年奔走各地，精于算计，恪守号规。", "stat": {"health": 86, "wealth": 4.8, "intellect": 68, "happiness": 55, "luck": 53, "rep": 57}, "trait": "精算守信"},
    {"title": "边镇屯戍军户", "desc": "世袭军籍，屯田守边，粮饷微薄，常在风沙中操练巡防，升迁无望。", "stat": {"health": 94, "wealth": 0.6, "intellect": 47, "happiness": 50, "luck": 48, "rep": 40}, "trait": "粗豪尚武"},
]
