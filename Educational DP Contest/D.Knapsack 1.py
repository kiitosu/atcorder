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
from operator import itemgetter
def resolve():
    input = sys.stdin.readline

    N,W = map(int, input().split())

    w=[0]
    v=[0]
    for _ in range(N):
        a,b = map(int, input().split())
        w.append(a)
        v.append(b)

    #
    dp=[[0 for _ in range(W+1)] for _ in range(N+1)]

    for i in range(1,N+1):
        for j in range(W+1):
            if j - w[i] < 0: # 重さjでは荷物が持ちきれない場合は
                dp[i][j] = dp[i-1][j] # それまでに荷物による評価値を使う
            else:
                dp[i][j] = max(dp[i-1][j],dp[i-1][j-w[i]]+v[i])
    print(dp[N][W])
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
        input = """3 8
3 30
4 50
5 60"""
        output = """90"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 5
1 1000000000
1 1000000000
1 1000000000
1 1000000000
1 1000000000"""
        output = """5000000000"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 15
6 5
5 6
6 4
6 6
3 5
7 2"""
        output = """17"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
