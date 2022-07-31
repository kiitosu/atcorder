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

    L1,R1,L2,R2 = map(int, input().split()) # 1 2 3などのように取りたいとき

    if L1 <= L2 <=R1 <= R2:
        ans = R1-L2
    elif L2 <= L1 <=R2 <= R1:
        ans = R2-L1
    elif L2 <= L1 <=R1 <= R2:
        ans = R1-L1
    elif L1 <= L2 <=R2 <= R1:
        ans = R2-L2
    else:
        ans = 0


    print(ans)

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
        input = """0 3 1 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """0 1 4 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0 3 3 7"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
