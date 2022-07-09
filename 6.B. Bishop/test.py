import io
import sys
import time
import subprocess
from subprocess import PIPE

_INPUT = [
"""\
4 5
"""
,
"""\
7 3
"""
,
"""\
1000000000 1000000000
"""
]
_EXPECTED = [
"""\
10
"""
,
"""\
11
"""
,
"""\
500000000000000000
"""
]

question_name = '6.B. Bishop'

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

