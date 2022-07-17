import io
import sys
import time
import subprocess
from subprocess import PIPE

_INPUT = [
"""\
7
"""
,
"""\
32
"""
,
"""\
1
"""
,
"""\
100
"""
]
_EXPECTED = [
"""\
4
"""
,
"""\
32
"""
,
"""\
1
"""
,
"""\
64
"""
]

question_name = '10.B. Card Game for Two'

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

