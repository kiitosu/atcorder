import sys
def resolve():
    input = sys.stdin.readline

    N=int(input())
    a=[0]*N
    b=[0]*N
    c=[0]*N

    for i in range(N):
        a[i],b[i],c[i] = map(int, input().split())

    # 前日までの全ての選択肢の幸福度を計算しておく
    dp = [[0 for _ in range(3)] for _ in range(N)]
    dp[0][0] = a[0]
    dp[0][1] = b[0]
    dp[0][2] = c[0]

    for i in range(1,N):
        dp[i][0] = max((dp[i-1][1] + a[i]),(dp[i-1][2] + a[i]))
        dp[i][1] = max((dp[i-1][0] + b[i]),(dp[i-1][2] + b[i]))
        dp[i][2] = max((dp[i-1][0] + c[i]),(dp[i-1][1] + c[i]))

    result = max(dp[N-1])
    print(result)
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
        input = """3
10 40 70
20 50 80
30 60 90"""
        output = """210"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1
100 10 1"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7
6 7 8
8 8 3
2 5 2
7 8 6
4 6 8
2 3 4
7 5 1"""
        output = """46"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
