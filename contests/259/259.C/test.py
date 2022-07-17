import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


_INPUT = [
"""\
abbaac
abbbbaaac
"""
,
"""\
xyzz
xyyzz
"""
]
_EXPECTED = [
"""\
Yes
"""
,
"""\
No
"""
]

question_name = '259.C'

import checker

checker.do(_INPUT, _EXPECTED, question_name)
