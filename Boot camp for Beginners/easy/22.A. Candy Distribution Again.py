def resolve():
    N,x = map(int, input().split())
    A = map(int, input().split())
    A = sorted(A)
    counter = 0
    for a in A:
        x -= a
        if x < 0:
            print(counter)
            return
        else:
            counter+=1     
    if x > 0:
        counter -=1
    print(counter)
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
        input = """3 70
20 30 10"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 10
20 30 10"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """4 1111
1 10 100 1000"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """2 10
20 20"""
        output = """0"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
