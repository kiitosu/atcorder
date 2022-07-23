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
    N,M = map(int, input().split()) # 1 2 3などのように取りたいとき

    x=[]
    y=[[] for _ in range(N+1)]
    for m in range(M):
        xx,yy=map(int, input().split())
        x.append(xx)
        y[xx].append(yy)
    y = tuple(y)
    x_set = set(x)

    flg = [False] * (N+1)
    dp = [0] * (N+1)

    def calc(a):
        if flg[a]:
            return dp[a]
        flg[a]=True
        retval=0
        
        for i in y[a]:
            retval = max(retval, calc(i)+1)

        dp[a]=retval
        return retval

    ans = 0
    for i in x_set:
        ans=max(ans, calc(i))
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
        input = """4 5
1 2
1 3
3 2
2 4
3 4"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 3
2 3
4 5
5 6"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 8
5 3
2 3
2 4
5 2
5 1
1 4
4 3
1 3"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

