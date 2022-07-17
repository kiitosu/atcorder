import sys
def resolve():
    S = input()
    min_diff = sys.maxsize
    for i in range(len(S)-2):
        v=str(S[i])
        v+=str(S[i+1])
        v+=str(S[i+2])
        value = int(str(v))
        min_diff = min_diff if min_diff < abs(value - 753) else abs(value - 753)
    print (min_diff)
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
        input = """1234567876"""
        output = """34"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """35753"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1111111111"""
        output = """642"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
