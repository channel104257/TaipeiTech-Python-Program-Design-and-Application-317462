list = [1, 2, 3, 4, 5]

for i in range(0, len(list)):
    for j in range(0, len(list)):
        index = j - i
        print(list[index], sep='', end='')
        if (j + 1) % 5 == 0:
            print("\n", end="")
