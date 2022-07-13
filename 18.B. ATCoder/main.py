S = input()

ACGT = "ACGT"

max_count = 0
counter = 0
for s in S:
    if s in ACGT:
        counter += 1
    else:
        if max_count < counter:
            max_count = counter
        counter = 0

if max_count < counter:
    max_count = counter

print(max_count)