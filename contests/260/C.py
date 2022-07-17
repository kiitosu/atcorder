def resolve():

    N,X,Y=map(int, input().split())

    def change_red(lr,nr):
        if lr == 1:
            return 0
        else:
            return change_red(lr-1,nr) + change_blue(lr,X) * lr

    def change_blue(lb,nb):
        if lb == 1:
            return nb
        else:
            return change_red(lb-1,nb) + change_blue(lb-1,Y) * (lb-1)

    print(change_red(N,1))



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
        input = """2 3 4"""
        output = """12"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 5 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 5 5"""
        output = """3942349900"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
