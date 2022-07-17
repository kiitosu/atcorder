import io
import sys
import time
import subprocess
from subprocess import PIPE

_INPUT = [
"""\
2 3 -10
1 2 3
3 2 1
1 2 2
"""
,
"""\
5 2 -4
-2 5
100 41
100 40
-3 0
-6 -2
18 -13
"""
,
"""\
3 3 0
100 -100 0
0 100 100
100 100 100
-100 100 100
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

question_name = '5.B - Can you solve this'

for input, expected in zip(_INPUT, _EXPECTED):

    StartTime = time.time()
    # --------------------------------------------------------
    #main.main()
    r = subprocess.run(['python', './{}/main.py'.format(question_name)], input=input.encode('utf-8'), stdout=PIPE, stderr=PIPE)
    result = r.stdout.decode().split('\r\n')
    expected = expected.split('\n')

    print(result)

    for r,e in zip(result, expected):
        print(r)
        print(e)
        assert str(e) == str(r)
    # --------------------------------------------------------
    print ("[Sec]"+str(time.time() - StartTime))

