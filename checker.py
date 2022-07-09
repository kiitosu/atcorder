import io
import time
import subprocess
from subprocess import PIPE

def do(_INPUT, _EXPECTED, question_name):
    for input, expected in zip(_INPUT, _EXPECTED):

        StartTime = time.time()
        # --------------------------------------------------------
        #main.main()
        r = subprocess.run(['python', './{}/main.py'.format(question_name)], input=input.encode('utf-8'), stdout=PIPE, stderr=PIPE)
        result = r.stdout.decode().split('\n')
        expected = expected.split('\n')

        for r,e in zip(result, expected):
            r = r.replace('\r','')
            e = e.replace('\r','')
            r = r.replace('\n','')
            e = e.replace('\n','')
            print(r)
            print(e)
            assert str(e) == str(r)
        # --------------------------------------------------------
        print ("[Sec]"+str(time.time() - StartTime))