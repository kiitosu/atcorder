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

    Y = int(input())

    if Y%4 == 1:
        Y+=1

    elif Y%4==2:
        pass

    elif Y%4 == 3:
        Y+=3

    else:
        Y+=2

    print(Y)

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
        input = """2022"""
        output = """2022"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2023"""
        output = """2026"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3000"""
        output = """3002"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
