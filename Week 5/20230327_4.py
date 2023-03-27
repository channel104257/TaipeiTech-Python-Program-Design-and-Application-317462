import random as rand

num = rand.sample(range(1, 43), 6)
for i in num:
    print(i, ',', sep="", end="")


