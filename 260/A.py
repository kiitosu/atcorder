def resolve():
    S = input()
    a = [0]*26
    for s in S:
        a[ord(s)-ord('a')]+=1

    for i,j in enumerate(a):
        if j == 1:
            print(chr(ord('a')+i))
            return

    print('-1')
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
        input = """pop"""
        output = """o"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """abc"""
        output = """a"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """xxx"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
