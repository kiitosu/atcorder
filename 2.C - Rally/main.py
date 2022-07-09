import sys

N = int(input())
n=[]

if n == 1:
    n.append(int(input()))
else:
    n = list(map(int, input().split()))

min_val= sys.maxsize
for i in range(max(n)):
    i=i+1
    temp_val=0
    for j in n:
        temp_val += (i-j)*(i-j)
    if temp_val < min_val:
        min_val = temp_val

print(min_val)
