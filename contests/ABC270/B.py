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

    X,Y,Z = map(int, input().split())

    ans = 0
    if X > 0 and Y > 0 and Y < X:
        if Z < 0:
            ans += abs(Z)*2 + abs(X)
        elif Z < Y:
            ans = abs(X)
        else:
            ans = -1
    elif X < 0 and Y < 0 and Y > X:
        if Z > 0:
            ans += abs(Z)*2 + abs(X)
        elif Z > Y:
            ans = abs(X)
        else:
            ans = -1

    else:
        ans = abs(X)
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
        input = """10 -10 1"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """20 10 -10"""
        output = """40"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100 1 1000"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
