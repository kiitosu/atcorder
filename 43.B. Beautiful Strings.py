def resolve():
    W = input()
    a = [0] * 26
    for w in W:
        a[ ord(w) - ord('a') ] += 1 

    for i in range(26):
        if a[i] % 2 == 1:
            print('No')
            return
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
        input = """abaccaba"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """hthth"""
        output = """No"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
