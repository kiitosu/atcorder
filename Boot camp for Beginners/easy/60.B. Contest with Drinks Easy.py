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

def resolve():
    N=int(input())
    T=list(map(int, input().split()))
    M=int(input())

    for i in range(M):
        p,x = map(int, input().split())
        T_copy = T.copy()
        T_copy[p-1] = x
        print(sum(T_copy))
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
        input = """3
2 1 4
2
1 1
2 3"""
        output = """6
9"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5
7 2 3 8 5
3
4 2
1 7
4 13"""
        output = """19
25
30"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
