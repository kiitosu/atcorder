A=[[0 for i in range(3)] for j in range(3)]
A[0][0], A[0][1], A[0][2] = map(int, input().split())
A[1][0], A[1][1], A[1][2] = map(int, input().split())
A[2][0], A[2][1], A[2][2] = map(int, input().split())

N = int(input())

B=[]
for i in range(N):
    B.append(int(input()))

# 行チェック
for i in range(3):
    counter = 0
    for j in range(3):
        if A[i][j] in B:
            counter += 1
    if counter == 3:
        print('Yes')
        quit()

# 列チェック
for j in range(3):
    counter = 0
    for i in range(3):
        if A[i][j] in B:
            counter += 1
    if counter == 3:
        print('Yes')
        quit()

# 対角チェック１
counter = 0
for i in range(3):
    if A[i][i] in B:
        counter += 1
if counter == 3:
    print('Yes')
    quit()

# 対角チェック2
counter = 0
for i in range(3):
    if A[2-i][i] in B:
        counter += 1
if counter == 3:
    print('Yes')
    quit()

print('No')