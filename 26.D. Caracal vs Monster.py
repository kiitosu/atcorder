def attack(H,c,ac):
    if H == 1:
        return 1, c+ac, ac*2
    else:
        return attack(int(H / 2), c + ac ,ac*2)

def resolve():
    H = int(input())
    H , c, ac = attack(H,0,1)
    print(c)
    


    # attack_count=1
    # counter=0
    # while (0 < H):
    #     H = int(H /2)
    #     counter+=attack_count
    #     attack_count*=2
       
    # print(counter)    
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
        input = """2"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4"""
        output = """7"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1000000000000"""
        output = """1099511627775"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
