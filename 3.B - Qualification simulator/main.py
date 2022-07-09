N, A, B = map(int, input().split())
S= input()
# print(N)
# print(A)
# print(B)
# print(S)

THREHOLD_PASS_NUMBER = int(A)+int(B)
counter_pass_all = 0
counter_pass_foreign = 0
for s in S:
    if s == 'a':
        if counter_pass_all < THREHOLD_PASS_NUMBER:
            counter_pass_all+=1
            print('Yes')
        else:
            print('No')
    elif s == 'b':
        if counter_pass_all < THREHOLD_PASS_NUMBER and counter_pass_foreign < B:
            counter_pass_foreign+=1
            counter_pass_all+=1
            print('Yes')
        else:
            print('No')
    else:
        print('No')
