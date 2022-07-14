def resolve():
    N=int(input())
    a = list(map(int, input().split()))
    b = [0] * len(a)
    flg = True
    while flg:
        for i in range(len(a)):
            if a[i] % 2 == 0:
                b[i]+=1
                a[i] = a[i] / 2
            else:
                flg = False
                break
    print(min(b))
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
        input = """3
8 12 40"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
5 6 8 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
382253568 723152896 37802240 379425024 404894720 471526144"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
