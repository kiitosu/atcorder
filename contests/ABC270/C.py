# メモ化用
# from functools import lru_cache
# @lru_cache(maxsize=None)

# パラメータ取得
# = input() # 文字列で取得
# = int(input()) # 整数で取得
# = map(int, input().split()) # 1 2 3などのように取りたいとき
# = input().split() # A B Cなどのように取りたいとき
# = list(map(int, input().split())) # 1 2 3などをリストで取りたいとき
# = list(input().split()) # A B Cなどをリストで取りたいとき
import sys
MAX = sys.maxsize
sys.setrecursionlimit(100000)
from operator import itemgetter

def trace(l,x,s,y):
    s.append(x)
    if x == y:
        return
    for i in l[x]:
        if i not in s:
            trace(l,i,s,y)
        else:
            if len(l[x])==1:
                s.pop()
        # else:
        #     if i != y:
        #         s.pop()
        #     else:
        #         return i


def resolve():
    input = sys.stdin.readline

    N,X,Y=map(int, input().split())

    l = [[] for _ in range(N+1)]

    for _ in range(N-1):
        A,B = map(int,input().split())
        l[A].append(B)
        l[B].append(A)

    s = []
    
    trace(l,X,s,Y)
    
    r = ''
    for i in s:
        r += str(i)
        r += ' '
    r = r.rstrip()
    print(r)

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
        input = """5 2 5
1 2
1 3
3 4
3 5"""
        output = """2 1 3 5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 1 2
3 1
2 5
1 2
4 1
2 6"""
        output = """1 2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
