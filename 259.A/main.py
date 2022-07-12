N, M, X, T, D = map(int, input().split())
if X <= M:
    print(T)
else:
    hight_in_1_year = T - X * D
    print(hight_in_1_year + M * D)