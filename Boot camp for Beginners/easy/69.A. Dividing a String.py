# メモ化用
# from functools import lru_cache
# @lru_cache(maxsize=None)

# パラメータ取得
# = input() # 文字列で取得
# = int(input()) # 整数で取得
# = map(int, input().split()) # 1 2 3などのように取りたいとき
# = input().split() # A B Cなどのように取りたいとき
# = list(map(int, input().split())) # 1 2 3などをリストで取りたいとき
# = list(input().split()) # A B Cなどをリストで取りたいとき
def resolve():
    S = input()
    N = len(S)

    # 文字の位置(i)とそこに至るときに幾つの文字を使ったか(ステップ数jとする)を状態として持つ
    # 状態ごとの分割数の最大を状態の値として保持する
    # jは高々2であるがindexをややこしくしないため3で確保
    pd = [[-1 for i in range(3)] for j in range(N)]
    pd[0][0] = 0 # 初期位置は0回更新
    # pd[0][1] = 0 # 初期位置は0回更新
    # pd[0][2] = 0 # 初期位置は0回更新

    # 文字の位置でループ
    for i in range(N):
        # 前回の文字列候補でループ
        for j in range(1, max(i,3)):
            # 該当ステップ数でたどり着いたことがなければ終了
            if pd[i-j][j] == 0:
                continue
            pre_value = S[i-j:i]
            # ここから次の場所の計算をする
            for k in range(0+1,2+1):
                # jだけステップした時の文字列が一つ前の文字列と異なる必要がある
                if pre_value != S[i:i+k]:
                    pd[i][k] = max( pd[i+k][k], pd[i][j]+1)

    result = max(pd[N-1][1],pd[N-1][2]) 
    print(result)




    # dp = [[-1 for i in range(3)] for j in range(N+1)]
    # dp[0][0] = 0

    # for i in range(N):
    #     for j in range(min(i,2)+1):
    #         suffix = S[i-j:i]
    #         for add in range(1,3):
    #             if i + add > N:
    #                 break
            
    #             if S[i:i+add] != suffix:
    #                 dp[i+add][add] = max(dp[i+add][add],dp[i][j]+1)


    # print(max(dp[N][1],dp[N][2]))


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
        input = """aabbaa"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """aaaccacabaababc"""
        output = """12"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
