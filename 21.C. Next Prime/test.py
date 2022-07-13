import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


_INPUT = [
"""\
20
"""
,"""\
2"""
,"""\
99992"""
]
_EXPECTED = [
"""\
23
"""
,"""\
2"""
,"""\
100003"""
]

question_name = '21.C. Next Prime'

import checker

checker.do(_INPUT, _EXPECTED, question_name)
