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
    X = int(input())
    N = int(X / 100)+1
    M = X % 100

    for i in range(N):
        for j in range(N-i):
            for k in range(N-i-j):
                for l in range(N-i-j):
                    for m in range(N-i-j-k-l):
                        if i*1+j*2+k*3+l*4+m*5 == M:
                            print(1)
                            return

    print(0)

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
        input = """615"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """217"""
        output = """0"""
        self.assertIO(input, output)

    def test_3(self):
        input = """100"""
        output = """1"""
        self.assertIO(input, output)

    def test_4(self):
        input = """101"""
        output = """1"""
        self.assertIO(input, output)

    def test_5(self):
        input = """102"""
        output = """1"""
        self.assertIO(input, output)

    def test_6(self):
        input = """103"""
        output = """1"""
        self.assertIO(input, output)

    def test_7(self):
        input = """104"""
        output = """1"""
        self.assertIO(input, output)

    def test_8(self):
        input = """105"""
        output = """1"""
        self.assertIO(input, output)

    def test_9(self):
        input = """1"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
