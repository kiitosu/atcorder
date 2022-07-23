import sys
def resolve():
    N,K = map(int, input().split())
    h = list(map(int, input().split()))
    dp = [sys.maxsize]*(N)
    dp[0]=0

    for i in range(1,N):
        for j in range(1,K+1):
            if i - j < 0:
                continue
            dp[i] = min(dp[i],dp[i-j]+abs(h[i]-h[i-j]))
    
    print(dp[N-1])
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
        input = """5 3
10 30 40 50 20"""
        output = """30"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 1
10 20 10"""
        output = """20"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 100
10 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """10 4
40 10 20 70 80 10 20 70 80 60"""
        output = """40"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
