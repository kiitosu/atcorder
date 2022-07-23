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
import math
def resolve():
    A,B= map(int, input().split())
    tmp = math.ceil(A/0.08)
    X1= X2 = -1
    if math.floor(tmp*0.1) == B:
        X1 = tmp

    tmp = math.ceil(B/0.1)
    if math.floor(tmp*0.08) == A:
        X2 = tmp  

    if X1 == -1 and X2 == -1:
        print(X1)
        return
    elif X1 == -1:
        print(X2)
    elif X2 == -1:
        print(X1)
    else:
        print(min(X1,X2))

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
        input = """2 2"""
        output = """25"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """8 10"""
        output = """100"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """19 99"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
