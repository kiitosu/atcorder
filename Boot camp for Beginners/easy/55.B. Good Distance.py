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
    N,D= map(int, input().split()) # 1 2 3などのように取りたいとき
    X = [[]]*N
    for i in range(N):
        X[i]=list(map(int, input().split()))
    count=0
    for i in range(N-1):
        for j in range(i+1,N):
            value=0
            for z in range(D):
                value += (X[i][z] - X[j][z])**2
            value = math.sqrt(value)
            if value.is_integer():
                count+=1
    print(count)
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
        input = """3 2
1 2
5 5
-2 8"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4
-3 7 8 2
-12 1 10 2
-2 8 9 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 1
1
2
3
4
5"""
        output = """10"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

