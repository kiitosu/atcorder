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
import math
MAX = sys.maxsize
sys.setrecursionlimit(100000)
from operator import itemgetter
def resolve():
    input = sys.stdin.readline
    N = int(input())
    A = [-1]
    A.extend(list(map(int, input().split())) )

    counter=0

    tmp_count=0
    for i,a in enumerate(A):
        # 自分の添字と値が同じものをカウント
        if i == a:
            tmp_count+=1
        else:
            # 異なる場合は
            # 自分の値を添え字とした値が、自分の添字となっているものを探す
            if i == A[a]:
                A[a] = -1 # 再度処理をしないように、値を無効値とする
                counter += 1

    if tmp_count <= 1:
        pass
    else:
        # counter = math.factorial(tmp_count) // (math.factorial(tmp_count-2)*math.factorial(2))
        counter += math.factorial(tmp_count) // (math.factorial(tmp_count-2)*2)

    print(counter)
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
        input = """4
1 3 2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
5 8 2 2 1 6 7 2 9 10"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()

        
