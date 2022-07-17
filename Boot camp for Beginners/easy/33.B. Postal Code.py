def resolve():
    A,B=map(int, input().split())
    S = input()
    for i in range(A):
        if not ('0' <= S[i] <= '9'):
            print('No')
            return
    i+=2
    if not S[A]=='-':
        print('No')
        return 

    for j in range(B):
        if not ('0' <= S[i+j] <= '9'):
            print('No')
            return
    print('Yes')
# resolve()

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
        input = """3 4
269-6650"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1
---"""
        output = """No"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 2
7444"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
