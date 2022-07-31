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

    N=int(input()) # 整数で取得
    A = []

    for i in range(N):
        A.append(list(input().rstrip()))


    val={}
    val['W']='L'
    val['L']='W'
    val['D']='D'

    for i in range(1,N):
        for j in range(i):
            if val[A[i][j]] != A[j][i]:
                print('incorrect')
                return
    print('correct')
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
        input = """4
-WWW
L-DD
LD-W
LDW-"""
        output = """incorrect"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
-D
D-"""
        output = """correct"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
