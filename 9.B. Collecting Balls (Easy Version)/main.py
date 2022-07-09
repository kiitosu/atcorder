N = int(input())
K = int(input())
X=[]
for i in input().split():
    X.append(int(i))

#-------------------------
value=0
for x in X:
    if x < abs(K-x):
        value += x*2
    else:
        value += abs(K-x)*2

print(value)