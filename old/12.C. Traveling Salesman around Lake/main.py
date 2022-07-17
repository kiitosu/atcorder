K ,N = map(int, input().split())
A=[]
for a in map(int, input().split()):
    A.append(a)

# 家の間の間隔を計算する
D=[]
for i in range(len(A)-1):
    D.append( A[i+1]-A[i] )
D.append(A[0]+(K-A[-1]))

max_dist = max(D)

print(K-max_dist)