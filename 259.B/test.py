import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


_INPUT = [
"""\
2 2 180
"""
]
_EXPECTED = [
"""\
-2 -2
"""
]

question_name = '259.B'

import checker

checker.do(_INPUT, _EXPECTED, question_name)
