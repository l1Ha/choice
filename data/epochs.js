/* ============================================================================
 * 《浮生录》· 文明长河纪元内容数据层
 *
 * 本文件由 tools/build_epochs_data.py 从 tools/civ_*.py 内容源自动生成，
 * 请勿手工编辑；如需修改时代背景、出身、事件，请改内容源后重新生成。
 *
 * 载入顺序：必须在 index.html 的主脚本之前引入。index.html 中的引擎函数
 * 会引用本文件定义的 CIVILIZATION_EPOCHS / GRAND_ERA_TABLE /
 * ANCIENT_STAGE_POOLS 等顶层常量（调用发生在两个脚本均已执行之后）。
 * ==========================================================================*/

    // ==================== 文明五大纪元 · 从华夏溯源到星海跃迁 ====================
    const CIVILIZATION_EPOCHS = [
      {
        id: "ancient",
        name: "先秦汉唐 · 华夏奠基",
        subTitle: "公元前2070年 ~ 公元907年",
        minYear: -2070,
        maxYear: 907,
        badge: "青铜风骨 · 盛唐万邦",
        desc: "武王伐纣、诸子百家争鸣、秦皇一统、大汉雄风凿通西域、盛唐长安万国来朝。",
        colorClass: "amber",
        eraIcon: "⚱️",
        legacyNoun: "青史竹简",
        namesMale: ["子墨", "季札", "无咎", "叔夜", "伯禽", "仲卿", "慕之", "长卿", "子渊", "仲宣"],
        namesFemale: ["阿禾", "清和", "素娥", "令仪", "罗敷", "文君", "昭华", "绿珠", "小蛮", "婉如"]
      },
      {
        id: "premodern",
        name: "宋韵明清 · 市井千帆",
        subTitle: "公元960年 ~ 公元1911年",
        minYear: 960,
        maxYear: 1911,
        badge: "繁华市井 · 刺桐海丝",
        desc: "汴京清明上河、大宋风雅格物、郑和远洋宝船、江南机杼与红楼梦回帝制夕阳。",
        colorClass: "emerald",
        eraIcon: "🏮",
        legacyNoun: "族谱与方志",
        namesMale: ["文昭", "仲舒", "念祖", "守拙", "德昌", "衡之", "砚秋", "望舒", "敬之", "行远"],
        namesFemale: ["清嘉", "素心", "婉卿", "蕙兰", "淑真", "月娥", "湘君", "妙玉", "静姝", "含章"]
      },
      {
        id: "modern",
        name: "近代破晓 · 烽火涅槃",
        subTitle: "公元1912年 ~ 公元1977年",
        minYear: 1912,
        maxYear: 1977,
        badge: "辛亥觉醒 · 浴血奠基",
        desc: "民国风雷、五四新文化破晓、十四载抗战御侮、新中国一五计划与大院拓荒岁月。",
        colorClass: "rose",
        eraIcon: "🌅",
        legacyNoun: "厂志与家书",
        namesMale: ["立本", "振华", "复生", "慕先", "志远", "觉民", "砚君", "望舒", "有德", "绍棠"],
        namesFemale: ["素秋", "毓秀", "婉如", "玉兰", "秀英", "桂芳", "静宜", "慧珍", "曼卿", "文淑"]
      },
      {
        id: "contemporary",
        name: "当代腾飞 · 浪潮狂飙",
        subTitle: "公元1978年 ~ 公元2035年",
        minYear: 1978,
        maxYear: 2035,
        badge: "包产到户 · 世界工厂",
        desc: "改革春风拂面、特区下海淘金、加入世贸大国崛起、移动互联百团大战与智算新质。",
        colorClass: "sky",
        eraIcon: "🏙️",
        legacyNoun: "市井与家书",
        namesMale: ["陈远", "陆明舟", "周子墨", "唐立本", "顾长风", "宋平", "江屿", "秦朗", "徐朝阳", "韩野"],
        namesFemale: ["林栖", "沈清弦", "许念安", "苏晚亭", "苏晴", "陆薇", "程一诺", "夏晓", "温言", "苏黎"]
      },
      {
        id: "future",
        name: "未来星海 · 戴森纪元",
        subTitle: "公元2036年 ~ 公元2150年",
        minYear: 2036,
        maxYear: 2150,
        badge: "太空天梯 · 戴森跃迁",
        desc: "常温超导聚变并网、太空电梯贯通、火星农场穹顶、量子脑机自组织与恒星戴森云。",
        colorClass: "purple",
        eraIcon: "🚀",
        legacyNoun: "星尘档案",
        namesMale: ["星野", "零壹", "沐辰", "陆知远", "凌云", "纪尘", "原野", "黎光", "衡宇", "折光"],
        namesFemale: ["艾柯", "苏黎", "弦歌", "澄澈", "若木", "阡陌", "月见", "素问", "弦月", "霜序"]
      },
    ];

    // 16 个生命阶段的默认年龄（用于 Python 侧对齐，JS 侧由随机时间线覆盖）
    const EPOCH_STAGE_AGES = [6, 10, 15, 18, 21, 24, 27, 31, 36, 40, 45, 51, 58, 66, 74, 80];

    function getEpochConfig(id) {
      return CIVILIZATION_EPOCHS.find(e => e.id === id) || CIVILIZATION_EPOCHS[3];
    }
    // 由具体年份反查所属纪元（公元前1600 ~ 公元2150，无间断）
    function getEpochIdForYear(year) {
      for (const e of CIVILIZATION_EPOCHS) { if (year <= e.maxYear) return e.id; }
      return CIVILIZATION_EPOCHS[CIVILIZATION_EPOCHS.length - 1].id;
    }
    function isFutureEpoch(id) { return id === "future"; }
    function isClassicalEpoch(id) { return id === "ancient" || id === "premodern" || id === "modern"; }
    function pickEpochName(id, gender = 'male') {
      const cfg = getEpochConfig(id);
      const pool = (gender === 'female' ? cfg.namesFemale : cfg.namesMale) || cfg.names || [];
      return pool[Math.floor(Math.random() * pool.length)] || "无名";
    }

    // ---- 连续时代背景表（覆盖公元前1600年至公元2150年及以外，全无间断）----
    const GRAND_ERA_TABLE = [
      [-2070, "上古传说 · 三皇五帝", "文字未立而口耳相传，炎黄逐鹿、尧舜禅让、洪水滔天与英雄治水，构成了华夏文明最深处的集体记忆。"],
      [-1600, "夏代肇兴 · 禹画九州", "大禹治水疏导江河，定九州铸九鼎，家天下自此始，泥陶与早期玉器诉说着文明开端的朴拙与坚韧。"],
      [-1046, "殷商青铜 · 占卜甲骨", "洹水之滨甲骨刻辞，青铜重器饕餮纹神秘庄重，巫祝与王权在祭祀与征伐中奠基礼仪雏形。"],
      [-771, "西周分封 · 礼乐井田", "武王克商封建万邦，周公制礼作乐，宗法井田井然有序，郁郁乎文哉而文明大备。"],
      [-476, "春秋争霸 · 百家争鸣", "诸侯争盟礼崩乐坏，孔丘问道老聃，士阶层崛起，思想星空迸发人类童年最璀璨的光芒。"],
      [-221, "战国兼并 · 铁血大争", "七雄并立商鞅变法，合纵连横名将辈出，郡县初萌，华夏在金戈铁马中奔向终极一统。"],
      [-202, "秦扫六合 · 帝国初成", "始皇帝车同轨书同文，修万里长城筑直道，废分封立郡县，开启两千年中央集权大一统。"],
      [9, "大汉雄风 · 丝路凿空", "文景休养汉武远拓，张骞策马绝域西域，卫青霍去病封狼居胥，丝绸之路首通亚欧大陆。"],
      [220, "光武中兴 · 经纬通达", "洛阳古都经学兴盛，蔡伦造纸张衡候风，班超投笔从戎定远三十六国，儒术与豪族相融。"],
      [280, "三国风云 · 英雄逐鹿", "曹操酾酒临江，刘备三顾草庐，赤壁烈火燎原，群雄在乱世烽烟中留下千古侠义奇谋。"],
      [420, "两晋风流 · 偏安江左", "洛神赋与竹林七贤，衣冠南渡金陵建康，名士清谈与山水诗赋在大动荡中绽放异彩。"],
      [581, "南北对峙 · 民族大融", "北魏孝文帝汉化改制，南朝烟雨四百八十寺，长城内外血脉相融，大一统生机悄然孕育。"],
      [618, "隋代风帆 · 运河科举", "开创科举抡才大典，开凿南北大运河贯通南北，营建大兴长安，气象恢弘却二世而斩。"],
      [755, "盛唐气象 · 万邦来朝", "贞观之治开元盛世，李白举杯邀明月，长安朱雀大街胡姬起舞，万国来朝气象万千。"],
      [907, "藩镇割据 · 残唐落日", "安史之乱两京陆沉，藩镇割据黄巢揭竿而起，晚唐诗韵苍凉沉郁，繁华落尽余晖脉脉。"],
      [960, "五代十国 · 烽火乱局", "朱温篡唐沙陀入主，城头变换大王旗，乱象纷呈却催生南方市井与刻书商业萌芽。"],
      [1127, "北宋风雅 · 汴京繁华", "清明上河图虹桥喧闹，苏轼赋赤壁，瓦舍勾栏百戏杂陈，活字印刷与指南针泽被后世。"],
      [1279, "南宋偏安 · 海丝千帆", "西湖歌舞与岳飞满江红，泉州刺桐港千帆竞发，海运航路遍及印度洋，富庶冠绝当世。"],
      [1368, "大元一统 · 欧亚驿道", "忽必烈定都大都，开辟横跨欧亚大驿道，马可波罗惊叹东方繁盛，杂剧元曲唱彻街巷。"],
      [1644, "大明风华 · 远洋郑和", "太祖布衣起兵，成祖永乐大典，郑和七下西洋宝船扬帆，江南机杼声中萌生新的萌芽。"],
      [1840, "康乾盛世 · 红楼斜阳", "人口突破三亿疆域辽阔，编纂四库全书，红楼梦笔力惊神，然闭关锁国已落后于世界大潮。"],
      [1912, "晚清危局 · 变法求存", "鸦片战争炮声惊醒天朝，洋务运动自强求富，甲午海战、辛亥秋风，两千年帝制轰然崩塌。"],
      [1937, "民国风雷 · 思想破晓", "新文化运动德先生赛先生震荡古老神州，白话文觉醒，黄埔风云激荡，实业救国步履维艰。"],
      [1949, "烽火抗战 · 浴血奠基", "十四年抗战御侮血肉筑长城，台儿庄百团大战，三大战役定乾坤，民族在血火中涅槃站立。"],
      [1958, "建国初期 · 一五筑基", "没收官僚资本土改归农，抗美援朝保家卫国，苏联援建重点工厂开工，红旗招展百废俱兴。"],
      [1966, "大庆精神 · 自力更生", "铁人王进喜跃进泥浆，原子弹大漠爆鸣，全国人民勒紧裤带自力更生，独立工业体系初成。"],
      [1978, "风雨激荡 · 红砖岁月", "凭票供应与粮本油票，红砖大院广播操与样板戏，千百万青年上山下乡磨砺筋骨。"],
      [1984, "真理讨论 · 春风破冰", "小岗村大包干与十一届三中全会，恢复高考改变千万学子命运，喇叭裤与流行乐悄然传遍。"],
      [1992, "商品初潮 · 特区拔地", "价格双轨制松动，民间个体户提皮包闯天下，深圳特区高楼平地起，商品意识全面觉醒。"],
      [1998, "南方谈话 · 市场狂潮", "春天的故事响彻神州，大批体制内骨干下海淘金，股票交易所开门红，沿海迎来狂飙发展。"],
      [2003, "世纪之交 · 世贸扬帆", "国企下岗阵痛与世纪之交相撞，加入WTO后外贸代工厂遍地开花，中国正式成为世界工厂。"],
      [2010, "北京奥运 · 四万亿潮", "鸟巢烟花点亮苍穹，四万亿基建全面铺开，高铁大网向全国延伸，房地产狂飙揭开大幕。"],
      [2016, "移动互联 · 创业神话", "智能手机普及与移动支付颠覆日常，百团大战风起云涌，大众创业催生无数科技风口神话。"],
      [2023, "动荡考验 · 产业洗牌", "疫情风波与全球产业链重构，教培互联网地产退潮，考公稳健与内生硬核制造成为共识。"],
      [2035, "生成式AI · 智算新质", "国产大模型颠覆知识脑力，新能源车横扫全球，商业航天与深空空间站并进，迈向高阶现代。"],
      [2045, "常温超导 · 聚变初并", "商业托卡马克聚变堆首度向城市群并网供电，常温超导输电网贯通，大城市建起恒温穹顶。"],
      [2055, "太空天梯 · 地月微重", "赤道太空电梯贯通低轨，微重力芯片晶圆厂常态生产，月球南极氦-3采掘船队往返穿梭。"],
      [2065, "神经脑机 · 算力配额", "视网膜脑机接口成为入世标配，全球碳积分与算力账户直接绑定，肉体与数据分化显现。"],
      [2075, "火星农业 · 外星拓荒", "水手峡谷基地人口突破两百万，地火航线常态化轮渡，年轻人在地球引力与异星自由间抉择。"],
      [2085, "自组超脑 · 硅基共治", "中央分布式超脑自主接管全球能源与司法调度，算法特区与旧人类自由城邦形成二元平衡。"],
      [2100, "强恒星暴 · 旧网归寂", "数十年一遇的超强太阳磁暴冲击内太阳系，行星偏转护盾彻夜泛起极光，考验文明抗灾韧性。"],
      [2110, "半人马座 · 星际点火", "人类首艘亚光速恒星际巨舰点火升空飞向比邻星，火种散播银河，正式迈向多恒星纪元。"],
      [null, "戴森云环 · 终幕跃迁", "人造能量金环环绕恒星熠熠生辉，戴森云初具规模，碳硅同辉，生命形式迈向全新维度。"],
    ];

    function resolveEraDetails(year, epochMode) {
      for (let i = 0; i < GRAND_ERA_TABLE.length; i++) {
        const row = GRAND_ERA_TABLE[i];
        if (row[0] === null || year < row[0]) return { name: row[1], desc: row[2] };
      }
      const last = GRAND_ERA_TABLE[GRAND_ERA_TABLE.length - 1];
      return { name: last[1], desc: last[2] };
    }

    function formatYearOnly(year) {
      const y = Math.round(year);
      if (y < 0) return `公元前 ${Math.abs(y)} 年`;
      if (y === 0) return '公元元年';
      return `公元 ${y} 年`;
    }
    function formatYearMonth(year, month) {
      const m = month || 1;
      return `${formatYearOnly(year)} ${m}月`;
    }
    function randomMonth() { return Math.floor(Math.random() * 12) + 1; }

    // 一生穿越过的所有大时代（按时间顺序去重）
    function listErasBetween(y0, y1) {
      const out = [];
      const a = Math.round(Math.min(y0, y1)), b = Math.round(Math.max(y0, y1));
      for (let y = a; y <= b; y++) {
        const n = resolveEraDetails(y, null).name;
        if (out[out.length - 1] !== n) out.push(n);
      }
      if (out.length === 0) out.push(resolveEraDetails(a, null).name);
      return out;
    }

    // 重大历史时事编年备考
    const HISTORICAL_LANDMARKS = [
      [-1046, "周武王克商，牧野之战，宗法礼乐与分封初立"],
      [-770, "周平王东迁洛邑，东周列国并起，春秋风云开端"],
      [-475, "战国争雄拉开帷幕，商鞅徙木立信主持秦国变法"],
      [-221, "始皇帝剪灭六国一统华夏，书同文车同轨立郡县"],
      [-202, "楚汉争霸落幕，汉高祖刘邦定都长安建立汉室"],
      [-138, "汉武帝遣张骞策马出使大月氏，丝绸之路自此凿空"],
      [220, "曹丕受禅汉帝退位魏国建立，天下三分鼎足而立"],
      [280, "西晋平定东吴重归一统，太康之治短暂承平"],
      [317, "琅琊王司马睿南渡建康，衣冠南渡开启东晋"],
      [589, "隋文帝发兵灭陈，南北分裂三百载后归于大一统"],
      [626, "太宗李世民登基改元贞观，励精图治辟贞观之治"],
      [713, "唐玄宗改元开元，万国商贾云集长安达极盛"],
      [755, "范阳安禄山起兵反叛，两京陆沉盛唐急转直下"],
      [960, "赵匡胤陈桥驿受袍代周立宋，杯酒释兵权消藩镇"],
      [1069, "神宗拜王安石为参知政事，青苗均输主持变法"],
      [1127, "靖康之变北宋东京陷落，赵构偏安临安建立南宋"],
      [1279, "崖山海战波涛沉绝，元世祖忽必烈大一统立行省"],
      [1368, "朱元璋于应天称帝建立大明，徐达北伐克复大都"],
      [1405, "郑和首率二百余艘宝船出刘家港，巡历西洋诸国"],
      [1644, "甲申之变崇祯殉社稷，清军入关定鼎北京"],
      [1684, "康熙开海贸易设立海关，四海晏然天下归心"],
      [1840, "第一次鸦片战争爆发，古老华夏被轰开海防国门"],
      [1898, "戊戌变法百日维新，变法志士血洒菜市口"],
      [1911, "武昌起义枪声裂夜，两千年帝制于辛亥之冬终结"],
      [1919, "五四风雷激荡北京，德先生赛先生启蒙一代青年"],
      [1937, "七七事变全面抗战爆发，全民族浴血守御山河"],
      [1945, "抗日战争取得伟大胜利，华夏大地洗雪百年屈辱"],
      [1949, "中华人民共和国中央人民政府成立，中国人民站起来了"],
      [1964, "大漠深处第一颗原子弹试验成功，挺起民族脊梁"],
      [1977, "中断十年的全国普通高等学校招生考试正式恢复"],
      [1978, "十一届三中全会召开，中国吹响改革开放宏阔号角"],
      [1992, "邓小平南巡发表历史性谈话，确定社会主义市场经济航向"],
      [1997, "香港历经百年沧桑洗礼正式回归祖国怀抱"],
      [2001, "中国正式签署协议加入世界贸易组织 (WTO)"],
      [2008, "第29届夏季奥林匹克运动会于北京鸟巢隆重开幕"],
      [2023, "以大型语言模型与算力矩阵为标志的生成式AI大爆发"],
      [2035, "首座商用全超导托卡马克核聚变堆试验并网成功"],
      [2050, "第一座地月引力平衡太空货运天梯正式交付商业运营"],
      [2075, "首批火星赤道区深岩闭环农业水耕穹顶全面丰收"],
      [2100, "首艘聚变驱动恒星际无人科学探测母舰驶离柯伊伯带"],
      [2150, "太阳系第一期全轨道戴森云聚能环骨架宣告初步合龙"],
    ];

    function resolveLandmark(year) {
      let closest = HISTORICAL_LANDMARKS[0];
      let minDiff = 999999;
      for (let i = 0; i < HISTORICAL_LANDMARKS.length; i++) {
        const diff = Math.abs(HISTORICAL_LANDMARKS[i][0] - year);
        if (diff < minDiff) { minDiff = diff; closest = HISTORICAL_LANDMARKS[i]; }
      }
      const yStr = formatYearOnly(closest[0]);
      return minDiff === 0 ? `${yStr} · ${closest[1]}` : (minDiff <= 8 ? `时近${yStr} · ${closest[1]}` : `${yStr} · ${closest[1]}`);
    }

    // ---- ancient 出身地域（8）与门第阶层（10）----
    const ANCIENT_REGIONS = [
{ name: "关中秦川", desc: "渭水两岸沃野千里，青铜农具初兴，军功爵下耕战并举，老秦人尚武重法。", stat: { health: 2, rep: 1 } },
{ name: "齐鲁之邦", desc: "洙泗之间儒风最盛，稷下论学、盐铁通商，士人抱竹简讲经，乡里重礼尚俭。", stat: { intellect: 3, rep: 2 } },
{ name: "荆楚云梦", desc: "江汉泽国水汽弥漫，稻作渔猎相济，漆器编钟见其工巧，楚人信巫好祀。", stat: { health: 1, happiness: 2 } },
{ name: "江南会稽", desc: "水乡稻熟鱼肥，越人断发文身，冶剑煮盐之利颇丰，商船沿江上下。", stat: { wealth: 2, luck: 1 } },
{ name: "陇西凉州", desc: "河西走廊胡商络绎，丝路驼铃与烽燧相望，边民自幼习骑射，风沙苦寒。", stat: { health: -1, luck: 2 } },
{ name: "中原洛邑", desc: "天下之中车马辐辏，诸侯会盟、百工聚居，市井喧嚣而礼法森严。", stat: { intellect: 2, wealth: 1, health: -1 } },
{ name: "燕赵之地", desc: "北接胡狄铁马边关，慷慨悲歌多壮士游侠，冬日苦寒而民风刚烈。", stat: { health: 2, rep: -1 } },
{ name: "巴蜀成都", desc: "岷江冲积沃野，都江堰引水灌田，蜀锦漆器行销四方，山高路险少兵祸。", stat: { health: 1, wealth: 2.5, happiness: 2 } }
    ];
    const ANCIENT_SOCIAL_STRATA = [
{
        title: "没落公族后裔",
        desc: "祖上曾列诸侯之卿，如今封邑尽削，只剩旧宅与几捆竹简；仍守祭祀礼数，却要变卖青铜器度日。",
        statMod: { health: 88, wealth: 3.2, intellect: 68, happiness: 52, luck: 49, rep: 58 },
        trait: "守礼自持"
      },
{
        title: "老秦耕战农卒",
        desc: "家在关中乡里，丁男按爵授田，农时扶犁、战时执戈；一纸军功文书便可改换门庭，故尚武不畏苦。",
        statMod: { health: 92, wealth: 0.8, intellect: 50, happiness: 55, luck: 50, rep: 40 },
        trait: "耐苦尚武"
      },
{
        title: "齐鲁经学儒士",
        desc: "世居洙泗之滨，家中藏经书数箧，子弟自幼习礼诵诗；以讲学授徒为业，虽清贫却颇受乡里敬重。",
        statMod: { health: 85, wealth: 2.5, intellect: 74, happiness: 58, luck: 52, rep: 66 },
        trait: "温厚好古"
      },
{
        title: "临淄盐铁巨贾",
        desc: "凭煮盐冶铁起家，车马奴婢成群，与官府往来密切；家中账册堆积，最怕朝廷一纸抑商之令。",
        statMod: { health: 86, wealth: 11.5, intellect: 66, happiness: 60, luck: 56, rep: 55 },
        trait: "精明豪爽"
      },
{
        title: "大唐西市胡商",
        desc: "自粟特远来，在长安西市经营香料珠宝，通数种语言；虽家资丰厚，却始终被视为异乡客，常思故土。",
        statMod: { health: 87, wealth: 9.8, intellect: 64, happiness: 57, luck: 58, rep: 42 },
        trait: "机敏健谈"
      },
{
        title: "终南山采药隐士",
        desc: "结庐终南山中，采药炼丹、观星著书，与樵夫野老为邻；不慕功名，只求清静长寿。",
        statMod: { health: 94, wealth: 0.6, intellect: 70, happiness: 66, luck: 54, rep: 62 },
        trait: "恬淡自适"
      },
{
        title: "太学博士门第",
        desc: "父祖累世为太学博士，家学以经义为本，子弟须通一经方能入仕；门庭清贵而俸禄微薄。",
        statMod: { health: 84, wealth: 4.6, intellect: 76, happiness: 60, luck: 51, rep: 74 },
        trait: "端方守正"
      },
{
        title: "边郡戍卒之家",
        desc: "父兄远戍烽燧，家中只有老母与幼弟，靠屯田薄收糊口；书信难通，年年盼望换防归乡的那一天。",
        statMod: { health: 91, wealth: 0.5, intellect: 47, happiness: 50, luck: 48, rep: 36 },
        trait: "坚忍寡言"
      },
{
        title: "织室匠户之家",
        desc: "隶属官营织室，母女终年坐机杼前，织成锦帛尽数入官；手艺极精却身役难脱，只盼朝廷宽免匠籍。",
        statMod: { health: 88, wealth: 1.4, intellect: 55, happiness: 53, luck: 52, rep: 34 },
        trait: "灵巧安分"
      },
{
        title: "豪强庄园宾客",
        desc: "寄身大姓庄园为宾客，耕其田、护其坞堡，得衣食与庇护；虽无户籍自由，却比编户安稳。",
        statMod: { health: 90, wealth: 7.6, intellect: 58, happiness: 56, luck: 53, rep: 60 },
        trait: "忠勇仗义"
      }
    ];

    // ---- premodern 出身地域（8）与门第阶层（10）----
    const PREMODERN_REGIONS = [
{ name: "汴京宣德门", desc: "御街宽阔，瓦舍勾栏彻夜喧闹，酒楼茶坊林立，四方商旅云集，市井繁华。", stat: { health: 1, wealth: 3, rep: 2 } },
{ name: "江南姑苏", desc: "水乡河道纵横，机户织坊林立，漕运码头帆樯相接，文风鼎盛，丝米富庶。", stat: { wealth: 3.5, intellect: 2, happiness: 1 } },
{ name: "泉州刺桐港", desc: "市舶司设于此，蕃商海舶辐辏，香料珠宝云集，海风咸湿，通贸四海。", stat: { wealth: 4, luck: 2, rep: -1 } },
{ name: "徽州休宁", desc: "山多田少，男子多出门行贾，宗族祠堂巍然，重儒重信，勤俭成风。", stat: { intellect: 3, rep: 4 } },
{ name: "直隶顺天", desc: "京师首善之地，官署林立，旗民杂居，街市规整，礼法森严。", stat: { rep: 3, wealth: 1.5, happiness: -1 } },
{ name: "天府成都", desc: "沃野千里，茶馆戏台声声入耳，蜀锦名扬，百姓闲适安逸。", stat: { happiness: 3, health: 1, intellect: 1 } },
{ name: "山陕商道", desc: "驼铃古道，晋商票号往来不绝，风沙扑面，商旅重诺守信。", stat: { wealth: 2, luck: 1, health: -1 } },
{ name: "广州十三行", desc: "海禁之下独口通商，洋货行栈毗邻，商贾云集，银钱往来浩繁。", stat: { wealth: 5, rep: -2, luck: 1 } }
    ];
    const PREMODERN_SOCIAL_STRATA = [
{
        title: "江南织造机户",
        desc: "家中织机数张，日夜赶织绸缎，靠机户手艺营生，日子殷实却辛苦。",
        statMod: { health: 86, wealth: 6.5, intellect: 58, happiness: 58, luck: 52, rep: 55 },
        trait: "勤巧持家"
      },
{
        title: "徽州儒商门第",
        desc: "祖上经商起家，亦贾亦儒，家训以诚信为本，子弟须读书应试，光耀门楣。",
        statMod: { health: 88, wealth: 9.5, intellect: 70, happiness: 60, luck: 54, rep: 68 },
        trait: "贾而好儒"
      },
{
        title: "钱塘书院耕读",
        desc: "家有薄田数亩，耕读并重，父辈供子弟入书院受业，盼科举改换门庭。",
        statMod: { health: 87, wealth: 3.2, intellect: 74, happiness: 57, luck: 50, rep: 62 },
        trait: "诗礼传家"
      },
{
        title: "泉州远洋海商",
        desc: "家中有海船股份，货通南洋诸国，风浪里讨生活，富贵与凶险并存。",
        statMod: { health: 84, wealth: 11, intellect: 62, happiness: 56, luck: 58, rep: 60 },
        trait: "敢闯重信"
      },
{
        title: "京畿旗人食禄",
        desc: "隶于旗籍，按月支领钱粮，不必躬耕劳作，闲时遛鸟听戏，日子安稳。",
        statMod: { health: 92, wealth: 8, intellect: 52, happiness: 64, luck: 56, rep: 58 },
        trait: "安闲守分"
      },
{
        title: "乡村私塾寒儒",
        desc: "世代教蒙学为生，束脩微薄，家徒四壁却藏书满架，清高自守，颇受乡邻敬重。",
        statMod: { health: 85, wealth: 1.2, intellect: 76, happiness: 51, luck: 49, rep: 50 },
        trait: "清贫守志"
      },
{
        title: "运河漕帮水手",
        desc: "常年在漕船上搬运粮米，靠力气吃饭，讲义气，风餐露宿，结交帮中兄弟。",
        statMod: { health: 90, wealth: 2.4, intellect: 49, happiness: 53, luck: 51, rep: 44 },
        trait: "义气耐劳"
      },
{
        title: "两淮盐引巨富",
        desc: "持盐引行销数省，家资巨万，宅第连云，仆从成群，与官府往来密切。",
        statMod: { health: 89, wealth: 12, intellect: 66, happiness: 62, luck: 57, rep: 72 },
        trait: "阔绰通权"
      },
{
        title: "晋商票号伙计",
        desc: "在票号学徒出身，掌银钱汇兑，常年奔走各地，精于算计，恪守号规。",
        statMod: { health: 86, wealth: 4.8, intellect: 68, happiness: 55, luck: 53, rep: 57 },
        trait: "精算守信"
      },
{
        title: "边镇屯戍军户",
        desc: "世袭军籍，屯田守边，粮饷微薄，常在风沙中操练巡防，升迁无望。",
        statMod: { health: 94, wealth: 0.6, intellect: 47, happiness: 50, luck: 48, rep: 40 },
        trait: "粗豪尚武"
      }
    ];

    // ---- modern 出身地域（8）与门第阶层（10）----
    const MODERN_REGIONS = [
{ name: "上海租界", desc: "黄包车往来于弄堂口，报馆与纱厂汽笛声里，银元与铜板在账房间叮当作响。", stat: { health: 1, wealth: 2, luck: 1 } },
{ name: "江南水乡", desc: "河港交错，乌篷船摇过石桥，蚕桑与稻米支撑着一家老小的口粮。", stat: { health: 2, wealth: 1 } },
{ name: "华北平原", desc: "黄土地里刨食，旱涝轮番，麦收之后仍要提防溃兵与散匪过境。", stat: { health: 2, wealth: -1 } },
{ name: "东北煤城", desc: "矿井巷道终年不见日头，工棚里煤灰味混着苞米面饼子的热气。", stat: { health: -1, wealth: 1, rep: 1 } },
{ name: "西南山城", desc: "石阶陡斜，雾汽终年不散，滑竿与挑担在坡道间换得一日三餐。", stat: { health: 2, luck: 1 } },
{ name: "西北军垦", desc: "风沙扑打营房，屯垦的人白天开渠，夜里听远处传来稀疏的枪声。", stat: { health: 2, rep: 1 } },
{ name: "岭南侨乡", desc: "骑楼连廊下茶肆喧嚷，侨批局的信差带来南洋汇款与一纸平安。", stat: { wealth: 2, intellect: 1 } },
{ name: "北平皇城根", desc: "城墙根底下卖豆汁与烤白薯，学堂里的读书声压过胡同的鸽哨。", stat: { intellect: 3, rep: 1 } }
    ];
    const MODERN_SOCIAL_STRATA = [
{
        title: "纱厂职员门第",
        desc: "父辈在纱厂账房间做文书，月薪折合几块银元，一家人在亭子间里维持体面。",
        statMod: { health: 86, wealth: 4.5, intellect: 60, happiness: 58, luck: 52, rep: 55 },
        trait: "谨小慎微"
      },
{
        title: "乡间佃农之家",
        desc: "租种东家几亩薄田，丰年缴完租子所剩无几，青黄不接时以野菜掺粮度日。",
        statMod: { health: 84, wealth: 0.5, intellect: 48, happiness: 52, luck: 50, rep: 38 },
        trait: "勤恳本分"
      },
{
        title: "县城私塾先生",
        desc: "守着一间旧书房，教村童认字读经，束脩微薄却受乡邻敬重。",
        statMod: { health: 84, wealth: 2.5, intellect: 74, happiness: 60, luck: 51, rep: 68 },
        trait: "清高自持"
      },
{
        title: "行商小贩人家",
        desc: "挑担赶集贩卖针头线脑，逢节赶庙会，风雨里算计着一家人的嚼用。",
        statMod: { health: 87, wealth: 3.2, intellect: 56, happiness: 57, luck: 55, rep: 46 },
        trait: "精打细算"
      },
{
        title: "铁路工人门庭",
        desc: "父兄在机务段抡扳手，靠工钱与工友互助过活，逢罢工便全家悬心。",
        statMod: { health: 88, wealth: 3.8, intellect: 54, happiness: 56, luck: 51, rep: 58 },
        trait: "仗义执言"
      },
{
        title: "军人家眷门第",
        desc: "男丁随军在外，家中靠抚恤与做针线糊口，一封信要等上半年。",
        statMod: { health: 82, wealth: 2, intellect: 50, happiness: 53, luck: 49, rep: 65 },
        trait: "含辛茹苦"
      },
{
        title: "中医坐堂世家",
        desc: "祖上三代坐堂问诊，药柜里藏着旧方，诊金随人给，贫者常不计较。",
        statMod: { health: 90, wealth: 5.5, intellect: 70, happiness: 62, luck: 53, rep: 72 },
        trait: "医者仁心"
      },
{
        title: "梨园戏班门第",
        desc: "在茶楼戏园里唱念做打，红时满堂喝彩，背时连行头都要典当。",
        statMod: { health: 85, wealth: 3, intellect: 58, happiness: 63, luck: 56, rep: 52 },
        trait: "洒脱不羁"
      },
{
        title: "邮政信差门第",
        desc: "穿绿制服走街串巷送信送报，脚力换来的薪水平稳，只是风雨无阻。",
        statMod: { health: 89, wealth: 3.6, intellect: 61, happiness: 60, luck: 52, rep: 62 },
        trait: "恪尽职守"
      },
{
        title: "华侨汇款之家",
        desc: "南洋的叔伯按月寄回侨批，家中衣食稍宽，却常年悬着远方的牵挂。",
        statMod: { health: 87, wealth: 8.5, intellect: 63, happiness: 57, luck: 54, rep: 60 },
        trait: "守望相助"
      }
    ];

    // ---- ancient 16 大生命阶段事件池（每阶段多个候选，单局随机抽取）----
    const ANCIENT_STAGE_POOLS = [
      [
      {
        period: "幼年启蒙",
        title: "竹简刀笔间初识天下字",
        narrative: (p, y) => "蒙学设在族中旧屋，先生以刀笔在竹简上刻字，命你逐字摹写。窗外井田里父兄正忙春耕，缺一个递水送饭的帮手。先生却道今日十简未成，不许归家。你握着刻刀，手心渐渐发汗。",
        choices: [
          { text: "咬牙刻完十简，宁可饿着肚子也要让先生点头", riskLevel: "寒窗苦读 · 稳妥积淀 · 成功率 75%", successChance: (p) => 75 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "先生抚简称善，将你的名字写在学簿头一行，族中长辈闻讯，派人送来一块干肉。", failFeedback: "手指被刀笔磨破，简上字迹歪斜，先生叹你心浮，罚你明日再刻二十简。", successEffect: { intellect: 10, rep: 5 }, failEffect: { intellect: 4, happiness: -5 }, tagSuccess: "刀笔初成", tagFail: "手拙受罚", isKey: true },
          { text: "借口腹痛溜去田头，帮父兄递水送饭，趁隙偷听农事", riskLevel: "亲近田垄 · 事功渐长 · 稳妥必成", successChance: (p) => 100, successFeedback: "父兄夸你懂事，教你辨认节气与土色，你把一句句农谚默默记在心里。", failFeedback: "", successEffect: { health: 6, wealth: 2, happiness: 6 }, failEffect: {  }, tagSuccess: "田垄情长", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "幼年启蒙",
        title: "宗庙习礼初见尊卑",
        narrative: (p, y) => "岁末祭祖，族中长者命你捧青铜小俎，立于阶下随众行礼。你腿脚酸麻，忽见邻家小儿在庙外招手，邀你去河边看新捕的鱼。长者目光沉沉扫来，俎中祭肉须捧到礼毕方止。",
        choices: [
          { text: "屏息站定，把俎捧到礼毕，一步也不曾挪动", riskLevel: "恪守宗法 · 沉稳有度 · 成功率 80%", successChance: (p) => 80, successFeedback: "长者当众赞你知礼，把祭余的一块肉亲手分给你，道此子可教，将来可托付。", failFeedback: "你终究忍不住回头张望，被长者一眼看见，罚你跪在阶下，直到日头西沉。", successEffect: { intellect: 4, rep: 8 }, failEffect: { health: -3, happiness: -6, rep: -5 }, tagSuccess: "知礼守节", tagFail: "失仪受罚", isKey: true },
          { text: "趁长者低头祝祷，悄悄溜出庙门去河边看鱼", riskLevel: "任性贪玩 · 快意当前 · 稳妥必成", successChance: (p) => 100, successFeedback: "你摸到一尾滑鱼，笑得很大声，回家时衣襟尽湿，心头却痛快极了。", failFeedback: "", successEffect: { health: 4, happiness: 10, rep: -3 }, failEffect: {  }, tagSuccess: "童心未泯", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "童年韶光",
        title: "乡塾比试射御夺头筹",
        narrative: (p, y) => "乡塾春日较艺，诸童须张弓射柳，胜者得先生一支刻字木牍。你用的弓是兄长旧物，弦已松软。同窗中有一人箭术极精，正笑你弓弱，先生却已击柝催令，众人列队上前。",
        choices: [
          { text: "借力巧射，专瞄近处柳枝，稳中求胜不逞强", riskLevel: "审时度势 · 巧取头筹 · 成功率 70%", successChance: (p) => 70 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 3 : 0), successFeedback: "三箭两中，先生将木牍递到你手中，同窗们围上来要摸那支箭，眼里都是羡慕。", failFeedback: "弓弦忽然崩断，箭落在柳树根下，众人哄笑，你脸红到耳根，握弓的手发颤。", successEffect: { health: 4, intellect: 6, rep: 8 }, failEffect: { health: -2, happiness: -6, rep: -5 }, tagSuccess: "箭无虚发", tagFail: "弦断人笑", isKey: true },
          { text: "远远退开十步再射，赌自己臂力过人，一箭惊人", riskLevel: "逞强好胜 · 意气用事 · 成功率 40%", successChance: (p) => 40 + (p.health > 60 ? 3 : 0), successFeedback: "箭如流星穿柳而过，满塾哗然，连先生也捋须颔首，说你力气不小。", failFeedback: "臂力不济，箭软软坠地，你被同窗起了绰号，半月抬不起头来。", successEffect: { health: 6, happiness: 5, rep: 10 }, failEffect: { health: -3, happiness: -8, rep: -4 }, tagSuccess: "一箭惊人", tagFail: "力不从心", isKey: false }
        ]
      },
      {
        period: "童年韶光",
        title: "随父兄入市贩粟议价",
        narrative: (p, y) => "秋收之后，父兄推车入市贩粟，命你看守钱袋并学着与买主议价。市中有掮客愿出高价全收，却要赊账至来年。族里正等这笔钱添置铁镰，你也想给自己买一册旧竹书。",
        choices: [
          { text: "压价卖给散客，宁可多等半日也要现钱落袋", riskLevel: "稳妥持家 · 细水长流 · 成功率 78%", successChance: (p) => 78 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "粟卖得干净，钱袋沉实，父兄允你留下一枚小钱，你买回半册旧书。", failFeedback: "散客挑拣压价，日暮仍有半车粟，父兄沉沉叹息，你懊恼地收摊。", successEffect: { wealth: 8, intellect: 5, happiness: 4 }, failEffect: { wealth: -4, happiness: -5 }, tagSuccess: "粒粟皆金", tagFail: "坐失良机", isKey: true },
          { text: "贪那高价，劝父兄赊给掮客，立下竹券为凭", riskLevel: "放债图利 · 险中求财 · 成功率 50%", successChance: (p) => 50 + (p.luck > 50 ? 4 : 0), successFeedback: "掮客如约践诺，来年送来双倍粟钱，还引你认得几位往来行商。", failFeedback: "掮客一去无踪，竹券成了废简，家中当年缺了农具，你愧疚良久。", successEffect: { wealth: 14, luck: 3, rep: 5 }, failEffect: { wealth: -10, happiness: -6 }, tagSuccess: "券约得偿", tagFail: "券成废简", isKey: false }
        ]
      }
      ],
      [
      {
        period: "少年分流",
        title: "负笈远行千里求见名师",
        narrative: (p, y) => "闻邻郡有位饱学先生开门授徒，讲论百家之说，士子往来如云。你欲负笈前往，然家中田亩将收，父母盼你留下帮工；路远盘缠不足，须卖掉母亲亲手织的一匹布。",
        choices: [
          { text: "卖掉那匹布作盘缠，星夜启程，投帖拜入先生门下", riskLevel: "负笈千里 · 孤注一掷 · 成功率 65%", successChance: (p) => 65 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 4 : 0), successFeedback: "先生见你衣衫破旧而应答不俗，破例收你为徒，还赐半间草舍安身。", failFeedback: "先生门徒已满，你被拒之门外，盘缠耗尽，只好沿路乞食徒步归家。", successEffect: { intellect: 14, happiness: 5, rep: 6 }, failEffect: { wealth: -8, intellect: 5, happiness: -7 }, tagSuccess: "得列门墙", tagFail: "白走一遭", isKey: true },
          { text: "先留家中收完秋粮，再挑一担新粟去换书简自学", riskLevel: "耕读两全 · 稳中有进 · 成功率 85%", successChance: (p) => 85, successFeedback: "秋粮入仓，你换回几卷书简，夜里就着灶火抄读，字迹工整可观。", failFeedback: "白日劳碌，夜里读不上两行便困倒，书简在手边积了一层灰。", successEffect: { wealth: 4, intellect: 8, happiness: 3 }, failEffect: { intellect: 2, happiness: -4 }, tagSuccess: "耕读自持", tagFail: "灯下倦读", isKey: false }
        ]
      },
      {
        period: "少年分流",
        title: "里正登门点选徭役",
        narrative: (p, y) => "郡县征发徭役，里正捧名册登门，你已够岁数，须随众去修驰道、筑边城。同里有人愿出钱代役，只求顶你的名额；父母年迈，你亦想去外头见见世面。",
        choices: [
          { text: "接下名册，随队上路，在役夫中多学一门手艺", riskLevel: "应役远行 · 见闻渐广 · 成功率 72%", successChance: (p) => 72 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.health > 60 ? 5 : 0), successFeedback: "你在工地上跟匠人学会夯土与量绳，还结识了一位识字的小吏。", failFeedback: "烈日之下水土不服，你病倒在工棚，被提前遣送回乡，一路颠簸。", successEffect: { health: 8, intellect: 6, rep: 5 }, failEffect: { health: -10, happiness: -6, rep: -3 }, tagSuccess: "应役有成", tagFail: "病卧工棚", isKey: true },
          { text: "收下那人的钱替家里添牛，自己躲过这趟徭役", riskLevel: "以钱代役 · 安守家门 · 稳妥必成", successChance: (p) => 100, successFeedback: "家中添了一头小牛，秋耕省力不少，父母难得舒展了眉头。", failFeedback: "", successEffect: { wealth: 10, happiness: 5 }, failEffect: {  }, tagSuccess: "以钱代役", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "成人立志",
        title: "郡府征辟与边关募兵",
        narrative: (p, y) => "郡府小吏来乡里访贤，言你若通经明法，可先充书佐；同时边关募兵，斩首有赏，立功可入行伍。两条路摆在眼前：一条稳而慢，一条险而快。父母只盼你平安，却也盼你出息。",
        choices: [
          { text: "投身边关，执戈从军，凭军功博一个出身", riskLevel: "投笔从戎 · 险中求贵 · 成功率 55%", successChance: (p) => 55 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 5 : 0) + (p.health > 60 ? 4 : 0), successFeedback: "你随军破敌，斩获首级，校尉记你首功，授你什长之职，同伍皆服。", failFeedback: "初战即伤，你被抬回营帐，虽保住性命，却落下每逢阴雨便痛的旧疾。", successEffect: { health: 6, wealth: 8, rep: 15 }, failEffect: { health: -15, happiness: -6, rep: -4 }, tagSuccess: "首功授职", tagFail: "负伤而归", isKey: true },
          { text: "入郡府为书佐，掌文书簿册，在案牍间积累人望", riskLevel: "案牍立身 · 稳进仕途 · 成功率 88%", successChance: (p) => 88 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "你抄录文书从不出错，郡丞颇赏识，将你举荐给上官，前途渐明。", failFeedback: "一笔误抄惹出是非，你被罚俸半月，同僚也渐渐疏远了你。", successEffect: { wealth: 6, intellect: 10, rep: 10 }, failEffect: { wealth: -3, happiness: -5, rep: -6 }, tagSuccess: "文牍见赏", tagFail: "误抄见罚", isKey: false }
        ]
      },
      {
        period: "成人立志",
        title: "胡商车队过境邀你同行",
        narrative: (p, y) => "一支胡商驼队过境歇脚，领头的胡商见你通晓数算、口齿伶俐，邀你随队西行贩运丝绸，许诺分你一份厚利。此去关山万里，归期难料；而家中正为你议亲，只待你点头。",
        choices: [
          { text: "收拾行囊随商队西行，把命与运押在长路上", riskLevel: "万里行商 · 富贵险求 · 成功率 50%", successChance: (p) => 50 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 6 : 0), successFeedback: "驼队平安出关，你贩丝获利数倍，归来时乡人皆出门观看，啧啧称奇。", failFeedback: "途中遇劫，货物尽失，你徒步东归，瘦得父母几乎认不出你来。", successEffect: { wealth: 25, luck: 4, rep: 8 }, failEffect: { health: -8, wealth: -18, happiness: -8 }, tagSuccess: "满载而归", tagFail: "货失人还", isKey: true },
          { text: "留在乡里，用积蓄开一间小肆，收售乡邻杂物", riskLevel: "守土小贾 · 安稳度日 · 稳妥必成", successChance: (p) => 100, successFeedback: "小肆开张，乡邻常来赊账却也常来照顾，日子过得安稳而有盈余。", failFeedback: "", successEffect: { wealth: 12, happiness: 6, rep: 3 }, failEffect: {  }, tagSuccess: "小肆安稳", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "青春韶华",
        title: "县廷征召，试为刀笔小吏",
        narrative: (p, y) => "乡啬夫传话过来，县廷缺一名书佐，要识字的年轻人前去应试。你案头摊着几卷残简，父亲却盼你留在家中照看田亩与年迈的祖母。同里已有人在县衙当差，衣冠整齐，说话也硬气。去试，或许能踏上吏途；不去，家中秋收便少一双手。",
        choices: [
          { text: "收拾好简牍笔墨，天明便去县廷报名应考书佐", riskLevel: "求名有路 · 失家劳力 · 成功率 65%", successChance: (p) => 65 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 3 : 0), successFeedback: "主吏考你书算，见你小篆工整，当场录为书佐，递来一枚竹简作凭信。", failFeedback: "你小篆尚可，算数却慢，主吏摇头让你回去，祖母的汤药钱仍无着落。", successEffect: { wealth: 3, intellect: 8, rep: 6 }, failEffect: { intellect: 3, happiness: -5 }, tagSuccess: "刀笔初试", tagFail: "铩羽而归", isKey: true },
          { text: "先留在家中操持农事，夜里就着豆灯自读律令", riskLevel: "守家尽责 · 缓图后计 · 稳妥必成", successChance: (p) => 100, successFeedback: "你白日扶犁，夜里诵律，乡邻都称你稳重，来日征召必先念及你。", failFeedback: "", successEffect: { intellect: 4, happiness: 5, rep: 4 }, failEffect: {  }, tagSuccess: "耕读自守", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "青春韶华",
        title: "负笈远游，拜入名师门下",
        narrative: (p, y) => "听说郡中有位老儒开门授徒，讲《春秋》与律令，弟子多被州府辟用。你背着一箱旧简走了三日，可拜师需奉束脩，家中只凑出一匹粗帛。同舍生多是豪族子弟，衣冠整齐，谈笑间已互称表字。留下，或可博一个出身；折返，则这三日脚程白费。",
        choices: [
          { text: "情愿奉上一匹粗帛，甘居下座替师门抄书抵束脩", riskLevel: "虚心求教 · 以劳补拙 · 成功率 70%", successChance: (p) => 70 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "老儒见你抄录细密无误，留你居下舍，命你专掌经卷，同门也来借问。", failFeedback: "抄错三处经文，被罚立在庭中背诵，粗帛已收，颜面也丢了半截。", successEffect: { intellect: 10, rep: 5 }, failEffect: { intellect: 4, happiness: -6 }, tagSuccess: "师门垂青", tagFail: "当庭受责", isKey: true },
          { text: "不拜师门，只在市旁赁屋替旅人代写书信契券", riskLevel: "自谋生计 · 学无常师 · 稳妥必成", successChance: (p) => 100, successFeedback: "你替旅人写家书、替乡邻写契券，铜钱虽少，识字的名声却传开了。", failFeedback: "", successEffect: { wealth: 5, happiness: 3, rep: 3 }, failEffect: {  }, tagSuccess: "市井笔耕", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "初涉人世",
        title: "边郡征戍，登烽燧望狼烟",
        narrative: (p, y) => "县里张榜，北边烽燧缺戍卒，去者免一岁赋，归来可叙功受爵。你新婚未久，妻子腹中已有身孕。里正说，边地苦寒，胡骑时来劫掠，也有人一去三年杳无音信。应征，或能凭军功脱去布衣；不去，则要纳钱代役，家中粟米本就见底。",
        choices: [
          { text: "应征北上，把自己的姓名报入戍卒名册，随队出发", riskLevel: "军功可期 · 生死难卜 · 成功率 55%", successChance: (p) => 55 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 4 : 0) + (p.health > 60 ? 4 : 0), successFeedback: "你随队登燧瞭望，一日烽火骤起，你率先举炬示警，都尉记你一功。", failFeedback: "深秋一场疫病，同伍倒了三人，你虽活下来，归期又拖了半年。", successEffect: { health: 3, wealth: 6, rep: 8 }, failEffect: { health: -10, wealth: 3, happiness: -8 }, tagSuccess: "烽燧立功", tagFail: "边地病归", isKey: true },
          { text: "留在乡里，替戍边之人纳粟代役并代为照料其家", riskLevel: "破财免行 · 结好乡邻 · 稳妥必成", successChance: (p) => 100, successFeedback: "你典卖半亩薄田完纳代役钱，乡邻念你信义，常来帮你收割。", failFeedback: "", successEffect: { wealth: -8, happiness: 4, rep: 6 }, failEffect: {  }, tagSuccess: "信义乡里", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "初涉人世",
        title: "随商队西行，贩缯帛于关市",
        narrative: (p, y) => "姑臧来的商队缺一个记账的伙计，说走一趟河西，缯帛换回玉与苜蓿，利可数倍。妻子不愿你远行，族中长辈却想借你探探关市行情。此行要过边关，路上有盗匪，也有盘查的关吏。若得利，家业可起；若折本，连聘礼的欠账都还不上。",
        choices: [
          { text: "随队西行，一路上替商主记账、验货、押运缯帛", riskLevel: "重利远行 · 关山险阻 · 成功率 60%", successChance: (p) => 60 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 4 : 0) + (p.health > 60 ? 3 : 0), successFeedback: "你在关市议价得当，缯帛脱手极快，商主分你两匹绢，另许下次同行。", failFeedback: "半途遇盗，货物折了大半，商主未责你，你却分文未得，还病了一场。", successEffect: { wealth: 18, intellect: 6, rep: 4 }, failEffect: { health: -6, wealth: -12, happiness: -5 }, tagSuccess: "关市获利", tagFail: "折货空归", isKey: true },
          { text: "不涉远途，只在县邑集市之间做些零碎转贩生意", riskLevel: "小本经营 · 稳中求进 · 稳妥必成", successChance: (p) => 100, successFeedback: "你收乡下的布、卖城里的盐，薄利细攒，一年下来也添了两只健牛。", failFeedback: "", successEffect: { wealth: 7, happiness: 3 }, failEffect: {  }, tagSuccess: "小贩积财", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "成家立业",
        title: "纳采问名，聘礼尚差一筹",
        narrative: (p, y) => "你与邻县女子相看已定，媒人来回奔走，只差最后一道纳征。女方家说，聘礼不论厚薄，只求体面；可你清点家中，粟不足十石，布只两匹。族兄劝你借债备礼，以免失了脸面；也有人劝你据实相告，莫为一时风光耗尽来年的种粮。",
        choices: [
          { text: "向族兄借贷，也要备齐聘礼风风光光地纳征", riskLevel: "顾全颜面 · 负债成婚 · 成功率 72%", successChance: (p) => 72 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "女方家见礼数周全，欣然许婚，乡里都说这门亲事体面，你也得了个贤内助。", failFeedback: "债主催得紧，婚后第一年你常为还钱奔忙，妻子虽无怨言，你心里不好受。", successEffect: { wealth: -10, happiness: 12, rep: 6 }, failEffect: { wealth: -16, happiness: 4, rep: 2 }, tagSuccess: "六礼告成", tagFail: "婚成债重", isKey: true },
          { text: "据实相告，以自家织的两匹布和十石粟为礼", riskLevel: "坦诚量力 · 平淡成礼 · 稳妥必成", successChance: (p) => 100, successFeedback: "女方父母见你诚实持重，反赞你可靠，婚事从简而办，两家都无怨言。", failFeedback: "", successEffect: { happiness: 9, rep: 4 }, failEffect: {  }, tagSuccess: "布粟为聘", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "成家立业",
        title: "族中分家，一卷薄田起争执",
        narrative: (p, y) => "父亲过世，族老主持析产。兄长的儿子多、人口重，主张按口分田；你只一房妻小，按理可分较肥的近水田。族老却劝你顾全兄弟情面，先让一步。争，或可多得几亩活命田；让，则要在族中落个谦让的名声。可来年春耕，种子和耕牛都等着用钱。",
        choices: [
          { text: "据理力争，务必请族老依据律令与旧契当众明断", riskLevel: "寸土必争 · 伤了手足 · 成功率 68%", successChance: (p) => 68 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "族老翻出旧契，判你分得近水田两段，秋收丰足，妻子终于展颜。", failFeedback: "兄长当众骂你刻薄，田虽多争半亩，族中却许久不与你往来。", successEffect: { wealth: 12, happiness: -3, rep: 4 }, failEffect: { wealth: 5, happiness: -8, rep: -8 }, tagSuccess: "依法得田", tagFail: "析产失和", isKey: true },
          { text: "主动让出近水肥田，另择坡地并多要农具", riskLevel: "谦让全亲 · 另图桑麻 · 稳妥必成", successChance: (p) => 100, successFeedback: "你让了好田却得全套农具与耕牛，坡地种桑养蚕，来年另有一份进项。", failFeedback: "", successEffect: { wealth: -3, happiness: 6, rep: 8 }, failEffect: {  }, tagSuccess: "让田得牛", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "三十而立",
        title: "郡国举荐，孝廉之名在望",
        narrative: (p, y) => "郡守下教，要举一名孝廉入京对策，乡里议论纷纷，数你的孝行与文书最好。可另一家是本地豪族的子弟，门生故吏众多，已暗中打点。郡中主吏暗示，你若肯送些土物，事便可成。举，则一生仕途由此起；不举，则数年耕读尽付流水。",
        choices: [
          { text: "备下薄礼拜访郡中主吏，请其在郡守面前美言", riskLevel: "通融求举 · 名节有损 · 成功率 58%", successChance: (p) => 58 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 4 : 0), successFeedback: "郡守果以你为孝廉，车马入京对策，你第一次望见宫阙的飞檐。", failFeedback: "主吏收了礼却不认账，豪族子弟得举，你反落下结交吏胥的话柄。", successEffect: { wealth: -5, intellect: 6, rep: 10 }, failEffect: { wealth: -8, happiness: -8, rep: -10 }, tagSuccess: "举为孝廉", tagFail: "求举见欺", isKey: true },
          { text: "不送一物，只把历年劝农赈济的簿册呈给郡守", riskLevel: "以实自荐 · 静候公论 · 稳妥必成", successChance: (p) => 100, successFeedback: "郡守翻阅簿册，见你历年赈济灾民条条有据，叹你朴实，将你列入备选。", failFeedback: "", successEffect: { intellect: 4, happiness: 4, rep: 7 }, failEffect: {  }, tagSuccess: "簿册自明", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "三十而立",
        title: "岁大饥，流民叩门求一斗粟",
        narrative: (p, y) => "连月大旱，邻郡流民成群过境，篷车停在里门外。你家仓中尚存粟三十石，是来年春耕与全家口粮。里正说，郡府令各户出粟赈济，可事后未必补偿；也有人说，此时开仓能结下四方人望，来日或有大用。妻子抱着幼子，望着你的脸不说话。",
        choices: [
          { text: "开仓出粟十石赈济流民，并邀壮者留下垦荒", riskLevel: "散粟结众 · 来年恐饥 · 成功率 70%", successChance: (p) => 70 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 3 : 0), successFeedback: "流民感你恩义，数十壮者留下替你开垦荒坡，里中皆称你有长者之风。", failFeedback: "流民一哄而散，粟去了大半，来年春耕你只得向族兄借种。", successEffect: { wealth: -10, happiness: 6, rep: 12 }, failEffect: { wealth: -16, happiness: -6, rep: 3 }, tagSuccess: "散粟得众", tagFail: "粟尽人散", isKey: true },
          { text: "只在门外施粥三日，其余时候闭门护住自家粮种", riskLevel: "量力施惠 · 先保家门 · 稳妥必成", successChance: (p) => 100, successFeedback: "你施粥三日全了情面，又保住大半粮种，春耕未误，一家安然。", failFeedback: "", successEffect: { wealth: 2, happiness: 2, rep: 3 }, failEffect: {  }, tagSuccess: "施粥护仓", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "负重前行",
        title: "郡府辟召，党锢之祸风声紧",
        narrative: (p, y) => "郡府征辟的檄文送到柴门，你却在乡里听闻朝中党锢再起，名士下狱者众。老母卧病在床，药石将尽；长子方习《春秋》，指望你谋一官半职。受辟可光门楣，却也恐被列为党人；拒之则清名自保，家中却要再熬几个荒年。你该何去何从？",
        choices: [
          { text: "应辟入府，只理刑名钱谷，不与清流名士往来结党", riskLevel: "宦海风波 · 清誉难全 · 成功率 62%", successChance: (p) => 62 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 3 : 0), successFeedback: "同僚只当你是个谨慎的佐吏，党狱大兴时未有人攀扯你。三年后你升任郡丞，俸禄渐丰，老母的药也未曾断过。", failFeedback: "党人名单上终究添了你的名字。免官下狱半年，虽未丧命，家资却折了大半，出狱时鬓边已白。", successEffect: { wealth: 12, intellect: 8, rep: 4 }, failEffect: { wealth: -5, happiness: -6, rep: -8 }, tagSuccess: "明哲保身", tagFail: "党锢牵连", isKey: true },
          { text: "称病谢辟，闭门奉母教子，把余粮换成桑田与书卷", riskLevel: "清贫自守 · 门第渐衰 · 稳妥必成", successChance: (p) => 100, successFeedback: "你闭门谢客，日日为母亲煎药，灯下教长子读《春秋》。乡里称你孝谨，州府后来竟以孝廉相举。", failFeedback: "", successEffect: { intellect: 5, happiness: 8, rep: 6 }, failEffect: {  }, tagSuccess: "守拙养亲", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "负重前行",
        title: "丁忧三载，族中田产待分",
        narrative: (p, y) => "老母终究没能熬过这个冬天。你按礼制解官持丧，庐墓三年。丧事方毕，族中长辈便提起祖田析分：叔父主张按房均分，堂兄却说你久宦在外，田界早已含混。妻儿要生计，亡母遗训在耳，你握着那卷发黄的田契，指节发白。",
        choices: [
          { text: "依礼庐墓，请族中三老作证，按旧契重新丈量田界", riskLevel: "丁忧守制 · 争产伤亲 · 成功率 68%", successChance: (p) => 68 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 2 : 0), successFeedback: "你请三老与乡邻作证，旧契界石一一勘明，祖田按房均分。族人虽有小怨，终究服你的公道。", failFeedback: "丈量时界石早被人挪动，堂兄又串通书吏改了鱼鳞册。你只争回薄田几亩，与堂兄从此不相往来。", successEffect: { wealth: 10, happiness: 4, rep: 8 }, failEffect: { wealth: -8, happiness: -8, rep: -5 }, tagSuccess: "依礼析产", tagFail: "阋墙生隙", isKey: true },
          { text: "索性把名下好田尽让堂兄，只留薄田数亩供祭扫", riskLevel: "让产全族 · 家计转薄 · 稳妥必成", successChance: (p) => 100, successFeedback: "你把好田尽让堂兄，只留祭田数亩。族中皆称你重义，此后每逢荒年，堂兄反倒常送粮相济。", failFeedback: "", successEffect: { wealth: -10, happiness: 6, rep: 12 }, failEffect: {  }, tagSuccess: "让田全义", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "中年险滩",
        title: "遭诬下狱，讼牒压在案头",
        narrative: (p, y) => "县廷一纸牒文将你收系狱中，告你侵吞漕粮。实情是主吏改了斛斗，账目被做了手脚。狱吏索钱，同囚劝你认罪求轻判；妻子在门外奔走，变卖嫁妆疏通门路。若屈招，家产可保一半，清名尽毁；若死扛，或能等到按察使覆核，也可能毙于杖下。",
        choices: [
          { text: "拒不画押，托旧交将原账与证人姓名递到州府按察", riskLevel: "生死一纸 · 昭雪难期 · 成功率 45%", successChance: (p) => 45 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 4 : 0) + (p.health > 60 ? 3 : 0), successFeedback: "按察使覆核旧账，果然查出主吏改斛之弊。你无罪开释，那吏员反坐，乡里都赞你骨头硬。", failFeedback: "证据未及递出，你已在狱中染了寒疾。杖责之后落下病根，出狱时人瘦如柴，家财也无几了。", successEffect: { intellect: 6, happiness: 5, rep: 12 }, failEffect: { health: -18, wealth: -10, happiness: -12 }, tagSuccess: "沉冤得雪", tagFail: "瘐死狱中", isKey: true },
          { text: "认下部分罪责，纳粟赎刑，保住性命与半数家产", riskLevel: "纳粟赎刑 · 名节有亏 · 稳妥必成", successChance: (p) => 100, successFeedback: "你纳粟赎了刑，虽有乡议指你软弱，命却是保住了。归家后你烧了旧账，从此只教子读书。", failFeedback: "", successEffect: { health: -6, wealth: -14, rep: -8 }, failEffect: {  }, tagSuccess: "忍辱全生", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "中年险滩",
        title: "中正定品，长子前程待择",
        narrative: (p, y) => "州中正将行乡品，你的长子已能属文。门第不算高，中正又是旧日政敌的门生。族老劝你倾尽家资为长子营求清望之职，走门阀捷径；塾师却说不如让他去州学苦读经义，凭才学取品。眼看秋集将至，这一步关乎儿孙后世，你须在人情与学问之间落子。",
        choices: [
          { text: "备下名帖与绢帛，登门拜谒中正，请为长子叙品", riskLevel: "攀附门第 · 清议可畏 · 成功率 58%", successChance: (p) => 58 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 5 : 0), successFeedback: "中正念你礼数周全，又碍着旧交情面，终给长子叙了个中品。门第渐起，只是清议间偶有讥声。", failFeedback: "中正收了礼却不肯出力，反将此事播扬出去。乡里讥你攀附，长子的品第反而落了下乘。", successEffect: { wealth: -8, happiness: 6, rep: 8 }, failEffect: { wealth: -10, happiness: -6, rep: -12 }, tagSuccess: "门第得叙", tagFail: "清议见讥", isKey: true },
          { text: "送长子入州学，令其苦读经义，待策试自陈才学", riskLevel: "十年寒窗 · 品第难料 · 稳妥必成", successChance: (p) => 100, successFeedback: "长子入州学三年，策试名列前茅，中正不得不以才学取之。乡里传为美谈，你也稍慰平生。", failFeedback: "", successEffect: { intellect: 10, happiness: 4, rep: 6 }, failEffect: {  }, tagSuccess: "经明行修", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "动荡考验",
        title: "胡骑南下，举族渡江避乱",
        narrative: (p, y) => "北地烽烟骤起，胡骑已破邻郡，坞堡里人心惶惶。族中商议南迁：渡江可避锋镝，却要弃下祖坟与百亩良田，舟车资费不菲；留守坞堡，凭高墙与乡曲部曲或许能撑过这个冬天。老族长问你，究竟带多少族人、多少粮种上路。",
        choices: [
          { text: "尽率族众渡江南下，变卖田宅作舟资，随衣冠士族侨居", riskLevel: "弃祖南迁 · 道路艰险 · 成功率 55%", successChance: (p) => 55 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 6 : 0) + (p.health > 60 ? 4 : 0), successFeedback: "舟行月余，举族在江南侨郡落脚。虽失了祖田，却以带来的粮种垦出薄田，子弟后来多有入仕者。", failFeedback: "半途遇乱兵劫掠，舟资尽失，族中老弱病殁于道。你携余众勉强渡江，从此家道中落，只余一身。", successEffect: { health: 6, wealth: 8, rep: 5 }, failEffect: { health: -15, wealth: -20, happiness: -10 }, tagSuccess: "衣冠南渡", tagFail: "道殣相望", isKey: true },
          { text: "留驻坞堡，率部曲坚壁清野，与乡邻共守乡土", riskLevel: "死守乡里 · 生死未卜 · 稳妥必成", successChance: (p) => 100, successFeedback: "坞堡高墙深壕，乡曲部曲协力死守，胡骑绕城而去。族中老小得以保全，乡邻都推你为坞主。", failFeedback: "", successEffect: { health: -6, happiness: -4, rep: 10 }, failEffect: {  }, tagSuccess: "保境安民", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "动荡考验",
        title: "藩镇征兵，老身与幼子孰往",
        narrative: (p, y) => "节度使的征兵牒下到里坊，凡丁壮皆须应募。你已年过四十，腰腿旧伤未愈；次子刚满十六，尚未婚配。军府许你以粟代役，可家中义仓才攒下几囤谷子，是族里荒年救命的底子。里正站在门口催得急，妻在灶下抹泪，你须在一炷香内定夺。",
        choices: [
          { text: "亲自应募，随军北上戍边，把幼子留在乡里承家", riskLevel: "从军远戍 · 生死由天 · 成功率 40%", successChance: (p) => 40 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 5 : 0) + (p.health > 60 ? 8 : 0), successFeedback: "你在军中因识文断字被擢为书佐，未几边事稍定，得以还乡。虽未立功名，却保住了次子的婚配。", failFeedback: "北戍途中你旧伤复发，又逢大雪，同行者死伤大半。你被人抬回时，义仓已空，次子也替了你的名籍。", successEffect: { health: -8, intellect: 5, rep: 12 }, failEffect: { health: -18, wealth: -6, happiness: -14 }, tagSuccess: "投笔从戎", tagFail: "马革裹尸", isKey: true },
          { text: "开义仓出粟代役，留次子在乡耕读，另雇乡勇应募", riskLevel: "倾仓免役 · 族中生怨 · 稳妥必成", successChance: (p) => 100, successFeedback: "你开仓出粟免了丁役，次子得以在家耕读。族中虽怨你擅动义仓，来年丰收后终究补上了亏空。", failFeedback: "", successEffect: { wealth: -16, happiness: 5, rep: -6 }, failEffect: {  }, tagSuccess: "破财免丁", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "知命之年",
        title: "宦情已倦，辞官择地而居",
        narrative: (p, y) => "你在仕途浮沉二十载，如今鬓已染霜。朝中党争又起，门生劝你依附新贵再进一步；老友则来信说，终南山下有薄田数顷，泉石清幽，可终老著书。归隐须弃官俸门荫，儿孙仕途或受影响；留任则日日如履薄冰，恐晚节不保。案上旧砚，正待落笔。",
        choices: [
          { text: "上表称病辞官，携家卜居山下，以耕读终老", riskLevel: "急流勇退 · 门荫渐薄 · 成功率 60%", successChance: (p) => 60 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 4 : 0) + (p.health > 60 ? 5 : 0), successFeedback: "你辞官归山，晨起荷锄，夜来著书。二十年后，那部《山居杂记》被门人刻印，乡里皆称你高致。", failFeedback: "你辞官未久，旧日政敌便奏请削了你的门荫，儿孙仕途受阻。你虽在山中安身，心中终有块垒难平。", successEffect: { health: 10, wealth: -6, happiness: 15, rep: 8 }, failEffect: { health: -6, happiness: -8, rep: -8 }, tagSuccess: "归园田居", tagFail: "晚节飘零", isKey: true },
          { text: "留任原职只求无过，把心力用在修桥赈饥上", riskLevel: "明哲保身 · 宦海浮沉 · 稳妥必成", successChance: (p) => 100, successFeedback: "你留任不争，只把心力用在修桥赈饥上。虽未再升迁，离任时百姓夹道相送，你也算无愧于心。", failFeedback: "", successEffect: { intellect: 4, happiness: -4, rep: 10 }, failEffect: {  }, tagSuccess: "守拙宥民", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "知命之年",
        title: "灾年起义仓，修谱立训",
        narrative: (p, y) => "这一年秋旱，四乡饥民流徙，族中义仓的谷子只够撑到开春。祠堂里，族老们争论：是把存粮按丁口平分，还是留作来年的种子与祭田。你已年过半百，正想趁此修一部族谱、立几条家训，好把荒年不闭仓的规矩刻进去，让后人记得今日之难。",
        choices: [
          { text: "开义仓设粥棚，尽散存粮赈济乡邻，只留祭田种子", riskLevel: "倾仓济众 · 来春可忧 · 成功率 65%", successChance: (p) => 65 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 3 : 0), successFeedback: "粥棚开了一冬，活人无数。来春族中子弟合力垦荒，义仓竟比往年更丰，你的家训也被刻在祠堂。", failFeedback: "存粮散尽，来春青黄不接，族中饿死了几个老弱。乡邻虽感你的恩，你却在祠堂前垂泪自责。", successEffect: { wealth: -12, happiness: 10, rep: 15 }, failEffect: { wealth: -18, happiness: -6, rep: 6 }, tagSuccess: "义仓活人", tagFail: "来岁啼饥", isKey: true },
          { text: "按丁口均分存粮，余谷封仓，趁冬修族谱立家训", riskLevel: "量入为出 · 各有怨言 · 稳妥必成", successChance: (p) => 100, successFeedback: "你按丁口分粮，余谷封仓，又趁冬修成族谱家训。族人虽嫌你吝，来年却无一人饿毙，渐渐服气。", failFeedback: "", successEffect: { wealth: -6, intellect: 6, happiness: 4, rep: 8 }, failEffect: {  }, tagSuccess: "修谱立训", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "花甲在望",
        title: "竹简分券，堂前析产定争",
        narrative: (p, y) => "你年近花甲，鬓上已白。长子束发成家，次子尚在读书，田宅、僮仆、桑麻之利皆要分明。里正劝你趁早析产，免得身后兄弟相争；可老妻说，一分家便如树折其干，人心也散了。堂上竹简与契券摊开，墨尚未干，你须定一个章程。",
        choices: [
          { text: "请族中尊长与里正作证，立券析产，田宅各半，留一份祭田归祠堂", riskLevel: "明分定争 · 人心或散 · 成功率 70%", successChance: (p) => 70 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 10 : 0), successFeedback: "契券两分，各执其一，祭田入祠。兄弟虽别居，逢节仍同席。族人称你不偏不倚，乡里传为美谈。", failFeedback: "田亩肥瘠之争终究难免，次子怨你偏袒。家分而心未平，你夜里翻看契券，只觉指节发凉。", successEffect: { wealth: -6, happiness: 4, rep: 8 }, failEffect: { happiness: -8, rep: -5 }, tagSuccess: "析产有方", tagFail: "家分心散", isKey: true },
          { text: "暂不分家，先命长子掌田事、次子理书卷，各试其能三年", riskLevel: "缓图其成 · 静观其变 · 稳妥必成", successChance: (p) => 100, successFeedback: "长子督耕有法，次子抄书得钱。三年之间，各见其长，你只需在堂上点头，家声自然不坠。", failFeedback: "", successEffect: { intellect: 3, happiness: 5 }, failEffect: {  }, tagSuccess: "缓图知子", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "花甲在望",
        title: "夜书家训，灯下笔落族规",
        narrative: (p, y) => "秋夜灯下，你以刀笔在竹简上刻字。族中子弟渐多，有赌博斗鸡者，有弃农从商者。老友劝你：世家大族皆立门风，无谱牒家训者，三代而衰。你提笔欲写，却又迟疑——规矩太严则子弟离心，太宽则门风日下。",
        choices: [
          { text: "立家训十余条，刻简悬于中堂，令子弟每月朔日诵读一遍", riskLevel: "严立门风 · 恐伤亲厚 · 成功率 68%", successChance: (p) => 68 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.health > 60 ? 5 : 0), successFeedback: "朔日诵读，童子声琅琅。数年之后，族中少赌少讼，邻村皆来求抄录一份。你的名字被写进谱牒序中。", failFeedback: "子弟当面诵读，背后照旧。侄儿抱怨你迂阔。家训虽悬，风吹简响，倒显得中堂格外空。", successEffect: { intellect: 5, happiness: 3, rep: 10 }, failEffect: { happiness: -6, rep: -4 }, tagSuccess: "门风有立", tagFail: "训而不行", isKey: true },
          { text: "只述先人事迹与耕读本分，录成一卷，不设罚则，任子孙自省", riskLevel: "述而不作 · 以宽化人 · 稳妥必成", successChance: (p) => 100, successFeedback: "你写祖上逃荒、垦田、抄书三事，笔笔平实。孙辈围读至夜，竟有人悄悄收起了赌具。", failFeedback: "", successEffect: { happiness: 6, rep: 4 }, failEffect: {  }, tagSuccess: "述祖化人", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "桑榆晚景",
        title: "故人零落，素幡又过柴门",
        narrative: (p, y) => "你六十四岁，今年已送走三位旧交。先是同窗的县吏病故，再是当年同游的僧人圆寂于佛寺。今日门前又过素幡，鼓声低而短。你拄杖立于门下，想去送最后一程，可风湿之疾正发，腿脚不听使唤。",
        choices: [
          { text: "强撑病体，备一束香与素绢，亲往灵前执绋，送故人入土", riskLevel: "抱病尽义 · 折损元气 · 成功率 62%", successChance: (p) => 62 + (p.health > 60 ? 8 : 0), successFeedback: "你在灵前添香，说了几句旧年之事，满堂皆泣。归途虽疲，心中郁结却松了，夜里睡得极沉。", failFeedback: "归途淋了秋雨，当夜寒热交作，延医煎了两剂柴胡。故人已送，病却添了三分。", successEffect: { health: -4, happiness: 6, rep: 8 }, failEffect: { health: -10, happiness: -4 }, tagSuccess: "执绋尽义", tagFail: "抱病添疾", isKey: true },
          { text: "在自家堂上设一席素菜，向北遥祭，唤儿孙同拜，代为尽礼", riskLevel: "遥祭代之 · 礼数稍减 · 稳妥必成", successChance: (p) => 100, successFeedback: "你率子孙向北三拜，说故人生平。孩子们第一次知道父辈也曾有肝胆之交，席间安静而恭敬。", failFeedback: "", successEffect: { happiness: 4, rep: 3 }, failEffect: {  }, tagSuccess: "遥祭寄怀", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "桑榆晚景",
        title: "口述旧事，弟子执笔记之",
        narrative: (p, y) => "你六十七岁，眼已昏花，抄书吃力。当年随军出关、亲见荒年与流民的旧事，若无人记下，便要随你入土。一位年轻的书生愿执笔为你笔录，只是他家境清寒，需你供纸墨与口粮；而你自家的仓廪也不算丰足。",
        choices: [
          { text: "留书生在家中厢房，每日口述两时辰，以帛书抄录，成卷后藏于祠堂", riskLevel: "耗资存史 · 家计有损 · 成功率 72%", successChance: (p) => 72 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 8 : 0), successFeedback: "三月成三卷，笔笔皆有年月。乡中长者传阅，说这是本地难得的实录。你把书卷放进祠堂木匣，手抚良久。", failFeedback: "帛贵墨残，抄到第二卷便断了粮。书生告辞远行，散简留在案头，你翻看时总觉缺了一段。", successEffect: { wealth: -8, intellect: 6, rep: 12 }, failEffect: { wealth: -6, happiness: -5 }, tagSuccess: "帛书记事", tagFail: "书残未竟", isKey: true },
          { text: "只将最要紧的三件事口授长孙，让他记住年月与乡里旧姓", riskLevel: "择要而传 · 所存无几 · 稳妥必成", successChance: (p) => 100, successFeedback: "长孙记性极好，反复背诵，连荒年赈粮的斗数都没错。夜里他复述给你听，你听着听着笑了。", failFeedback: "", successEffect: { intellect: 3, happiness: 6 }, failEffect: {  }, tagSuccess: "口授择要", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "古稀沧桑",
        title: "稚孙绕膝，次子远赴边戍",
        narrative: (p, y) => "你七十二岁，膝下孙儿绕膝嬉闹，最是舍不下。可州府征发，次子被点入军中，要去北边戍守三年。临行前夜，他要你一句话。堂上烛短，里屋孙儿睡熟的呼吸声清晰可闻。",
        choices: [
          { text: "取出旧箭一枚与祖传短刀相赠，嘱其守军令、护同伴，勿以勇犯险", riskLevel: "壮其行色 · 忧在心头 · 成功率 65%", successChance: (p) => 65 + (p.luck > 50 ? 10 : 0), successFeedback: "次子跪受刀箭，起身时腰背挺直。三年后他随军归来，肩上添了疤，却带回了整队同乡的性命。", failFeedback: "边境风雪苦寒，消息一断数月。你每日倚门望北，白发又添一层，直到来年开春才有书信。", successEffect: { health: -3, happiness: 6, rep: 10 }, failEffect: { health: -6, happiness: -10 }, tagSuccess: "壮子从军", tagFail: "倚门望北", isKey: true },
          { text: "把家中积攒的钱帛分一半与他，广托同乡照应，只求他平安归来", riskLevel: "破财求安 · 未必如愿 · 稳妥必成", successChance: (p) => 100, successFeedback: "钱帛分装在两个布囊里，你一一数清。次子含泪收下，说爹放心。你只回了一句：活着回来。", failFeedback: "", successEffect: { wealth: -10, happiness: 4 }, failEffect: {  }, tagSuccess: "破财求安", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "古稀沧桑",
        title: "重修坟茔，勒石立于墓前",
        narrative: (p, y) => "你七十五岁，祖坟经年风雨，封土塌了一角，墓碑字迹也漫漶难辨。族中商议重修，需按门阀谱牒上的世系，把父祖名讳官位一一勒石。可请人撰墓志、雇石工立碑，是一笔不小的开销，族人各房心思不一。",
        choices: [
          { text: "自出半数资财，按谱牒考订世系，请乡中老儒撰墓志，重立石碑", riskLevel: "考系立石 · 耗财招议 · 成功率 70%", successChance: (p) => 70 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.health > 60 ? 6 : 0), successFeedback: "封土重新培厚，碑上名讳世系分明。清明之日，各房齐来拜扫，连多年不往来的远支也到了。", failFeedback: "世系一考便生出争议，某房说漏了他家一支。碑虽立起，祭日里的寒脸却比石还冷。", successEffect: { wealth: -12, happiness: 5, rep: 12 }, failEffect: { wealth: -10, happiness: -6, rep: -6 }, tagSuccess: "立石收族", tagFail: "考系生争", isKey: true },
          { text: "先只培土加固，另以墨笔在木牌上重书名讳，待来年从容再议立碑", riskLevel: "权宜培土 · 事缓礼存 · 稳妥必成", successChance: (p) => 100, successFeedback: "众人担土夯筑一日，木牌新墨黑亮。你亲手把坟前杂草拔净，说先人住处不能荒。", failFeedback: "", successEffect: { happiness: 4, rep: 3 }, failEffect: {  }, tagSuccess: "培土守茔", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "夕阳辞章",
        title: "灯尽堂深，子孙环侍榻前",
        narrative: (p, y) => "你七十九岁，入冬后便少下床。儿孙轮番侍药，煎的是本草上的方子，也请过僧人诵经、医者针灸。今夜灯火将残，你气息微而心却清明。堂下子孙环立，人人等你开口；窗外月色如水，照见你一生走过的那条村路。",
        choices: [
          { text: "唤子孙近前，一一叫出名字，嘱其守住耕读家风，然后安然闭目", riskLevel: "含笑付托 · 灯尽而终 · 稳妥必成", successChance: (p) => 100, successFeedback: "你把每个孩子的名字都叫了一遍，最后说：田要种，书要读，人要和。说完手一松，面色平静如水，满堂低泣。", failFeedback: "", successEffect: { happiness: 8, rep: 10 }, failEffect: {  }, tagSuccess: "含笑而终", tagFail: "另寻他途", isKey: false },
          { text: "命人扶你起身，换上旧日布衣，独自倚窗看最后一轮月，不再言语", riskLevel: "独对山水 · 坦然归去 · 成功率 88%", successChance: (p) => 88 + (p.luck > 50 ? 10 : 0), successFeedback: "月色移过窗棂，你看了许久，眉目舒展。天明时子孙来唤，你已端坐而去，衣冠整齐，如睡一般。", failFeedback: "夜半寒气入骨，你咳了几声才稳下来。虽未如你所愿那般静好，终究是在自家窗下合了眼。", successEffect: { happiness: 8, rep: 6 }, failEffect: { health: -8, happiness: -2 }, tagSuccess: "月下归真", tagFail: "寒夜灯残", isKey: true }
        ]
      },
      {
        period: "夕阳辞章",
        title: "病榻托付，散尽余财济乡",
        narrative: (p, y) => "你八十二岁，卧床已久，自知来日无多。匣中还有田契数纸、钱帛若干，另有一卷家训未完。族中侄辈眼望匣子，乡里却有数户因去年旱灾卖儿鬻女。你要在闭眼之前，把这两件事一并了断。",
        choices: [
          { text: "唤族中尊长与诸子到榻前，逐条交付家训与田契，立下分付之契，各无异议", riskLevel: "榻前分付 · 争心暗伏 · 成功率 82%", successChance: (p) => 82 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "你一条条念，一条条指给人看，诸子唯唯。契成之后，你让人扶你靠好，说：我无事矣。是夜遂卒。", failFeedback: "念到第三卷时，侄儿忽然插嘴争祭田。你气息一滞，终究按住不提，只把契纸塞进长子手中。", successEffect: { happiness: 6, rep: 10 }, failEffect: { happiness: -8, rep: -4 }, tagSuccess: "榻前交付", tagFail: "遗言见争", isKey: true },
          { text: "命开仓散尽余财与存粮，济助乡里受灾之户，只留家训一卷与薄田数亩", riskLevel: "散财济乡 · 身后萧然 · 稳妥必成", successChance: (p) => 100, successFeedback: "门前来领粮的人排出半里地。你躺在床上听外头人声，说够了，够了。第三日清晨，你在人声渐远时安然离世，乡人白衣相送。", failFeedback: "", successEffect: { wealth: -25, happiness: 8, rep: 15 }, failEffect: {  }, tagSuccess: "散财归去", tagFail: "另寻他途", isKey: false }
        ]
      }
      ]
    ];

    // ---- premodern 16 大生命阶段事件池（每阶段多个候选，单局随机抽取）----
    const PREMODERN_STAGE_POOLS = [
      [
      {
        period: "幼年启蒙",
        title: "塾师授三字经，村塾开蒙第一课",
        narrative: (p, y) => "你年方六岁，父亲提着一方腊肉，领你拜入村塾。塾师姓陈，案上摆着戒尺和一册翻旧的《三字经》，窗外传来邻家舂米的闷响。同窗开蒙都先背这千字，背不出便要在掌心上挨三下。父亲临走只留一句话：家中只供得起一个读书人，你要想清楚。",
        choices: [
          { text: "端坐案前逐字跟读，把“人之初”背得滚瓜烂熟，再请塾师圈点", riskLevel: "勤勉 · 稳妥 · 成功率 75%", successChance: (p) => 75 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "半月后你已能整段背诵，塾师用朱笔在你书页上画了个圈，父亲听说后多要了一碗米酒。", failFeedback: "你张口结舌，掌心挨了戒尺，回家抱着书箱坐到油灯下，倒把“性本善”记了个牢。", successEffect: { intellect: 10, rep: 5 }, failEffect: { intellect: 4, happiness: -5 }, tagSuccess: "初通文墨", tagFail: "涩口难言", isKey: true },
          { text: "只顾看窗外货郎的糖人和拨浪鼓，把书页翻得哗哗响", riskLevel: "贪玩 · 无伤 · 稳妥必成", successChance: (p) => 100, successFeedback: "一日自在，你尝了半块麦芽糖，也记住了货郎吆喝的调子，夜里竟把它当童谣哼给弟弟听。", failFeedback: "", successEffect: { happiness: 8, luck: 3 }, failEffect: {  }, tagSuccess: "顽童一乐", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "幼年启蒙",
        title: "上元庙会，随母亲看社戏傀儡",
        narrative: (p, y) => "上元夜，镇上搭起灯棚，母亲用粗布巾裹着你挤进人堆。台上傀儡正演《劈山救母》，锣鼓一响，满街都是卖糖炒栗子和面人的吆喝。父亲给的几枚铜钱还揣在你怀里，母亲却攥紧你的手，说散场前要赶回去给祖母熬药。",
        choices: [
          { text: "挣开母亲的手，钻到台前去摸那傀儡的丝线，看它如何抬手", riskLevel: "好奇 · 冒险 · 成功率 70%", successChance: (p) => 70 + (p.luck > 50 ? 5 : 0), successFeedback: "你挤到台角，看清老艺人十指翻飞，回家用竹片和烂布头扎了个小傀儡，逗得祖母咳着也笑了。", failFeedback: "人潮一涌你跌在青石板上，膝盖磕出淤青，回家被母亲数落，却记住了那句唱词。", successEffect: { intellect: 4, happiness: 8 }, failEffect: { health: -4, happiness: 3 }, tagSuccess: "眼明手巧", tagFail: "跌撞有得", isKey: false },
          { text: "陪母亲守在药炉边，把庙会听来的故事讲给祖母听", riskLevel: "孝顺 · 安稳 · 稳妥必成", successChance: (p) => 100, successFeedback: "祖母听得合眼微笑，赏你一枚磨得发亮的旧铜钱，母亲看你的眼神也柔和了几分。", failFeedback: "", successEffect: { happiness: 6, rep: 4 }, failEffect: {  }, tagSuccess: "膝下承欢", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "童年韶光",
        title: "随父兄入商号，学记账打算盘",
        narrative: (p, y) => "镇上的米行兼卖布匹，你十岁那年被父亲领进后柜。掌柜姓吴，先让你磨墨誊账，再把一把旧算盘推过来，珠子被前头学徒摸得发亮。门外有交子铺的伙计来兑钱，柜上银钱出出进进。兄长小声提醒你：账目错一笔，一年工钱都赔不起。",
        choices: [
          { text: "每日临一遍账簿，把算盘口诀背熟，宁可晚睡也要对清当日进出", riskLevel: "勤恳 · 立身 · 成功率 72%", successChance: (p) => 72 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "一季下来你算珠不乱，吴掌柜当众把一本小账交你管，还添了两文月钱。", failFeedback: "你错记了两笔布价，被罚跪在柜台后重抄账本，手指发酸，却把珠算口诀记死了。", successEffect: { wealth: 6, intellect: 10, rep: 5 }, failEffect: { intellect: 5, happiness: -6 }, tagSuccess: "心中有账", tagFail: "错中学乖", isKey: true },
          { text: "陪东家少爷斗蛐蛐，替他跑腿买糖糕，图个清闲热闹", riskLevel: "随和 · 无争 · 稳妥必成", successChance: (p) => 100, successFeedback: "你与少爷混熟了，常有零嘴分润，也从他口里听来不少城里商号的闲话门道。", failFeedback: "", successEffect: { happiness: 7, luck: 3 }, failEffect: {  }, tagSuccess: "街头人缘", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "童年韶光",
        title: "村中拳师设场，授你扎马步习射",
        narrative: (p, y) => "村西的打谷场上，一位走镖回乡的老拳师摆开场子，教孩子们扎马步、拉硬弓。弓是竹胎牛筋的，拉满时手臂发抖。同来的孩童多熬不住，跑去看瓦舍说书。拳师眯眼看你，说学武先学忍痛，你若怕苦，趁早回家挑水。",
        choices: [
          { text: "咬牙扎稳马步，日日拉弓百次，手心磨破也不肯先收势", riskLevel: "坚忍 · 强身 · 成功率 65%", successChance: (p) => 65 + (p.health > 60 ? 8 : 0), successFeedback: "两月后你一箭射中草人咽喉，拳师点头收你入正式弟子行列，村人见了都称你有股狠劲。", failFeedback: "你拉伤了肩，被拳师按在药酒里揉搓，疼得直咧嘴，却把弓步的架势记进了骨头。", successEffect: { health: 10, intellect: 3, rep: 5 }, failEffect: { health: -4, intellect: 3, happiness: -4 }, tagSuccess: "筋骨渐壮", tagFail: "带伤知法", isKey: false },
          { text: "只学几路防身招式，余下时辰去瓦舍听人说书", riskLevel: "取巧 · 安稳 · 稳妥必成", successChance: (p) => 100, successFeedback: "你学了三招护身，又听了几回《三国》故事，回家讲给玩伴听，颇受欢迎。", failFeedback: "", successEffect: { health: 4, happiness: 6 }, failEffect: {  }, tagSuccess: "粗通拳脚", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "少年分流",
        title: "县试将近，你提篮赴童子试",
        narrative: (p, y) => "县衙前贴出考期，你十四岁，父亲翻出压箱底的青布长衫，又托人寻廪生作保。考棚里一人一桌，墨臭混着汗味，试题出自四书。邻座少年进场时被搜出夹带，当场逐出，围观的人指指点点。父亲只说了一句：若考不中，明年就得下田或入铺。",
        choices: [
          { text: "闭门苦读经义，把历年考题逐篇揣摩，孤注一掷赴考", riskLevel: "拼搏 · 险中 · 成功率 55%", successChance: (p) => 55 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 5 : 0), successFeedback: "榜上你的名字列在末等，虽未中秀才，县学先生却记住了你，愿留你在塾中帮教蒙童。", failFeedback: "卷上文章写偏了题，你落榜归家，父亲没骂你，只把一盏灯留到深夜，让你自己想明白。", successEffect: { intellect: 12, rep: 8 }, failEffect: { intellect: 6, happiness: -8 }, tagSuccess: "榜上有名", tagFail: "落榜知耻", isKey: true },
          { text: "与乡邻结伴同行，只求稳妥应考，考完便回家帮忙收麦", riskLevel: "平稳 · 务实 · 稳妥必成", successChance: (p) => 100, successFeedback: "你规规矩矩考完，回来赶上割麦，父亲看你惜力气又肯下力，心里踏实了几分。", failFeedback: "", successEffect: { wealth: 3, intellect: 4, happiness: 5 }, failEffect: {  }, tagSuccess: "安分守拙", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "少年分流",
        title: "家道中落，父亲欲送你投师学艺",
        narrative: (p, y) => "家里为祖母治病借了印子钱，父亲把几亩薄田抵了出去。饭桌上他沉默半晌，说读书这条道恐怕走不通了，城里木匠铺正收学徒，三年出师，管饭不给工钱。你床头还压着读了一半的《千字文》，油灯芯烧得只剩一点亮，窗外雨敲着瓦。",
        choices: [
          { text: "次日便去木匠铺叩头拜师，从拉大锯、刨木料学起，三年不悔", riskLevel: "务实 · 立身 · 成功率 78%", successChance: (p) => 78 + (p.health > 60 ? 5 : 0), successFeedback: "师父见你手稳心细，半年便许你上刨台，说这门手艺饿不死人，你也第一次挣回自己的工钱。", failFeedback: "你刨坏了东家的门板，赔了半月工钱，师父骂你手笨，你却把那道木纹记了一辈子。", successEffect: { health: 5, wealth: 8, rep: 5 }, failEffect: { wealth: -4, intellect: 4, happiness: -6 }, tagSuccess: "一技在手", tagFail: "赔钱长艺", isKey: true },
          { text: "白天替人挑水打短工，夜里就着残灯把旧书再读一遍", riskLevel: "倔强 · 苦撑 · 成功率 45%", successChance: (p) => 45 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "塾中先生听说你夜读不辍，让你白日抄书换米，你竟又摸回了笔墨生计。", failFeedback: "连熬几夜你病倒了，草药钱花去大半积蓄，书到底没能接着读下去。", successEffect: { intellect: 10, rep: 6 }, failEffect: { health: -10, wealth: -6, intellect: 5 }, tagSuccess: "灯下不辍", tagFail: "贫病折志", isKey: false }
        ]
      }
      ],
      [
      {
        period: "成人立志",
        title: "晋商票号招学徒，你随乡人入号",
        narrative: (p, y) => "镇上几位老西儿回乡招人，说票号要在南边开分庄，收识字的少年学汇兑。你十七岁，能写会算，正合他们眼缘。号中规矩极严：白日算银、誊写汇票，夜里还要习字，三年不得私留一文钱。同乡有人劝你留下守几亩田，安稳一生。",
        choices: [
          { text: "入号立契，苦练珠算与汇券笔法，随掌柜远行分庄见世面", riskLevel: "远行 · 搏业 · 成功率 60%", successChance: (p) => 60 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 6 : 0), successFeedback: "三年后你已能独当一面，一封汇票在你笔下分毫不差，掌柜许你跟着走南闯北，见识了白银的斤两。", failFeedback: "分庄遇上官府封号查账，你被扣了半年工钱，虽失了财，却学会了如何与官面周旋。", successEffect: { wealth: 18, intellect: 8, rep: 8 }, failEffect: { wealth: -8, intellect: 6, happiness: -6 }, tagSuccess: "汇通四方", tagFail: "折银长识", isKey: true },
          { text: "留在本号打杂，替老掌柜抄信记账，静观行情再作打算", riskLevel: "守成 · 观望 · 稳妥必成", successChance: (p) => 100, successFeedback: "你在总号站住了脚，识得银钱往来的门道，虽未出门，也攒下了一份踏实名声。", failFeedback: "", successEffect: { wealth: 8, intellect: 6, rep: 4 }, failEffect: {  }, tagSuccess: "稳坐总号", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "成人立志",
        title: "粤海开市，十三行招记账伙计",
        narrative: (p, y) => "海禁稍有松弛，广州城外十三行的商馆又热闹起来。有行商到内地招识字伙计，管账、验货、招呼番客。你十九岁，正想立一番事业，族中长辈却摇头：与番人打交道，弄不好便倾家荡产，还落个通番的名声。行商给的工钱，是你眼下活计的三倍。",
        choices: [
          { text: "应招南下，学说几句番话，替行商验货记账，摸清海上货价", riskLevel: "闯荡 · 逐利 · 成功率 58%", successChance: (p) => 58 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 8 : 0), successFeedback: "你记清了茶叶与生丝的行情，一季下来分得花红，行商许你独自押货看仓，眼界大开。", failFeedback: "一船货物遇上风浪延误，你被扣了月钱，还替人赔了亏空，好在学明白了海船的凶险。", successEffect: { wealth: 25, intellect: 8, luck: 5 }, failEffect: { wealth: -12, intellect: 5, happiness: -7 }, tagSuccess: "行商起家", tagFail: "亏空识险", isKey: true },
          { text: "谢过行商，留在乡中守着祖业，农闲时教几个蒙童识字", riskLevel: "安分 · 守拙 · 稳妥必成", successChance: (p) => 100, successFeedback: "你守着几亩田与一屋旧书，日子清淡却无风波，乡邻都称你是个稳妥后生。", failFeedback: "", successEffect: { wealth: 4, happiness: 8, rep: 6 }, failEffect: {  }, tagSuccess: "耕读传家", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "青春韶华",
        title: "贡院秋风里的一场落第",
        narrative: (p, y) => "秋闱放榜，你挤在贡院墙外的人群里，从杏榜上寻到自己的名字，却只落在副榜。同乡的富家子已备下回乡的骡马，你若再留一年，盘缠只够赁一间城郊破屋；若就此南归，塾师的束脩与母亲的期盼又该如何交代。",
        choices: [
          { text: "留在京城赁屋再读一年，替书铺抄书换取灯油与饭食", riskLevel: "盘缠告罄 · 得失难料 · 成功率 65%", successChance: (p) => 65 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 5 : 0), successFeedback: "你抄书换来的铜钱勉强够用，寒夜里就着一盏油灯把八股文章磨了又磨。次年乡试，你的名字终于登上正榜，同乡再不敢轻看你。", failFeedback: "冬衣当了又当，抄书的钱终究不敷。你病倒在破屋里，被人抬上南归的船；功名未成，倒把身子与家财都赔了进去。", successEffect: { intellect: 10, rep: 6 }, failEffect: { health: -8, wealth: -12, intellect: 4 }, tagSuccess: "苦读成名", tagFail: "铩羽而归", isKey: true },
          { text: "收拾行囊趁早回乡，把落第之事说与母亲，先做几年塾师", riskLevel: "安分守拙 · 无甚波澜 · 稳妥必成", successChance: (p) => 100, successFeedback: "你回到乡里设馆授徒，束脩虽薄，却能晨昏侍奉母亲。旧日同窗来寄书信，你提笔回了一首自嘲的诗，竟也渐渐在乡里有了些名声。", failFeedback: "", successEffect: { happiness: 4, rep: 3 }, failEffect: {  }, tagSuccess: "安分守拙", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "青春韶华",
        title: "商号柜前的第一封荐书",
        narrative: (p, y) => "族叔在城里缎庄做二掌柜，愿为你写一封荐书，引荐你入商号当伙计。可同乡又说，口外的茶马道上利厚，只消两三年便能攒下本钱。你攥着那封信站在城门口，风把信角吹得发响，一时不知该往哪边走。",
        choices: [
          { text: "揣着荐书入商号，从扫地抹柜学起，先攒见识与人脉", riskLevel: "寄人篱下 · 前程未卜 · 成功率 72%", successChance: (p) => 72 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 6 : 0), successFeedback: "你手脚勤快，账目记得分明，掌柜渐渐许你上柜。三年下来，你识得银钱成色、行市涨落，也攒下第一笔体己银子。", failFeedback: "你算错一笔货账，掌柜当众斥责，伙计们背后叫你外乡呆子。工钱扣了大半，年节也不好意思回乡。", successEffect: { wealth: 15, intellect: 8, rep: 4 }, failEffect: { wealth: -8, happiness: -6, rep: -3 }, tagSuccess: "柜前立身", tagFail: "算错一账", isKey: true },
          { text: "留在族叔的缎庄里做个帮闲，先看清行情再定去留", riskLevel: "稳扎稳打 · 不冒大险 · 稳妥必成", successChance: (p) => 100, successFeedback: "你在缎庄里看货议价，学着分辨绸缎的成色与产地。虽没赚到大钱，却把行里的门道摸清，来日若自立门户便不吃亏。", failFeedback: "", successEffect: { wealth: 5, intellect: 6, happiness: 2 }, failEffect: {  }, tagSuccess: "稳扎稳打", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "初涉人世",
        title: "县衙书吏房的一纸投充",
        narrative: (p, y) => "县衙书吏房缺一名缮写，熟人递话，说只消纳几两银子的纸笔费便可投充。可书吏俸薄，衙中陋规却多；你若接了这差，往后经手的田赋册籍，难免要替人做手脚，夜里还能否睡得安稳。",
        choices: [
          { text: "纳银投充书吏，专管抄录田契与钱粮册，暗记其中门道", riskLevel: "近墨者黑 · 心怀惴惴 · 成功率 68%", successChance: (p) => 68 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 4 : 0), successFeedback: "你字迹端正，册籍抄得清楚，县丞也肯赏脸。三年间你把田赋、里甲的关节都看在眼里，往后替人办一桩事，便有人情可收。", failFeedback: "一桩钱粮亏空追查下来，上官只拿书吏顶罪。你赔了银子，还落了个手脚不净的名声，走在街上都被人指点。", successEffect: { wealth: 10, intellect: 8, rep: 5 }, failEffect: { wealth: -15, happiness: -5, rep: -8 }, tagSuccess: "衙中老手", tagFail: "替人顶罪", isKey: true },
          { text: "婉言推却这桩差事，宁可回乡守着几亩薄田度日", riskLevel: "安贫守拙 · 无欲则刚 · 稳妥必成", successChance: (p) => 100, successFeedback: "你没接那纸投充，照旧在乡里耕种读书。日子虽清苦，夜里睡觉却安稳，族中长辈也说你是个本分人。", failFeedback: "", successEffect: { happiness: 6, rep: 4 }, failEffect: {  }, tagSuccess: "清白持身", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "初涉人世",
        title: "漕船离岸前的生死文书",
        narrative: (p, y) => "漕帮船主招人押货北上，说这一趟走运河，过了清江浦便要签一张生死文书，翻船则人货两空，与船主无涉。给的船资是你在乡下做一年活计也攒不下的数，可母亲这两日正犯咳疾，药钱尚无着落。",
        choices: [
          { text: "签下文书随漕船北上，替船主看货对单、照料舱中货物", riskLevel: "风涛莫测 · 命悬一线 · 成功率 60%", successChance: (p) => 60 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 8 : 0) + (p.health > 60 ? 6 : 0), successFeedback: "一路过闸穿坝，你学着看水位、认码头，也替船主识破一回掺假的货色。到通州卸货时，你揣着船资，第一次觉出运河水有多养人。", failFeedback: "船在风口搁浅，货物浸水，你虽捡回性命，船资却被扣个干净，还落下寒疾，回乡整整咳了一个冬天。", successEffect: { wealth: 22, intellect: 7, rep: 3 }, failEffect: { health: -12, wealth: -6, happiness: -6 }, tagSuccess: "漕河历练", tagFail: "风涛受挫", isKey: true },
          { text: "谢过船主，留在岸上替人挑脚搬运，守着母亲煎药", riskLevel: "粗茶淡饭 · 亲侍汤药 · 稳妥必成", successChance: (p) => 100, successFeedback: "你日日挑担换几文铜钱，夜里替母亲煎药捶背。银钱不多，母亲的病却渐渐好了，邻里都说你是个孝子。", failFeedback: "", successEffect: { health: 2, happiness: 8, rep: 4 }, failEffect: {  }, tagSuccess: "孝养亲前", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "成家立业",
        title: "三媒六聘里的一桩难事",
        narrative: (p, y) => "媒婆来递庚帖，说的是绸缎行东家的女儿，嫁妆丰厚，只是要你入赘，日后孩子须随女家姓。你自家也有一位青梅竹马的姑娘，聘礼却拿不出，她父母已放出话来，说要另许人家。",
        choices: [
          { text: "咬牙四处告贷，典当祖传银镯，凑齐聘礼娶那位青梅竹马", riskLevel: "债台高筑 · 情义两全 · 成功率 66%", successChance: (p) => 66 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 5 : 0), successFeedback: "你典了祖父留下的一对银镯，又向同窗告贷，聘礼总算凑齐。花轿进门那日，她掀帘看你，眼睛红红的，往后的苦日子也算有了奔头。", failFeedback: "银子到底没凑够，姑娘被许给了邻县的粮商。你背着一身债回乡，夜里听见锣鼓声，都觉得像是替别人办的喜事。", successEffect: { wealth: -8, happiness: 12, rep: 5 }, failEffect: { wealth: -6, happiness: -15 }, tagSuccess: "有情人成", tagFail: "聘礼成空", isKey: true },
          { text: "婉拒入赘，也暂缓婚事，先攒两年本钱再从容议亲", riskLevel: "缓议婚期 · 稳中求全 · 稳妥必成", successChance: (p) => 100, successFeedback: "你把心思都放在生计上，两年间攒下些本钱。虽误了婚期，说亲的人反倒多了起来，你也不必再看谁的脸色行事。", failFeedback: "", successEffect: { wealth: 10, intellect: 4, happiness: -2 }, failEffect: {  }, tagSuccess: "缓议婚期", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "成家立业",
        title: "巷口小铺开张前的那一夜",
        narrative: (p, y) => "你在城隍庙巷口赁下半间门面，打算开一间杂货铺，卖些针头线脑、酱醋茶盐。牙行的人却来讨行帖钱，说没有牙帖，货便不许过秤；隔壁的老铺也放出风来，说要与你斗价。",
        choices: [
          { text: "照数交了牙帖钱，再从一个利字上让利三分，先留住街坊主顾", riskLevel: "本小利薄 · 前途难料 · 成功率 70%", successChance: (p) => 70 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 5 : 0), successFeedback: "你把秤放足，货色又实在，街坊渐渐认你的招牌。半年下来，隔壁老铺没挤倒你，你倒添了两口货柜，还雇了个半大孩子看店。", failFeedback: "让利太狠，本钱周转不开，赊出去的账又收不回来。入冬时你只得把货柜折价盘给隔壁，铺面换了别家的幌子。", successEffect: { wealth: 18, intellect: 5, rep: 6 }, failEffect: { wealth: -18, happiness: -6, rep: -4 }, tagSuccess: "铺面兴隆", tagFail: "折本关张", isKey: true },
          { text: "先不开铺，挑担走街串巷叫卖，摸清行情再谈门面", riskLevel: "小本经营 · 稳妥无虞 · 稳妥必成", successChance: (p) => 100, successFeedback: "你挑着担子走遍几条街巷，什么货好卖、哪位街坊讲信用，心里都有了数。攒下的铜钱虽少，却是实打实的本钱。", failFeedback: "", successEffect: { wealth: 8, intellect: 6 }, failEffect: {  }, tagSuccess: "货郎识市", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "三十而立",
        title: "族祠分产时的那纸田契",
        narrative: (p, y) => "族中长辈故去，祠堂里议分祭田与房舍。你这一支寡母幼弟，按旧例只该得薄田两亩；可你手里另有一纸祖父手书的字据，写着祭田归长房掌管，余田三房均分，眼下正该不该当众取出来。",
        choices: [
          { text: "当众取出祖父手书字据，请族长与三房长辈一同验看", riskLevel: "族议难测 · 得罪长房 · 成功率 64%", successChance: (p) => 64 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 6 : 0), successFeedback: "族老传看字据，认得出是祖父笔迹，长房无话可说。你分得田六亩，还替寡母争下一间正屋；只是长房从此见你便冷着脸。", failFeedback: "长房一口咬定字据是伪造，族老们各打圆场，最后你只得薄田三亩了事。兄弟间从此生分，逢年过节也不相往来。", successEffect: { wealth: 20, happiness: -3, rep: 5 }, failEffect: { wealth: -5, happiness: -10, rep: -4 }, tagSuccess: "据理分产", tagFail: "族中生隙", isKey: true },
          { text: "不与长房相争，只领应得的薄田，另谋别业养家", riskLevel: "吃亏是福 · 家和为上 · 稳妥必成", successChance: (p) => 100, successFeedback: "你拱手让了祭田，族长反觉得你识大体，日后族中有事，总先想着你。你带着妻儿另谋生计，日子虽窄，心却是齐的。", failFeedback: "", successEffect: { happiness: 5, rep: 8 }, failEffect: {  }, tagSuccess: "让产得和", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "三十而立",
        title: "清丈田亩时那根丈量绳",
        narrative: (p, y) => "县里奉文清丈田亩，重新攒造鱼鳞图册。丈量书手到了你们村，说你家那块河滩地量出来比原册多出三分，若不多纳粮，便要报作隐田。乡邻私下劝你塞些银子，把弓绳放松些。",
        choices: [
          { text: "如数认下多出的田亩，照新册纳税，免得日后被人首告", riskLevel: "赋役加重 · 问心无愧 · 成功率 74%", successChance: (p) => 74 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 4 : 0) + (p.health > 60 ? 4 : 0), successFeedback: "你当着里正与书手的面把田亩一一认下。虽每年多纳几斗粮，却换得一身清白；后来邻村有人因隐田被追缴三年，你家安然无事。", failFeedback: "新册虽上了，你的名字却被人记下。往后乡里摊派差役、修堤筑坝，总先点你出钱出力，你才知老实二字也是要付利息的。", successEffect: { wealth: -6, happiness: 4, rep: 10 }, failEffect: { wealth: -12, happiness: -6, rep: 3 }, tagSuccess: "奉公守册", tagFail: "忠厚受累", isKey: true },
          { text: "私下寻书手说合，松一松弓绳，仍旧按旧册完粮", riskLevel: "因循旧例 · 稳中有险 · 稳妥必成", successChance: (p) => 100, successFeedback: "你塞了两串铜钱，书手在树荫下把弓绳松了半寸，田亩终按旧册报了上去。事情办得隐秘，只是你从此见着官差便心里发虚。", failFeedback: "", successEffect: { wealth: 6, happiness: -4, rep: -2 }, failEffect: {  }, tagSuccess: "旧册完粮", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "负重前行",
        title: "里甲催征秋粮，牙行压价",
        narrative: (p, y) => "秋粮开征，里长沿门催逼，你家中尚缺三成。本欲挑新谷往镇上牙行粜卖，牙人却串通压价，还说可代你垫纳、秋后加利偿还。邻家老陈欠粮未清，已被锁进班房。天一亮便要点名赴县衙听点，你手里只剩一夜工夫。",
        choices: [
          { text: "连夜挑谷进城，寻熟识米行现银粜卖，绕开牙人", riskLevel: "风霜夜路 · 行市难料 · 成功率 65%", successChance: (p) => 65 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 5 : 0), successFeedback: "米行掌柜念旧交，按市价收了你的谷，现银到手，粮数凑足。里长见你爽利，点名时也未多加刁难。", failFeedback: "夜半遇雨，谷袋受潮折了斤两，只得贱价出手。粮数仍缺一斗，里长记了你一笔，日后再补。", successEffect: { wealth: 6, intellect: 8, rep: 5 }, failEffect: { wealth: -8, intellect: 4, happiness: -5 }, tagSuccess: "谷贱心稳", tagFail: "夜雨折粮", isKey: true },
          { text: "变卖家里那头耕牛，凑足粮数封纳，先保清白", riskLevel: "断腕保身 · 来年乏力 · 稳妥必成", successChance: (p) => 100, successFeedback: "牛贩趁急压价，你仍咬牙卖了。粮数如数封纳，里长挑了挑眉，把名字从欠单上划去。来年春耕，只能借邻家牛力。", failFeedback: "", successEffect: { wealth: -5, happiness: -4, rep: 4 }, failEffect: {  }, tagSuccess: "清白封纳", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "负重前行",
        title: "兄弟析产，老宅该归谁",
        narrative: (p, y) => "父亲故去三年，族中长辈终于发话析产。兄长以长子奉祀为由，要独占临街老宅；你出力最多，却只分得城外两亩薄田。宗祠议事这日，族长捻着胡须等你表态，妻子在屏后红了眼眶。",
        choices: [
          { text: "请族长与族老公议，立下分家文书，各执一纸为凭", riskLevel: "对簿宗祠 · 亲情生隙 · 成功率 60%", successChance: (p) => 60 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "族老翻出旧年账簿，说你侍疾出力最多，判老宅归你、兄长另得田租补偿。文书用印，各有凭据，兄长脸色难看。", failFeedback: "兄长跪在祠堂前哭诉奉祀之责，族老动了恻隐，老宅仍归他，只补你十两银子，兄弟从此生分。", successEffect: { wealth: 12, happiness: 3, rep: 8 }, failEffect: { wealth: 5, happiness: -8, rep: -3 }, tagSuccess: "文书为凭", tagFail: "手足生隙", isKey: true },
          { text: "让出老宅，只求兄长立契，替你供母亲晚年汤药", riskLevel: "退让求稳 · 人情难倚 · 稳妥必成", successChance: (p) => 100, successFeedback: "兄长当众立契，允诺母亲药食由他承担。族长点头称善，你搬出老宅，心里空了一块，却也卸下一副担子。", failFeedback: "", successEffect: { happiness: -3, rep: 5 }, failEffect: {  }, tagSuccess: "让宅求安", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "中年险滩",
        title: "遭诬入狱，衙役暗索贿",
        narrative: (p, y) => "邻村失窃的绸缎，竟从你佃户家中搜出，仇家趁机递了状纸。县衙差役将你锁走，牢头在耳旁低语：使些银子便可取保候审。堂上老爷尚未升座，家中已当尽首饰，狱卒开始按日索要饭钱。",
        choices: [
          { text: "托旧友向刑房书吏递银打点，先求取保，再寻反证", riskLevel: "官门似海 · 理屈难明 · 成功率 55%", successChance: (p) => 55 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 5 : 0), successFeedback: "书吏收了银子，替你递上一纸保状。你出狱寻到当日买绸的货郎，对上了牙行账簿，冤情终于有了转机。", failFeedback: "银子如泥牛入海，牢头翻脸，将你与盗贼同押。你在稻草上熬了半月，人瘦了一圈，所幸未曾屈打成招。", successEffect: { wealth: -10, intellect: 8, rep: 3 }, failEffect: { health: -10, wealth: -12, happiness: -8 }, tagSuccess: "银通枢吏", tagFail: "钱落黑牢", isKey: true },
          { text: "请里正与乡邻二十人联名具保，先行出狱，再慢慢辩白", riskLevel: "众口为凭 · 只保一时 · 稳妥必成", successChance: (p) => 100, successFeedback: "里正念你平素修桥补路，邀二十户联名画押。县衙准了保状，你暂得归家，案卷却仍悬着，日子过得提心吊胆。", failFeedback: "", successEffect: { happiness: -4, rep: 6 }, failEffect: {  }, tagSuccess: "乡邻具保", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "中年险滩",
        title: "商号倒账，债主登门",
        narrative: (p, y) => "你与人合开的布号，因合伙人在苏州囤货失手，账面亏空三百两。年关将近，债主揣着借据堵在门口，伙计已散了大半。掌柜劝你连夜关铺走人，账上却还压着十几户织工的工钱。",
        choices: [
          { text: "召集债主当众盘账，变卖铺面存货，按成分还", riskLevel: "砸锅卖铁 · 信誉扛肩 · 成功率 60%", successChance: (p) => 60 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "债主见你肯变产清账，倒有几人愿意宽限三月。铺面盘出去，还清七成，织工工钱也结了，余下慢慢填补。", failFeedback: "存货贱卖，只够还四成。有债主一纸诉状告到衙门，你被拘了半日，靠邻里凑银才得脱身。", successEffect: { wealth: -15, intellect: 5, rep: 12 }, failEffect: { wealth: -18, happiness: -8, rep: -5 }, tagSuccess: "变产清账", tagFail: "债主鸣官", isKey: true },
          { text: "先结清织工血汗工钱，再与债主逐一立约缓期归还", riskLevel: "先顾人心 · 后补银账 · 稳妥必成", successChance: (p) => 100, successFeedback: "织工拿到工钱千恩万谢，替你在街坊间说了不少好话。债主见人心向着你，多半肯宽限。铺子虽关，名声未倒。", failFeedback: "", successEffect: { wealth: -10, happiness: 3, rep: 8 }, failEffect: {  }, tagSuccess: "工钱不欠", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "动荡考验",
        title: "兵信传来，举家何往",
        narrative: (p, y) => "江北传来兵信，长毛已破邻府，官道上的逃难人一日多过一日。族中议定迁往山里祖坟旁的旧屋，可你铺中还有一批货未脱手，老母又病着经不起颠簸。城门守军开始盘查路引，风声一日紧似一日。",
        choices: [
          { text: "连夜烧掉欠据，携老母细软先行入山，货留给伙计照看", riskLevel: "弃货保命 · 乱世难料 · 成功率 58%", successChance: (p) => 58 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 5 : 0) + (p.health > 60 ? 5 : 0), successFeedback: "山路虽险，一家老小终在祖屋安顿。三日后乱兵过境，镇上铺面被抢掠一空，你只损失了那批货。", failFeedback: "半路遇溃兵盘查，细软被搜去大半，老母受了风寒。所幸你递上路引，一家才被放过，仓皇抵达山中。", successEffect: { health: 3, wealth: -8, rep: 5 }, failEffect: { health: -8, wealth: -15, happiness: -8 }, tagSuccess: "弃货全生", tagFail: "途中遭掠", isKey: true },
          { text: "闭门不出，将粮米藏入地窖，静候官军收复城池", riskLevel: "以静待动 · 祸福难卜 · 稳妥必成", successChance: (p) => 100, successFeedback: "你把门户钉死，粮米分藏三处地窖，阖家缩在后院。乱兵过巷两回，竟未破门。半月后官军入城，市面重开。", failFeedback: "", successEffect: { wealth: -5, happiness: -3, rep: 4 }, failEffect: {  }, tagSuccess: "闭门避乱", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "动荡考验",
        title: "老母病故，丁忧守制",
        narrative: (p, y) => "老母熬过残冬，终究在三月里去了。按制，你须去官守孝三年，衙署里的差事眼看要被人接手；可若夺情留任，言官一支笔便能参你个不孝。灵前白幡还没挂稳，同僚已上门探问口风。",
        choices: [
          { text: "上呈丁忧文书，归乡守制三年，田里读书兼课子侄", riskLevel: "守礼全孝 · 仕途暂歇 · 成功率 70%", successChance: (p) => 70 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "上司准了丁忧，同僚赞你知礼。三年里你在乡设塾教蒙童，声名反而更重，丧满之日便有旧交来邀。", failFeedback: "你递了文书，却有人在背后说你借孝避差。差事果然被他人接手，三年后再想复起，位置早已没了。", successEffect: { intellect: 6, happiness: 3, rep: 10 }, failEffect: { wealth: -5, happiness: -6, rep: -5 }, tagSuccess: "守制全孝", tagFail: "去位失势", isKey: true },
          { text: "托上官具疏夺情，留任办完河工再补守制", riskLevel: "夺情留任 · 物议难平 · 稳妥必成", successChance: (p) => 100, successFeedback: "上官念你河工要紧，具疏夺情。你留任把堤修完，却总有人背地里指点，说你不肯放下乌纱。夜里想起母亲，泪湿枕席。", failFeedback: "", successEffect: { wealth: 8, happiness: -8, rep: -6 }, failEffect: {  }, tagSuccess: "夺情留任", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "知命之年",
        title: "荒年米贵，仓门开否",
        narrative: (p, y) => "连月大旱，米价一日三涨。你是乡里推举的仓正，社仓里还存着三百石谷。饥民聚在仓外，有人跪地磕头，也有人磨刀扬言要砸仓。县衙的赈粮文书迟迟未到，擅动社仓是罪，不开又怕闹出人命。",
        choices: [
          { text: "按户造册，先贷后赈，开仓平粜，同时具报县衙", riskLevel: "擅动社仓 · 罪责自担 · 成功率 62%", successChance: (p) => 62 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "你按户造册，米价应声落了三成，饥民散了大半。县衙追认你权宜得当，只申饬一句，乡里却记了你的好。", failFeedback: "仓谷出了大半，账目却对不上，有人告你私吞。你自掏银两补齐亏空，虽免了官司，家底也去了一层。", successEffect: { wealth: -8, intellect: 6, rep: 15 }, failEffect: { wealth: -15, happiness: -6, rep: -8 }, tagSuccess: "开仓济饥", tagFail: "账亏蒙冤", isKey: true },
          { text: "严守仓规，只将自家存粮分与最贫的十余户", riskLevel: "量力而行 · 杯水车薪 · 稳妥必成", successChance: (p) => 100, successFeedback: "你把自家米缸分了一半出去，最难的十余户熬过了青黄不接。其余人家散去，仓谷未动，你也未惹官司。", failFeedback: "", successEffect: { wealth: -6, happiness: 3, rep: 5 }, failEffect: {  }, tagSuccess: "分粮济急", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "知命之年",
        title: "倦于簿书，辞官归乡",
        narrative: (p, y) => "你在衙署做了半辈子书吏，案牍堆得比人高，升迁却总轮不到。新来的知县带了自家幕友，处处架空老人。故乡来信说老宅漏雨、儿子科考无钱打点。你年过五十，开始盘算这顶帽子还值不值得戴。",
        choices: [
          { text: "递上辞呈，收拾行囊归乡，设馆授徒兼课子侄", riskLevel: "挂冠而去 · 生计另谋 · 成功率 68%", successChance: (p) => 68 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "辞呈递上，知县假意挽留几句便准了。你回到老宅修屋开馆，四乡学子登门，束脩虽薄，日子倒清净自在。", failFeedback: "归乡后方知人情冷暖，旧日同年避而不见，馆也一时开不起来。你守着薄田熬了两年，才慢慢有了起色。", successEffect: { intellect: 8, happiness: 10, rep: 5 }, failEffect: { wealth: -8, happiness: -8, rep: -3 }, tagSuccess: "挂冠归里", tagFail: "归乡冷落", isKey: true },
          { text: "暂不辞官，暗中誊录旧年案卷，另寻门路调任他县", riskLevel: "忍气周旋 · 静待时机 · 稳妥必成", successChance: (p) => 100, successFeedback: "你把历年案卷誊得清清楚楚，借公差之便结识邻县主簿。调任虽未成，新知县却也看出你的用处，不再处处相逼。", failFeedback: "", successEffect: { wealth: 3, intellect: 6, rep: 3 }, failEffect: {  }, tagSuccess: "案牍周旋", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "花甲在望",
        title: "祠堂灯下与族老重修谱牒",
        narrative: (p, y) => "族老捧出虫蛀旧谱，叹三代名讳已无从查考。你年近花甲，儿孙绕膝，理当为宗族留下规矩。修谱需银三十两，还要开罪两房旁支；若不修，他日子孙相逢，竟不知同出一祖。",
        choices: [
          { text: "捐半年束脩，请老塾师秉笔，先订族规十二则，再续谱系", riskLevel: "散财 · 结怨 · 成功率 68%", successChance: (p) => 68 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 10 : 0), successFeedback: "族谱装成，宗祠设宴，旁支虽有不快，终在规条前低了头；小儿辈第一次知道自己从何处来。", failFeedback: "银钱花去大半，旁支仍藏私册不交，谱中缺了两房；你方知聚族之事，急不得。", successEffect: { wealth: -12, happiness: 6, rep: 8 }, failEffect: { wealth: -12, happiness: -4, rep: -5 }, tagSuccess: "谱牒初成", tagFail: "聚族未谐", isKey: true },
          { text: "只录本支三代，抄成简册藏于家庙，量力而行", riskLevel: "守分 · 稳妥 · 稳妥必成", successChance: (p) => 100, successFeedback: "简册虽薄，名讳清晰，儿孙日日可诵；族中老人亦赞你稳妥，不争一时之名，反多得几分敬重。", failFeedback: "", successEffect: { happiness: 4, rep: 4 }, failEffect: {  }, tagSuccess: "简册传家", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "花甲在望",
        title: "捐田设义庄以赡族中孤寡",
        narrative: (p, y) => "族中寡嫂无力自养，城外饥民亦常来叩门。你手头有薄田八十亩，若仿范氏旧例设义庄，可养族中孤寡、延师课读；只是自家几个儿子未必情愿，田一捐出，便再收不回。",
        choices: [
          { text: "划出五十亩作义庄公田，立契入祠，请族中正直者轮管", riskLevel: "让利 · 招怨 · 成功率 60%", successChance: (p) => 60 + (p.luck > 50 ? 10 : 0), successFeedback: "义庄立成，孤寡按月领米，义学里书声不绝；你路过时，孩子们起身唤你一声太公。", failFeedback: "管事者中饱私囊，账目不清，儿子们怨你偏心；你亲自查账，追回半数，也看清了人心。", successEffect: { wealth: -18, happiness: 8, rep: 10 }, failEffect: { wealth: -18, happiness: -5, rep: -3 }, tagSuccess: "义庄初立", tagFail: "账目生疑", isKey: true },
          { text: "先设义学一间，请塾师课族中子弟，余田留给儿孙", riskLevel: "择要 · 周全 · 稳妥必成", successChance: (p) => 100, successFeedback: "义学开在祠堂西厢，族中子弟免费附读；儿孙虽少得几亩，却也无人再怨你偏心。", failFeedback: "", successEffect: { wealth: -8, happiness: 5, rep: 6 }, failEffect: {  }, tagSuccess: "义学开蒙", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "桑榆晚景",
        title: "召齐子侄交付田契账册",
        narrative: (p, y) => "你年过六旬，眼力不济，账簿细字已看不明。三个儿子各有心思：长子稳妥却懦，次子精明而贪，三子尚幼。田契账册终要交出去，是当众分明立下析产文书，还是只交一半、留一手以观其后？",
        choices: [
          { text: "请族老作中，当众立析产文书，田宅账目一一分明", riskLevel: "明分 · 失权 · 成功率 65%", successChance: (p) => 65 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 10 : 0), successFeedback: "文书画押，三房各得其所，族老赞你公道；此后你只管含饴弄孙，不再过问钱粮。", failFeedback: "次子嫌分得少，当场争执，文书虽立，兄弟已生嫌隙；你夜里辗转，知家业难齐。", successEffect: { happiness: 7, rep: 6 }, failEffect: { happiness: -7, rep: -4 }, tagSuccess: "析产分明", tagFail: "兄弟生隙", isKey: true },
          { text: "只交田契与半数银钱，自留养老之资，余者立遗嘱封存", riskLevel: "留手 · 自养 · 稳妥必成", successChance: (p) => 100, successFeedback: "儿子们各得其所，你手中有粮心不慌；谁孝顺谁疏懒，日子一长自然看得分明。", failFeedback: "", successEffect: { wealth: 6, happiness: 4 }, failEffect: {  }, tagSuccess: "留资自养", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "桑榆晚景",
        title: "延请坐堂郎中细论本草",
        narrative: (p, y) => "入秋后你咳嗽不止，夜里盗汗。城南药铺有位坐堂郎中，善用本草与针灸，诊金却不薄；另有游方道人自称有祖传丹方，价廉速效。家中积蓄有限，你信哪一个？",
        choices: [
          { text: "请坐堂郎中诊脉，依本草方子慢慢调养，辅以针灸", riskLevel: "费钱 · 缓效 · 成功率 75%", successChance: (p) => 75 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 10 : 0) + (p.health > 60 ? 8 : 0), successFeedback: "郎中切脉细问饮食起居，三帖药后咳止，针过几次，腿上旧疾也松快了；钱花得值。", failFeedback: "药力终究有限，咳是止住了，元气却再难复原；你把药方抄在册上，留与后人。", successEffect: { health: 10, wealth: -8 }, failEffect: { health: 3, wealth: -8, happiness: -3 }, tagSuccess: "药石有功", tagFail: "元气难复", isKey: true },
          { text: "谢绝丹药，只取寻常食疗，早睡少思，静养待春", riskLevel: "清俭 · 静守 · 稳妥必成", successChance: (p) => 100, successFeedback: "你不再奔波劳神，晨起散步，午后小睡，入春时咳嗽竟自己好了；省下的钱给孙儿买了纸笔。", failFeedback: "", successEffect: { health: 6, wealth: 4, happiness: 5 }, failEffect: {  }, tagSuccess: "静养待春", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "古稀沧桑",
        title: "故交零落后重订旧时稿",
        narrative: (p, y) => "同窗故交一年走了三个，白幡一次次挂在巷口。你翻出早年所记的乡里见闻与农桑旧法，纸页已黄。有人劝你刻书传世，只是刻工索价不菲；也有人劝你留着，说人走文散本是常事。",
        choices: [
          { text: "自费请刻工刊印百部，分赠乡塾与故交诸子弟", riskLevel: "破费 · 传世 · 成功率 60%", successChance: (p) => 60 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 10 : 0), successFeedback: "书成百部，墨香犹新，乡塾先生捧读再三；数十年后，仍有人从旧书肆中翻出你的名字。", failFeedback: "刻工潦草，错字不少，书成而无人细读；你把残卷抱回家，叹一声也好，总比散了强。", successEffect: { wealth: -15, happiness: 8, rep: 10 }, failEffect: { wealth: -15, happiness: -4, rep: -2 }, tagSuccess: "丹墨传世", tagFail: "枣梨粗劣", isKey: true },
          { text: "灯下亲手抄成两部，一藏家庙，一赠得意门生", riskLevel: "费神 · 存真 · 稳妥必成", successChance: (p) => 100, successFeedback: "你伏案三月，楷字工整，抄成两部；门生跪受，说此生必替先生守着这卷书，一字不敢损。", failFeedback: "", successEffect: { intellect: 4, happiness: 6 }, failEffect: {  }, tagSuccess: "手泽犹存", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "古稀沧桑",
        title: "荒年设粥棚兼修乡里桥",
        narrative: (p, y) => "连月大旱，流民结队入乡，米价一日三涨。乡里公议设粥棚，又逢石桥被洪水冲塌，春耕难行。你仓中尚有陈粮，捐粮则自家儿孙要勒紧裤带，不捐则眼见有人倒毙路旁。",
        choices: [
          { text: "开仓出粟二百石，设粥棚济饥民，并出资雇人修桥", riskLevel: "倾仓 · 积德 · 成功率 62%", successChance: (p) => 62 + (p.luck > 50 ? 10 : 0), successFeedback: "粥棚日日不断火，桥也在秋前合龙；乡人立碑记名，你的儿孙走在桥上，总被人拱手称谢。", failFeedback: "粮尽得比预想快，粥棚被迫撤了半月，有人未能熬过；桥却修成了，也算留下一点实在。", successEffect: { wealth: -22, happiness: 8, rep: 12 }, failEffect: { wealth: -22, happiness: -6, rep: 4 }, tagSuccess: "粥棚济饥", tagFail: "力有未逮", isKey: true },
          { text: "量力捐粟五十石，先保族人，再往县仓告赈请平粜", riskLevel: "量力 · 有序 · 稳妥必成", successChance: (p) => 100, successFeedback: "族人无一饿倒，县衙也开仓平粜；你虽未博得大名，夜里听着邻家炊烟，心中稍安。", failFeedback: "", successEffect: { wealth: -8, happiness: 4, rep: 4 }, failEffect: {  }, tagSuccess: "量力而行", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "夕阳辞章",
        title: "宗祠灯火子孙环侍榻前",
        narrative: (p, y) => "自知大限将近，你命人把自己抬进宗祠，在列祖牌位前铺一张竹榻。子孙三十余口跪满一院，烛火照得匾额发亮。你手里还攥着那部修了半生的族谱，是当着众人把话说完，还是留几句体己只与长孙？",
        choices: [
          { text: "聚齐子孙，将族规与田契当众交付长孙，一一嘱明", riskLevel: "传承 · 诀别 · 成功率 70%", successChance: (p) => 70 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 10 : 0), successFeedback: "你声音渐低，话却句句清楚。阖族叩首，烛芯爆了一声，你在列祖牌位环绕中安然闭目。", failFeedback: "话说一半，气息已接不上，末一句未竟；长孙含泪点头，你看着他，终究带着笑意松了手。", successEffect: { happiness: 10, rep: 10 }, failEffect: { happiness: 5, rep: 4 }, tagSuccess: "含笑归祠", tagFail: "遗言未尽", isKey: true },
          { text: "屏退众人只留长孙，指族谱空白处嘱他补全旁支", riskLevel: "静托 · 归去 · 稳妥必成", successChance: (p) => 100, successFeedback: "长孙伏在榻边记下每一句。窗外晨光初起，你握着他的手慢慢合眼，如一卷书轻轻合上。", failFeedback: "", successEffect: { happiness: 10, rep: 6 }, failEffect: {  }, tagSuccess: "书卷轻合", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "夕阳辞章",
        title: "散财济乡后在梅下长眠",
        narrative: (p, y) => "腊月里你忽觉胸口空了一块，自知时候到了。儿孙问你还有何遗愿，你说想再看一眼故园那株老梅。这些年攒下的银钱与藏书，是散与贫寒乡邻，还是尽数留给子孙？",
        choices: [
          { text: "取银三百两分赠乡邻，藏书捐与义学，再赴梅下", riskLevel: "散尽 · 归去 · 成功率 68%", successChance: (p) => 68 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 10 : 0), successFeedback: "受赠者跪了一地。你要人搀到梅树下，花瓣落在膝头，你望着满树清影，安静地合上了眼。", failFeedback: "银钱尚未分完，你已气力不支。儿孙抬你到树下，梅香里你只听清风过枝头，便再无声息。", successEffect: { wealth: -20, happiness: 12, rep: 12 }, failEffect: { wealth: -20, happiness: 8, rep: 6 }, tagSuccess: "梅下长眠", tagFail: "遗愿未竟", isKey: true },
          { text: "将银钱藏书尽付子孙，只携一卷旧书坐于梅下", riskLevel: "安然 · 归去 · 稳妥必成", successChance: (p) => 100, successFeedback: "子孙跪送，你翻着那卷读过无数遍的旧书，指腹停在某一页；风起梅落，你便不再翻动了。", failFeedback: "", successEffect: { happiness: 10, rep: 4 }, failEffect: {  }, tagSuccess: "掩卷而逝", tagFail: "另寻他途", isKey: false }
        ]
      }
      ]
    ];

    // ---- modern 16 大生命阶段事件池（每阶段多个候选，单局随机抽取）----
    const MODERN_STAGE_POOLS = [
      [
      {
        period: "幼年启蒙",
        title: "私塾戒尺与新式学堂的铃声",
        narrative: (p, y) => "民国初立，街口私塾仍摆着孔夫子牌位，先生持戒尺教《三字经》；隔巷的新式学堂却挂起黑板，教国文、算学与体操。母亲用铜板凑了学费，只够一处。你站在两扇门之间，听着一边的念诵与一边的风琴声，不知该往哪边走。",
        choices: [
          { text: "进新式学堂，学白话国文与算学，放学后自己抄《千字文》补上旧学", riskLevel: "新旧兼修 · 根基 · 成功率 75%", successChance: (p) => 75 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "先生夸你字写得端正，算盘也打得快；晚上你在油灯下抄完《千字文》，父亲摸了摸你的头，说这孩子两条腿都能站。", failFeedback: "课程跳得太快，你算学跟不上，旧学也丢了大半。先生摇头，母亲却把省下的铜板换成纸笔，说再熬一熬。", successEffect: { intellect: 10, rep: 5 }, failEffect: { intellect: 4, happiness: -5 }, tagSuccess: "开蒙启智", tagFail: "根基未稳", isKey: true },
          { text: "留在私塾，先把《四书》背熟，认字写毛笔字，图个稳妥", riskLevel: "守旧 · 稳妥 · 稳妥必成", successChance: (p) => 100, successFeedback: "戒尺下你背熟了半部《论语》，字也像模像样。街坊说这孩子将来能写对联、记账，不会吃亏。", failFeedback: "", successEffect: { intellect: 5, rep: 4 }, failEffect: {  }, tagSuccess: "旧学扎实", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "幼年启蒙",
        title: "剪辫那天父亲关上了院门",
        narrative: (p, y) => "城里贴出剪辫告示，巡警带着剪刀在街上拦人。父亲留了半辈子的辫子，昨夜自己铰了，灰白的头发散在肩上。他把你叫到院里，让你看那截辫子，又问你：往后出门，是低着头走，还是挺着胸走？",
        choices: [
          { text: "替父亲把辫子收进木匣，自己剃短头发，第二天照常去街口买豆腐", riskLevel: "顺势 · 露面 · 成功率 70%", successChance: (p) => 70 + (p.luck > 50 ? 8 : 0), successFeedback: "邻人指指点点，却没人为难你。卖豆腐的老张还多给了一块，说新朝新气象，孩子精神。父亲在门后松了口气。", failFeedback: "巷口几个闲汉哄笑，追着你喊“假洋鬼子”。你跑回家，母亲给你拍掉身上的灰，说别怕，日子总要往前走。", successEffect: { luck: 6, rep: 4 }, failEffect: { happiness: -6, luck: 3 }, tagSuccess: "随世而变", tagFail: "当街受辱", isKey: true },
          { text: "暂时不出门，在家帮母亲糊纸盒，等人心定下来再说", riskLevel: "避风 · 稳妥 · 稳妥必成", successChance: (p) => 100, successFeedback: "你在家糊了三天纸盒，换回十几个铜板。风声过去，街上辫子少了，你也悄悄出了门，没人多看你一眼。", failFeedback: "", successEffect: { wealth: 3, happiness: 2 }, failEffect: {  }, tagSuccess: "静观其变", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "童年韶光",
        title: "军阀过境那夜的包袱",
        narrative: (p, y) => "夜里枪声从城西传来，说是过境的兵要征粮拉夫。母亲摸黑把两件旧棉袄、一包炒米和几块银元裹进布包袱，父亲去后院牵驴。巷子里全是脚步声与婴儿的哭。母亲攥着你的手问：往山里走，还是去教堂后头躲一躲？",
        choices: [
          { text: "跟着乡邻往山里走，路上照看弟弟，把自己那份炒米省下一半", riskLevel: "逃难 · 饥寒 · 成功率 60%", successChance: (p) => 60 + (p.luck > 50 ? 10 : 0) + (p.health > 60 ? 8 : 0), successFeedback: "走了两夜，脚底磨破，你把炒米分给弟弟，自己啃树皮。到了山坳舅家，人都还在，母亲抱着你哭，说你长大了。", failFeedback: "半路遇上散兵，包袱被抢走，一家人跌跌撞撞走散又聚拢。你饿得站不住，却死死牵着弟弟的手没松。", successEffect: { health: -4, happiness: 4, rep: 8 }, failEffect: { health: -8, wealth: -8, happiness: -6 }, tagSuccess: "患难相依", tagFail: "流离失所", isKey: true },
          { text: "躲进教堂后院，那儿人多，兵一般不进去搜", riskLevel: "借庇 · 稳妥 · 稳妥必成", successChance: (p) => 100, successFeedback: "教堂里挤了几十户人家，神父煮了一锅稀粥分给众人。天亮后兵开走了，你回家一看，米缸空了，人平安。", failFeedback: "", successEffect: { health: -3, happiness: 1 }, failEffect: {  }, tagSuccess: "暂得安身", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "童年韶光",
        title: "警报声里替家里守铺子",
        narrative: (p, y) => "父亲去乡下收账，铺子只剩你和母亲。午后警报骤响，街上人往防空洞跑，可柜上还摆着刚进的洋布与煤油，卷帘门一锁就顾不上货。母亲问你：是拉着她一起躲，还是留下看铺子？远处已有飞机声。",
        choices: [
          { text: "让母亲先躲，自己把洋布和钱匣搬进地窖，再锁门去追她", riskLevel: "涉险 · 护家 · 成功率 55%", successChance: (p) => 55 + (p.luck > 50 ? 8 : 0) + (p.health > 60 ? 6 : 0), successFeedback: "你来回两趟，手心全是汗，最后一趟才钻进防空洞。飞机只掠过城郊，铺子的货无损，母亲骂了你一句，又把你搂紧。", failFeedback: "你搬第二趟时瓦片震落，砸在柜台上。货保住了大半，你却磕破了额角，母亲连夜用草药给你敷上。", successEffect: { health: -3, wealth: 6, rep: 5 }, failEffect: { health: -7, wealth: 3, happiness: -4 }, tagSuccess: "临危守业", tagFail: "血溅柜台", isKey: true },
          { text: "锁上门跟母亲一起进防空洞，货没了还能再挣", riskLevel: "舍财 · 稳妥 · 稳妥必成", successChance: (p) => 100, successFeedback: "你扶着母亲挤进洞里，蹲在墙角听外面闷响。警报解除后回来，丢了两匹布，人却都好好的，父亲回来也没多责骂。", failFeedback: "", successEffect: { wealth: -4, happiness: 3 }, failEffect: {  }, tagSuccess: "人安为先", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "少年分流",
        title: "家道中落后的两支笔",
        narrative: (p, y) => "父亲的商号抵了债，家里只剩一架旧书柜和母亲陪嫁的银镯。你十五岁，成绩在学堂里数一数二。先生上门劝考师范，说免学费还有膳费；同乡的远房叔父却来信，说上海纱厂招练习生，管吃管住，月有工钱。母亲把银镯放在桌上，问你怎么选。",
        choices: [
          { text: "去考省立师范，靠免膳读书，课余给报馆抄稿挣纸笔钱", riskLevel: "清贫 · 向学 · 成功率 65%", successChance: (p) => 65 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "你榜上有名，穿着洗白的蓝布衫进了师范。夜里替报馆抄稿，稿酬是几只铜板，却让你第一次读到了白话报上的新道理。", failFeedback: "考试那日你发起烧，作文只写了半篇，落榜回家。先生叹气，母亲却说：明年再考，家里的米还够。", successEffect: { intellect: 14, rep: 6 }, failEffect: { intellect: 5, happiness: -7 }, tagSuccess: "负笈求学", tagFail: "抱病落榜", isKey: true },
          { text: "去上海纱厂当练习生，先把工钱寄回家，夜里上夜校识字", riskLevel: "进厂 · 稳妥 · 稳妥必成", successChance: (p) => 100, successFeedback: "你进了纱厂，机器声震耳，一天站十个钟头。工钱虽薄，每月能寄回几块银元；夜校里你学会了记账，也认得几个字。", failFeedback: "", successEffect: { health: -4, wealth: 8, intellect: 4 }, failEffect: {  }, tagSuccess: "做工养家", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "少年分流",
        title: "救亡歌咏队敲响了校门",
        narrative: (p, y) => "北方局势一日紧似一日，城里学生们组织救亡歌咏队，上街唱《松花江上》，散发传单，也有人悄悄收拾行装去投军。学堂先生睁一只眼闭一只眼。你是班上年岁最大的，同学都看你。唱歌要担风险，读书也不能耽误。",
        choices: [
          { text: "白天照常上课，傍晚带歌咏队去码头与茶馆唱，教工友识字", riskLevel: "涉世 · 担当 · 成功率 60%", successChance: (p) => 60 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 6 : 0), successFeedback: "码头工人围了半圈听你唱，有人跟着抹泪。散场后一位老工人塞给你两个馒头，说学生也该吃饱了再喊。你嗓子哑了三天，心里却亮堂。", failFeedback: "巡警驱散队伍，你被记了名字。校长把你叫去训话，母亲听说后一夜没睡，但你仍把传单藏在了书页里。", successEffect: { happiness: 5, rep: 12 }, failEffect: { happiness: -5, luck: -3, rep: 4 }, tagSuccess: "唤醒街巷", tagFail: "名列警册", isKey: true },
          { text: "先不抛头露面，安心读书，把功课考好再说", riskLevel: "专注 · 稳妥 · 稳妥必成", successChance: (p) => 100, successFeedback: "你躲在教室后头做题，期末考名列前茅。歌咏队的事你只远远看着，心里有些愧，却也没让家里多担一分心。", failFeedback: "", successEffect: { intellect: 7, happiness: -2 }, failEffect: {  }, tagSuccess: "埋头书卷", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "成人立志",
        title: "十字街口的招兵旗与留洋船票",
        narrative: (p, y) => "你十八岁，师范将毕业。城门贴着招兵告示，管饭发饷；城里教会学堂有一张赴法勤工俭学的名额，需自筹盘缠；母亲鬓角已白，家中弟妹尚小。同学里有人已经换上灰布军装。夜里你翻来覆去，铺上摆着三样东西：一支笔、一张船票存根、弟妹的旧鞋。",
        choices: [
          { text: "报名赴法勤工俭学，先在码头做工攒盘缠，把一半工钱寄回家", riskLevel: "远行 · 求索 · 成功率 55%", successChance: (p) => 55 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 8 : 0) + (p.health > 60 ? 5 : 0), successFeedback: "你在码头扛了半年货，凑够船资。开船那日母亲没哭，只把一双新纳的布鞋塞进你怀里，说出去别丢中国人的脸。", failFeedback: "盘缠凑不齐，名额让给了别人。你把船票存根夹进书里，留在城里教书，白日上课，夜里读译来的新书，也没停下。", successEffect: { wealth: -8, intellect: 15, luck: 8 }, failEffect: { intellect: 8, happiness: -6, rep: 4 }, tagSuccess: "远渡求索", tagFail: "留城守志", isKey: true },
          { text: "应招入伍，随军做文书，管饭发饷，也能照应家里", riskLevel: "从戎 · 稳妥 · 稳妥必成", successChance: (p) => 100, successFeedback: "你换上灰布军装，在营部抄写公文、替不识字的兵写信回家。饷银不多，按月寄回，母亲来信只写了四个字：好生保重。", failFeedback: "", successEffect: { health: -3, wealth: 5, rep: 8 }, failEffect: {  }, tagSuccess: "投笔从戎", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "成人立志",
        title: "三人夜谈：办夜校还是南下考学",
        narrative: (p, y) => "同窗三人围着一盏煤油灯。老周说城郊工厂多文盲，该去办工人夜校；阿元说南方新式中学招考，考上可免学费；你手里还有母亲托人捎来的几块银元，是家里最后的积蓄。灯花爆了一下，谁也没先开口。窗外传来黄包车夫的吆喝。",
        choices: [
          { text: "拿出银元办夜校，租半间铺面，自编识字课本，不收学费", riskLevel: "启蒙 · 倾囊 · 成功率 62%", successChance: (p) => 62 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 5 : 0), successFeedback: "夜校开了，二十几个工人挤在铺面里，油灯下写自己的名字。有个车夫第一次写会“人”字，笑得像个孩子。你把最后一块银元也换成了灯油。", failFeedback: "铺租涨了，来的工人渐渐少，夜校办了三个月就散了。可那本手抄的识字课本，被一个学徒带走，说要在厂里接着教。", successEffect: { wealth: -10, intellect: 8, rep: 14 }, failEffect: { wealth: -8, happiness: -5, rep: 6 }, tagSuccess: "点灯照人", tagFail: "散而未灭", isKey: true },
          { text: "南下考学，银元只做路费，考上了再半工半读", riskLevel: "赶考 · 稳妥 · 稳妥必成", successChance: (p) => 100, successFeedback: "你坐了三天火车，考进南方一所中学的高中部。课余替人抄书、校对报稿，勉强糊口。夜里躺在窄铺上，你想起那盏煤油灯，给老周去了封信。", failFeedback: "", successEffect: { wealth: -5, intellect: 10, luck: 3 }, failEffect: {  }, tagSuccess: "南行就学", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "青春韶华",
        title: "青布长衫投考师范讲习所",
        narrative: (p, y) => "县里师范讲习所招生，免学费，还管一顿糙米饭。你攥着借来的两块银元，天不亮走了三十里土路。可家中七亩薄田正等着人下地，父亲说读书人填不饱肚子。报名处就设在文庙廊下，考还是不考，你得当场拿定主意。",
        choices: [
          { text: "先应下考卷，考完再连夜赶回村里，求父亲点头", riskLevel: "前程未定 · 家计难舍 · 成功率 68%", successChance: (p) => 68 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "榜上第十九名。父亲把烟袋在门槛上磕了三下，终究把地契押给族里，替你凑齐了铺盖钱。", failFeedback: "你落了榜，回家正赶上秋收。父亲没说什么，只把你能吃的糙米省给了弟妹。", successEffect: { intellect: 10, rep: 5 }, failEffect: { intellect: 4, happiness: -5 }, tagSuccess: "题名有望", tagFail: "归田收秋", isKey: true },
          { text: "留在家里帮父亲把七亩地种完，夜里再去乡塾借书自学", riskLevel: "两全其难 · 心志不堕 · 稳妥必成", successChance: (p) => 100, successFeedback: "秋粮进了仓，你把一本《算术》翻得卷了边，村里的孩子开始追着喊你先生。", failFeedback: "", successEffect: { intellect: 6, happiness: 3, rep: 3 }, failEffect: {  }, tagSuccess: "耕读不辍", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "青春韶华",
        title: "纱厂招练习生，铁门里汽笛响",
        narrative: (p, y) => "日资纱厂的铁门外挤满了人，招二十个练习生，月给八块银元，管住不管吃。工头捏着你的手掌看茧，说细纱车间热得能拧出水，一天要站十二个钟头。同村有人递话来，码头扛包当天就结现钱。",
        choices: [
          { text: "咬牙留下考工，进细纱车间做学徒，先挣一份稳当工钱", riskLevel: "苦干立身 · 积劳伤身 · 成功率 72%", successChance: (p) => 72 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.health > 60 ? 8 : 0), successFeedback: "三年后你摸熟了细纱机的脾性，能听声辨断头，工钱涨到十二块，还把铺盖从通铺搬进了小屋。", failFeedback: "机器咬去了你左手半截指尖。工头给了两块银元养伤钱，你把它缝进棉袄里，没敢寄回家。", successEffect: { wealth: 8, intellect: 5 }, failEffect: { health: -12, wealth: 2, happiness: -6 }, tagSuccess: "听声辨纱", tagFail: "断指存银", isKey: true },
          { text: "跟着同村人去码头扛包，当日结钱，先顾眼前", riskLevel: "现钱糊口 · 肩背难支 · 稳妥必成", successChance: (p) => 100, successFeedback: "你在码头上喊了三年号子，肩膀磨出厚茧，攒下的银元寄回家翻修了两间瓦房。", failFeedback: "", successEffect: { health: 4, wealth: 6, rep: 2 }, failEffect: {  }, tagSuccess: "号子立身", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "初涉人世",
        title: "沪上码头送别，留洋的船票",
        narrative: (p, y) => "亲戚牵线，有人愿资助你去法国勤工俭学，船票和介绍信都备下了；只是路费要自筹一半，此去少则五年，家中老母的病还没好。码头上四等舱的舷梯已收起一半，同行的青年正喊着你的名字。",
        choices: [
          { text: "典当母亲的银镯凑齐船票，登上开往马赛的四等舱", riskLevel: "远渡求新 · 亲恩难报 · 成功率 62%", successChance: (p) => 62 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "你在里昂的工厂半工半读，学会了看图纸，也学会在夜校里跟人争论中国该往何处去。", failFeedback: "船到新加坡你病倒了，被送上岸养了两个月，钱花去大半，只得折回上海，银镯也没能赎回。", successEffect: { wealth: -4, intellect: 12, rep: 6 }, failEffect: { wealth: -6, intellect: 5, happiness: -8 }, tagSuccess: "负笈远洋", tagFail: "中途折返", isKey: true },
          { text: "留下侍奉老母，在县城中学谋一份教书的差事", riskLevel: "晨昏定省 · 壮志稍敛 · 稳妥必成", successChance: (p) => 100, successFeedback: "你在县立中学教算术，月薪十八元，课余替人抄写状纸，母亲的药没有断过。", failFeedback: "", successEffect: { intellect: 6, happiness: 6, rep: 5 }, failEffect: {  }, tagSuccess: "侍疾守志", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "初涉人世",
        title: "城门口贴出告示，招学兵",
        narrative: (p, y) => "城门口贴着招兵告示，说一人当兵，全家免捐。街那头，学生救亡宣传队正搭台子唱《松花江上》。你手里还捏着半张没写完的启事——部队要识字的人当文书，宣传队却只管一顿午饭。",
        choices: [
          { text: "投考学兵队，凭一手好字去连部做个文书", riskLevel: "投笔从戎 · 生死难料 · 成功率 66%", successChance: (p) => 66 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "你替连长誊清花名册，也替不识字的弟兄写家信。一次夜行军，你把全连带出了岔路口。", failFeedback: "部队在皖北被打散，你背着伤兵走了三天，回到家乡时军装已被老乡换走，只剩一块干粮。", successEffect: { health: -4, intellect: 5, rep: 10 }, failEffect: { health: -10, happiness: -5, rep: 4 }, tagSuccess: "文书赴难", tagFail: "散兵归乡", isKey: true },
          { text: "加入学生救亡宣传队，走街串巷演活报剧", riskLevel: "唤醒乡邻 · 清苦自持 · 稳妥必成", successChance: (p) => 100, successFeedback: "你在集市上演《放下你的鞭子》，台下的老农攥紧了拳头。队里管饭，你瘦了，嗓子却越来越亮。", failFeedback: "", successEffect: { intellect: 4, happiness: 6, rep: 8 }, failEffect: {  }, tagSuccess: "街头呐喊", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "成家立业",
        title: "媒人上门说亲，聘礼要四色",
        narrative: (p, y) => "媒人第三次上门，说女方是邻村织布的好手，只是聘礼要银元六十、细布四匹、猪肉半扇。你攒了三年的工钱只够一半，女方娘舅又放出话来，年底前凑不齐便另许人家。",
        choices: [
          { text: "向厂里工友起个会借钱，赶在冬至前把亲定下", riskLevel: "举债成家 · 日后还偿 · 成功率 70%", successChance: (p) => 70 + (p.luck > 50 ? 6 : 0), successFeedback: "工友凑了二十八块，你终于赶在冬至前下了定。新房里贴着红纸剪的喜字，灶上炖着借来的半只鸡。", failFeedback: "会钱没凑齐，女方改许了镇上的布商。你把那几匹细布退给店里，折了两成价，独自喝了半斤酒。", successEffect: { wealth: -6, happiness: 12, rep: 5 }, failEffect: { wealth: -3, happiness: -10, rep: -2 }, tagSuccess: "冬至下定", tagFail: "亲事他许", isKey: true },
          { text: "与女方商量简办，只迎亲不摆席，往后一起挣", riskLevel: "两情相谅 · 从简结发 · 稳妥必成", successChance: (p) => 100, successFeedback: "她拎着一只蓝布包袱过了门，你们在租来的厢房里对坐吃了一碗面，说定往后日子一起挣。", failFeedback: "", successEffect: { wealth: 2, happiness: 9, rep: 2 }, failEffect: {  }, tagSuccess: "布衣结发", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "成家立业",
        title: "江边码头，工厂要迁往重庆",
        narrative: (p, y) => "战事逼近，纱厂奉命拆卸机器西迁，工头说愿走的每人补三块银元，家眷随船，只是江上要过三道封锁线。你刚出生的孩子还在发热，岳母一家又不肯离开老屋。",
        choices: [
          { text: "携妻儿随厂西迁，跟着机器一程一程拆运", riskLevel: "逆江西行 · 家小颠沛 · 成功率 64%", successChance: (p) => 64 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "船在宜昌换小船，你的孩子在舱里退了热。到了重庆，你守着重新开工的纱锭，成了熟练的保全工。", failFeedback: "船在江上遇了空袭，铺盖和行李都沉了，一家人在巫山脚下走了半个月才追上大部队。", successEffect: { health: -5, intellect: 8, rep: 6 }, failEffect: { health: -9, wealth: -5, happiness: -8 }, tagSuccess: "溯江保全", tagFail: "失箧追队", isKey: true },
          { text: "留下看守老屋，在本地另寻一份零工", riskLevel: "守土安家 · 生计日蹙 · 稳妥必成", successChance: (p) => 100, successFeedback: "你替粮行挑脚，又在城隍庙前摆了个修车摊。日子紧，但妻儿都在身边，老屋的瓦也没塌。", failFeedback: "", successEffect: { health: -3, wealth: 3, happiness: 5 }, failEffect: {  }, tagSuccess: "守屋度日", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "三十而立",
        title: "村里丈量土地，要重新立契",
        narrative: (p, y) => "土改工作队进了村，丈量土地，重立契据。你家分到七亩水田和半头耕牛，可老父卧病在床，两位叔伯盯着祖屋的三间正房，说长子应当多担赡养，房产却要摊平。",
        choices: [
          { text: "接下赡养担子，把分到的田契写成兄弟共有", riskLevel: "独担养老 · 让产求安 · 成功率 75%", successChance: (p) => 75 + (p.luck > 50 ? 5 : 0), successFeedback: "工作队把公议记在册子上，两位叔伯再没为房争执。老人的药钱你一人出，秋后收了十石谷子。", failFeedback: "田契写共有的次日，二叔又反悔，说祖屋的梁是你爹换的，该归他。你气得砸了一只碗。", successEffect: { wealth: 4, happiness: 5, rep: 10 }, failEffect: { wealth: 2, happiness: -8, rep: -3 }, tagSuccess: "立契让产", tagFail: "房争伤和", isKey: true },
          { text: "请村干部与族老当众评理，按人口均分田产", riskLevel: "当众评理 · 亲族生隙 · 稳妥必成", successChance: (p) => 100, successFeedback: "族老在祠堂里把话说透，田按人头分，赡养按月轮。你落了个公道，只是逢年过节少了往来。", failFeedback: "", successEffect: { wealth: 3, happiness: 3, rep: 6 }, failEffect: {  }, tagSuccess: "祠堂公议", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "三十而立",
        title: "车间黑板报贴出技术革新榜",
        narrative: (p, y) => "厂里响应一五计划，要推广苏联专家的高速切削法，黑板报上列出技术革新榜，谁改进了工装就记功。夜校晚上开课，教代数与识图；可车间定额也加了三成，你家里刚添了第二个孩子。",
        choices: [
          { text: "报名夜校学识图，琢磨着把车床夹具改一改", riskLevel: "以工代学 · 力有未逮 · 成功率 68%", successChance: (p) => 68 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "你的夹具把辅助时间省了一半，黑板报上登了你的名字，厂里奖了一支金星钢笔和二十尺布票。", failFeedback: "夹具崩了刀，废了两根料，你赔了半个月工资，夜校的课也落了三成，图纸总算看懂了。", successEffect: { wealth: 5, intellect: 12, rep: 10 }, failEffect: { wealth: -5, intellect: 5, happiness: -5 }, tagSuccess: "革新记功", tagFail: "崩刀赔料", isKey: true },
          { text: "先把定额干满，下班后帮家里糊纸盒补用度", riskLevel: "安分守额 · 持家补用 · 稳妥必成", successChance: (p) => 100, successFeedback: "你月月超额完成定额，评上先进生产者，奖金买了二斤猪肉和一双胶鞋，孩子的棉衣也絮上新棉花。", failFeedback: "", successEffect: { wealth: 6, happiness: 4, rep: 5 }, failEffect: {  }, tagSuccess: "先进守额", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "负重前行",
        title: "一封家书过了三道封锁线",
        narrative: (p, y) => "民国二十九年冬，你在镇上做木匠，妻子咳血已有月余。邮路断了三回，终于捎来老家口信，说岳母病重，盼你回去一趟；可厂里接了军需的活，工钱翻倍，走了这活就归别人。你捏着那张纸条，站在檐下听北风。",
        choices: [
          { text: "先赶完这批军需木箱，托同乡捎钱捎药回老家", riskLevel: "误了归期 · 得保工钱 · 成功率 62%", successChance: (p) => 62 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 6 : 0), successFeedback: "木箱如期交齐，工钱翻倍，你托人捎回药钱和一封短信。妻子接过信，咳得轻了些。", failFeedback: "你赶完工时岳母已入土，妻子怨你心硬，家里冷了半冬，你却攒下一笔救命钱。", successEffect: { wealth: 12, rep: 4 }, failEffect: { wealth: 8, happiness: -8 }, tagSuccess: "如期交货", tagFail: "归迟憾深", isKey: true },
          { text: "告假还乡，把军需的活让与同行，先顾病人", riskLevel: "舍利取义 · 心有所安 · 稳妥必成", successChance: (p) => 100, successFeedback: "你连夜赶回，煎药侍疾半月，岳母转危为安，同行也承你这份人情，日后常来帮衬。", failFeedback: "", successEffect: { happiness: 10, rep: 6 }, failEffect: {  }, tagSuccess: "亲恩为重", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "负重前行",
        title: "公共食堂锅底那半勺稀粥",
        narrative: (p, y) => "一九六〇年冬，公社食堂按人头打饭，你家小子正是长个子，碗里总不见稠的。邻家寡妇带着三个娃，昨日已断粮，夜里来敲门，想借你藏在炕洞里的半袋红薯干。可那是你攒着给孩子过冬的。你握着门闩，半晌没作声。",
        choices: [
          { text: "匀出半袋红薯干，约定开春队里分红再还", riskLevel: "恤邻济困 · 自家受窘 · 成功率 68%", successChance: (p) => 68 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 6 : 0), successFeedback: "开春分红，她如数还来，还捎了一篮野菜。两家的孩子一处上学，从此成了伴。", failFeedback: "开春她家仍紧，红薯干没还上，你家小子饿了半月，你却得了全队一句厚道。", successEffect: { happiness: 5, rep: 10 }, failEffect: { happiness: -6, rep: 8 }, tagSuccess: "邻里相济", tagFail: "亏己全义", isKey: true },
          { text: "婉言推说自家也紧，只借出一小瓢应急", riskLevel: "量力而行 · 各守本分 · 稳妥必成", successChance: (p) => 100, successFeedback: "你舀了一瓢递过去，话说得软。她千恩万谢走了，两家情分没断，自家口粮也保住了。", failFeedback: "", successEffect: { wealth: 3, happiness: 4 }, failEffect: {  }, tagSuccess: "量力周济", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "中年险滩",
        title: "车间黑板报上的技术革新",
        narrative: (p, y) => "一九五六年，厂里号召技术革新，你熬了三个通宵，把车床的夹具改了一道，能省两成料。可老师傅说这是祖上传下的规矩，动了要出事故；车间主任让你先报上去评先进。你捏着图纸，指节发白。",
        choices: [
          { text: "把图纸交上去，请在老师傅跟前当场试车", riskLevel: "冒犯旧规 · 险中求进 · 成功率 58%", successChance: (p) => 58 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.health > 60 ? 4 : 0), successFeedback: "试车三回，夹具稳当，省料两成。老师傅点点头，你上了黑板报，还评上市里先进。", failFeedback: "头一回试车崩了刀，老师傅没说什么，只让你把图纸收回去。你赔了料钱，却把机理想透。", successEffect: { intellect: 12, rep: 8 }, failEffect: { wealth: -6, intellect: 8 }, tagSuccess: "技改争先", tagFail: "吃亏长智", isKey: true },
          { text: "压下图纸，先私下请老师傅指点再作打算", riskLevel: "藏锋守拙 · 稳中求全 · 稳妥必成", successChance: (p) => 100, successFeedback: "老师傅看了半宿，指你改了一处夹角。你把功劳记在他名下，两人都得了体面。", failFeedback: "", successEffect: { intellect: 4, rep: 5 }, failEffect: {  }, tagSuccess: "藏器待时", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "中年险滩",
        title: "知青报名表上的名字",
        narrative: (p, y) => "一九六九年，街道敲锣打鼓送知青下乡，你儿子刚满十六，报名表递到手上。他成份一栏填的是职员，不算差也不算好，去与不去都有人议论。妻子夜里抹泪，说独子走了，家里就冷清了。你把表在灯下看了又看。",
        choices: [
          { text: "让儿子报名去北大荒，临行把棉袄絮厚", riskLevel: "骨肉远别 · 历练成人 · 成功率 62%", successChance: (p) => 62 + (p.luck > 50 ? 8 : 0), successFeedback: "儿子在北大荒学会了开拖拉机，来信字迹愈发端正，三年后招工回城，人结实也沉稳。", failFeedback: "北地苦寒，儿子冻伤了脚，信里却不诉苦。你寄去一双毡靴，心里疼了整冬。", successEffect: { happiness: 6, rep: 6 }, failEffect: { happiness: -8, rep: 4 }, tagSuccess: "送子支边", tagFail: "牵肠挂肚", isKey: true },
          { text: "托人情把儿子留在城里，先当个学徒工", riskLevel: "骨肉在侧 · 落人话柄 · 稳妥必成", successChance: (p) => 100, successFeedback: "儿子进了街办小厂，早晚能回家吃饭。邻里背后说你家会打算，妻子却总算睡得安稳。", failFeedback: "", successEffect: { happiness: 8, rep: -4 }, failEffect: {  }, tagSuccess: "承欢膝下", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "动荡考验",
        title: "大字报贴到了车间门口",
        narrative: (p, y) => "一九六七年春，厂门口贴满了大字报，有人点名要你表态，说老会计有历史问题，人人得划清界限。你与他共事十二年，知道他不过是旧社会当过账房。夜里你翻来覆去，笔在纸上写了又划。",
        choices: [
          { text: "只写自己不谙内情，不给人扣帽子", riskLevel: "缄口守拙 · 得罪两边 · 成功率 55%", successChance: (p) => 55 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "你的检讨写得含糊，两边都不满意，却也没人再追。老会计后来悄悄朝你拱了拱手。", failFeedback: "有人贴出你的大字报，说你立场暧昧。你被叫去学习班半个月，回来时瘦了一圈。", successEffect: { happiness: 3, rep: 6 }, failEffect: { health: -4, happiness: -10 }, tagSuccess: "守口如瓶", tagFail: "处境转难", isKey: true },
          { text: "按报上口径写一张大字报，随大流签上名", riskLevel: "明哲保身 · 心有余愧 · 稳妥必成", successChance: (p) => 100, successFeedback: "你照抄了报上的话，签了名，风波绕过了你家。只是再遇见老会计，你总低着头快步走开。", failFeedback: "", successEffect: { happiness: -3, rep: 4 }, failEffect: {  }, tagSuccess: "随波自保", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "动荡考验",
        title: "五七干校来的那张调令",
        narrative: (p, y) => "一九七〇年，机关精简，一张调令要你去五七干校，说是劳动锻炼，归期未定。同一批里有人托病不去，有人抢着报名表忠心。你妻子体弱，孩子还在读书，行囊收拾了又拆开。",
        choices: [
          { text: "主动申请下干校，说改造思想也锻炼身体", riskLevel: "以退为进 · 前程未卜 · 成功率 60%", successChance: (p) => 60 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.health > 60 ? 6 : 0), successFeedback: "你在干校挑粪种菜，晒黑了也结实了。两年后调令回城，组织说你表现好，安排了新岗。", failFeedback: "干校湿冷，你落下腰疾，回城时岗位已被人顶了，只能从头做起。", successEffect: { health: 6, rep: 8 }, failEffect: { health: -6, wealth: -4 }, tagSuccess: "主动请缨", tagFail: "劳身失位", isKey: true },
          { text: "以妻子病重为由请假缓行，留在原单位", riskLevel: "家室为重 · 落人口实 · 稳妥必成", successChance: (p) => 100, successFeedback: "你交了病假条，留下来照顾妻子。单位里有人说你恋家，可妻子熬过了那个冬天。", failFeedback: "", successEffect: { happiness: 8, rep: -3 }, failEffect: {  }, tagSuccess: "顾家守拙", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "知命之年",
        title: "平反通知书下来的那天",
        narrative: (p, y) => "一九七七年秋，单位来人通知，说当年扣在你头上的那顶帽子可以摘了，档案里的材料要重新写。你跑了三趟，最后在一间办公室里看见那张薄纸。窗外梧桐落叶，你手抖得签不成名字。",
        choices: [
          { text: "要求把当年的结论一并改正，恢复原职级", riskLevel: "据理力争 · 一波三折 · 成功率 58%", successChance: (p) => 58 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 8 : 0), successFeedback: "材料改了，职称补上，补发的工资装了一个信封。你把信封压在箱底，先给妻子买了一斤肉。", failFeedback: "来回扯了半年，只改了一半。你没再争，回家把旧笔记本一页页烧了。", successEffect: { wealth: 10, rep: 12 }, failEffect: { happiness: -6, rep: 4 }, tagSuccess: "沉冤得雪", tagFail: "半纸平反", isKey: true },
          { text: "只领回那张通知，不再申辩，回岗位做事", riskLevel: "但求清白 · 不争长短 · 稳妥必成", successChance: (p) => 100, successFeedback: "你把通知叠好收进抽屉，第二天照常上班。同事待你客气了，日子也一点点回到正轨。", failFeedback: "", successEffect: { happiness: 8, rep: 4 }, failEffect: {  }, tagSuccess: "清白自守", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "知命之年",
        title: "恢复高考的第一个冬天",
        narrative: (p, y) => "一九七七年冬，广播里说恢复高考，不拘成份，自愿报名。你女儿在乡下插队七年，课本早当了引火纸。她连夜翻出旧笔记，眼睛亮得吓人；可家里拿不出路费和复习的工夫。你在灯下算了半宿。",
        choices: [
          { text: "让女儿请假回城复习，全家省口粮供她", riskLevel: "孤注一掷 · 望女成凤 · 成功率 64%", successChance: (p) => 64 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 6 : 0), successFeedback: "她考上了省城的师范学院，走那天你送到车站，把攒的布票缝进她棉袄里。信里说食堂有白面馒头。", failFeedback: "她差了几分落榜，回村时没哭。第二年再考，中了中专。你才知她夜里背书到天亮。", successEffect: { happiness: 12, rep: 8 }, failEffect: { intellect: 4, happiness: -5 }, tagSuccess: "寒门折桂", tagFail: "来年再试", isKey: true },
          { text: "劝她安心务农，先顾眼下工分和口粮", riskLevel: "务实守成 · 埋没心愿 · 稳妥必成", successChance: (p) => 100, successFeedback: "她没报名，把笔记又收进箱底。年底分红多了几十斤粮，家里过了个踏实年。", failFeedback: "", successEffect: { wealth: 5, happiness: -3 }, failEffect: {  }, tagSuccess: "安分守成", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "花甲在望",
        title: "退休证压在抽屉最底下的那个下午",
        narrative: (p, y) => "退休证和工资折压在抽屉最底下，厂门口敲锣打鼓送你回家。食堂师傅说，往后打饭就得自己掏钱了。小儿子还在北边插队，老伴的药也快吃完。你站在院子里，是留在城里守着这份体面，还是回乡下陪老母亲过几年清苦日子？",
        choices: [
          { text: "收拾行李回乡下，侍奉老母亲，顺带照看几分自留地", riskLevel: "归乡奉亲 · 生计渐薄 · 成功率 68%", successChance: (p) => 68 + (p.luck > 50 ? 10 : 0) + (p.health > 60 ? 8 : 0), successFeedback: "老屋的灶膛重新烧暖，母亲夜里不再咳得那样久。你日出下地，日落煮粥，日子清苦，心里却踏实。", failFeedback: "水土不服，腰腿旧伤又犯，母亲的药钱也紧。你在灯下算账，明白尽孝二字，从来比想象中更沉。", successEffect: { health: 4, happiness: 9, rep: 4 }, failEffect: { health: -8, wealth: -3, happiness: -4 }, tagSuccess: "膝前尽孝", tagFail: "力不从心", isKey: true },
          { text: "留在城里，把退休金攒作药钱，按月给乡下寄去", riskLevel: "守城寄养 · 两处牵肠 · 稳妥必成", successChance: (p) => 100, successFeedback: "每月十五，你把汇款单仔细折好投进邮筒。母亲的回信总说家中安好，你却把每个字都读了两遍。", failFeedback: "", successEffect: { wealth: 3, happiness: 2, rep: 5 }, failEffect: {  }, tagSuccess: "两地相安", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "花甲在望",
        title: "旧藤箱里翻出一叠泛黄的家书",
        narrative: (p, y) => "收拾屋子，旧藤箱底翻出半辈子的家书与旧照片，纸边脆得像秋叶。有人劝你把这些年的事写下来，留给儿孙；也有人说，往事多舛，提笔便是揭疤。你坐在窗前，望着收音机里正播的样板戏，久久没有落笔。",
        choices: [
          { text: "按年份理好旧信，一页一页写下自己这一生的来路", riskLevel: "秉笔存真 · 心绪难平 · 成功率 72%", successChance: (p) => 72 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 10 : 0), successFeedback: "字迹一行行落定，离散的人、走过的路都回来了。孙子趴桌边问东问西，你忽然觉得这一生有了交代。", failFeedback: "写到战乱那几年，笔顿住了，夜里连做几场旧梦。稿纸只写了半册，你把它收好，说再缓缓罢。", successEffect: { intellect: 4, happiness: 8, rep: 5 }, failEffect: { health: -6, happiness: -7 }, tagSuccess: "落纸存心", tagFail: "旧事难提", isKey: true },
          { text: "把旧信旧照分门别类收好，只给儿孙讲些轻省的往事", riskLevel: "择善而述 · 旧物长存 · 稳妥必成", successChance: (p) => 100, successFeedback: "抽屉里多了三只纸包，分别写着年份与人名。孩子问起时，你便挑一段温热的旧事，慢慢讲给他们听。", failFeedback: "", successEffect: { intellect: 2, happiness: 5 }, failEffect: {  }, tagSuccess: "旧物有温", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "桑榆晚景",
        title: "登门寻访三十年未见的老同事",
        narrative: (p, y) => "老同事的消息终于问到了，住在城西旧楼的三层。你换上洗得发白的中山装，揣着两斤点心出门。有人劝你这把年纪别再奔波，也有人说起当年那场争执，怕见面更难堪。公共汽车摇晃着，你一时不知该不该去。",
        choices: [
          { text: "提着点心登门，把当年的话当面说开", riskLevel: "旧怨冰释 · 来路已远 · 成功率 70%", successChance: (p) => 70 + (p.luck > 50 ? 10 : 0) + (p.health > 60 ? 8 : 0), successFeedback: "两位老人在藤椅上坐了半日，从食堂的菜价说到当年的误会，末了都笑了。回来的路上，你脚步轻了许多。", failFeedback: "门开了，话却始终没有说到那一层。临走他送你到楼梯口，你回头看见他扶着栏杆，也没有再说什么。", successEffect: { health: 3, happiness: 9, rep: 5 }, failEffect: { health: -5, happiness: -7 }, tagSuccess: "一笑泯恩", tagFail: "话到嘴边", isKey: true },
          { text: "只托人捎口信问候，不打扰他晚年的清净", riskLevel: "遥寄平安 · 各守余年 · 稳妥必成", successChance: (p) => 100, successFeedback: "口信捎去半月，回话只有一句：他身子还好，也惦记你。你把这句话在心里放了许多天，像收好一件旧物。", failFeedback: "", successEffect: { happiness: 4, rep: 3 }, failEffect: {  }, tagSuccess: "遥遥相念", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "桑榆晚景",
        title: "雪夜陪着返城的儿子商议工作去处",
        narrative: (p, y) => "知青返城的文件下来了，儿子背着铺盖卷回家，户口与工作还悬着。街道办说名额有限，单位食堂正缺个帮工，也有人劝他去南方碰运气。屋外飘雪，老伴把炉子添旺。你握着那只搪瓷缸，一时难下决断。",
        choices: [
          { text: "拿出大半积蓄走动门路，替儿子谋一个稳妥的去处", riskLevel: "倾囊铺路 · 成败难料 · 成功率 62%", successChance: (p) => 62 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 10 : 0), successFeedback: "开春时儿子进了厂，学徒工的名牌压在胸前。他领到第一份工资，给你买了一包好烟，你却舍不得抽。", failFeedback: "钱花了，事没成，儿子只好先去食堂帮工。他并不怨你，只是你夜里听见他翻身，心里像压了块冷铁。", successEffect: { wealth: -8, happiness: 8, rep: 6 }, failEffect: { health: -4, wealth: -10, happiness: -6 }, tagSuccess: "父荫成事", tagFail: "钱财两空", isKey: true },
          { text: "让他自个儿去街道办排队苦等，路要自己走出来", riskLevel: "放手自立 · 前路维艰 · 稳妥必成", successChance: (p) => 100, successFeedback: "儿子天不亮就去排队，回来时鞋上全是雪泥。几个月后他自有去处，虽不体面，却站得直。你看着他，没有说话。", failFeedback: "", successEffect: { wealth: 2, happiness: 4, rep: 4 }, failEffect: {  }, tagSuccess: "自立成人", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "古稀沧桑",
        title: "平反的通知送到胡同老院门口",
        narrative: (p, y) => "街道的同志敲开院门，递来一纸落实政策的通知，说要为你当年的事恢复名誉，还补发一笔钱。消息传得很快，街坊都来道喜。你却想起那些年月里不敢来往的故人，提起笔，不知先去告诉谁。",
        choices: [
          { text: "把补发的钱分送几户当年受牵连的旧邻，再登门谢过他们", riskLevel: "推己及人 · 人心难量 · 成功率 74%", successChance: (p) => 74 + (p.luck > 50 ? 10 : 0) + (p.health > 60 ? 8 : 0), successFeedback: "有人推辞，有人红了眼眶，末了都收下了。胡同里过了几天热闹日子，你走在其中，觉得腰杆终于是直的。", failFeedback: "有两户闭门不见，说旧账不必再提。你把钱留下，独自走回院中，明白有些亏欠，一辈子也还不完。", successEffect: { wealth: -6, happiness: 8, rep: 9 }, failEffect: { wealth: -6, happiness: -5, rep: 2 }, tagSuccess: "尘埃落定", tagFail: "旧债难偿", isKey: true },
          { text: "把钱存进工资折，只去坟前静静坐一坐", riskLevel: "沉默谢幕 · 各安其位 · 稳妥必成", successChance: (p) => 100, successFeedback: "你在坟前坐了很久，把通知的内容一句一句念给他听。回来时把存折压回抽屉，日子仍是原来的日子。", failFeedback: "", successEffect: { wealth: 5, happiness: 5, rep: 2 }, failEffect: {  }, tagSuccess: "静水流深", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "古稀沧桑",
        title: "把攒了半辈子的存折摊在灯下",
        narrative: (p, y) => "夜里你把几张存折与票证摊在桌上，那是给儿孙攒下的那点家底。小儿子想借钱换一台缝纫机，说能挣些活钱；女儿却说，不如留着给你看病养老。灯光昏黄，老伴坐在一旁，等你拿主意。",
        choices: [
          { text: "匀出一半给儿子添置缝纫机，剩下的封存备医", riskLevel: "慈心难断 · 两头兼顾 · 成功率 70%", successChance: (p) => 70 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 10 : 0), successFeedback: "缝纫机抬进门那天，全家围看。儿媳接的活儿渐渐多了，逢年过节总给你捎来新做的棉袄，针脚细密。", failFeedback: "活儿没接着几单，机器在墙角落了灰。你嘴上说不要紧，心里却盘算着往后的药钱，从此更省了些。", successEffect: { wealth: 4, happiness: 8, rep: 4 }, failEffect: { wealth: -8, happiness: -5 }, tagSuccess: "家底生暖", tagFail: "机杼蒙尘", isKey: true },
          { text: "一文不动，明明白白告诉儿女这份钱只作养老送终之用", riskLevel: "守本自持 · 亲情有隙 · 稳妥必成", successChance: (p) => 100, successFeedback: "你把话说明白了，儿女都点头。往后看病抓药不必向谁开口，你夜里睡得安稳，只是家里少了几分热闹。", failFeedback: "", successEffect: { health: 3, wealth: 3, happiness: -2 }, failEffect: {  }, tagSuccess: "自有分寸", tagFail: "另寻他途", isKey: false }
        ]
      }
      ],
      [
      {
        period: "夕阳辞章",
        title: "儿孙守候床前听你交代最后几句",
        narrative: (p, y) => "入了冬，你躺在床上，气力一日不如一日。儿女轮班守着，药炉在墙角温着，收音机开得很轻。你让孙子把那只旧藤箱搬来，想最后说几句话，也想再看看那些泛黄的家书与照片。",
        choices: [
          { text: "把旧信旧照一封封分给儿孙，交代完身后事，安然合眼", riskLevel: "交代清楚 · 魂归平和 · 成功率 76%", successChance: (p) => 76 + (p.luck > 50 ? 10 : 0) + (p.health > 60 ? 8 : 0), successFeedback: "信件分完，你一一唤过他们的名字，说各自珍重。屋外落着细雪，你握着老伴的手，慢慢合上眼，神色安然。", failFeedback: "话未说完，气已不继，只攥着那张全家福。儿孙都懂了你的意思，低声应着，陪你坐到天亮。", successEffect: { happiness: 12, rep: 8 }, failEffect: { health: -6, happiness: -4 }, tagSuccess: "含笑长眠", tagFail: "未尽之言", isKey: true },
          { text: "让儿孙把窗帘拉开，看着院子里那株老树，静静等天黑", riskLevel: "无言以对 · 各自安宁 · 稳妥必成", successChance: (p) => 100, successFeedback: "光从窗棂上一点点退去，儿孙都在屋里。你望着老树的枝影，呼吸渐渐轻了，像忙完一天的人终于歇下。", failFeedback: "", successEffect: { happiness: 10, rep: 6 }, failEffect: {  }, tagSuccess: "安然谢幕", tagFail: "另寻他途", isKey: false }
        ]
      },
      {
        period: "夕阳辞章",
        title: "藤椅上手握全家福看最后一次夕阳",
        narrative: (p, y) => "你执意要从床上起来，坐到老屋那张藤椅里去。儿孙把毯子搭在你膝上，又端来一碗温水。夕阳斜过屋脊，照片里的年轻人早已不在，膝下的孩子却都长成了。你慢慢握紧了那张全家福。",
        choices: [
          { text: "留下话把一生的积蓄捐给村小学，再回故里老屋住到最后", riskLevel: "散尽家财 · 落叶归根 · 成功率 72%", successChance: (p) => 72 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 10 : 0), successFeedback: "你回老屋住了半月，每日看村里孩子背着书包经过。课本是新的，木窗是旧的。一个午后，你在藤椅上睡着了，没有再醒。", failFeedback: "钱捐了出去，身子却没能撑回故里。你在城里的屋中走完最后一程，望着窗外的树梢，也算安静。", successEffect: { wealth: -12, happiness: 10, rep: 12 }, failEffect: { health: -6, happiness: 2, rep: 8 }, tagSuccess: "夕阳辞章", tagFail: "归途未竟", isKey: true },
          { text: "哪儿也不去，就守着这间老屋与家人，把手边的事放下", riskLevel: "守屋待终 · 灯火可亲 · 稳妥必成", successChance: (p) => 100, successFeedback: "你把全家福贴在心口，听着屋里锅碗的动静与孩子的笑闹。夕阳沉下去时，你仍旧坐着，像是看着一家人慢慢长大。", failFeedback: "", successEffect: { happiness: 11, rep: 5 }, failEffect: {  }, tagSuccess: "灯火长明", tagFail: "另寻他途", isKey: false }
        ]
      }
      ]
    ];

    // ---- 出身表 / 事件池 按纪元统一取用 ----
    function getEpochOriginTables(id) {
      if (id === "ancient") return { regions: ANCIENT_REGIONS, strata: ANCIENT_SOCIAL_STRATA };
      if (id === "premodern") return { regions: PREMODERN_REGIONS, strata: PREMODERN_SOCIAL_STRATA };
      if (id === "modern") return { regions: MODERN_REGIONS, strata: MODERN_SOCIAL_STRATA };
      if (id === "contemporary") return { regions: PAST_REGIONS, strata: PAST_SOCIAL_STRATA };
      return { regions: FUTURE_REGIONS, strata: FUTURE_SOCIAL_STRATA };
    }
    function getEpochStagePools(id) {
      if (id === "ancient") return ANCIENT_STAGE_POOLS;
      if (id === "premodern") return PREMODERN_STAGE_POOLS;
      if (id === "modern") return MODERN_STAGE_POOLS;
      if (id === "contemporary") return PAST_STAGE_POOLS;
      return FUTURE_STAGE_POOLS;
    }


// 各纪元货币单位：避免先秦人生出现「万元」这类时代错位
function wealthUnit(epochId) {
  if (epochId === "ancient") return "两金";
  if (epochId === "premodern") return "两银";
  if (epochId === "modern") return "块银元";
  if (epochId === "contemporary") return "万元";
  return "信用点";
}

function wealthUnitShort(epochId) {
  if (epochId === "ancient") return "两";
  if (epochId === "premodern") return "两";
  if (epochId === "modern") return "元";
  if (epochId === "contemporary") return "万";
  return "点";
}


    // ==================== 女性专属处境事件（主角为女性时进入该阶段候选池） ====================
    const WOMEN_EVENT_POOLS = {
      "ancient": {
        2: [
      {
        period: "少年分流",
        title: "机杼声中偷听邻塾诵诗",
        narrative: (p, y) => "母亲在堂屋织缣，你坐机前续麻，隔壁塾中传来童子诵《诗》之声。父亲说女儿家识得几个字便够，学得一手好织，才是他日出嫁的体面妆奁。塾师却隔着篱笆问你，可愿每日来抄半卷书。梭子在你手中一顿。",
        choices: [
          { text: "白日续麻织缣，夜里就一盏油灯借简抄书", riskLevel: "偷光识字 · 心志渐明 · 成功率 62%", successChance: (p) => 62 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "塾师见你字迹端正，许你每旬借一卷竹简，母亲虽唠叨，却把灯油多添了一勺。", failFeedback: "灯下久坐，天未亮便被唤去上机，手指发颤断了经线，被母亲罚跪织室半日。", successEffect: { intellect: 10, happiness: 4 }, failEffect: { health: -4, intellect: 4, happiness: -5 }, tagSuccess: "偷光识字", tagFail: "断经受罚", isKey: true },
          { text: "收了心思，把一匹绢织得经纬匀密，做母亲的帮手", riskLevel: "坐守机杼 · 女红渐精 · 稳妥必成", successChance: (p) => 100, successFeedback: "那匹绢素净如霜，母亲拿在手里反复摩挲，说你已织得出嫁时压箱底的锦。", failFeedback: "", successEffect: { health: 3, wealth: 3, happiness: 5 }, failEffect: {  }, tagSuccess: "女红初成", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        3: [
      {
        period: "成人立志",
        title: "及笄绾发，医门与媒妁并至",
        narrative: (p, y) => "你刚行过及笄礼，母亲为你绾发插笄。里中老医妪登门，说她年逾花甲，一身切脉施针的本事无人可传，愿收你为徒。同月媒人也踏破门槛，说城东某户愿以三牲六礼相聘。铜笄映着烛火，两条路都摆在眼前。",
        choices: [
          { text: "婉辞媒妁，负箧随老医妪认药施针，学一门立身本事", riskLevel: "弃嫁从医 · 立身有术 · 成功率 58%", successChance: (p) => 58 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "三年后你能独诊妇科诸疾，乡里妇人夜半叩门求医，你背着药囊出诊，身后递来一盏灯。", failFeedback: "乡人以女子行医为怪，寻医者寥寥，你只得替人接生、代煎汤药，勉强度日。", successEffect: { wealth: 2, intellect: 12, rep: 8 }, failEffect: { intellect: 6, happiness: -5, rep: -4 }, tagSuccess: "悬壶立身", tagFail: "见疑乡里", isKey: true },
          { text: "依父母之命受聘定亲，备办妆奁，安稳待嫁", riskLevel: "顺亲守礼 · 安稳有靠 · 稳妥必成", successChance: (p) => 100, successFeedback: "亲事议定，两家长辈往来如礼，母亲替你收好嫁衣，说这门亲事门当户对，你心下稍安。", failFeedback: "", successEffect: { wealth: 3, happiness: 4, rep: 6 }, failEffect: {  }, tagSuccess: "六礼既定", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        4: [
      {
        period: "青春韶华",
        title: "妆奁底层压着一册手抄账簿",
        narrative: (p, y) => "出阁那日，母亲在妆奁底层压了一册手抄账簿与一柄铜尺，说掌家先要识数。夫家在西市开一间绢帛铺，婆婆久病卧床，夫君常随商队走丝路。铺面钥匙挂在门后，婆婆的汤药也在灶上温着，你须先择一头。",
        choices: [
          { text: "取下钥匙坐柜台，逐匹清点绢帛出入，学做坊市营生", riskLevel: "抛头露面 · 掌铺理事 · 成功率 64%", successChance: (p) => 64 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "你分得清胡商压价的伎俩，一季下来账面盈余，铺中伙计改口称你一声东家娘子。", failFeedback: "市井牙人欺你年轻妇道，以次充好骗去两匹上绢，婆婆闻讯在病榻上叹气。", successEffect: { wealth: 8, intellect: 6, rep: 5 }, failEffect: { wealth: -6, happiness: -6, rep: -3 }, tagSuccess: "柜台立信", tagFail: "初出受欺", isKey: true },
          { text: "闭门侍奉婆婆汤药，把内闱诸事料理得齐齐整整", riskLevel: "侍疾守内 · 恭谨无失 · 稳妥必成", successChance: (p) => 100, successFeedback: "婆婆病中握你的手，把腕上一只银镯褪下给你，说这个家往后有你，她放心。", failFeedback: "", successEffect: { health: 2, happiness: 5, rep: 8 }, failEffect: {  }, tagSuccess: "内闱称贤", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        5: [
      {
        period: "初涉人世",
        title: "产褥未起，账房已候在床边",
        narrative: (p, y) => "你产后十日，尚在褥中，婆婆便催你起身理事，说家中米缸见底，佃户租粮未齐。夫君在外未归，书信也无。乳母劝你歇息养身，账房婆子却捧着旧账簿立在床边，只等你一句话。窗外新妇的婴儿正哭。",
        choices: [
          { text: "强撑起身，就着灯核账，遣人去佃户门上催租", riskLevel: "忍身理事 · 撑持门户 · 成功率 60%", successChance: (p) => 60 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.health > 60 ? 2 : 0), successFeedback: "你查出账房私吞两石粟，当场换了人，佃户也补缴了新粮，米缸终于见了底下的新米。", failFeedback: "你冒风出门催租，落下畏寒的病根，往后阴雨天便觉腰膝酸软，账也没催齐。", successEffect: { wealth: 5, intellect: 5, rep: 6 }, failEffect: { health: -10, happiness: -5 }, tagSuccess: "撑持门户", tagFail: "落病催租", isKey: true },
          { text: "闭门养息满月，将家事暂托婆婆与乳母照看", riskLevel: "安身养息 · 蓄力待时 · 稳妥必成", successChance: (p) => 100, successFeedback: "满月后你气色转好，乳汁也足，婴儿白白胖胖，乳母笑说娘子这一个月没白躺。", failFeedback: "", successEffect: { health: 10, happiness: 6 }, failEffect: {  }, tagSuccess: "养息蓄力", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        6: [
      {
        period: "成家立业",
        title: "三更机杼声里的织造字号",
        narrative: (p, y) => "你织的锦在市中被胡商认作字号，一冬可换十数贯钱。夫君想添机雇工，把织坊做大，你却怕官家织室抽税、又怕荒了儿子的功课。灯下机杼未歇，儿子捧着《论语》立在机旁，等你听他背完这一章。",
        choices: [
          { text: "添置织机，雇几名织娘，自立一处织造字号", riskLevel: "扩机营商 · 与夫并立 · 成功率 63%", successChance: (p) => 63 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "你的锦在坊市挂了名号，凉州胡商先付定金再来取货，家中仓房堆满了待染的生丝。", failFeedback: "官家织室摊派急织，织娘昼夜赶工仍误了期限，赔了工钱，还落下苛待之名。", successEffect: { wealth: 12, intellect: 4, rep: 6 }, failEffect: { health: -5, wealth: -8, happiness: -6 }, tagSuccess: "织造立业", tagFail: "摊派折本", isKey: true },
          { text: "收敛机坊，亲自陪儿子读经，把指望放在他的前程上", riskLevel: "督子读书 · 静守本分 · 稳妥必成", successChance: (p) => 100, successFeedback: "儿子开卷能诵，塾师夸他聪敏，你在一旁补缀他的衣角，心里比织出锦还熨帖。", failFeedback: "", successEffect: { intellect: 8, happiness: 8, rep: 3 }, failEffect: {  }, tagSuccess: "课子有成", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        7: [
      {
        period: "三十而立",
        title: "夫君书信断在玉门关外",
        narrative: (p, y) => "夫君随商队远赴凉州，去岁书信只到玉门便断。族中叔伯觊觎你家田产，说妇人不可为户主，要代管田契。县衙的均田文书上，尚缺一个当家人的画押。儿女尚幼，都仰头望着你，等你拿主意。",
        choices: [
          { text: "携田契亲赴县衙，依律自请为户主，把田亩一注明白", riskLevel: "对簿公堂 · 独当门户 · 成功率 55%", successChance: (p) => 55 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "县吏验过契书，文书上写了你的名字，叔伯们拂袖而去，你抱着田契走出衙门，日头正好。", failFeedback: "县吏含糊推诿，说妇人立户须有族中保结，叔伯扣着不画押，田契终究没能落定。", successEffect: { wealth: 6, intellect: 6, rep: 10 }, failEffect: { wealth: -4, happiness: -8, rep: -5 }, tagSuccess: "自立门户", tagFail: "为吏所阻", isKey: true },
          { text: "请族中长辈代管田产，只求母子安稳，少生争端", riskLevel: "托付族亲 · 退让求安 · 稳妥必成", successChance: (p) => 100, successFeedback: "叔伯代管田租，年年按时送来口粮，虽比往年少些，母子几人总算衣食无缺。", failFeedback: "", successEffect: { wealth: 2, happiness: 5, rep: 2 }, failEffect: {  }, tagSuccess: "退让求安", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        9: [
      {
        period: "中年险滩",
        title: "素衣未除，族人已议分产",
        narrative: (p, y) => "夫君病故，灵前素衣未除，族中已有人上门议分家产，说寡母难守，不如过继一子承嗣，田宅另作处置。也有旧识托媒来问，愿娶你为继室，带你与儿女离开此地另寻安身。儿子的手一直攥着你的衣角。",
        choices: [
          { text: "立志守节抚孤，把田契铺账一一执定，不使家业外流", riskLevel: "守节抚孤 · 执契护产 · 成功率 58%", successChance: (p) => 58 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "你请里正为证，把田宅写在自己与儿子名下，族人无话可说，儿子在你膝下安心读起了书。", failFeedback: "族中以承嗣为由强分了两顷水田，你独力难争，夜里对着灵位坐了很久。", successEffect: { intellect: 6, happiness: 4, rep: 10 }, failEffect: { wealth: -10, happiness: -10, rep: -4 }, tagSuccess: "执契守家", tagFail: "寡母受欺", isKey: true },
          { text: "允了再嫁，携儿女随新夫迁居，另立一处门户", riskLevel: "再醮远去 · 另寻生路 · 稳妥必成", successChance: (p) => 100, successFeedback: "新夫待儿女不薄，你换了居处，重新支起织机，旧日的邻人只在梦里出现。", failFeedback: "", successEffect: { health: 4, happiness: 8, rep: -5 }, failEffect: {  }, tagSuccess: "再醮安身", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        12: [
      {
        period: "花甲在望",
        title: "白发主母灯前口授家训",
        narrative: (p, y) => "你已是一家长辈，儿孙绕膝，孙女的婚事、儿媳的织坊都来请你定夺。案上那卷家训只写到一半，墨已研好。窗外孙女的机杼声断续传来。是趁天色尚明把织造诀窍与家训一并传下，还是先把田契铺账核清，替儿孙留下明白家底？",
        choices: [
          { text: "召集儿媳孙女于灯前，把织艺与家训一条条口授下去", riskLevel: "传艺立训 · 家风有继 · 成功率 70%", successChance: (p) => 70 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "儿媳记下家训，孙女学会挑经断纬的诀窍，那卷家训抄成两份，一份压在机下，一份供在堂前。", failFeedback: "孙女嫌织造劳苦，学了半月便放下梭子，你只得把诀窍写进家训，盼后人再拾起来。", successEffect: { intellect: 8, happiness: 6, rep: 10 }, failEffect: { intellect: 4, happiness: -5, rep: 3 }, tagSuccess: "传艺立训", tagFail: "后人不继", isKey: true },
          { text: "闭门把田契铺账逐一核清，写成一本明白账簿留给儿孙", riskLevel: "核产留账 · 家底分明 · 稳妥必成", successChance: (p) => 100, successFeedback: "账目一注明白，哪处田、哪间铺、欠何人多少，儿孙翻看便知，无人再敢含糊。", failFeedback: "", successEffect: { wealth: 6, intellect: 6, rep: 5 }, failEffect: {  }, tagSuccess: "账目分明", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
      },
      "premodern": {
        2: [
      {
        period: "少年分流",
        title: "绣绷与账本同摆在灯下",
        narrative: (p, y) => "你十四岁，家在县前开着间茶铺，父亲赊欠簿上的数总对不齐。母亲把一方绣绷浆好递来，说女儿家针线是立身的本分；父亲却把你的算盘拨得噼啪响，让你替他誊清欠户名录。窗外汴河夜船摇过，母亲的呼吸就在耳后。",
        choices: [
          { text: "白日随母亲学挑绣，夜里就灯替父亲誊写赊欠簿", riskLevel: "灯下掌算 · 心志渐明 · 成功率 66%", successChance: (p) => 66 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "半年后你能报出各户欠账，父亲把茶铺流水交你经手，说女娃的算盘也拨得响。", failFeedback: "你错记一笔赊账，赔了几句闲话，却由此懂得了银钱的轻重，账本再没离过手。", successEffect: { wealth: 5, intellect: 10, rep: 4 }, failEffect: { wealth: -3, intellect: 6, happiness: -5 }, tagSuccess: "掌算立身", tagFail: "误记账目", isKey: true },
          { text: "收了算盘，随母亲一针一线学绣，闲时只翻两页账本", riskLevel: "坐守绣绷 · 女红渐精 · 稳妥必成", successChance: (p) => 100, successFeedback: "你的针脚平整，一方帕子换了半升米，夜里照旧把账本上的字认全，母亲看你时眼里有光。", failFeedback: "", successEffect: { wealth: 4, intellect: 3, happiness: 6 }, failEffect: {  }, tagSuccess: "女红初成", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        3: [
      {
        period: "成人立志",
        title: "媒人踏破门槛，绣坊也在等你回话",
        narrative: (p, y) => "你十八岁，媒婆第三回上门，说的是绸缎铺少东家，聘礼不薄。你却在瓦舍见过一位女医当街诊脉，也在绣坊见绣娘自己养家。母亲说嫁人最稳当，父亲放下茶碗，只问你一句：你自己拿什么主意？檐下燕子正衔泥。",
        choices: [
          { text: "婉辞这门亲事，投绣坊拜师，从劈线描样学起，自己挣口饭食", riskLevel: "弃嫁从艺 · 立身有术 · 成功率 58%", successChance: (p) => 58 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "三年后你绣的百子帐被绸缎庄高价收走，绣坊留你作师傅，媒人再来时，你已能自己开口。", failFeedback: "你手慢赶不出工期，被扣了工钱，只得回家；可那一双描样的好眼力，从此再没还给谁。", successEffect: { wealth: 9, intellect: 10, rep: 8 }, failEffect: { wealth: -4, intellect: 5, happiness: -6 }, tagSuccess: "绣坊立身", tagFail: "失工存艺", isKey: true },
          { text: "依父母之命受聘定亲，安心备办嫁妆，学管家认亲戚", riskLevel: "顺亲守礼 · 安稳有靠 · 稳妥必成", successChance: (p) => 100, successFeedback: "六礼按序走完，你随母亲学掌中馈、认族中亲眷，出嫁那日妆奁齐整，心里并不慌。", failFeedback: "", successEffect: { wealth: 5, happiness: 5, rep: 6 }, failEffect: {  }, tagSuccess: "六礼既定", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        4: [
      {
        period: "青春韶华",
        title: "花轿三日，婆婆递来一串铜钥匙",
        narrative: (p, y) => "你二十岁，过门第三日，婆婆把一串黄铜钥匙放进你手心，说米缸、酱缸、后院的鸡鸭从此归你。丈夫常随漕船走货，一年在家不足两月。族中妯娌都拿眼盯着你，这串钥匙能开米柜，也能开临街那间空铺面。",
        choices: [
          { text: "接下钥匙，先清米盐账目，再把临街铺面收拾出来做点营生", riskLevel: "抛头露面 · 掌铺理事 · 成功率 64%", successChance: (p) => 64 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "你把铺面盘成针线布头小铺，进出账目清楚，婆婆在外人前头一回夸你，妯娌也收了口。", failFeedback: "头一季进货看走了眼，压了半柜子货，你赔上压箱底的嫁资，却认得了布行的规矩。", successEffect: { wealth: 12, intellect: 6, rep: 6 }, failEffect: { wealth: -7, intellect: 6, happiness: -6 }, tagSuccess: "柜台立信", tagFail: "初出受欺", isKey: true },
          { text: "只管家中中馈，节俭度日，凡事请婆婆示下", riskLevel: "侍疾守内 · 恭谨无失 · 稳妥必成", successChance: (p) => 100, successFeedback: "你把一家吃穿用度料理得齐齐整整，婆媳相安，日子虽无大进项，也没叫人挑出错处。", failFeedback: "", successEffect: { wealth: 3, happiness: 7, rep: 6 }, failEffect: {  }, tagSuccess: "中馈无失", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        5: [
      {
        period: "初涉人世",
        title: "产房添丁，账上却添一笔亏空",
        narrative: (p, y) => "你二十四岁，头胎生了个女儿。婆婆脸色淡了三分，说下一胎再求儿子，转身把雇乳母的钱压下。你自己奶孩子，夜里睡不足，白日还得盯着灶头与铺面。丈夫捎信回来说外头周转不开，问你嫁妆里的银镯能否先当出去。",
        choices: [
          { text: "当掉银镯救急，自己哺乳兼管账，把铺面典期往后延一延", riskLevel: "忍身理事 · 撑持门户 · 成功率 60%", successChance: (p) => 60 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.health > 60 ? 2 : 0), successFeedback: "开春生意回暖，丈夫赎回镯子还添了一对，婆婆见你撑得住家，待你与女儿都亲厚了。", failFeedback: "你熬得气血两亏，孩子也跟着病了一场，铺面终究典了出去；可这家离了你也转不动。", successEffect: { wealth: 9, happiness: 5, rep: 8 }, failEffect: { health: -8, wealth: -9, happiness: -6 }, tagSuccess: "撑持门户", tagFail: "熬损识家", isKey: true },
          { text: "辞了铺面，专心育儿侍奉婆婆，银镯原封不动留着", riskLevel: "安身养息 · 蓄力待时 · 稳妥必成", successChance: (p) => 100, successFeedback: "家中吃用紧了些，你却把孩子与婆婆都照料妥帖，丈夫归家见家宅安稳，心里感念。", failFeedback: "", successEffect: { health: 5, happiness: 8, rep: 4 }, failEffect: {  }, tagSuccess: "养息蓄力", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        6: [
      {
        period: "成家立业",
        title: "旧绣坊待盘，你在巷口挂招牌",
        narrative: (p, y) => "你二十八岁，攒下一笔银钱。原先雇你的绣坊要盘出去，老师傅劝你接手，说有几位旧姊妹肯跟来帮工。可接手要押金，还得请牙行作保、给里正递帖子。丈夫说风险太大，不如把钱留着给儿子将来读书赴考。",
        choices: [
          { text: "接下绣坊，招旧姊妹帮工，自己描样验货、跑绸缎庄接单", riskLevel: "自立字号 · 担险兴业 · 成功率 56%", successChance: (p) => 56 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 4 : 0), successFeedback: "你的绣坊接上绸缎庄的常年活计，四季有单，几位绣娘跟着你吃饭，里正也肯为你作保。", failFeedback: "一单大活被牙行压价，你贴了工钱，绣坊勉强撑着；但你的针法与名号进了城里人的口。", successEffect: { wealth: 20, intellect: 6, rep: 12 }, failEffect: { wealth: -12, happiness: -7, rep: 5 }, tagSuccess: "招牌立起", tagFail: "赔工留名", isKey: true },
          { text: "不接绣坊，在家设灯课子，教儿子与邻童识字", riskLevel: "督子读书 · 静守本分 · 稳妥必成", successChance: (p) => 100, successFeedback: "你白日做针线，夜里教儿子读《千字文》，邻家也送孩子来，束脩虽薄，母子灯下相伴却安稳。", failFeedback: "", successEffect: { intellect: 8, happiness: 6, rep: 6 }, failEffect: {  }, tagSuccess: "课子灯前", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        7: [
      {
        period: "三十而立",
        title: "夫行两年无音信，族中议你田产",
        narrative: (p, y) => "你三十二岁，丈夫随商队北上贩丝，两年没有音信。族中叔伯说妇道人家管不了田产铺面，劝你把陪嫁的三十亩水田并给长房代管，年底分你几石租米。田契就压在妆匣底下，儿子在灯下描红，尚不知家中风波。",
        choices: [
          { text: "不交田契，自己下乡对租续约，请里正与老账房当面作证", riskLevel: "下乡对租 · 独当门户 · 成功率 56%", successChance: (p) => 56 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 4 : 0), successFeedback: "你带着老账房挨户对租，佃户见你清楚明白都肯认你，族叔没了话，你头一回上了族中议事的席。", failFeedback: "族中拦你在祠堂外，几亩租米仍被长房代收；你把契纸贴身收好，等一个说法，也等一个人。", successEffect: { wealth: 16, intellect: 6, rep: 10 }, failEffect: { wealth: -9, happiness: -8, rep: 4 }, tagSuccess: "契纸在手", tagFail: "忍待时机", isKey: true },
          { text: "让长房代管田产，自己带孩子在城中支个茶摊糊口", riskLevel: "托付族亲 · 退让求安 · 稳妥必成", successChance: (p) => 100, successFeedback: "茶摊生意虽小，你与孩子衣食有着，族中也不再为难你，只当你是不争的人。", failFeedback: "", successEffect: { wealth: 5, happiness: 6, rep: 3 }, failEffect: {  }, tagSuccess: "退守自养", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        9: [
      {
        period: "中年险滩",
        title: "灵幡未撤，族伯已上门算产",
        narrative: (p, y) => "你四十岁，丈夫病故，棺木刚下葬。族伯带着中人上门，说你无子承嗣，铺面宅子该归族中，只给你一间偏屋养老。你膝下有个十四岁的女儿，另有过继来的六岁侄儿。夜里你翻出房契与丈夫留下的欠条，油灯一直亮到天明。",
        choices: [
          { text: "抱过继子去县衙立契，请讼师写文书，把房产记在嗣子名下", riskLevel: "争产抗族 · 立契保家 · 成功率 50%", successChance: (p) => 50 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 6 : 0), successFeedback: "县衙批了文书，房产归嗣子，你以主母身份代管到他成人，族伯当众下不来台，门户却立住了。", failFeedback: "讼师收了钱不肯尽力，族伯又买通中人，你只保住半间铺面；从那日起，你认得了官文书的轻重。", successEffect: { wealth: 14, intellect: 8, rep: 12 }, failEffect: { wealth: -10, intellect: 6, happiness: -9 }, tagSuccess: "立契保产", tagFail: "失产知律", isKey: true },
          { text: "立志守节不再嫁，闭门纺绩教女，把家事让出一半求安稳", riskLevel: "守节抚孤 · 退让求安 · 稳妥必成", successChance: (p) => 100, successFeedback: "你不与人争，闭门纺绩，女儿学得一手好针线；族中见你安分，不再步步紧逼，家业到底薄了些。", failFeedback: "", successEffect: { health: 3, wealth: -3, happiness: 5, rep: 8 }, failEffect: {  }, tagSuccess: "纺绩守门", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        12: [
      {
        period: "花甲在望",
        title: "五十八岁，族中请你主祭修谱",
        narrative: (p, y) => "你五十八岁，儿子已成家，铺面交媳妇打理。族中重修族谱，请你坐堂，说你一生守住了门户，又带出几房人手艺。修谱先生搁笔问：媳妇名讳、孙女名讳要不要上谱？你手边针线篓里，压着一本记了三十年的家训旧稿。",
        choices: [
          { text: "口述掌家心得，把持家账目针法写入家训，请先生把媳女名讳一并上谱", riskLevel: "传艺立训 · 家风有继 · 成功率 66%", successChance: (p) => 66 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "家训写成三十二条，媳妇与孙女的名讳赫然在谱；你教孙女描样记账，说女子手中既要有针，也要有算盘。", failFeedback: "先生摇头说妇人之言不宜入谱，族人议论纷纷，你只把家训抄在自家账本背页；可那句话已教进孙女心里。", successEffect: { intellect: 8, happiness: 8, rep: 14 }, failEffect: { intellect: 6, happiness: -6, rep: 3 }, tagSuccess: "家训入谱", tagFail: "私录传心", isKey: true },
          { text: "谢过族中，只把绣法与账本私下传给媳妇孙女，不争谱上一笔", riskLevel: "传艺于内 · 不争虚名 · 稳妥必成", successChance: (p) => 100, successFeedback: "媳妇的针脚越来越像你，孙女的算盘也拨得清脆，你坐在檐下看她们，觉得有些东西不必写在纸上。", failFeedback: "", successEffect: { intellect: 4, happiness: 10, rep: 6 }, failEffect: {  }, tagSuccess: "檐下传艺", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
      },
      "modern": {
        2: [
      {
        period: "少年分流",
        title: "缠脚布解开的那一日",
        narrative: (p, y) => "民国六年，镇上的女学堂挂出新匾，先生挨家劝女孩放脚剪发。母亲把缠脚布藏在箱底，说缠过的脚才嫁得出去。你十四岁了，能自己走三里土路去报名。",
        choices: [
          { text: "当着母亲解开缠脚布，剪去发辫，去女学堂报名识字", riskLevel: "众叛亲离 · 前程未卜 · 成功率 65%", successChance: (p) => 65 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "先生给你一支铅笔，你在糙纸上写下自己的名字。放学路上脚还疼，可步子第一次由你自己迈。", failFeedback: "母亲把你锁在灶房三天，字没认成几个。可缠脚布被你烧了，那双脚再没裹回去。", successEffect: { intellect: 12, rep: 4 }, failEffect: { intellect: 4, happiness: -6 }, tagSuccess: "开蒙识字", tagFail: "骨气未折", isKey: true },
          { text: "托城里亲戚进纱厂当童工，按月把铜板交回家里", riskLevel: "任劳任怨 · 自食其力 · 稳妥必成", successChance: (p) => 100, successFeedback: "你成了车间里最小的一个，日日站十二个钟头，月底把工钱攥出汗交给母亲。手粗了，米缸满了。", failFeedback: "", successEffect: { health: -5, wealth: 9, happiness: -3 }, failEffect: {  }, tagSuccess: "自食其力", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        3: [
      {
        period: "成人立志",
        title: "师范榜下，有人相看",
        narrative: (p, y) => "县里女子师范贴出招生榜，不收学费还管膳宿，毕业能当教员。夜里媒人上门，说城南米行东家看中你，定了亲便不愁吃穿。母亲把两人的八字压在灯下。",
        choices: [
          { text: "先偷偷去投考女子师范，考中了再向家里开口", riskLevel: "先斩后奏 · 前路未定 · 成功率 58%", successChance: (p) => 58 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "榜单上有你的名字。你抱着铺盖进校门，穿黑裙白衫，第一次听见女先生讲科学与人当自立。", failFeedback: "差了几名落榜，家里已经收下聘礼。你哭着求母亲宽限一年，答应再考，母亲到底点了头。", successEffect: { intellect: 14, happiness: 6, rep: 5 }, failEffect: { intellect: 4, happiness: -7, rep: -3 }, tagSuccess: "榜上有名", tagFail: "一年之约", isKey: true },
          { text: "由着家里定下亲事，把聘礼省下来供弟弟念书", riskLevel: "顺亲安分 · 各得其所 · 稳妥必成", successChance: (p) => 100, successFeedback: "红烛下你拜了堂，丈夫待你平和。夜里你把师范的招生简章折好，夹进陪嫁的箱底。", failFeedback: "", successEffect: { wealth: 10, happiness: 3, rep: 4 }, failEffect: {  }, tagSuccess: "安分持家", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        4: [
      {
        period: "青春韶华",
        title: "救护棚前的那张桌",
        narrative: (p, y) => "战事吃紧，红十字会来厂里招救护员，说上前线抬担架、缝绷带。同宿舍的秀兰报了名。母亲托人带信，叫你别去，家里正在替你说一门稳妥的亲事。",
        choices: [
          { text: "瞒着家里报名随救护队北上，学包扎、止血与抬担架", riskLevel: "生死难料 · 家书难递 · 成功率 55%", successChance: (p) => 55 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.health > 60 ? 6 : 0), successFeedback: "你在炮声里学会用盐水洗伤口，也背得动半袋米。有个伤兵叫你一声同志，你记了一辈子。", failFeedback: "路遇溃兵，队伍散了。你护送两个伤员绕回后方，瘦脱了形，却从没后悔走过这一趟。", successEffect: { health: 5, intellect: 6, rep: 12 }, failEffect: { health: -8, happiness: -4, rep: 6 }, tagSuccess: "临危受命", tagFail: "风尘仆仆", isKey: true },
          { text: "留在城里应下小学教员的差事，按月领薪养家", riskLevel: "执鞭立身 · 安分守己 · 稳妥必成", successChance: (p) => 100, successFeedback: "三十几个孩子齐声喊先生。薪米不厚，可每月发薪那天，你都能给母亲捎两块银元回去。", failFeedback: "", successEffect: { wealth: 6, intellect: 5, rep: 8 }, failEffect: {  }, tagSuccess: "执鞭立身", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        5: [
      {
        period: "初涉人世",
        title: "产假只批了四十五天",
        narrative: (p, y) => "厂里催你回车间，说细纱岗缺人；婆婆说孩子还小，女人的本分在灶台边。产假只批四十五天，厂办托儿所一个月要两块银元，你的工钱刚够三块。",
        choices: [
          { text: "把孩子送进厂办托儿所，按期回车间保住岗位", riskLevel: "骨肉牵挂 · 饭碗要紧 · 成功率 62%", successChance: (p) => 62 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "你白天挡车接线头，夜里给孩子喂奶。工段长在墙上记你满勤，工资袋上第一次印着你自己的名字。", failFeedback: "孩子夜里发烧，你请假三天，岗位被调去看仓库。工钱少了，可你守住了做母亲的那份心。", successEffect: { wealth: 8, happiness: 4, rep: 7 }, failEffect: { wealth: -5, happiness: -6, rep: -3 }, tagSuccess: "双肩挑担", tagFail: "母职难舍", isKey: true },
          { text: "夜里去工人夜校识字，跟着先生学记账与算术", riskLevel: "灯下苦读 · 日久见功 · 稳妥必成", successChance: (p) => 100, successFeedback: "一年下来你认了两千字，能自己读厂里的通知。结业那天，先生把一支钢笔插在你衣襟上。", failFeedback: "", successEffect: { intellect: 12, rep: 5 }, failEffect: {  }, tagSuccess: "勤学不辍", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        6: [
      {
        period: "成家立业",
        title: "黑板一侧写上你的名字",
        narrative: (p, y) => "建国后厂里评先进生产者，要挑人去学新式细纱机。名单上有你，可要脱产去城里学三个月。丈夫在码头扛包，两个孩子要接送，婆婆说她只认得灶火不认得机器。",
        choices: [
          { text: "报名技术培训班，脱产三个月学细纱机维修", riskLevel: "两头难顾 · 技术在手 · 成功率 60%", successChance: (p) => 60 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "结业考核你拿了第一，回厂当上技术员，工装口袋别着卡尺。机器一出毛病，女工们都来喊你。", failFeedback: "头一个月孩子病了两回，你中途退学。回车间照旧挡车，可师傅教的每一句口诀你都记着。", successEffect: { wealth: 6, intellect: 12, rep: 10 }, failEffect: { intellect: 5, happiness: -5, rep: -2 }, tagSuccess: "技压群芳", tagFail: "半途折返", isKey: true },
          { text: "和丈夫商量好，家务轮着做，孩子轮着接送", riskLevel: "夫妻同心 · 家事分摊 · 稳妥必成", successChance: (p) => 100, successFeedback: "他笨手笨脚地学擀面，孩子笑作一团。街坊有闲话，说你家男人怕老婆，可你晚上能歇歇脚了。", failFeedback: "", successEffect: { health: 4, happiness: 8, rep: 3 }, failEffect: {  }, tagSuccess: "同担家事", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        7: [
      {
        period: "三十而立",
        title: "公社广播喊你去接生",
        narrative: (p, y) => "公社要办卫生员训练班，学接生、认草药、打针。队长说你是妇女队长，最合适。可小女儿刚断奶，家里一摊事；队里记工分的旧章程又正惹人议论。",
        choices: [
          { text: "报名去县里学接生，背上药箱走遍十里八村", riskLevel: "夜路难行 · 人命关天 · 成功率 64%", successChance: (p) => 64 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "头一回接生遇上难产，你守着产妇一整夜。鸡叫时孩子落地，那家人煮了两个荷包蛋，叫你恩人。", failFeedback: "一次雪夜出诊，你滑进沟里扭了脚，药箱也摔开。可你还是爬到产妇家，只从此落了腿疼的毛病。", successEffect: { health: -3, intellect: 8, rep: 14 }, failEffect: { health: -8, happiness: -3, rep: 8 }, tagSuccess: "赤脚行医", tagFail: "雪夜失足", isKey: true },
          { text: "带头在队里争同工同酬，替妇女去评先进生产者", riskLevel: "得罪众人 · 出头招风 · 成功率 55%", successChance: (p) => 55 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "记工分的老会计改了章程，妇女干一样的活记一样的分。你的照片贴上光荣榜，写着劳动模范。", failFeedback: "有人背地里说你争强好胜，工分照旧少记两成。你没再吵，只把每天割的亩数记在小本上。", successEffect: { wealth: 6, happiness: 5, rep: 12 }, failEffect: { happiness: -6, rep: -5 }, tagSuccess: "巾帼不让", tagFail: "人言可畏", isKey: false }
        ]
      }
        ],
        9: [
      {
        period: "中年险滩",
        title: "锣鼓响时，去与留的抉择",
        narrative: (p, y) => "运动来了，有人贴出大字报，说你出身不好、又讲过技术不要讲政治。文件下来，一批人要下放干校。丈夫劝你主动报名避风头，可你刚接手车间质检，走了这道关怕没人守。",
        choices: [
          { text: "主动报名下放干校，避过风头，保全一家老小", riskLevel: "前路茫茫 · 屈身求全 · 成功率 72%", successChance: (p) => 72, successFeedback: "干校的田埂上你学会了插秧。清早收工，你还在纸上默写公差表。两年后调回城，手上的茧没白长。", failFeedback: "下放第三年丈夫病倒，你两头奔波。回城时岗位没了，被安排去仓库点数，工龄却还是连着的。", successEffect: { health: -4, intellect: 8, rep: -2 }, failEffect: { health: -8, wealth: -4, happiness: -6 }, tagSuccess: "随遇而安", tagFail: "磋磨经年", isKey: false },
          { text: "坚持留在车间守住质检岗，任凭大字报贴满墙", riskLevel: "孤立无援 · 坚守到底 · 成功率 45%", successChance: (p) => 45 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "你照旧每天量纱的支数，一笔笔记在本上。后来有人翻出那些记录，替厂里挡下一桩大事故。", failFeedback: "你被停了职，扫了半年厕所。可每天路过车间，你还是忍不住朝纱锭的方向多看上一眼。", successEffect: { intellect: 8, happiness: 4, rep: 10 }, failEffect: { health: -4, happiness: -8, rep: -6 }, tagSuccess: "守岗如初", tagFail: "蒙尘不屈", isKey: true }
        ]
      }
        ],
        12: [
      {
        period: "花甲在望",
        title: "冬夜里，等一张准考证",
        narrative: (p, y) => "恢复高考的消息从广播里传出来，儿子翻出压箱底的课本。厂里要你办退休，说再干两年就该让位给年轻人。你摸着车间的机器，又看着灯下念书的儿子。",
        choices: [
          { text: "办了退休，白天带孙辈，夜里陪儿子复习功课", riskLevel: "含饴弄孙 · 灯下守望 · 稳妥必成", successChance: (p) => 100, successFeedback: "你守着一盏煤油灯，给儿子端热水、削铅笔。放榜那天他跑回家，喊妈我考上了，你手里的针线掉在地上。", failFeedback: "", successEffect: { happiness: 14, rep: 8 }, failEffect: {  }, tagSuccess: "灯下守望", tagFail: "另寻他途", isKey: false },
          { text: "跟厂里说推迟退休，带出最后一批青年女工", riskLevel: "薪火相传 · 去留两难 · 成功率 58%", successChance: (p) => 58 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "你手把手教她们摸纱的粗细，把三十年攒的笔记抄成一本。徒弟们送你一副手套，说师傅的活有人接了。", failFeedback: "厂里终究没有批，退休手续照办。你把笔记留给最勤的那个姑娘，看她攥着本子红了眼眶。", successEffect: { intellect: 8, happiness: 6, rep: 12 }, failEffect: { intellect: 3, happiness: -4, rep: 4 }, tagSuccess: "薪火相传", tagFail: "交了班", isKey: true }
        ]
      }
        ],
      },
      "contemporary": {
        2: [
      {
        period: "少年分流",
        title: "粮票将尽，家里的算盘",
        narrative: (p, y) => "一九九三年秋，粮票快作废了，镇上的粮站改成粮油店。你十五岁，中考排在年级前五。父亲说女娃读到初中就够，弟弟还得念书；母亲把一张中专招生简章压在米缸上：会计专业，三年毕业包分配。窗外，从东莞回来的阿姐手腕上戴着电子表。",
        choices: [
          { text: "跟父亲立下字据：考上县一中就自己挣学费，假期去镇上服装厂踩缝纫机", riskLevel: "立据抗争 · 自筹学费 · 成功率 55%", successChance: (p) => 55 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "你考上了县一中，暑假在服装厂一天踩十二个小时缝纫机。开学那天你把一沓皱巴巴的钞票放在父亲面前，他没说话，把字据撕了。", failFeedback: "你差了三分，只能去读中专。字据还压在父亲抽屉底下，他没提，你也没提。夜里你把借来的高一课本一页页抄进本子。", successEffect: { intellect: 12, happiness: 4, rep: 5 }, failEffect: { wealth: 4, intellect: 6, happiness: -8 }, tagSuccess: "负笈县中", tagFail: "抄书自读", isKey: true },
          { text: "去读中专会计，三年后包分配进镇供销社，先给家里端上铁饭碗", riskLevel: "稳妥就业 · 早立门户 · 稳妥必成", successChance: (p) => 100, successFeedback: "你进了中专，算盘打得飞快，毕业分到镇供销社。工资不高，但每月能往家里交钱，弟妹的学费总算有了着落。", failFeedback: "", successEffect: { wealth: 10, intellect: 6, happiness: -3 }, failEffect: {  }, tagSuccess: "端上铁碗", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        3: [
      {
        period: "成人立志",
        title: "录取通知书与南下招工单",
        narrative: (p, y) => "一九九六年夏，省城的录取通知书和一张深圳电子厂的招工单同时摆在桌上。学费一年两千四，家里拿不出；同村阿姐南下三年，寄回来的钱盖起了两层小楼。母亲一边给你缝被褥，一边说邻村有户人家托媒人来问过你，人老实，家里有拖拉机。",
        choices: [
          { text: "揣着东拼西凑的学费去省城读书，课余做家教、在食堂帮工，四年不向家里伸手", riskLevel: "负笈苦读 · 半工自立 · 成功率 55%", successChance: (p) => 55 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 4 : 0), successFeedback: "你在图书馆待到闭馆，周末骑一辆旧自行车跑三个小区做家教。毕业那年你签了省城的工作，把第一笔安家费寄回家还债。", failFeedback: "大二那年母亲病了，你把学费挪去交了住院费，休学半年。回校后你比同届晚一年毕业，简历上那段空白你从不解释。", successEffect: { wealth: 2, intellect: 14, rep: 6 }, failEffect: { wealth: -4, intellect: 8, happiness: -6 }, tagSuccess: "负笈省城", tagFail: "中途缓行", isKey: true },
          { text: "跟同乡南下进电子厂，先挣钱替家里还债，也看看外面的世界", riskLevel: "南下进厂 · 稳妥谋生 · 稳妥必成", successChance: (p) => 100, successFeedback: "你进了东莞的电子厂，第一个月就寄回八百块。宿舍八个人一间，你学会了用粤语讲价，也攒下了自己的第一笔私房钱。", failFeedback: "", successEffect: { health: -3, wealth: 9, intellect: 4 }, failEffect: {  }, tagSuccess: "南下谋生", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        4: [
      {
        period: "青春韶华",
        title: "写字楼里的高跟鞋与夜校",
        narrative: (p, y) => "二〇〇〇年，你在省城外企做前台，月薪一千八，要穿套装和高跟鞋，中午在写字楼下吃六块钱的盖饭。同屋的姑娘在考注册会计师，劝你也报个班。隔壁巷口的裁缝铺要转租，老板娘说这位置做童装准能挣钱。你手里攒了八千块。",
        choices: [
          { text: "报班考注册会计师，白天上班晚上听课，三年内转进财务部", riskLevel: "苦考证书 · 力争上行 · 成功率 50%", successChance: (p) => 50 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0), successFeedback: "你连考三年，最后一门险险过线。转岗那天，主管把财务部的钥匙交到你手里，工资翻了一倍，你给自己买了第一支像样的口红。", failFeedback: "第二年你差四分，第三年正赶上公司缩编，报名费都要掂量。你把书收进纸箱，搁在床底，却没舍得扔掉。", successEffect: { wealth: 8, intellect: 14, rep: 6 }, failEffect: { wealth: -5, intellect: 7, happiness: -6 }, tagSuccess: "持证上行", tagFail: "一纸未成", isKey: true },
          { text: "先租下裁缝铺的一半柜台试卖童装，不辞职，晚上和周末看店", riskLevel: "半柜试水 · 稳妥副业 · 稳妥必成", successChance: (p) => 100, successFeedback: "你在柜台后站了半年周末，摸清街坊爱买什么款式，也认识了几家批发商。年底一算账，副业挣的竟比工资还多。", failFeedback: "", successEffect: { wealth: 6, intellect: 4, happiness: 3 }, failEffect: {  }, tagSuccess: "小试门面", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        5: [
      {
        period: "初涉人世",
        title: "电话那头的催婚与首付",
        narrative: (p, y) => "二〇〇三年春节，你二十五岁，在城里做外贸跟单。母亲在电话里说，隔壁小你三岁的都抱上孩子了。经理刚暗示要提你做小组长，这岗位却要随时出差。你存折上有六万块，够不够付城郊小户型的首付，你自己也算了几个晚上。",
        choices: [
          { text: "先付首付买下城郊的小户型，把户口和退路都落在城里", riskLevel: "举债置业 · 落脚扎根 · 成功率 55%", successChance: (p) => 55 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 4 : 0), successFeedback: "你签下三十年贷款，房子小得转不开身，但拿到房产证那天，你在阳台上站了很久。母亲来住了一晚，说总算有个落脚的地方。", failFeedback: "首付差两万，你找同事东拼西凑，最后还是没赶上那套房。半年后房价涨了一截，你把存折锁进抽屉，再没提起。", successEffect: { wealth: 12, happiness: 5, rep: 4 }, failEffect: { wealth: 1, happiness: -6 }, tagSuccess: "安身有屋", tagFail: "一步之差", isKey: true },
          { text: "答应母亲回家相亲，先把婚事定下来，工作的事以后再说", riskLevel: "顺从成家 · 稳妥定亲 · 稳妥必成", successChance: (p) => 100, successFeedback: "你见了三个相亲对象，最后跟县中学的物理老师定了亲。他脾气温和，母亲很满意；回城的火车上，你把出差申请单叠好收进包里。", failFeedback: "", successEffect: { happiness: 4, rep: 5 }, failEffect: {  }, tagSuccess: "顺水成家", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        6: [
      {
        period: "成家立业",
        title: "产假结束前的那通电话",
        narrative: (p, y) => "二〇〇六年，你休完产假，孩子夜里还要喂两次奶。公司新来的副总说岗位有调整，你原来的位置已经有人坐了，愿意回来就先做助理。丈夫说要不你在家带两年孩子，反正他的工资够还房贷。婆婆从老家来帮忙，却总念叨女人不该在外抛头露面。",
        choices: [
          { text: "接下降职先回公司，白天上班夜里带娃，半年内把丢掉的老客户一个个谈回来", riskLevel: "降职重回 · 两头硬撑 · 成功率 50%", successChance: (p) => 50 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.health > 60 ? 6 : 0), successFeedback: "你背着吸奶器挤地铁，午休时间在楼梯间打电话。半年后你把三个老客户重新签了回来，副总在会上点了你的名字。", failFeedback: "孩子连着发烧，你请了太多假，年终评优没有你。委屈你咽了下去，仍旧每天准时坐到工位上——这个家需要这份工资。", successEffect: { health: -6, wealth: 8, happiness: 3, rep: 10 }, failEffect: { health: -4, happiness: -8, rep: -2 }, tagSuccess: "重执旧业", tagFail: "两头吃力", isKey: true },
          { text: "辞职在家带娃三年，把家里账目和孩子都管好，等孩子上了幼儿园再出来", riskLevel: "辞职持家 · 稳妥三年 · 稳妥必成", successChance: (p) => 100, successFeedback: "你把家里开支记成一本细账，房贷提前还了三万。孩子学会走路那天，你拍了照片发给丈夫。夜里你偶尔翻出从前的名片看看。", failFeedback: "", successEffect: { wealth: -3, intellect: -2, happiness: 4 }, failEffect: {  }, tagSuccess: "持家三载", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        7: [
      {
        period: "三十而立",
        title: "三十五岁前的最后一张牌",
        narrative: (p, y) => "二〇一〇年，你三十二岁，孩子刚上幼儿园。公司里新招的年轻人加班到十点也不喊累，而你每天六点要去接孩子。老同学在淘宝上卖母婴用品，一年挣了二十万，喊你一起做。猎头打来电话，说外地有个管理岗，薪水高，只是要常驻。",
        choices: [
          { text: "跳去外地做部门经理，把丈夫和孩子一起接过去租房，全家重新安顿", riskLevel: "异地博取 · 举家迁徙 · 成功率 45%", successChance: (p) => 45 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 5 : 0), successFeedback: "你在新城市带起十二人的团队，工资涨了一倍。孩子在新幼儿园交到了朋友，丈夫半年后也找到了工作。你终于不再怕接幼儿园的电话。", failFeedback: "团队里两个老员工不服你，项目拖了半年。丈夫辞职过来后一直没找到合适的工作，你深夜坐在出租屋里，第一次怀疑这个决定。", successEffect: { wealth: 14, happiness: 5, rep: 12 }, failEffect: { wealth: -8, happiness: -10, rep: -3 }, tagSuccess: "异地立局", tagFail: "迁徙代价", isKey: true },
          { text: "留在原公司，业余跟老同学合伙开淘宝店，先把第二条路慢慢铺起来", riskLevel: "副业铺路 · 稳妥创业 · 稳妥必成", successChance: (p) => 100, successFeedback: "你下班后打包发货，周末去批发市场拿货。第一年赚得不多，可店铺的信用一颗星一颗星涨起来，你心里踏实了些。", failFeedback: "", successEffect: { health: -3, wealth: 7, intellect: 5 }, failEffect: {  }, tagSuccess: "另辟蹊径", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        9: [
      {
        period: "中年险滩",
        title: "优化名单上的那个名字",
        narrative: (p, y) => "二〇一八年冬，公司裁员，你四十一岁，在这里做了十三年。HR说赔偿按 N+1 算，签字当天到账。父亲中风住院，母亲一个人照看不过来；孩子的补习费下个月还要交。你投了两个月简历，回音寥寥，有的岗位明写着年龄三十五岁以下。",
        choices: [
          { text: "先跑网约车撑住现金流，同时系统学数据分析，半年后争取转行", riskLevel: "零工蛰伏 · 中年转型 · 成功率 45%", successChance: (p) => 45 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 4 : 0), successFeedback: "你白天开车晚上上课，把三个月的收入算了又算。半年后一家小公司要你做运营分析，工资只有从前的一半，你不介意。", failFeedback: "你考了两次证书都没过，面试时对方嫌你没有相关经验。开车成了常事，好在每个月的房贷一次也没有断过。", successEffect: { wealth: 6, intellect: 10, happiness: 3, rep: 5 }, failEffect: { health: -5, wealth: 2, intellect: 5, happiness: -6 }, tagSuccess: "中年转身", tagFail: "缓行未止", isKey: true },
          { text: "把父母接来城里同住，自己担起照料，先顾家里再谈事业", riskLevel: "侍疾尽孝 · 稳妥持家 · 稳妥必成", successChance: (p) => 100, successFeedback: "你在客厅支起护理床，学会了量血压、翻身、喂流食。父亲能扶着走两步那天，母亲在厨房里哭了。你的简历上又空了一年。", failFeedback: "", successEffect: { health: -4, wealth: -6, happiness: 4, rep: 6 }, failEffect: {  }, tagSuccess: "侍疾持家", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        12: [
      {
        period: "花甲在望",
        title: "退休通知与女儿的行李箱",
        narrative: (p, y) => "二〇三四年，你五十八岁，延迟退休细则刚落地，你却先接到劝退通知。女儿三十岁，说不想结婚，要辞职去大理开民宿。家里老人还在，智能音箱催你吃药，手机里的AI助手替你挂号、比价、写申请材料。你半生攒下的经验，有一半用不上了。",
        choices: [
          { text: "不劝女儿，把自己攒下的积蓄和见识讲给她，再去学一门新手艺", riskLevel: "放手更生 · 暮年学技 · 成功率 50%", successChance: (p) => 50 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 5 : 0) + (p.health > 60 ? 4 : 0), successFeedback: "你报了社区大学的剪辑班，第一次把父亲讲过的老厂故事剪成短片，播放过了十万。女儿在大理打来电话，说妈你真行。", failFeedback: "你学了两个月，还是弄不懂那些弹窗和后台。民宿的生意也清淡，女儿打来电话借钱，你转过去一半养老钱，没敢告诉老伴。", successEffect: { wealth: 3, intellect: 10, happiness: 8, rep: 6 }, failEffect: { wealth: -10, intellect: 4, happiness: -6 }, tagSuccess: "暮年新技", tagFail: "转账之后", isKey: true },
          { text: "跟女儿把账算清楚，让她先在城里稳两年，攒够本钱再谈民宿", riskLevel: "细账铺路 · 稳妥劝阻 · 稳妥必成", successChance: (p) => 100, successFeedback: "你把家里的收支列成一张表，给她看每月的固定开销。女儿沉默了很久，答应先不辞职，周末去大理看铺面，回来再谈。", failFeedback: "", successEffect: { wealth: 2, happiness: 3, rep: 5 }, failEffect: {  }, tagSuccess: "细账铺路", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
      },
      "future": {
        2: [
      {
        period: "少年分流",
        title: "分流日，母亲把工牌推过来",
        narrative: (p, y) => "穹顶十四岁分流日，基因档案与算力配额一并摊在桌上，你的编辑页标着「第二代合规」，配额只够走一条路。轨道学院的招生员说操舵预科要自费模拟时长；母亲把袖子卷起，露出手腕上运维班的工牌，她刚排上夜班。",
        choices: [
          { text: "报考深空轨道学院操舵预科，用自己攒的配额换模拟器时长", riskLevel: "凌云 · 孤注 · 成功率 63%", successChance: (p) => 63 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.health > 60 ? 6 : 0), successFeedback: "模拟器里你第一次握住操纵杆，第三次考核就压住侧风。招生员签字那天，母亲把夜班换成白班，说穹顶外也得有人看着。", failFeedback: "配额烧尽，考核差两名落榜。你回穹顶做运维学徒，掌心磨出茧，却认得每一条缆线，也算没白走一遭。", successEffect: { intellect: 12, luck: 2, rep: 6 }, failEffect: { health: -3, intellect: 5, happiness: -6 }, tagSuccess: "星轨初执", tagFail: "折翼复起", isKey: true },
          { text: "听母亲的，进穹顶算力运维班，毕业即定编，配额按月足额发放", riskLevel: "守成 · 稳妥 · 稳妥必成", successChance: (p) => 100, successFeedback: "你穿上运维制服，在穹顶上巡线，风噪隔着穹壳像海。每月配额准时到账，母亲的夜班也少了，她说这样踏实。", failFeedback: "", successEffect: { wealth: 5, intellect: 6, happiness: 4 }, failEffect: {  }, tagSuccess: "安守穹顶", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        3: [
      {
        period: "成人立志",
        title: "电梯票根与一张排班表",
        narrative: (p, y) => "地月货运电梯放出十二个见习席位，报名要自付地月往返的加加速度检查费。同日，母亲把穹顶物流科的排班表推到你面前——定编、双休、离她三站磁轨。电梯调度员补一句：女性见习生须先签一年不育协议，理由是辐射剂量。",
        choices: [
          { text: "签下辐射协议去争见习席位，同时联名要求同步取消男性同款条款", riskLevel: "破格 · 逆流 · 成功率 58%", successChance: (p) => 58 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 8 : 0), successFeedback: "你成了首批登梯的见习调度，还把那一页不平等条款送进公听会。三个月后协议废止，后来者不必再签。", failFeedback: "你落选，协议却因你的申诉被复议。母亲没说什么，只把你熬夜写的材料收进抽屉，说留着，往后还有用。", successEffect: { intellect: 10, happiness: 5, rep: 12 }, failEffect: { health: -3, happiness: -8, rep: 6 }, tagSuccess: "登梯破例", tagFail: "为民试路", isKey: true },
          { text: "接下物流科定编岗位，先攒够配额与年资，把远方留到下一轮", riskLevel: "循序 · 稳妥 · 稳妥必成", successChance: (p) => 100, successFeedback: "你熟悉了每一班磁轨的货单，也在职校夜课补了轨道力学。三年后升组长，母亲的排班表上，你们的名字挨在一起。", failFeedback: "", successEffect: { wealth: 6, intellect: 4, rep: 3 }, failEffect: {  }, tagSuccess: "步步为营", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        4: [
      {
        period: "青春韶华",
        title: "上传舱里的第七次心跳",
        narrative: (p, y) => "毕业那年，三家小行星驻站递来合同，年薪抵穹顶十年；同一周，神经所的早期上传计划招志愿者：分七次扫描把意识结构搬上云端，每次都可能丢一段短期记忆。知情书要求一位「延续人」替你签字，而父母都拒签。",
        choices: [
          { text: "报名早期上传计划，先备份再谈身体，把记忆清单交给自己保管", riskLevel: "舍身 · 问心 · 成功率 52%", successChance: (p) => 52 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 6 : 0), successFeedback: "第七次扫描后你在云端醒来，记得母亲煮的汤的味道，却忘了她哪天生的病。你给自己列了清单，从此每天手写一行日记。", failFeedback: "扫描中断，你丢了整整两年记忆，连恋人的脸都对不上。懊恼之余你去做记忆康复师，专陪别人认回自己。", successEffect: { intellect: 15, happiness: -4, luck: 6 }, failEffect: { health: -6, intellect: 6, happiness: -8 }, tagSuccess: "云上初醒", tagFail: "失忆拾人", isKey: true },
          { text: "去小行星驻站做脑机接口算法岗，先把身体留在有重力的地方", riskLevel: "务实 · 稳妥 · 稳妥必成", successChance: (p) => 100, successFeedback: "你在旋转站里调算法，窗外矿石像一串钝星。年薪汇回穹顶，父亲用那笔钱换了新义肢，视频里他走了两圈给你看。", failFeedback: "", successEffect: { health: 2, wealth: 12, intellect: 8 }, failEffect: {  }, tagSuccess: "驻站有得", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        5: [
      {
        period: "初涉人世",
        title: "生育排期表压在工位键盘旁",
        narrative: (p, y) => "人造子宫排期已排到第四年，生殖中心说你的配子正处黄金窗口，越早越好；同一个月，公司把跨区主管名额和一条「两年内不排产假」的隐形条款一起递来。伴侣在火星班次上，视频有十一分钟延迟。",
        choices: [
          { text: "签下人造子宫排期，与伴侣改成错班轮值，婴儿舱满月后再回岗", riskLevel: "生养 · 竞速 · 成功率 66%", successChance: (p) => 66 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.health > 60 ? 8 : 0), successFeedback: "孩子从育婴舱抱出来那天，你左手托着襁褓，右手开线上会。主管名额定给了别人，但夜里孩子攥住你手指，你觉得这买卖不亏。", failFeedback: "排期撞上项目上线，你两头奔命，产褥期并发症住了三次院，晋升也黄了。伴侣从火星调回地勤，说以后换他熬夜。", successEffect: { health: -4, happiness: 10, rep: 4 }, failEffect: { health: -12, wealth: -8, happiness: -6 }, tagSuccess: "双肩担月", tagFail: "顾此失彼", isKey: true },
          { text: "先接下主管名额，把排期推到下一轮，用算力配额换延期保管", riskLevel: "缓行 · 稳妥 · 稳妥必成", successChance: (p) => 100, successFeedback: "你把配子送进低温库，换来三年保额与一个主管头衔。夜里你偶尔打开抽屉看那张排期单，告诉自己只是晚一点，不是放弃。", failFeedback: "", successEffect: { wealth: 10, intellect: 6, rep: 8 }, failEffect: {  }, tagSuccess: "先立后生", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        6: [
      {
        period: "成家立业",
        title: "三代人挤在穹顶一间配给房",
        narrative: (p, y) => "外婆的肺叶换过两次，护理舱占掉半间配给房；祖母刚做完第三代基因修正，脾气像换了个人。此时火星农业拓荒队招主责农艺师，三年一期，家属配额翻倍，却赶不上下月外婆的第三次手术签字——只有你能签。",
        choices: [
          { text: "报名火星农业拓荒，请远程医疗代理人代签，每月定时视频陪床", riskLevel: "远拓 · 牵心 · 成功率 60%", successChance: (p) => 60 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.health > 60 ? 10 : 0), successFeedback: "你在火星穹顶下种出第一茬耐盐小麦，麦芒在低重力里轻轻翘着。外婆手术顺利，视频里她戴上老花镜看你身后的红土，说像老家黄昏。", failFeedback: "手术出了并发症，你在三十分钟延迟里什么也做不了。回来后你在外婆床前守了两个月，也把火星的轮作数据整理成册，交给下一批人。", successEffect: { wealth: 8, intellect: 12, rep: 10 }, failEffect: { health: -3, happiness: -10, rep: 4 }, tagSuccess: "拓土有收", tagFail: "远信难及", isKey: true },
          { text: "留在穹顶升任分区主管，把三代人的护理舱与排班一并理顺", riskLevel: "持家 · 稳妥 · 稳妥必成", successChance: (p) => 100, successFeedback: "你给外婆和祖母排了错峰护理，顺手改掉楼里三十户的排队规则。年底考核你评了优，只是火星寄来的种子，你收在柜里没种。", failFeedback: "", successEffect: { wealth: 4, happiness: 4, rep: 10 }, failEffect: {  }, tagSuccess: "内宅能臣", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        7: [
      {
        period: "三十而立",
        title: "共治协议里被划掉的那一行",
        narrative: (p, y) => "强AI共治委员会请你起草资源分配条款。你的修订稿里有一句：算力与寿命延长额度按生殖贡献与照护劳动加权。有人递条子，说这会「把机器政治带回身体政治」。更棘手的是，你的女儿是第一代高编辑儿，她刚拒绝承认你是她的监护样本来源。",
        choices: [
          { text: "坚持写入照护劳动加权，同时公开自己的编辑档案作为利益披露", riskLevel: "立言 · 剖白 · 成功率 55%", successChance: (p) => 55 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 8 : 0), successFeedback: "条款通过那天，女儿在公听会后门等你。她没说话，只把自己的档案卡递过来，监护人一栏，她终于填了你的名字。", failFeedback: "条款被删，你被指利用职务照顾自身，女儿连视频也不接了。你把修订稿锁进私库，只在每年重读一遍，等下一个提出的人。", successEffect: { intellect: 10, happiness: 5, rep: 15 }, failEffect: { intellect: 5, happiness: -8, rep: -8 }, tagSuccess: "字字千钧", tagFail: "孤稿存志", isKey: true },
          { text: "退出共治起草，回轨道工坊做义体神经接口，把话留给别人说", riskLevel: "退身 · 稳妥 · 稳妥必成", successChance: (p) => 100, successFeedback: "工坊里你替矿工修被辐射烧坏的神经束，手很稳。有人拿共治条款来问你，你只说我做接口的，先让人能握住东西，再谈分配。", failFeedback: "", successEffect: { health: 4, wealth: 9, intellect: 6 }, failEffect: {  }, tagSuccess: "匠手安生", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        9: [
      {
        period: "中年险滩",
        title: "备份舱外的强太阳风暴",
        narrative: (p, y) => "太阳风暴烧穿轨道中继，公司整个中层被算法重构，你的岗位落在名单边缘。同一周，云端备份公司来信：你的意识快照已存到第九版，问是否升级到「全角膜本」，费用是二十年配额。而母亲刚过世，她的备份因保额不足被永久封存。",
        choices: [
          { text: "只留第九版快照，把配额转给母亲旧备份解封，让女儿还能问外婆", riskLevel: "取舍 · 承情 · 成功率 60%", successChance: (p) => 60 + (p.intellect > 50 ? Math.floor((p.intellect - 50) / 2) : 0) + (p.luck > 50 ? 6 : 0), successFeedback: "母亲的三分钟语音备份解封了，她照旧念叨你别熬夜。你被降到边缘岗，却每天睡前听一遍那段录音，睡得比升职那些年都沉。", failFeedback: "解封申请卡在伦理审查，母亲的备份终究成了废码。你丢了岗，也没留下她。女儿抱着你说，没关系，我们记得的也是她。", successEffect: { health: 4, wealth: -10, happiness: 8 }, failEffect: { wealth: -12, happiness: -12, rep: 3 }, tagSuccess: "留声传代", tagFail: "人财两空", isKey: true },
          { text: "升级全角膜本，转岗去做风暴后的中继重建设计", riskLevel: "重构 · 稳妥 · 稳妥必成", successChance: (p) => 100, successFeedback: "新中继按你的方案加了冗余环，再没断过。全角膜本躺在云端，偶尔提醒你某年某月的心率。重装后的天线在风里慢慢转，像没受过伤。", failFeedback: "", successEffect: { health: -4, wealth: 8, intellect: 10 }, failEffect: {  }, tagSuccess: "履险如夷", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
        12: [
      {
        period: "花甲在望",
        title: "火种船票只发一张，落谁手里",
        narrative: (p, y) => "恒星际火种船点火在即，船上按基因多样性抽签，你抽中一张永不复返的票。地面这头，孙辈刚接入脑机课程，儿子在戴森云环上做桁架工，一年回一次视频。舱位不设返程，航程一百二十年，你会比所有留在地面的人晚很久才老去。",
        choices: [
          { text: "登船，把毕生日志与穹顶旧照封进船载档案，任航行期心理维持岗", riskLevel: "远航 · 诀别 · 成功率 48%", successChance: (p) => 48 + (p.luck > 50 ? 10 : 0) + (p.health > 60 ? 8 : 0), successFeedback: "点火那日，蓝色尾焰把火种船推出黄道。你在船上给孙辈录第一封延时信，说这一百二十年你们都会收到我，只是我收不到你们回信。", failFeedback: "体检未过关，你被移出名单，名额换给一位更年轻的基因样本。你在发射场看那道光远去，直到它比星还小，才转身去买回程磁轨票。", successEffect: { happiness: -6, luck: 12, rep: 10 }, failEffect: { health: -4, intellect: 6, happiness: -5 }, tagSuccess: "长夜传薪", tagFail: "留地观星", isKey: true },
          { text: "留在戴森云环的地面学院，把六十年工程经验编成育才课程", riskLevel: "授业 · 稳妥 · 稳妥必成", successChance: (p) => 100, successFeedback: "你在课堂上拆解一台报废的中继器，学生围了三圈。结课时有人问人类为什么要去那么远，你说因为总得有人留下，把来路说清楚。", failFeedback: "", successEffect: { intellect: 8, happiness: 6, rep: 12 }, failEffect: {  }, tagSuccess: "薪火在地", tagFail: "另寻他途", isKey: false }
        ]
      }
        ],
      },
    };

    // ==================== 文明五大纪元专属突发偶发事件库 ====================
    const RANDOM_EVENT_POOLS = {
      "ancient": [
        { id: "ancient_re_jade", title: "山涧偶拾古玉", tag: "古玉通灵", desc: "山行避雨，在溪涧泥沙中偶拾得一枚温润古玉。虽无印款，质地却极通透，暗合吉兆。", effect: { wealth: 1.2, happiness: 8, luck: 4 } },
        { id: "ancient_re_monk", title: "古刹隐僧问道", tag: "心源豁然", desc: "古道暮色中遇一云游老僧，席地饮凉茶数巡，数语直指心源，使你久郁的心结豁然开朗。", effect: { happiness: 12, intellect: 6, luck: 2 } },
        { id: "ancient_re_flood", title: "连雨山洪浸屋", tag: "水患维艰", desc: "夏秋连旬暴雨，后山泥流漫入土屋，积谷受潮，梁柱亦有倾斜，不得不耗费钱粮修葺。", effect: { wealth: -1, health: -4, happiness: -6 } },
        { id: "ancient_re_cure", title: "游方草医良方", tag: "逢医愈疾", desc: "路遇背负青囊的游方草医，赠以一剂熬透的驱寒草药，陈年风湿暗疾竟大见舒缓。", effect: { health: 12, happiness: 6, intellect: 2 } },
        { id: "ancient_re_elder", title: "里正公推保举", tag: "乡党誉重", desc: "乡里宗族耆老在公堂上赞你操行笃厚、守礼慎行，县衙公文上特予记名表彰。", effect: { rep: 10, happiness: 6, luck: 3 } },
        { id: "ancient_re_bandit_alarm", title: "戍烽边警虚惊", tag: "惊弓之险", desc: "山关烽火骤起，夜半鸡犬不宁，村民皆裹粮避入深山，三日后探知方知是巡哨虚惊。", effect: { health: -6, happiness: -8, wealth: -0.5 } },
        { id: "ancient_re_bronze", title: "市集低纳残铜", tag: "古铭生辉", desc: "在城邑墟市角落以几斗粟米购得数件锈蚀铜器，归家磨洗竟辨出商周铭文，引来雅士重金求借观。", effect: { wealth: 2, intellect: 8, rep: 5 } },
        { id: "ancient_re_bountiful", title: "风调雨顺丰稔", tag: "五谷丰登", desc: "一年四时风调雨顺，租田菽粟齐熟，所纳官粮外尚有赢余，邻里共饮春酒。", effect: { wealth: 1.5, happiness: 10, health: 4 } },
      ],
      "premodern": [
        { id: "premodern_re_rubbing", title: "旧肆偶得前朝残拓", tag: "墨海得珍", desc: "瓦舍书肆尘封角落翻得一卷苏黄法帖残拓，墨香沉郁，细加摩挲，笔意大有进益。", effect: { intellect: 10, happiness: 6, rep: 4 } },
        { id: "premodern_re_flood_granary", title: "梅雨湿仓霉丝", tag: "梅雨蚀利", desc: "江南连月梅雨淫霏不绝，仓底生潮，数匹上好贡缎发霉斑蚀，亏了当季行利。", effect: { wealth: -1.5, happiness: -8, health: -2 } },
        { id: "premodern_re_tea_meeting", title: "山馆品茗结清交", tag: "茗社良朋", desc: "游山遇雨暂避茶肆，同一商号掌柜煮泉斗茶，对方深赏你品行，引荐了通达路子。", effect: { intellect: 6, wealth: 1.5, luck: 4 } },
        { id: "premodern_re_theft", title: "柜坊夜失细软", tag: "夜警失金", desc: "市镇遭宵小潜入，铺前藏银与细软账册被翻箱倒柜，所幸借据藏于夹壁，仅折了零银。", effect: { wealth: -1.8, happiness: -10, luck: -3 } },
        { id: "premodern_re_clan_aid", title: "宗族义田分惠", tag: "宗族庇荫", desc: "族中义庄按岁分发胙肉与冬谷，长房感念你平素谦谨，格外添拨了半口良田收益。", effect: { wealth: 1.6, happiness: 8, rep: 6 } },
        { id: "premodern_re_epidemic", title: "时疫避凶逢吉", tag: "积善避瘟", desc: "城中突发热症时疫，你谨守草方洁舍闭门深居，全家皆得安宁，反以余药济贫积了阴骘。", effect: { health: 6, happiness: 8, rep: 8, luck: 4 } },
        { id: "premodern_re_ticket", title: "钱庄票号分息", tag: "票号利丰", desc: "旧年寄存晋陕票号的闲银，逢着外贸大顺岁，东家特发加息两厘，平添一份喜钱。", effect: { wealth: 2.5, happiness: 6, luck: 2 } },
        { id: "premodern_re_street_fire", title: "市巷回禄之灾", tag: "劫后余生", desc: "邻家失慎走水，火借风势延烧数丈，奋力搬运只保得身家无虞，房屋微损需整葺。", effect: { wealth: -1.2, health: -5, happiness: -8 } },
      ],
      "modern": [
        { id: "modern_re_foreign_letter", title: "邮差送达海外侨批", tag: "天涯侨批", desc: "南洋远亲历尽艰难寄回一封泛黄的侨批与银汇，虽经数道邮路折损，终在燃眉之际解了全家饥荒。", effect: { wealth: 3, happiness: 12, luck: 4 } },
        { id: "modern_re_night_study", title: "夜校烛光与借阅新书", tag: "灯下求真", desc: "工友从省城带回一本翻烂的《大众哲学》与工业图解，两人在油灯下轮流抄录至天明。", effect: { intellect: 12, happiness: 8, rep: 4 } },
        { id: "modern_re_curfew", title: "警笛骤响的惊悸之夜", tag: "乱世惊弓", desc: "戒严巡逻的哨子与皮靴声在弄堂回响，全家屏息熄灯躲在阁楼，心悬半宿，惊魂甫定。", effect: { health: -4, happiness: -10, luck: -2 } },
        { id: "modern_re_ration_coupon", title: "合作社拾遗物归原主", tag: "诚恪扬名", desc: "在粮站排队时拾得遗落的布票与购粮簿，多方寻访归还失主，厂里特开黑板报通报嘉奖。", effect: { rep: 12, happiness: 10, luck: 3 } },
        { id: "modern_re_train_delay", title: "蒸汽火车大误点", tag: "羁旅同舟", desc: "运煤车皮脱轨导致客车困在荒野道岔整整两日，干粮断顿，幸与同车乘客分饮凉水共渡难关。", effect: { health: -6, happiness: -6, intellect: 4 } },
        { id: "modern_re_invention", title: "车间边角料巧改农具", tag: "格物巧手", desc: "利用厂区淘汰的报废角钢，自制了一把轻便好用的滚珠深耕犁，在农忙支农中大获赞誉。", effect: { intellect: 8, rep: 8, happiness: 6 } },
        { id: "modern_re_frozen_pipeline", title: "严冬水管冻裂与邻里抢险", tag: "风雪同心", desc: "零下二十度寒潮冻裂总管道，大家在冰水里抢险排涝，虽受了风寒，工友却送来热姜汤。", effect: { health: -4, happiness: 6, rep: 6 } },
        { id: "modern_re_bonus", title: "节约革新标兵津贴", tag: "立功受奖", desc: "提出的降耗小革新在全车间推广，月底大会受到表扬，并领到一张簇新的洗脸盆兑换券与小额奖励。", effect: { wealth: 1.5, rep: 10, happiness: 8 } },
      ],
      "contemporary": [
        { id: "contemporary_re_lottery", title: "街头彩票微幸", tag: "微幸眷顾", desc: "路过街头报刊亭随手刮了一张体育彩票，竟中了二等小奖！虽非巨资，却在捉襟见肘时添了口温热饭菜。", effect: { wealth: 2, happiness: 8, luck: -2 } },
        { id: "contemporary_re_illness_scare", title: "深夜急诊惊魂", tag: "疾痛惊魂", desc: "深夜高烧突发呼吸急促，被救护车紧急送医折腾了一整夜。输液到天明虽脱险，医药费却花了半月薪资。", effect: { health: -10, wealth: -2, happiness: -6 } },
        { id: "contemporary_re_friend_scam", title: "老友借贷失联", tag: "信义落空", desc: "昔日挚友以资金周转为名求借一笔周转金，承诺数月即还。不料半年后微信拉黑人去楼空，令人心寒彻骨。", effect: { wealth: -3.5, happiness: -12, rep: -2 } },
        { id: "contemporary_re_mentor", title: "贵人偶指迷津", tag: "高人指路", desc: "行业沙龙散场后，偶遇一位退休的前辈行尊。对方就着茶水三言两语点破你职业天花板，令你茅塞顿开。", effect: { intellect: 10, happiness: 6, rep: 4 } },
        { id: "contemporary_re_stock_bubble", title: "跟风理财踩雷", tag: "折戟商海", desc: "轻信朋友推荐的理财新产品，遭遇行情闪崩与赎回冻结，辛苦攒下的活钱平白打了水漂。", effect: { wealth: -4, happiness: -10, luck: -4 } },
        { id: "contemporary_re_overtime_crash", title: "连续通宵身体亮红灯", tag: "透支预警", desc: "为了赶项目进度连续通宵加班一周，清晨心悸晕眩几乎倒在工位，不得不自费购买昂贵保健品调理。", effect: { health: -12, happiness: -6, wealth: -1 } },
        { id: "contemporary_re_viral", title: "随手自媒体微火一把", tag: "浮名微光", desc: "下班途中随手拍摄的生活感悟视频竟然在短视频平台小火出圈，收到不少读者鼓励与微薄流量收益。", effect: { rep: 8, wealth: 1.5, happiness: 10 } },
        { id: "contemporary_re_rent_hike", title: "房东突击涨租逼迁", tag: "居无定所", desc: "租约未满房东突然宣布涨租三成，不得不顶着严寒连夜打包行李四处找房搬家，筋疲力竭。", effect: { wealth: -1.8, happiness: -12, health: -4 } },
      ],
      "future": [
        { id: "future_re_neural_glitch", title: "神经脉冲震荡", tag: "神经震颤", desc: "人造电离穹顶遭遇强太阳风暴微扰，脑机接口神经信号出现短暂延迟反冲，视网膜全息界面频频雪花乱闪。", effect: { health: -8, happiness: -6, intellect: -2 } },
        { id: "future_re_quantum_airdrop", title: "暗网算力盲盒空投", tag: "天降算力", desc: "由于早期参与过开源超导协议的节点维护，突然收到去中心化自治组织空投的一笔高阶加密算力配额！", effect: { wealth: 4, luck: 4, happiness: 8 } },
        { id: "future_re_synth_recall", title: "二阶仿生器官例行召回", tag: "义体维保", desc: "收到生物义体制造商的通函，左臂的人工神经束存在隐患需入舱返厂检修，自费垫付了昂贵的保外调试费。", effect: { wealth: -2.5, health: 4, happiness: -6 } },
        { id: "future_re_deep_mentor", title: "深空先驱的遗留日志", tag: "星尘启蒙", desc: "在小行星采矿站的公共数据库中翻阅到一段未加密的深空拓荒者私人音频，其宏阔深邃的宇宙观深深震撼了你。", effect: { intellect: 12, happiness: 10, rep: 5 } },
        { id: "future_re_carbon_fine", title: "超额碳排二级罚单", tag: "配额红线", desc: "因违规在室内使用老旧电阻炉烹调真实肉食，被社区无人机检测开出二级碳排放惩戒罚单。", effect: { wealth: -2.5, happiness: -8, rep: -3 } },
        { id: "future_re_cosmic_ray", title: "近轨高能辐射透射警报", tag: "射线惊险", desc: "空间站磁盾例行充能时遭遇微陨石擦碰，微量宇宙射线穿透舱壁，全员在辐射舱静置排毒并注射防辐射血清。", effect: { health: -6, wealth: -1.5, happiness: -4 } },
        { id: "future_re_seed_cultivar", title: "水耕舱培育出稀有变异甘薯", tag: "拓荒丰获", desc: "在受控重力培养槽中培育出抗辐射高糖新株系，被火星拓荒科研所按专利高价收购。", effect: { wealth: 3.5, intellect: 8, happiness: 8 } },
        { id: "future_re_ai_glitch", title: "生活伴侣强AI逻辑循环死锁", tag: "硅基感伤", desc: "家中的管家级合成仿生人突然遭遇感情悖论逻辑死锁，不得不花费两日时间重置核心模型并丢失了一部分温馨记忆。", effect: { happiness: -10, wealth: -1, intellect: 4 } },
      ],
    };
