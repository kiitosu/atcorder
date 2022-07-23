
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

    s = input().rstrip()
    t = input().rstrip()
    len_s = len(s)
    len_t = len(t)

    dp = [[0 for _ in range(len_t+1)] for _ in range(len_s+1)]

    for i in range(1,len_s+1):
        for j in range(1,len_t+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])

    ansl=dp[i][j]
    ans = ''
    while ansl > 0:
        if s[i-1] == t[j-1]:
            ans = s[i-1]+ans
            i-=1
            j-=1
            ansl-=1
        elif dp[i-1][j] >= dp[i][j-1]:
            i -= 1
        else:
            j -= 1
        
    print(ans)
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
        input = """axyb
abyxb"""
        output = """axb"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """aa
xayaz"""
        output = """aa"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """a
z"""
        output = """"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """abracadabra
avadakedavra"""
        output = """aaadara"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
