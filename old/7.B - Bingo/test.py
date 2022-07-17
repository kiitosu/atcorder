import io
import sys
import time
import subprocess
from subprocess import PIPE

_INPUT = [
"""\
84 97 66
79 89 11
61 59 7
7
89
7
87
79
24
84
30
"""
]
_EXPECTED = [
"""\
Yes
"""
]

question_name = '7.B - Bingo'

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

