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
def resolve():
    H,W = map(int, input().split()) # A,B,Cなどのように取りたいとき
    image = []
    for h in range(H):
        image .append(input()) # A,B,Cなどをリストで取りたいとき
    first_line = '#' * W
    image.insert(0,first_line)
    image.append(first_line)
    for h in range(len(image)):
        image[h] = '#'+ image[h]
        image[h] = image[h] + '#'
    for h in image:
        print(h)
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
        input = """2 3
abc
arc"""
        output = """#####
#abc#
#arc#
#####"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1
z"""
        output = """###
#z#
###"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
