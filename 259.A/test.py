import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


_INPUT = [
"""\
38 20 17 168 3
"""
,
"""\
1 0 1 3 2
"""
,
"""\
100 10 100 180 1
"""
]
_EXPECTED = [
"""\
168
"""
,
"""\
1
"""
,
"""\
90
"""
]

question_name = '259.A'

import checker

checker.do(_INPUT, _EXPECTED, question_name)
