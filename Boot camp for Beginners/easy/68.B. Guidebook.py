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
    N = int(input())
    l = []
    t = []
    for i in range(N):
        name,point = input().split()
        point = int(point)
        t = [name,-point,i+1]
        l.append(t)

    for i in sorted(l):
        print(i[2])
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
        input = """6
khabarovsk 20
moscow 10
kazan 50
kazan 35
moscow 60
khabarovsk 40"""
        output = """3
4
6
1
5
2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10
yakutsk 10
yakutsk 20
yakutsk 30
yakutsk 40
yakutsk 50
yakutsk 60
yakutsk 70
yakutsk 80
yakutsk 90
yakutsk 100"""
        output = """10
9
8
7
6
5
4
3
2
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
