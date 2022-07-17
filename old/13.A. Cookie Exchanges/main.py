A,B,C=map(int, input().split())

counter = 0

pattern=[]

while True:
    if A % 2 == 1:
        break
    if B % 2 == 1:
        break
    if C % 2 == 1:
        break

    A, B, C = B / 2 + C / 2, A / 2 + C / 2, A/2 + B/2


    if sorted([A,B,C]) in pattern:
        print(-1)
        quit()

    counter += 1

    pattern.append(sorted([A,B,C]))

print(counter)