# メモ化用
# from functools import lru_cache
# @lru_cache(maxsize=None)

# パラメータ取得
# = input() # 文字列で取得
# = int(input()) # 整数で取得
# = map(int, input().split()) # A,B,Cなどのように取りたいとき
# = list(map(int, input().split())) # A,B,Cなどをリストで取りたいとき

def resolve():
    N = int(input()) # 整数で取得
    H = list(map(int, input().split())) # A,B,Cなどをリストで取りたいとき
    count_max = 0
    counter=0
    for i in range(len(H)-1):
        if H[i] >= H[i+1]:
            counter += 1
        else:
            counter = 0
        if count_max < counter:
            count_max = counter
    print(count_max)

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
        input = """5
10 4 8 7 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
4 4 5 6 6 5 5"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4
1 2 3 4"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
