A,B=map(int, input().split())
AB=str(A)+str(B)
AB=int(AB)

import math
for i in range(int(math.sqrt(100100))):
    if AB == i*i:
        print('Yes')
        quit()
print('No')