import sys
def resolve():
    N = int(input())
    dp = [sys.maxsize]*N
    dp[0]=0
    h = list(map(int, input().split()))

    for n in(range(N)):      
        for i in (range(1,min(n,2)+1)):

            if sys.maxsize == dp[n-i]:
                add = 0
            else:
                add = dp[n-i]
            tmp=abs(h[n]-h[n-i])+add
            if dp[n] > tmp:
                dp[n] = tmp

    
    print(dp[N-1])
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
        input = """4
10 30 40 20"""
        output = """30"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
10 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
30 10 60 10 60 50"""
        output = """40"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
