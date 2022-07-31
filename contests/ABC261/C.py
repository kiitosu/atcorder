
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

    N=int(input())
    v={}
    for i in range(N):
        s = input().rstrip()
        if s in v:
            v[s] = v[s] + 1
            print(s+'({})'.format(v[s]))
        else:
            v[s]=0
            print(s)
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
newfile
newfile
newfolder
newfile
newfolder"""
        output = """newfile
newfile(1)
newfolder
newfile(2)
newfolder(1)"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """11
a
a
a
a
a
a
a
a
a
a
a"""
        output = """a
a(1)
a(2)
a(3)
a(4)
a(5)
a(6)
a(7)
a(8)
a(9)
a(10)"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
