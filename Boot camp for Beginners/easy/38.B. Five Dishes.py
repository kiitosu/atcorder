import math
def resolve():
    X = [0]*5
    min_v = 10
    min_value = None
    min_idx = -1
    for i in range(5):
        X[i] = int(input())
        x = X[i] % 10
        if (x != 0) and (x<min_v):
            min_v = x
            min_value = X[i]
            min_idx = i
    
    value = 0
    for i in range(5):
        if i != min_idx:
            X[i] = math.ceil(X[i]/10)*10
        value += X[i]
    print(value)
    
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
        input = """29
20
7
35
120"""
        output = """215"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """101
86
119
108
57"""
        output = """481"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """123
123
123
123
123"""
        output = """643"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
