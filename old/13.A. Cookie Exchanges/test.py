import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


_INPUT = [
"""\
4 12 20
"""
,
"""\
14 14 14
"""
]
_EXPECTED = [
"""\
3
"""
,
"""\
-1
"""
]

question_name = '13.A. Cookie Exchanges'

import checker

checker.do(_INPUT, _EXPECTED, question_name)
