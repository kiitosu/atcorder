def resolve():
    A,B = map(int, input().split())

    count=0
    for i in range(A,B+1):
        j = str(i)
        if (j[0] == j[4]) and (j[1] == j[3]):
            count+=1
    
    print(count)
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
        input = """11009 11332"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """31415 92653"""
        output = """612"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
