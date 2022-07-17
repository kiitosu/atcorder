def resolve():
    a,b=map(int, input().split())
    if a > 0:
        print('Positive')
        return
    elif a < 0 and b >= 0:
        print('Zero')
        return
    elif (a == 0) or (b == 0 ):
        print('Zero')
        return
    elif a == b:
        print('Positive')
    else:
        if (abs(a-b) % 2) == 0:
            print('Negative')
        else:
            print('Positive')
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
        input = """1 3"""
        output = """Positive"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """-3 -1"""
        output = """Negative"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """-3 -3"""
        output = """Positive"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """-3 1"""
        output = """Zero"""
        self.assertIO(input, output)

    def test_入力例_5(self):
        input = """-3 0"""
        output = """Zero"""
        self.assertIO(input, output)

    def test_入力例_6(self):
        input = """0 0"""
        output = """Zero"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()
