import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))


_INPUT = [
"""\
3
2 3 1
"""
,"""\
5
1 2 3 4 5
"""
,"""\
8
8 2 7 3 4 5 6 1
"""
]
_EXPECTED = [
"""\
3 1 2
"""
,"""\
1 2 3 4 5
"""
,"""\
8 2 4 5 6 7 3 1
"""
]

question_name = '16.C. Go to School'

import checker

checker.do(_INPUT, _EXPECTED, question_name)
