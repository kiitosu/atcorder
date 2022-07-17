def resolve():
    N = int(input())
    M = N * 2
    result = ''
    counter = 0

    for i in range(int(N/4)):
        result += '4'
    if N % 4 != 0:
        result = str((N%4))+result
    print(M)
    print(result)   
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
        input = """3"""
        output = """6
3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6"""
        output = """12
24"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100"""
        output = """200
4444444444444444444444444"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
