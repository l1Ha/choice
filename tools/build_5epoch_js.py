import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.dirname(_HERE)
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
os.chdir(_ROOT)

# -*- coding: utf-8 -*-
"""把五大文明纪元（先秦汉唐 / 宋韵明清 / 近代破晓 / 当代腾飞 / 未来星海）
完整注入 index.html：纪元配置、连续时代解析、程序化出身、分纪元事件池、出生年月。"""

import importlib
import sys

import civ_core as C

NEW_EPOCHS = ("ancient", "premodern", "modern")
DATA = {}


def line_start(text, idx):
    """返回 idx 所在行的行首位置。"""
    nl = text.rfind("\n", 0, idx)
    return 0 if nl < 0 else nl + 1


def js_function_span(text, sig):
    """按花括号配对定位一个 JS 函数的完整区间 (start, end)。"""
    i = text.index(sig)
    b = text.index("{", i)
    depth = 0
    k = b
    while k < len(text):
        if text[k] == "{":
            depth += 1
        elif text[k] == "}":
            depth -= 1
            if depth == 0:
                return i, k + 1
        k += 1
    raise ValueError("unbalanced braces for " + sig)


def replace_js_function(text, sig, new_code, label):
    i, j = js_function_span(text, sig)
    print("  patched: %s" % label)
    return text[:i] + new_code + text[j:]


def load_data():
    import civ_loader
    DATA.update(civ_loader.load_all())
    for eid in NEW_EPOCHS:
        d = DATA[eid]
        print("  %s: regions=%d strata=%d stages=%d events=%d"
              % (eid, len(d.REGIONS), len(d.STRATA), len(d.STAGE_EVENTS), d.event_count()))


