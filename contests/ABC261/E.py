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

    N,C=map(int, input().split())
    T=[]
    A=[]
    for i in range(N):
        t,a=map(int, input().split())
        T.append(t)
        A.append(a)
        for j in range(i+1):
            if T[j] == 1:
                C = C & A[j]
            elif T[j] == 2:
                C = C | A[j]
            elif T[j] == 3:
                C = C ^ A[j]
            else:
                pass
        
        print(C)

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
        input = """3 10
3 3
2 5
1 12"""
        output = """9
15
12"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9 12
1 1
2 2
3 3
1 4
2 5
3 6
1 7
2 8
3 9"""
        output = """0
2
1
0
5
3
3
11
2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
