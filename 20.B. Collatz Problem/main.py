S = int(input())

def func(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

s=[]
s.append(S)
while True:
    S = func(S)
    if S in s:
        print(len(s)+1)
        quit()
    else:
        s.append(S)
