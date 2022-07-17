import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


_INPUT = [
"""\
7
"""
]
_EXPECTED = [
"""\
4
"""
]

question_name = '10.B. Card Game for Two'

import checker

checker.do(_INPUT, _EXPECTED, question_name)
