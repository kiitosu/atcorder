import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


_INPUT = [
"""\
ATCODER
"""
,
"""\
HATAGAYA
"""
,
"""\
SHINJUKU
"""
]
_EXPECTED = [
"""\
3
"""
,
"""\
5
"""
,
"""\
0
"""
]

question_name = '18.B. ATCoder'

import checker

checker.do(_INPUT, _EXPECTED, question_name)
