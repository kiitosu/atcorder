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

    N, M = map(int, input().split()) # 1 2 3などのように取りたいとき

    arr = [[0 for _ in range(N+1)] for _ in range(N+1)]

    for m in range(M):
        a,b = map(int, input().split()) # 1 2 3などのように取りたいとき
        arr[min(a,b)][max(a,b)] = 1
    
    counter=0
    for i in range(1,N+1):
        for j in range(i+1,N+1):
            for k in range(j+1,N+1):
                if arr[i][j] == 1 and arr[i][k] == 1 and arr[min(j,k)][max(j,k)]:
                    counter += 1
    
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
        input = """5 6
1 5
4 5
2 3
1 4
3 5
2 5"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 1
1 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """7 10
1 7
5 7
2 5
3 6
4 7
1 5
2 4
1 3
1 6
2 7"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
