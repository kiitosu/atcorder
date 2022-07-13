import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


_INPUT = [
"""\
7 4
"""
,
"""\
2 6
"""
,
"""\
1000000000000000000 1
"""
]
_EXPECTED = [
"""\
1
"""
,
"""\
2
"""
,
"""\
0
"""
]

question_name = '14.C. Replacing Integer'

import checker

checker.do(_INPUT, _EXPECTED, question_name)
