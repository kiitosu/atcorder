N,M,X = map(int , input().split())
m=map(int, input().split())

m=sorted(m)
to_0=0
to_n=0
for i in m:
    if X > i:
        to_0 += 1
    else:
        to_n += 1


print(to_0 if to_0 < to_n else to_n)
