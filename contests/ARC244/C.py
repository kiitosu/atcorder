from functools import lru_cache

memo={}
def f(n):
    if n in memo:
        return memo[n]
    ret = n if n <= 1 else f(n - 1) + f(n - 2)
    memo[n]=ret
    return ret
print(f(70))


def resolve():
    N = int(input())

    @lru_cache(maxsize=None)
    def calc(n):
        if n==1:
            return [n]
        else:
            return calc(n-1) + [n] + calc(n-1)
    
    tmp = calc(N)
    result =''
    for i in tmp: 
        result+=str(i)
        result+=' '

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
        input = """2"""
        output = """1 2 1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4"""
        output = """1 2 1 3 1 2 1 4 1 2 1 3 1 2 1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
