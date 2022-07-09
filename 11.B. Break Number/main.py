N=int(input())
value=0
sign=1
ai=[]
ai = map(int, input().split())
ai = sorted(ai,reverse=True)
for i in ai:
    value += i * sign
    sign = sign * -1
print(value)