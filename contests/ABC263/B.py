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
    N= int(input())

    P=[]
    P.append(-1)
    P.append(-1)
    P.extend(list(map(int, input().split())))

    counter=0
    n=N
    while P[n] != -1:
        n=P[n]
        counter+=1

    print(counter)
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
1 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
1 2 3 4 5 6 7 8 9"""
        output = """9"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

