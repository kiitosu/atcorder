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
# = list(input().rstrip()) # ABC などを ['A','B','C']などのようなリストにしたいとき

import sys
MAX = sys.maxsize
sys.setrecursionlimit(100000)
from operator import itemgetter
def resolve():
    input = sys.stdin.readline
    H,W = map(int, input().split())
    dp = [[0 for _ in range(W)] for _ in range(H)]
    route = []
    for h in range(H):
        route.append(list(input().rstrip()))
    dp[0][0] = 1
    for h in range(H):
        for w in range(W):
            if route[h][w] == '#':
                dp[h][w] = 0
            else:
                if w > 0:
                    dp[h][w] += dp[h][w-1]
                if h > 0:
                    dp[h][w] += dp[h-1][w]
    
    print(dp[H-1][W-1]%(10**9+7))
    

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
        input = """3 4
...#
.#..
...."""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 2
..
#.
..
.#
.."""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 5
..#..
.....
#...#
.....
..#.."""
        output = """24"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """20 20
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
....................
...................."""
        output = """345263555"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
