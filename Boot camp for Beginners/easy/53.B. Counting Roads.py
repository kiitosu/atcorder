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

    N,M = map(int, input().split()) # 1 2 3などのように取りたいとき
    city = [0] *(N+1)
    for i in range(M):
        a, b = map(int, input().split()) # 1 2 3などのように取りたいとき
        city[a] += 1
        city[b] += 1
    for i in range(1,N+1):
        # if city[i] !=0:
        print(city[i])
        
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
        input = """4 3
1 2
2 3
1 4"""
        output = """2
2
1
1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 5
1 2
2 1
1 2
2 1
1 2"""
        output = """5
5"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8 8
1 2
3 4
1 5
2 8
3 7
5 2
4 1
6 8"""
        output = """3
3
2
2
2
1
1
2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

