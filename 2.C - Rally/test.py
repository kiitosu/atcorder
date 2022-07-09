import io
import sys
import time
# import main
import subprocess
from subprocess import PIPE

_INPUT = [
"""\
2
1 4
"""
,
"""\
7
14 14 2 13 56 2 37
"""
]
_EXPECTED = [
    5,
    2354
]


for input, expected in zip(_INPUT, _EXPECTED):

    StartTime = time.time()
    # --------------------------------------------------------
    #main.main()
    r = subprocess.run(['python', './abc156_c/main.py'], input=input.encode('utf-8'), stdout=PIPE, stderr=PIPE)
    result = r.stdout.decode().rstrip('\n')
    result = result.rstrip('\r')
    assert str(expected) == str(result)
    # --------------------------------------------------------
    print ("[Sec]"+str(time.time() - StartTime))

