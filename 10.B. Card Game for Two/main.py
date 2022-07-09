N=int(input())
max_counter=0
value=0

for n in range(N):
    counter=0
    tmp=n+1
    while True:
        if tmp % 2 == 1:
            break
        else:
            tmp = tmp / 2
            counter += 1
    if max_counter <= counter:
        max_counter = counter
        value = n+1
print(value)
