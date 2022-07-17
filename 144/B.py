
def resolve():
    N, a, b = map(int, input().split())
    A = list(map(int, input().split()))
    max_min = min(A)

    while True:
        min_idx = A.index(max_min)
        max_idx = A.index(max(A))
        if min_idx == max_idx:
            print(max_min)
            return
        elif max_min == A[max_idx]:
            print(max_min)
            return

        A[min_idx] += a
        A[max_idx] -= b

        tmp_max_min = max([min(A),max_min])
        if tmp_max_min <= max_min:
            print(max_min)
            return
        else:
            max_min = tmp_max_min

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
        input = """3 2 2
1 5 9"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 2 3
11 1 2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """3 1 100
8 5 6"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_4(self):
        input = """6 123 321
10 100 1000 10000 100000 1000000"""
        output = """90688"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
