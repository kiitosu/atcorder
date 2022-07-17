def resolve():
    N = int(input())
    S = input()
    A = {'D':-1,'I':1}
    max_value = 0
    value = 0
    for i in range(len(S)):
        value += A[S[i]]
        if value > max_value:
            max_value = value
    print(max_value)
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
IIDID"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
DDIDDII"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
