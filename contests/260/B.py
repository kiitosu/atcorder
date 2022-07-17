def resolve():
    N,X,Y,Z = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = []
    for i,j in zip(a,b):
        c.append(i+j)

    l = []
    counter=0
    while( counter < X):
        num = a.index((max(a)))+1
        a[num-1]=-1
        if num not in l:
            l.append(num)
            counter+=1
        else:
            pass

    counter=0
    while( counter < Y):
        num = b.index((max(b)))+1
        b[num-1]=-1
        if num not in l:
            l.append(num)
            counter+=1
        else:
            pass
        
    counter=0
    while( counter < Z):
        num = c.index((max(c)))+1
        c[num-1]=-1
        if num not in l:
            l.append(num)
            counter+=1
        else:
            pass        

    l = sorted(l)
    for i in l:
        print(i)
        
resolve()

import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """6 1 0 2
80 60 80 60 70 70
40 20 50 90 90 80"""
        output = """1
4
5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2 1 2
0 100 0 100 0
0 0 100 100 0"""
        output = """1
2
3
4
5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """15 4 3 2
30 65 20 95 100 45 70 85 20 35 95 50 40 15 85
0 25 45 35 65 70 80 90 40 55 20 20 45 75 100"""
        output = """2
4
5
6
7
8
11
14
15"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
