N=int(input())
d = []
for i in map(int, input().split()):
    d.append(i)

d = sorted(d)

# 真ん中の数字が境界をまたいでいたら半分に分けられない
if d[int(N/2)-1] == d[int(N/2)]:
    print(0)
    quit() 

print(d[int(N/2)] - d[int(N/2)-1])