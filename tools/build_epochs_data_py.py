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
"""生成命令行端纪元内容数据层 fsl_epochs.py。

组成：手写的当代 / 未来旧内容（tools/legacy_data_py.py）+ 由 tools/civ_*.py
内容源生成的三大新纪元内容（epoch_pack.build_py_pack）。

本脚本只写 fsl_epochs.py，不触碰 life_game.py，因此命令行端引擎代码可以安全地
独立演进（life_game.py 通过 `from fsl_epochs import *` 取得全部纪元数据）。
"""

import epoch_pack as P

HEADER = '''# -*- coding: utf-8 -*-
"""《浮生录》纪元内容数据层（由 tools/build_epochs_data_py.py 自动生成）。

请勿手工编辑本文件：
  * 三大新纪元内容来自 tools/civ_meta_*.py 与 tools/civ_stages_*.py
  * 当代 / 未来旧内容来自 tools/legacy_data_py.py

life_game.py 通过 `from fsl_epochs import *` 取得本模块的全部纪元数据与解析函数。
"""

import random
'''


def main():
    P.load_data()
    P.load_women()
    legacy = open(os.path.join(_HERE, 'legacy_data_py.py'), encoding='utf-8').read()
    # 去掉 legacy 模块自身的编码声明，避免在同一文件里重复出现
    legacy = legacy.replace('# -*- coding: utf-8 -*-\n', '', 1)
    out = (HEADER + '\n' + legacy.rstrip() + '\n\n\n' + P.build_py_pack()
           + '\n\n\n' + P.build_women_py()
           + '\n\n\n' + P.build_random_events_py() + '\n')
    path = os.path.join(_ROOT, 'fsl_epochs.py')
    with open(path, 'w', encoding='utf-8') as f:
        f.write(out)
    import ast
    ast.parse(out)
    print("fsl_epochs.py: %d chars, %d lines" % (len(out), out.count('\n')))


if __name__ == '__main__':
    main()
