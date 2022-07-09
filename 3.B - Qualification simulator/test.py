import io
import sys
import time
# import main
import subprocess
from subprocess import PIPE

_INPUT = [
"""\
10 2 3
abccabaabb
"""
]
_EXPECTED = [
"""\
Yes
Yes
No
No
Yes
Yes
Yes
No
No
No
"""
]

question_name = 'B - Qualification simulator'

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

