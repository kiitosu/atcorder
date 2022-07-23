# メモ化用
# from functools import lru_cache
# @lru_cache(maxsize=None)

# パラメータ取得
# = input() # 文字列で取得
# = int(input()) # 整数で取得
# = map(int, input().split()) # A,B,Cなどのように取りたいとき
# = list(map(int, input().split()))　# A,B,Cなどをリストで取りたいとき

memo={}
def resolve():
    N = int(input())

    @lru_cache(maxsize=None)
    def calc(n):
        if n in memo:
            return memo[n]

        if n == 0:
            retval = 2
        elif n == 1:
            retval = 1 
        else:
            retval = calc(n-2) + calc(n-1)
        
        memo[n]=retval
        return retval

    result = calc(N)
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
        input = """5"""
        output = """11"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """86"""
        output = """939587134549734843"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
