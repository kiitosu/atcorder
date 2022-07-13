import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


_INPUT = [
"""\
6
9 1 4 4 6 7
"""
,"""\
8
9 1 14 5 5 4 4 14
"""
,"""\
14
99592 10342 29105 78532 83018 11639 92015 77204 30914 21912 34519 80835 100000 1
"""
]
_EXPECTED = [
"""\
2
"""
,"""\
0"""
,"""\
42685
"""
]

question_name = '15.C - Divide the Problems'

import checker

checker.do(_INPUT, _EXPECTED, question_name)
