import sys


def resolve():
    N,M=map(int, input().split())
    min_r = sys.maxsize
    max_l = 0
    for i in range(M):
        l, r = map(int, input().split())
        max_l = max(l,max_l)
        min_r = min(r,min_r)
        count = min_r - max_l
        if count >= 0:
            count += 1
        else:
            count = 0
    print(count)
resolve()

        # L.append(l)
        # R.append(r)

    # for i in range(M):
    #     l1 = L[i]
    #     for j in range(l1-1,R[i]):
    #         a[i][j]=True

    # b=[True]*N
    # for j in range(N):
    #     for i in range(M):
    #         b[j] &= a[i][j]
    #         if not b[j]:
    #             break
    # print(sum(b)) 
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
        input = """4 2
1 3
2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """10 3
3 6
5 7
6 9"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """100000 1
1 100000"""
        output = """100000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
