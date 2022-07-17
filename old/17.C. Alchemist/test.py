import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


_INPUT = [
"""\
2
3 4
"""
,"""\
3
500 300 200
"""
,"""\
5
138 138 138 138 138
"""
]
_EXPECTED = [
"""\
3.5
"""
,"""\
375
"""
,"""\
138
"""
]

question_name = '17.C. Alchemist'

import checker

checker.do(_INPUT, _EXPECTED, question_name)
