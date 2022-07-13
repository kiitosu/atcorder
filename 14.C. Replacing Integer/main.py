N, K = map(int, input().split())

ns = []

import sys
min_n = sys.maxsize
n = N % K
while True:
    n = abs(n-K)
    if min_n > n:
        min_n = n
    if n in ns:
        break
    ns.append(n)

print(min_n)