def build_js_pack():
    L = []
    L.append("    // ==================== 文明五大纪元 · 从华夏溯源到星海跃迁 ====================")
    L.append("    const CIVILIZATION_EPOCHS = [")
    for e in C.EPOCHS:
        L.append("      {")
        L.append("        id: %s," % C.js_str(e["id"]))
        L.append("        name: %s," % C.js_str(e["name"]))
        L.append("        subTitle: %s," % C.js_str(e["sub_title"]))
        L.append("        minYear: %d," % e["min_year"])
        L.append("        maxYear: %d," % e["max_year"])
        L.append("        badge: %s," % C.js_str(e["badge"]))
        L.append("        desc: %s," % C.js_str(e["desc"]))
        L.append("        colorClass: %s," % C.js_str(e["color"]))
        L.append("        eraIcon: %s," % C.js_str(e["icon"]))
        L.append("        legacyNoun: %s," % C.js_str({
            "ancient": "青史竹简", "premodern": "族谱与方志", "modern": "厂志与家书",
            "contemporary": "市井与家书", "future": "星尘档案",
        }[e["id"]]))
        L.append("        names: [%s]" % ", ".join(C.js_str(n) for n in e["names"]))
        L.append("      },")
    L.append("    ];")
    L.append("")
    L.append("    // 16 个生命阶段的默认年龄（用于 Python 侧对齐，JS 侧由随机时间线覆盖）")
    L.append("    const EPOCH_STAGE_AGES = [6, 10, 15, 18, 21, 24, 27, 31, 36, 40, 45, 51, 58, 66, 74, 80];")
    L.append("")
    L.append("    function getEpochConfig(id) {")
    L.append("      return CIVILIZATION_EPOCHS.find(e => e.id === id) || CIVILIZATION_EPOCHS[3];")
    L.append("    }")
    L.append("    // 由具体年份反查所属纪元（公元前1600 ~ 公元2150，无间断）")
    L.append("    function getEpochIdForYear(year) {")
    L.append("      for (const e of CIVILIZATION_EPOCHS) { if (year <= e.maxYear) return e.id; }")
    L.append("      return CIVILIZATION_EPOCHS[CIVILIZATION_EPOCHS.length - 1].id;")
    L.append("    }")
    L.append("    function isFutureEpoch(id) { return id === \"future\"; }")
    L.append("    function isClassicalEpoch(id) { return id === \"ancient\" || id === \"premodern\" || id === \"modern\"; }")
    L.append("    function pickEpochName(id) {")
    L.append("      const cfg = getEpochConfig(id);")
    L.append("      return cfg.names[Math.floor(Math.random() * cfg.names.length)] || \"无名\";")
    L.append("    }")
    L.append("")
    L.append("    // ---- 连续时代背景表（覆盖公元前1600年至公元2150年及以外，全无间断）----")
    L.append("    const GRAND_ERA_TABLE = [")
    for upper, name, desc in C.GRAND_ERA_BUCKETS:
        L.append("      [%s, %s, %s]," % ("null" if upper is None else upper, C.js_str(name), C.js_str(desc)))
    L.append("    ];")
    L.append("")
    L.append("    function resolveEraDetails(year, epochMode) {")
    L.append("      for (let i = 0; i < GRAND_ERA_TABLE.length; i++) {")
    L.append("        const row = GRAND_ERA_TABLE[i];")
    L.append("        if (row[0] === null || year < row[0]) return { name: row[1], desc: row[2] };")
    L.append("      }")
    L.append("      const last = GRAND_ERA_TABLE[GRAND_ERA_TABLE.length - 1];")
    L.append("      return { name: last[1], desc: last[2] };")
    L.append("    }")
    L.append("")
    L.append("    function formatYearOnly(year) {")
    L.append("      const y = Math.round(year);")
    L.append("      if (y < 0) return `公元前 ${Math.abs(y)} 年`;")
    L.append("      if (y === 0) return '公元元年';")
    L.append("      return `公元 ${y} 年`;")
    L.append("    }")
    L.append("    function formatYearMonth(year, month) {")
    L.append("      const m = month || 1;")
    L.append("      return `${formatYearOnly(year)} ${m}月`;")
    L.append("    }")
    L.append("    function randomMonth() { return Math.floor(Math.random() * 12) + 1; }")
    L.append("")
    L.append("    // 一生穿越过的所有大时代（按时间顺序去重）")
    L.append("    function listErasBetween(y0, y1) {")
    L.append("      const out = [];")
    L.append("      const a = Math.round(Math.min(y0, y1)), b = Math.round(Math.max(y0, y1));")
    L.append("      for (let y = a; y <= b; y++) {")
    L.append("        const n = resolveEraDetails(y, null).name;")
    L.append("        if (out[out.length - 1] !== n) out.push(n);")
    L.append("      }")
    L.append("      if (out.length === 0) out.push(resolveEraDetails(a, null).name);")
    L.append("      return out;")
    L.append("    }")
    L.append("")

    # 各纪元出身表
    for eid in NEW_EPOCHS:
        mod = DATA[eid]
        L.append("    // ---- %s 出身地域（8）与门第阶层（10）----" % getattr(mod, "EPOCH_ID", eid))
        L.append("    const %s_REGIONS = [" % eid.upper())
        L.append(",\n".join(C.region_to_js(r) for r in mod.REGIONS))
        L.append("    ];")
        L.append("    const %s_SOCIAL_STRATA = [" % eid.upper())
        L.append(",\n".join(C.strata_to_js(s) for s in mod.STRATA))
        L.append("    ];")
        L.append("")

    # 各纪元 16 阶段事件池
    for eid in NEW_EPOCHS:
        mod = DATA[eid]
        L.append("    // ---- %s 16 大生命阶段事件池（每阶段多个候选，单局随机抽取）----" % eid)
        L.append("    const %s_STAGE_POOLS = [" % eid.upper())
        stages = []
        for i, st in enumerate(mod.STAGE_EVENTS):
            evs = ",\n".join(C.event_to_js(ev, i) for ev in st)
            stages.append("      [\n%s\n      ]" % evs)
        L.append(",\n".join(stages))
        L.append("    ];")
        L.append("")

    L.append("    // ---- 出身表 / 事件池 按纪元统一取用 ----")
    L.append("    function getEpochOriginTables(id) {")
    L.append("      if (id === \"ancient\") return { regions: ANCIENT_REGIONS, strata: ANCIENT_SOCIAL_STRATA };")
    L.append("      if (id === \"premodern\") return { regions: PREMODERN_REGIONS, strata: PREMODERN_SOCIAL_STRATA };")
    L.append("      if (id === \"modern\") return { regions: MODERN_REGIONS, strata: MODERN_SOCIAL_STRATA };")
    L.append("      if (id === \"contemporary\") return { regions: PAST_REGIONS, strata: PAST_SOCIAL_STRATA };")
    L.append("      return { regions: FUTURE_REGIONS, strata: FUTURE_SOCIAL_STRATA };")
    L.append("    }")
    L.append("    function getEpochStagePools(id) {")
    L.append("      if (id === \"ancient\") return ANCIENT_STAGE_POOLS;")
    L.append("      if (id === \"premodern\") return PREMODERN_STAGE_POOLS;")
    L.append("      if (id === \"modern\") return MODERN_STAGE_POOLS;")
    L.append("      if (id === \"contemporary\") return PAST_STAGE_POOLS;")
    L.append("      return FUTURE_STAGE_POOLS;")
    L.append("    }")
    L.append("")
    L.append("" )
    L.append("// 各纪元货币单位：避免先秦人生出现「万元」这类时代错位")
    L.append("function wealthUnit(epochId) {")
    L.append('  if (epochId === "ancient") return "两金";')
    L.append('  if (epochId === "premodern") return "两银";')
    L.append('  if (epochId === "modern") return "块银元";')
    L.append('  if (epochId === "contemporary") return "万元";')
    L.append('  return "信用点";')
    L.append("}")
    L.append("")
    L.append("function wealthUnitShort(epochId) {")
    L.append('  if (epochId === "ancient") return "两";')
    L.append('  if (epochId === "premodern") return "两";')
    L.append('  if (epochId === "modern") return "元";')
    L.append('  if (epochId === "contemporary") return "万";')
    L.append('  return "点";')
    L.append("}")
    return "\n".join(L) + "\n"


