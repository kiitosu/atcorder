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
import re


def resolve():
    A,B,K = map(int, input().split()) # 1 2 3
    for i in range(K):
        tmp = A + i
        if tmp <=B:
            v = tmp
            print(v)

    for i in reversed(range(K)):
        if (B - i) > v:
            print(B-i)

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
        input = """3 8 2"""
        output = """3
4
7
8"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 8 3"""
        output = """4
5
6
7
8"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 9 100"""
        output = """2
3
4
5
6
7
8
9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
