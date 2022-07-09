N,M,C = map(int, input().split())

B=[]
for b in map(int, input().split()):
    B.append(b)

A=[]
for n in range(N):
    a=[]
    for i in map(int, input().split()):
        a.append(i)
    A.append(a)

counter=0
for n in range(N):
    value=0
    for m in range(M):
        value += B[m]*A[n][m]
    value+=C
    if value > 0:
        counter+=1


print(counter)