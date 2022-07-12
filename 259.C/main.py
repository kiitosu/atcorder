src = input()
target = input()

src_chars=[]
target_chars=[]

count = 0
char = 0
for i in range(len(src)):
    if char == 0:
        char = src[i]
        count += 1
    elif src[i-1] == src[i]:
        count += 1
    else:
        src_chars.append([char,count])
        char = src[i]
        count = 1
src_chars.append([char,count])

count = 0
char = 0
for i in range(len(target)):
    if char == 0:
        char = src[i]
        count += 1
    elif target[i-1] == target[i]:
        count += 1
    else:
        target_chars.append([char,count])
        char = target[i]
        count = 1
target_chars.append([char,count])

if len(src_chars) != len(target_chars):
    print('No')
    quit()

for s,t in zip(src_chars, target_chars):
    if (s[0] != t[0]):
        print('No')
        quit()


for s,t in zip(src_chars, target_chars):
    if (s[1]==t[1]):
        continue

    elif (s[1] < t[ 1]) and (s[1] > 1):
        continue


    print('No')
    quit()


print('Yes')