EPOCH_CARDS = '''        <!-- 时代纪元自主选择 / 随机投放（五大文明纪元） -->
        <div class="max-w-2xl mx-auto mb-4 bg-zinc-900/60 p-3 rounded-lg border border-zinc-800 text-left font-sans-sc">
          <div class="flex items-center justify-between mb-2 gap-2">
            <span class="text-xs font-bold text-amber-300 flex items-center">
              <span>⏳ 时代纪元定位（公元前1600年 ~ 公元2150年，可自选或随机）：</span>
            </span>
            <button onclick="pickRandomEpochMode()" class="shrink-0 text-[11px] px-2 py-1 rounded bg-zinc-800 hover:bg-zinc-700 text-amber-300 border border-zinc-700">
              🎲 随机投掷时代
            </button>
          </div>
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs" id="epoch-card-grid"></div>
          <p class="text-[10px] text-zinc-500 mt-2 leading-relaxed">
            投胎年份将在所选纪元区间内全域随机，出生月亦随机；一生将随年代推移自动切换时代背景与事件，直至晚年。
          </p>
        </div>

'''

EPOCH_UI_JS = '''    // 动态渲染五大纪元选择卡（支持手机单列 / 桌面双列）
    function renderEpochCards() {
      const grid = document.getElementById('epoch-card-grid');
      if (!grid) return;
      const tone = {
        amber: "border-amber-500/70 bg-amber-950/30 text-amber-200",
        emerald: "border-emerald-500/70 bg-emerald-950/30 text-emerald-200",
        rose: "border-rose-500/70 bg-rose-950/30 text-rose-200",
        sky: "border-sky-500/70 bg-sky-950/30 text-sky-200",
        purple: "border-purple-500/70 bg-purple-950/30 text-purple-200"
      };
      grid.innerHTML = CIVILIZATION_EPOCHS.map(e => {
        const on = (e.id === selectedEpochMode);
        const cls = on ? tone[e.colorClass] : "border-zinc-700/80 bg-zinc-800/80 text-zinc-200";
        return `
        <label class="flex items-start p-2.5 rounded-lg border cursor-pointer hover:border-amber-400/60 transition ${cls}">
          <input type="radio" name="epoch_mode" value="${e.id}" ${on ? 'checked' : ''}
                 onchange="onEpochModeChange('${e.id}')" class="mt-0.5 mr-2 text-amber-500 focus:ring-0">
          <div class="min-w-0">
            <div class="font-bold flex items-center gap-1">
              <span>${e.eraIcon}</span><span class="truncate">${e.name}</span>
            </div>
            <div class="text-[10px] opacity-80 mt-0.5">${e.subTitle} · ${e.badge}</div>
          </div>
        </label>`;
      }).join('');
    }

    function syncEpochCards() {
      const radios = document.getElementsByName('epoch_mode');
      if (radios && radios.forEach) {
        radios.forEach(r => {
          if (r.value === selectedEpochMode) r.checked = true;
          r.parentElement && r.parentElement.className &&
            r.parentElement.classList.toggle('ring-2', r.value === selectedEpochMode);
        });
      }
      renderEpochCards();
    }

'''


