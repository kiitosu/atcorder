import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


_INPUT = [
"""\
10 7 5
1 2 3 4 6 8 9
"""
]
_EXPECTED = [
"""\
3
"""
]

question_name = '19.B. Toll Gates'

import checker

checker.do(_INPUT, _EXPECTED, question_name)
