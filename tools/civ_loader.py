# -*- coding: utf-8 -*-
"""纪元内容装配器：把分片生成的内容（meta + 4 段阶段）组装成完整纪元数据。

分片约定：
  civ_meta_{epoch}.py           ->  REGIONS (8), STRATA (10)
  civ_stages_{epoch}_{k}.py      ->  STAGES，恰好 4 个阶段事件列表，k = 0..3
                                     （对应生命阶段 4k .. 4k+3）
"""

import importlib

EPOCH_IDS = ("ancient", "premodern", "modern")
CHUNKS_PER_EPOCH = 4
STAGES_PER_CHUNK = 4
TOTAL_STAGES = 16


class EpochData(object):
    def __init__(self, eid, regions, strata, stage_events):
        self.id = eid
        self.REGIONS = regions
        self.STRATA = strata
        self.STAGE_EVENTS = stage_events

    def event_count(self):
        return sum(len(s) for s in self.STAGE_EVENTS)

    def __repr__(self):
        return "<EpochData %s regions=%d strata=%d stages=%d events=%d>" % (
            self.id, len(self.REGIONS), len(self.STRATA),
            len(self.STAGE_EVENTS), self.event_count())


def _reload(name):
    mod = importlib.import_module(name)
    return mod


def load(eid, strict=True):
    problems = []
    meta = _reload("civ_meta_%s" % eid)
    regions = list(meta.REGIONS)
    strata = list(meta.STRATA)
    if len(regions) != 8:
        problems.append("%s regions=%d (need 8)" % (eid, len(regions)))
    if len(strata) != 10:
        problems.append("%s strata=%d (need 10)" % (eid, len(strata)))

    stages = []
    for k in range(CHUNKS_PER_EPOCH):
        part = _reload("civ_stages_%s_%d" % (eid, k))
        chunk = list(part.STAGES)
        if len(chunk) != STAGES_PER_CHUNK:
            problems.append("%s chunk %d has %d stages (need %d)"
                            % (eid, k, len(chunk), STAGES_PER_CHUNK))
        stages.extend(chunk)

    if len(stages) != TOTAL_STAGES:
        problems.append("%s total stages=%d (need %d)" % (eid, len(stages), TOTAL_STAGES))

    for i, st in enumerate(stages):
        if not isinstance(st, (list, tuple)) or len(st) < 2:
            problems.append("%s stage %d has %d events (need >=2)"
                            % (eid, i, len(st) if hasattr(st, "__len__") else -1))
            continue
        for j, ev in enumerate(st):
            if not ev.get("title") or not ev.get("choices"):
                problems.append("%s stage %d event %d malformed" % (eid, i, j))
            if len(ev.get("choices", [])) < 2:
                problems.append("%s stage %d event %d has <2 choices" % (eid, i, j))
            if not ev.get("narrative"):
                problems.append("%s stage %d event %d missing narrative" % (eid, i, j))

    if problems:
        msg = "纪元内容校验失败:\n  - " + "\n  - ".join(problems)
        if strict:
            raise AssertionError(msg)
        print(msg)

    return EpochData(eid, regions, strata, stages)


def load_all(strict=True):
    return {eid: load(eid, strict=strict) for eid in EPOCH_IDS}