def main():
    load_data()

    path = 'index.html'
    html = open(path, encoding='utf-8').read()
    orig_len = len(html)

    # ---------------- 1. 程序化出身：改为按纪元查表 ----------------
    i = line_start(html, html.index("function generateProceduralOrigin(epochMode) {"))
    j = line_start(html, html.index("const RANDOM_TRAITS = [", i))
    new_origin = '''    function generateProceduralOrigin(epochId) {
      const tables = getEpochOriginTables(epochId);
      const regions = tables.regions;
      const strataList = tables.strata;

      const region = regions[Math.floor(Math.random() * regions.length)];
      const strata = strataList[Math.floor(Math.random() * strataList.length)];

      const title = `${region.name.slice(0, 5)} · ${strata.title}`;
      const desc = `降生于【${region.name}】。${region.desc}；家庭是【${strata.title}】，${strata.desc}。`;

      const statMod = {
        health: strata.statMod.health + (region.stat.health || 0),
        wealth: +(strata.statMod.wealth + (region.stat.wealth || 0)).toFixed(1),
        intellect: strata.statMod.intellect + (region.stat.intellect || 0),
        happiness: strata.statMod.happiness + (region.stat.happiness || 0),
        luck: strata.statMod.luck + (region.stat.luck || 0),
        rep: strata.statMod.rep + (region.stat.rep || 0)
      };

      return {
        id: "origin_" + Math.random().toString(36).slice(2, 8),
        title,
        desc,
        regionName: region.name,
        strataTitle: strata.title,
        statMod,
        trait: strata.trait,
        eraFlavor: strata.desc
      };
    }

'''
    html = html[:i] + new_origin + html[j:]

    # ---------------- 2. 删除旧的两纪元时代解析器（由 pack 提供） ----------------
    i = line_start(html, html.index("// --- 动态连续历史/未来大时代背景解析器"))
    j = line_start(html, html.index("function generateRandomDestiny() {", i))
    html = html[:i] + html[j:]

    # ---------------- 3. 命运生成：任意纪元 + 任意年月 ----------------
    i = line_start(html, html.index("function generateRandomDestiny() {"))
    j = line_start(html, html.index("function rollNewDestiny() {", i))
    new_destiny = '''    function generateRandomDestiny() {
      const cfg = getEpochConfig(selectedEpochMode);

      // 出生年份在该纪元区间内全域随机；出生月份亦随机（1-12月）
      const birthYear = Math.floor(Math.random() * (cfg.maxYear - cfg.minYear + 1)) + cfg.minYear;
      const birthMonth = randomMonth();

      // 出身家庭按该纪元的地域 × 阶层组合程序化生成
      const origin = generateProceduralOrigin(cfg.id);
      const trait = RANDOM_TRAITS[Math.floor(Math.random() * RANDOM_TRAITS.length)];

      const deltaHealth = Math.floor(Math.random() * 9) - 4;
      const deltaIntellect = Math.floor(Math.random() * 9) - 4;
      const deltaLuck = Math.floor(Math.random() * 15) - 7;

      const health = Math.max(70, Math.min(100, origin.statMod.health + (trait.mod.health || 0) + deltaHealth));
      const wealth = Math.max(0.1, +(origin.statMod.wealth + (trait.mod.wealth || 0) + (Math.random() * 1.5 - 0.7)).toFixed(1));
      const intellect = Math.max(40, Math.min(95, origin.statMod.intellect + (trait.mod.intellect || 0) + deltaIntellect));
      const happiness = Math.max(40, Math.min(95, origin.statMod.happiness + (trait.mod.happiness || 0)));
      const luck = Math.max(25, Math.min(95, origin.statMod.luck + (trait.mod.luck || 0) + deltaLuck));

      return {
        epochMode: cfg.id,
        birthYear,
        birthMonth,
        origin,
        trait,
        health,
        wealth,
        intellect,
        happiness,
        luck,
        rep: origin.statMod.rep
      };
    }

'''
    html = html[:i] + new_destiny + html[j:]

    # ---------------- 4. 纪元切换 / 随机投掷（五选一） ----------------
    old_switch = '''    function pickRandomEpochMode() {
      soundDice();
      selectedEpochMode = Math.random() < 0.5 ? "past" : "future";
      const radios = document.getElementsByName('epoch_mode');
      radios.forEach(r => {
        r.checked = (r.value === selectedEpochMode);
      });
      rollNewDestiny();
    }'''
    new_switch = '''    function pickRandomEpochMode() {
      soundDice();
      const idx = Math.floor(Math.random() * CIVILIZATION_EPOCHS.length);
      selectedEpochMode = CIVILIZATION_EPOCHS[idx].id;
      syncEpochCards();
      rollNewDestiny();
    }'''
    html = replace_js_function(html, "function pickRandomEpochMode() {", new_switch + "\n", "pickRandomEpochMode")

    old_change = '''    function onEpochModeChange(mode) {
      selectedEpochMode = mode;
      rollNewDestiny();
    }'''
    new_change = '''    function onEpochModeChange(mode) {
      selectedEpochMode = mode;
      syncEpochCards();
      rollNewDestiny();
    }'''
    html = replace_js_function(html, "function onEpochModeChange(mode) {", new_change + "\n", "onEpochModeChange")

    # ---------------- 5. 投胎卡片文案：显示纪元名 + 年月 ----------------
    old_line = """
      document.getElementById('init-era-text').innerText = `${currentDestinyDraft.birthYear}年 · ${yearInfo.name}`;"""
    new_line = """      const draftCfg = getEpochConfig(currentDestinyDraft.epochMode);
      document.getElementById('init-era-text').innerText =
        `${draftCfg.eraIcon} ${draftCfg.name} · ${formatYearMonth(currentDestinyDraft.birthYear, currentDestinyDraft.birthMonth)} · ${yearInfo.name}`;"""
    assert old_line in html
    html = html.replace(old_line, new_line, 1)

    # ---------------- 5b. 货币单位随纪元变化（HUD 徽章 + 终局结算） ----------------
    old_title = 'title="财富总额 (万元)"'
    assert old_title in html, "wealth badge title not found"
    html = html.replace(old_title, 'id="wealth-badge" title="财富总额"', 1)
    old_hud = "document.getElementById('val-wealth').innerText = player.wealth >= 0 ? `${player.wealth.toFixed(1)}万` : `负债${Math.abs(player.wealth).toFixed(1)}万`;"
    assert old_hud in html, "val-wealth HUD line not found"
    new_hud = ("const _wuShort = wealthUnitShort(player.epochMode);\n"
               "      document.getElementById('val-wealth').innerText = player.wealth >= 0 ? `${player.wealth.toFixed(1)}${_wuShort}` : `负债${Math.abs(player.wealth).toFixed(1)}${_wuShort}`;\n"
               "      document.getElementById('wealth-badge').title = `财富总额 (${wealthUnit(player.epochMode)})`;")
    html = html.replace(old_hud, new_hud, 1)
    old_end_w = "document.getElementById('end-val-wealth').innerText = `${player.wealth.toFixed(1)} 万元`;"
    assert old_end_w in html, "end-val-wealth line not found"
    new_end_w = "document.getElementById('end-val-wealth').innerText = `${player.wealth.toFixed(1)} ${wealthUnit(player.epochMode)}`;"
    html = html.replace(old_end_w, new_end_w, 1)
    print("  patched: epoch-aware currency unit (web)")

    # ---------------- 5d. 人生轨迹关键词扩展：覆盖先秦至近代语汇 ----------------
    _tk_old = ['/考编|公务员|体制|军旅|入伍|纪检|行政|公职|团长|协调官|防御|上岸|保供/', '/经商|淘宝|电商|创业|个体户|操盘|股市|商海|小行星|矿业|水务|买房|信托|首富|红利/', '/无线电|实验室|论文|科研|工程师|算法|智脑|黑客|聚变|脑机|量子|质子|核能/', '/乐队|摇滚|武侠|自由|海岛|江湖|茶楼|房车|诗社|民宿|艺术|写诗/']
    _tk_new = ['/考编|公务员|体制|军旅|入伍|纪检|行政|公职|团长|协调官|防御|上岸|保供|科举|功名|为吏|衙门|官场|朝廷|仕途|幕僚|举人|进士|孝廉|征辟|辟召|刺史|太守|县令|士大夫|戍边|烽燧|投军|从军|行伍|参军|支前|干部|大队|公社|革委会|编制|出仕/', '/经商|淘宝|电商|创业|个体户|操盘|股市|商海|小行星|矿业|水务|买房|信托|首富|红利|商号|票号|盐铁|牙行|市舶|货殖|贩运|商队|胡商|绸缎|茶马|当铺|钱庄|作坊|机户|铺子|买卖|田产|织造|十三行|合伙|开厂|车间|技术员|承包|学徒|柜上/', '/无线电|实验室|论文|科研|工程师|算法|智脑|黑客|聚变|脑机|量子|质子|核能|读书|经书|竹简|著述|治学|书院|私塾|蒙学|游学|太学|拜师|医术|本草|郎中|针灸|算学|历法|图纸|夜校|师范|学堂/', '/乐队|摇滚|武侠|自由|海岛|江湖|茶楼|房车|诗社|民宿|艺术|写诗|诗词|书画|琴|社戏|游侠|隐逸|归隐|山水|田园|寺院|清谈|雅集|杂剧|刻书|藏书|戏班|票友/']
    for _o, _n in zip(_tk_old, _tk_new):
        assert _o in html, "track regex not found: " + _o
        html = html.replace(_o, _n, 1)
    print("  patched: career-track keywords (web)")

    # ---------------- 5e. 重开一局时重置人生轨迹，避免上一局残留 ----------------
    _reset_old = """      player.randomEventsTriggered = [];
      player.isDead = false;
      currentEventIndex = 0;"""
    _reset_new = """      player.randomEventsTriggered = [];
      player.isDead = false;
      currentEventIndex = 0;

      // 重置人生轨迹与社会坐标，避免上一局的数据残留到本局
      player.trackScores = { "体制政务": 0, "商海实业": 0, "学术科技": 0, "文艺江湖": 0, "守拙布衣": 0 };
      player.careerTrack = "守拙自持";
      player.socialRank = "风雨布衣";"""
    assert _reset_old in html, "startGame reset block not found"
    html = html.replace(_reset_old, _reset_new, 1)
    print("  patched: per-run trajectory reset (web)")

    # ---------------- 5f. 轨迹权重再平衡：命中赛道 +4，寻常度日 +1 ----------------
    _tails = [
        ("|出仕/", "|出仕|差役|里正|保长|粮长|驿丞|公文|文书|官/"),
        ("|柜上/", "|柜上|行商|验货|记账|货价|借贷|告贷|典当|田契|田亩|租佃|钱粮|贩货|营生/"),
        ("|师范|学堂/", "|师范|学堂|抄书|苦读|灯油|方剂|匠作|营造|先生|游历|问道/"),
        ("|戏班|票友/", "|戏班|票友|诗酒|雅集|田园|寺院|归隐|诗书|游历|闲云/"),
    ]
    for _a, _b in _tails:
        assert _a in html, "track regex tail not found: " + _a
        html = html.replace(_a, _b, 1)
    for _k in ("体制政务", "商海实业", "学术科技", "文艺江湖"):
        _o = 'player.trackScores["%s"] += 2;' % _k
        _n = 'player.trackScores["%s"] += 4;' % _k
        assert _o in html, "track weight not found: " + _k
        html = html.replace(_o, _n, 1)
    print("  patched: career-track weighting (web)")

    # ---------------- 6. 单局事件组装：按“该阶段所处年代”取对应纪元的事件池 ----------------
    i = line_start(html, html.index("function assembleDynamicSessionEvents(epochMode) {"))
    j = line_start(html, html.index("// --- 游戏运行态控制 ---", i))
    new_assemble = '''    // 为单局游戏动态组装 16 个事件：以“该阶段实际所处的年代”决定取自哪个纪元的事件池，
    // 因此一个横跨数十年乃至数百年的生命，会自然经历古代 -> 近世 -> 当代 -> 未来的时代切换。
    function assembleDynamicSessionEvents(birthYear) {
      const timeline = generateRandomTimeline();
      let assembled = [];

      for (let i = 0; i < timeline.length; i++) {
        const stageAge = timeline[i];
        const year = birthYear + stageAge;
        const eraId = getEpochIdForYear(year);
        const pools = getEpochStagePools(eraId);
        const pool = pools[i] || pools[pools.length - 1];
        const pickedEvent = pool[Math.floor(Math.random() * pool.length)];

        assembled.push({
          ...pickedEvent,
          stageIndex: i,
          assignedAge: stageAge,
          eraId: eraId,
          getAge: () => stageAge,
          getYear: (b) => b + stageAge
        });
      }
      return assembled;
    }

'''
    html = html[:i] + new_assemble + html[j:]

    # ---------------- 7. startGame：传入出生年 + 记录出生月 + 纪元取名 ----------------
    old_start = """      player.epochMode = currentDestinyDraft.epochMode;
      player.birthYear = currentDestinyDraft.birthYear;"""
    new_start = """      player.epochMode = currentDestinyDraft.epochMode;
      player.birthYear = currentDestinyDraft.birthYear;
      player.birthMonth = currentDestinyDraft.birthMonth;"""
    assert old_start in html
    html = html.replace(old_start, new_start, 1)

    old_call = "      activeEpochEvents = assembleDynamicSessionEvents(player.epochMode);"
    new_call = "      activeEpochEvents = assembleDynamicSessionEvents(player.birthYear);"
    assert old_call in html
    html = html.replace(old_call, new_call, 1)

    old_name = "      player.name = nameInput || DEFAULT_NAMES[Math.floor(Math.random() * DEFAULT_NAMES.length)];"
    new_name = "      player.name = nameInput || pickEpochName(player.epochMode);"
    assert old_name in html
    html = html.replace(old_name, new_name, 1)

    # ---------------- 8. 突发事件池：按当前年代所属纪元选择 ----------------
    old_rand = """      const randPool = (player.epochMode === "past") ? PAST_RANDOM_EVENTS : FUTURE_RANDOM_EVENTS;"""
    new_rand = """      const randPool = isFutureEpoch(getEpochIdForYear(year)) ? FUTURE_RANDOM_EVENTS : PAST_RANDOM_EVENTS;"""
    assert old_rand in html
    html = html.replace(old_rand, new_rand, 1)

    # ---------------- 9. 终局评定：新增古典纪元专属宿命 ----------------
    old_flag = '      const isFuture = (player.epochMode === "future");'
    new_flag = ('      const isFuture = isFutureEpoch(player.epochMode);\n'
                '      const isClassical = isClassicalEpoch(player.epochMode);\n'
                '      const eraCfg = getEpochConfig(player.epochMode);')
    assert old_flag in html
    html = html.replace(old_flag, new_flag, 1)

    anchor = '''      } else {
        if (w >= 45 && hap >= 55) {
          return {
            archetype: "时代弄潮翁 · 功成身退",'''
    classical = '''      } else if (isClassical) {
        if (w >= 30 && player.reputation >= 60) {
          return {
            archetype: "名标青史 · 一世风流",
            epitaph: `你的名字被郑重写进了${eraCfg.legacyNoun}，与那个时代的山川人物并列。富贵或已散去，声名却比血肉活得更久。`
          };
        } else if (w >= 15 && hap < 45) {
          return {
            archetype: "负重跋涉者 · 寒暑苦行",
            epitaph: "你一生都在为一族人的口粮与体面奔波，风霜刻在额角，未曾有一日懈怠，也未曾真正为自己活过。"
          };
        } else if (hap >= 70 && w < 15) {
          return {
            archetype: "林泉散人 · 自在一生",
            epitaph: "不慕朱门车马，只爱一壶浊酒、半亩薄田。你以清贫换得心安，是那个时代少数真正自由的人。"
          };
        } else if (i >= 78) {
          return {
            archetype: "明哲通达 · 洞观兴替",
            epitaph: "你冷眼看尽王朝更迭与人事翻覆，读懂了兴衰的规律，因而对世人多了一份悲悯与宽恕。"
          };
        } else if (player.age < 50) {
          return {
            archetype: "断弦流星 · 孤勇悲歌",
            epitaph: "乱世里的性命如风中烛火，你疾行过，灿然过，终是太早熄灭了。山河依旧，只是再无你的消息。"
          };
        } else {
          return {
            archetype: "烟火凡人 · 坚韧一生",
            epitaph: "你没有在史书上留下一行字，却用一粥一饭把血脉与家训传了下去。这本身就是了不起的功业。"
          };
        }
''' + anchor
    assert anchor in html, "archetype anchor not found"
    html = html.replace(anchor, classical, 1)

    # ---------------- 10. 时代长河回响：按实际跨越的时代生成 ----------------
    i = line_start(html, html.index("function generateEraReflection() {"))
    j = line_start(html, html.index("function generateVividBiography() {", i))
    new_reflection = '''    function generateEraReflection() {
      const p = player;
      const originTitle = p.origin ? p.origin.title : "寻常人家";
      const deathYear = p.birthYear + p.age;
      const birthInfo = resolveEraDetails(p.birthYear, null);
      const deathInfo = resolveEraDetails(deathYear, null);
      const eras = listErasBetween(p.birthYear, deathYear);
      const cfg = getEpochConfig(p.epochMode);

      let text = `${p.name} 于 ${formatYearMonth(p.birthYear, p.birthMonth)} 降生于【${originTitle}】。`;
      text += `\\n出生之时的天下底色是「${birthInfo.name}」——${birthInfo.desc}`;
      text += `\\n此后 ${p.age} 年间，其一生先后穿越 ${eras.length} 重大时代：${eras.join(" → ")}。`;
      if (deathInfo.name !== birthInfo.name) {
        text += `\\n辞世之时，世道已是「${deathInfo.name}」——${deathInfo.desc}`;
      }
      text += `\\n${cfg.desc}`;
      text += `\\n大时代每一次翻覆重构，都在这一个普通生命的悲欢离合里，留下了深浅不一的年轮。`;
      return text;
    }

'''
    html = html[:i] + new_reflection + html[j:]

    # ---------------- 11. 导出文案中的纪元名称 ----------------
    old_export = """纪元模式：${player.epochMode === 'past' ? '过去纪元' : '未来纪元'}"""
    new_export = """所属纪元：${getEpochConfig(player.epochMode).name}（${formatYearMonth(player.birthYear, player.birthMonth)} 生）"""
    assert old_export in html
    html = html.replace(old_export, new_export, 1)

    # ---------------- 12. 结局页生平年代表述（含出生月） ----------------
    old_life = """      document.getElementById('end-lifespan').innerText = `${player.birthYear} - ${endYear} · 享年 ${player.age} 岁 · ${deathReason}`;"""
    new_life = """      document.getElementById('end-lifespan').innerText =
        `${formatYearMonth(player.birthYear, player.birthMonth)} - ${formatYearOnly(endYear)} · 享年 ${player.age} 岁 · ${deathReason}`;"""
    assert old_life in html
    html = html.replace(old_life, new_life, 1)

    # ---------------- 13. 纪元选择 UI ----------------
    i = html.index("        <!-- 时代跨度自主选择 / 随机投放 -->")
    j = html.index("        <!-- 随机投胎抽卡卡片 -->", i)
    html = html[:i] + EPOCH_CARDS + html[j:]

    # ---------------- 14. player 状态：出生月 ----------------
    old_state = """      birthYear: 1982,
      origin: null,"""
    new_state = """      birthYear: 1982,
      birthMonth: 1,
      origin: null,"""
    assert old_state in html
    html = html.replace(old_state, new_state, 1)

    old_sel = '    let selectedEpochMode = "past"; // "past" | "future"'
    new_sel = '    let selectedEpochMode = "contemporary"; // 五大纪元 id: ancient | premodern | modern | contemporary | future'
    assert old_sel in html
    html = html.replace(old_sel, new_sel, 1)

    old_pmode = '      epochMode: "past",\n      birthYear: 1982,'
    new_pmode = '      epochMode: "contemporary",\n      birthYear: 1982,'
    assert old_pmode in html
    html = html.replace(old_pmode, new_pmode, 1)

    # ---------------- 15. 初始化：渲染纪元卡 + 默认选卡 ----------------
    old_boot = """    const defaultRadio = document.querySelector('input[name="epoch_mode"][value="past"]');"""
    new_boot = """    renderEpochCards();
    const defaultRadio = document.querySelector('input[name="epoch_mode"][value="' + selectedEpochMode + '"]');"""
    assert old_boot in html
    html = html.replace(old_boot, new_boot, 1)

    # ---------------- 16. 注入纪元数据与函数包 ----------------
    marker = "    const DEFAULT_NAMES = ["
    assert marker in html
    html = html.replace(marker, build_js_pack() + "\n" + EPOCH_UI_JS + marker, 1)

    open(path, 'w', encoding='utf-8').write(html)
    print("index.html: %d -> %d chars (+%d)" % (orig_len, len(html), len(html) - orig_len))


if __name__ == '__main__':
    main()
