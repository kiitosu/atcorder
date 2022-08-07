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
def resolve():
    input = sys.stdin.readline
    N,L,R=map(int, input().split())
    A = []
    A.extend(list(map(int, input().split())))

    SUM = sum(A)
    min = SUM
    min_i=-1
    for i in range(N):
        SUM += -A[i]+L
        if min > SUM:
            min = SUM
            min_i=i
    for i in range(min_i+1):
        A[i] = L

    SUM = sum(A)
    for i in range(N):
        SUM += -A[-i-1]+R
        if min >= SUM:
            min = SUM

    print(min)
# resolve()


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
        input = """5 4 3
5 5 0 6 3"""
        output = """14"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 10 10
1 2 3 4"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 -5 -3
9 -6 10 -1 2 10 -1 7 -15 5"""
        output = """-58"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1 -5 -3
1"""
        output = """-5"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """1 5 3
1"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

