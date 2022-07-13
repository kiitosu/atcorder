def resolve():
    A,B,M = map(int ,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    x = []
    for m in range(M):
        x.append(map(int, input().split()))
    #----------------------------
    # 本値が最も安い組み合わせ
    result = 0
    result = min(a) + min(b)

    for i,j,k in x:
        cost = a[i-1] + b[j-1] - k
        if cost < result:
            result = cost
    
    print(result)
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
        input = """2 3 1
3 3
3 3 3
1 2 1"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 1 2
10
10
1 1 5
1 1 10"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2 2 1
3 5
3 5
2 2 2"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
