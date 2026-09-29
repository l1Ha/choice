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
"""生成网页端纪元内容数据层 data/epochs.js。

内容源：tools/civ_meta_*.py + tools/civ_stages_*.py + tools/civ_women_*.py
本脚本只写 data/epochs.js，不触碰 index.html，因此引擎代码可以安全地独立演进。
"""

import epoch_pack as P

HEADER = '''/* ============================================================================
 * 《浮生录》· 文明长河纪元内容数据层
 *
 * 本文件由 tools/build_epochs_data.py 从 tools/civ_*.py 内容源自动生成，
 * 请勿手工编辑；如需修改时代背景、出身、事件，请改内容源后重新生成。
 *
 * 载入顺序：必须在 index.html 的主脚本之前引入。index.html 中的引擎函数
 * 会引用本文件定义的 CIVILIZATION_EPOCHS / GRAND_ERA_TABLE /
 * ANCIENT_STAGE_POOLS 等顶层常量（调用发生在两个脚本均已执行之后）。
 * ==========================================================================*/

'''


def main():
    P.load_data()
    P.load_women()
    out = HEADER + P.build_js_pack() + "\n\n" + P.build_women_js() + "\n"
    path = os.path.join(_ROOT, 'data', 'epochs.js')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(out)
    print("data/epochs.js: %d chars, %d lines" % (len(out), out.count('\n')))


if __name__ == '__main__':
    main()
