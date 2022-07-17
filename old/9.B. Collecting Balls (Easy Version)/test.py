import io
import sys
import time
import subprocess
from subprocess import PIPE

_INPUT = [
"""\
2
9
3 6
"""
,
"""\
5
20
11 12 9 17 12
"""
]
_EXPECTED = [
"""\
12
"""
,
"""\
74
"""
]

question_name = '9.B. Collecting Balls (Easy Version)'

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

