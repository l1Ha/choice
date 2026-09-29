// 临时验证脚本：在 Node 中以最小 DOM 模拟完整跑通《浮生录》Web 版
const fs = require('fs'), vm = require('vm'), path = require('path');
const ROOT = path.dirname(__dirname);
const html = fs.readFileSync(path.join(ROOT, 'index.html'), 'utf8');
// 按出现顺序收集脚本：本地外链脚本从磁盘读入，CDN 等远端脚本跳过执行
const scripts = [];
{
  const tagRe = /<script([^>]*)>([\s\S]*?)<\/script>/gi;
  let m;
  while ((m = tagRe.exec(html)) !== null) {
    const src = (m[1].match(/src=["']([^"']+)["']/) || [])[1];
    if (src) {
      if (/^(https?:)?\/\//.test(src)) { scripts.push({ label: src, external: true, code: '' }); continue; }
      const file = path.join(ROOT, src.replace(/^\.\//, ''));
      scripts.push({ label: src, code: fs.readFileSync(file, 'utf8') });
    } else {
      scripts.push({ label: 'inline#' + scripts.length, code: m[2] });
    }
  }
}

let synthOk = true;
scripts.forEach((s, i) => {
  if (s.external) return;
  try { new vm.Script(s.code, { filename: s.label }); console.log('Script ' + i + ' (' + s.label + ') syntax: OK!'); }
  catch (e) { synthOk = false; console.error('Script ' + i + ' (' + s.label + ') ERROR:', e.message); }
});

const els = {};
function mkEl(id) {
  const el = {
    id, children: [], value: '', checked: false,
    style: {}, className: '', _innerHTML: '', _innerText: '',
    classList: { add() {}, remove() {}, toggle() {}, contains() { return false; } },
    addEventListener() {}, setAttribute() {}, getAttribute() { return null; },
    appendChild(c) { this.children.push(c); return c; },
    removeChild() {}, querySelector() { return mkEl('q'); }, querySelectorAll() { return []; },
    parentElement: null, dataset: {}
  };
  Object.defineProperty(el, 'innerHTML', { get() { return this._innerHTML; }, set(v) { this._innerHTML = v; this.children = []; } });
  Object.defineProperty(el, 'innerText', { get() { return this._innerText; }, set(v) { this._innerText = v; } });
  return el;
}
const getEl = (id) => (els[id] = els[id] || mkEl(id));
function textOf(el) {
  if (!el) return '';
  let t = (el._innerText || '') + ' ' + (el._innerHTML || '');
  for (const k of (el.children || [])) t += ' ' + textOf(k);
  return t;
}

const ctx = {
  __els: els, __text: textOf, __getEl: getEl,
  window: { addEventListener() {} },
  document: {
    getElementById: getEl,
    createElement: (tag) => mkEl('new:' + tag),
    querySelectorAll: () => [],
    querySelector: () => mkEl('q'),
    getElementsByName: () => []
  },
  navigator: { serviceWorker: { register: () => Promise.resolve() } },
  AudioContext: function () {
    return {
      createGain: () => ({ connect() {}, gain: { setValueAtTime() {}, exponentialRampToValueAtTime() {} } }),
      createOscillator: () => ({ connect() {}, start() {}, stop() {}, frequency: { setValueAtTime() {}, exponentialRampToValueAtTime() {} } }),
      currentTime: 0
    };
  },
  Math, console, setTimeout, clearTimeout, Date, JSON
};
vm.createContext(ctx);

const code = scripts.filter(s => !s.external).map(s => s.code).join('\n;\n');

const harness = `;(function(){
const R = {};
R.epochs = CIVILIZATION_EPOCHS.map(e => e.id + ' ' + e.eraIcon + ' ' + e.name + ' [' + e.minYear + ',' + e.maxYear + ']');
R.eraContinuity = [-1600,-1046,-221,9,265,618,960,1279,1368,1644,1840,1912,1937,1949,1958,1978,1992,2003,2024,2035,2050,2100,2300]
  .map(y => y + ':' + resolveEraDetails(y, null).name);

// 1) 全纪元事件池与选项可用性
let ev = 0, ch = 0, missingFail = 0;
CIVILIZATION_EPOCHS.forEach(e => {
  [e.minYear, e.minYear + 17, (e.minYear + e.maxYear) >> 1, e.maxYear - 3, e.maxYear].forEach(by => {
    const evs = assembleDynamicSessionEvents(by);
    if (evs.length !== 16) throw new Error('stage count ' + by);
    evs.forEach((x, i) => {
      ev++;
      if (!x.title || !x.narrative || !x.period) throw new Error('bad event ' + by + ' ' + i);
      if (!x.choices || x.choices.length < 2) throw new Error('bad choices');
      if (typeof x.getAge() !== 'number' || typeof x.getYear() !== 'number') throw new Error('bad getters');
      if (typeof x.narrative(player, x.getYear()) !== 'string') throw new Error('narrative not string');
      x.choices.forEach(c => {
        ch++;
        const n = c.successChance(player);
        if (typeof n !== 'number' || !isFinite(n) || n < 0 || n > 100) throw new Error('chance ' + n);
        if (!c.text || !c.successFeedback) throw new Error('choice text missing');
        if (n < 100 && !c.failFeedback) missingFail++;
      });
    });
  });
});
R.totals = { events: ev, choices: ch, missingFailFeedback: missingFail };

// 2) 投胎随机性：每纪元 400 次
R.randomness = {};
CIVILIZATION_EPOCHS.forEach(e => {
  const ys = new Set(), os = new Set(), ms = new Set(), combos = new Set();
  for (let i = 0; i < 400; i++) {
    selectedEpochMode = e.id;
    const d = generateRandomDestiny();
    if (d.birthYear < e.minYear || d.birthYear > e.maxYear) throw new Error('year out of range ' + e.id);
    if (d.birthMonth < 1 || d.birthMonth > 12) throw new Error('month');
    if (!d.origin.title || !d.trait.name) throw new Error('origin/trait');
    ys.add(d.birthYear); os.add(d.origin.title); ms.add(d.birthMonth); combos.add(d.origin.regionName + '|' + d.origin.strataTitle);
  }
  R.randomness[e.id] = { yearSpan: Math.max(...ys) - Math.min(...ys), distinctBirthYears: ys.size, distinctOrigins: os.size, distinctMonths: ms.size, distinctCombos: combos.size };
});

// 3) 完整人生模拟：每纪元 20 条，随机作选，跑通传记与宿命评定
let bioLens = [], archetypes = new Set(), titles = new Set(), ranks = new Set(), tracks = new Set();
for (let t = 0; t < 100; t++) {
  const e = CIVILIZATION_EPOCHS[t % CIVILIZATION_EPOCHS.length];
  selectedEpochMode = e.id;
  const d = generateRandomDestiny();
  currentDestinyDraft = d;
  player.gender = d.gender;
  player.name = pickEpochName(e.id, d.gender);
  player.epochMode = d.epochMode; player.birthYear = d.birthYear; player.birthMonth = d.birthMonth;
  player.origin = d.origin; player.trait = d.trait;
  player.health = d.health; player.wealth = d.wealth; player.intellect = d.intellect;
  player.happiness = d.happiness; player.luck = d.luck; player.reputation = d.rep;
  player.tags = [d.origin.trait, d.trait.name, d.gender === 'female' ? '巾帼女史' : '须眉男儿'];
  player.age = 0; player.history = []; player.keyChoices = []; player.randomEventsTriggered = [];
  player.randomEvents = []; player.isDead = false; player.deathReason = '寿终正寝';
  player.family = initializeFamily(player);
  player.familyLogs = [];
  player.trackScores = { '体制政务': 0, '商海实业': 0, '学术科技': 0, '文艺江湖': 0, '守拙布衣': 0 };
  player.careerTrack = ''; player.socialRank = '';

  const evs = assembleDynamicSessionEvents(d.birthYear, d.gender);
  activeEpochEvents = evs;
  for (let si = 0; si < evs.length; si++) {
    if (player.health <= 12) { player.deathReason = '积劳成疾，中年早逝'; break; }
    currentEventIndex = si;
    const x = evs[si];
    player.age = x.getAge();
    titles.add(x.title);
    advanceFamily(player, player.age, d.birthYear + player.age);
    // 走真实的抉择结算管线（含人生轨迹研判与社会坐标评定）
    handleChoiceSelection(Math.floor(Math.random() * x.choices.length));
  }

  const endYear = player.birthYear + player.age;
  __getEl('end-player-name').innerText = player.name;
  __getEl('end-lifespan').innerText = formatYearMonth(player.birthYear, player.birthMonth) + ' - ' + formatYearOnly(endYear);
  __getEl('end-val-wealth').innerText = player.wealth.toFixed(1) + ' ' + wealthUnit(player.epochMode);
  const reflRaw = generateEraReflection();
  renderFamilyEnding();
  generateVividBiography();
  const arch = evaluateLifeArchetype();
  if (!arch || typeof arch.archetype !== 'string' || !arch.archetype) throw new Error('archetype missing for ' + e.id);
  if (!arch.epitaph || arch.epitaph.length < 10) throw new Error('epitaph missing for ' + e.id);
  __getEl('end-archetype').innerText = arch.archetype;
  __getEl('end-quote').innerText = arch.epitaph;

  const bioTxt = __text(__els["end-biography"]);
  if (bioTxt.replace(/\\s/g, '').length < 150) throw new Error('biography too short (' + bioTxt.length + ') for ' + e.id);
  bioLens.push(bioTxt.length);
  const refl = (typeof reflRaw === 'string' && reflRaw) ? reflRaw : __text(__els['end-era-reflection']);
  if (refl.replace(/\\s/g, '').length < 40) throw new Error('era reflection too short for ' + e.id);
  archetypes.add(__getEl('end-archetype').innerText);
  ranks.add(player.socialRank); tracks.add(player.careerTrack);
}

R.sim = { lives: 100, distinctEventTitlesSeen: titles.size,
  bioLen: { min: Math.min(...bioLens), max: Math.max(...bioLens) },
  distinctArchetypes: archetypes.size, archetypes: [...archetypes].slice(0, 8),
  distinctTracks: tracks.size, tracks: [...tracks].slice(0, 6),
  distinctRanks: ranks.size, ranks: [...ranks].slice(0, 6) };

// 4) 时代穿越跨度
R.spans = [[-1000, '先秦人'], [600, '盛唐人'], [1500, '明人'], [1840, '清末人'], [1970, '当代人'], [2010, '新千年人'], [2100, '未来人']]
  .map(([by, label]) => {
    const tl = generateRandomTimeline();
    const end = by + tl[tl.length - 1];
    const eras = listErasBetween(by, end);
    return label + ' 生' + by + ' 终' + end + ' 穿越' + eras.length + '个时代';
  });

// 5) 年龄严格递增
for (let i = 0; i < 300; i++) {
  const tl = generateRandomTimeline();
  for (let k = 1; k < tl.length; k++) if (tl[k] <= tl[k - 1]) throw new Error('timeline not monotonic');
}
R.monotonic = 'ok (' + 300 + ' timelines)';
return JSON.stringify(R, null, 1);
})();`;

const out = vm.runInContext(code + harness, ctx);
console.log(out);
process.exit(synthOk ? 0 : 1);
