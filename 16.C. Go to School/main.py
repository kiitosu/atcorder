N=int(input())
a = {}
counter = 1
for i in map(int, input().split()):
    a[str(i)]=counter
    counter+=1
a = sorted(a.items(),key=lambda x:int(x[0]))

result = ''
for i in a:
    result += str(i[1])
    result += ' '

result = result.rstrip()
print(result)