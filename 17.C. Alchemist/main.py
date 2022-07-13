N=int(input())
v = []
for i in map(int, input().split()):
    v.append(i)

v = sorted(v)

result = 0
for i in range(len(v)-1):
    if result == 0:
        result += (v[i]+v[i+1])/2
    else:
        result = (result + v[i+1])/2

print(result)