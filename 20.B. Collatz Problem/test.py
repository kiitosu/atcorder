import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


_INPUT = [
"""\
8
"""
,"""\
54"""
]
_EXPECTED = [
"""\
5
"""
,"""\
114"""
]

question_name = '20.B. Collatz Problem'

import checker

checker.do(_INPUT, _EXPECTED, question_name)
