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
import itertools
def resolve():
    input = sys.stdin.readline
    N,M = map(int, input().split())
    l=[]
    for i in range(M):
        l.append(i+1)
    result=''
    for v in itertools.combinations(l,N):
        for i in v:
            result+='{} '.format(i)
        result += '\n'
    print(result.rstrip())
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
        input = """2 3"""
        output = """1 2 
1 3 
2 3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 5"""
        output = """1 2 3 
1 2 4 
1 2 5 
1 3 4 
1 3 5 
1 4 5 
2 3 4 
2 3 5 
2 4 5 
3 4 5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
