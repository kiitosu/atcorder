X = int(input())

prime_candidate = X
is_prime=True
while True:
    is_prime=True
    for i in range(X-2):
        if X % (i+2) == 0:
            is_prime=False
            break
    if is_prime:
        print(X)
        quit()
    X+=1


