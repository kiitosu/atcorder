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
    N,A,B = map(int, input().split()) 

    if N < A:
        print(0)
        return

    if A == 1:
        print(N)
        return

    if A == B:
        print(N-(A-1))
        return

    if B > A:
        B = A
    result = (int(N / A) - 1)*B
    if N % A >= (B-1):
        result += B
    else:
        result += N%A + 1

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
        input = """4 2 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """27182818284 59045 23356"""
        output = """10752495144"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 2 1"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """1 1 1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """10 3 3"""
        output = """8"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
