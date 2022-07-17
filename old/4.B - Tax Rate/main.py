N = int(input())
rate = 1.08
n = int(N / 1.08)
if float(n) != (N / 1.08): # 割り切れない場合は1を足す
    n+=1
if int(n * 1.08)==N:
    print(int(n))
else:
    print(':(')
