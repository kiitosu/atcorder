def resolve():
    S = input()
    counter1 = 0 # 奇数が1
    counter2 = 0 # 偶数が1
    for i,s in enumerate(S):
        if (i + 1 ) % 2 == 1:
            if s == '1':
                counter2 += 1
            else:
                counter1 += 1
        else:
            if s == '1':
                counter1 += 1
            else:
                counter2 += 1
    print(min(counter1,counter2))
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
        input = """000"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10010010"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """0"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
