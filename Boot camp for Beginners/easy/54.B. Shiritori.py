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
    N = int(input()) # 整数で取得
    l = []
    for n in range(N):
        w = input()
        if w in l:
            print('No')
            return
        else:
            if n != 0:
                if l[-1][-1] != w[0]:
                    print('No')
                    return
            l.append(w)
    print('Yes')
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
hoge
english
hoge
enigma"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """9
basic
c
cpp
php
python
nadesico
ocaml
lua
assembly"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """8
a
aa
aaa
aaaa
aaaaa
aaaaaa
aaa
aaaaaaa"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """3
abc
arc
agc"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
