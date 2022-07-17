import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


_INPUT = [
"""\
20 3
5 10 15
"""
,
"""\
20 3
0 5 15
"""
]
_EXPECTED = [
"""\
10
"""
,
"""\
10
"""
]

question_name = '12.C. Traveling Salesman around Lake'

import checker

checker.do(_INPUT, _EXPECTED, question_name)
