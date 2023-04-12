import random
list = []
info = {}

for i in range(25):
    temp = random.randint(1, 9)
    list.append(temp)
    for j in range(10): 
        if (temp == j):
            if (j in info):
                info[j] += 1
                break
            else:
                info[j] = 1
                break

print(list)
          
for i in range(1, 10): 
    if (i not in info):
        print(i, '->', 0, sep=' ', end=', ')
    else:
        print(i, '->', info[i], sep=' ', end=', ')