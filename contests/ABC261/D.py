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
    N,M = map(int, input().split())
    X=[0]
    X.extend(list(map(int, input().split())))    
    bonus=[0 for _ in range(N+1)]
    for i in range(M):
        c,y=map(int, input().split())
        bonus[c] = y

    # i回目のコイントスでカウンタがjの時の最大値を探す
    dp = [[0 for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0]=0
    for i in range(1,N+1):
        for j in range(0,i+1):
            if j == 0:
                dp[i][j] = max(dp[i-1])
            else:
                dp[i][j] = dp[i-1][j-1] + X[i] + bonus[j]

    print(max(dp[N]))
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
        input = """6 3
2 7 1 8 2 8
2 10
3 1
5 5"""
        output = """48"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2
1000000000 1000000000 1000000000
1 1000000000
3 1000000000"""
        output = """5000000000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
