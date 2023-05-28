def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

with open('fac.txt', 'w') as file:
    for i in range(1, 26):
        result = factorial(i)
        file.write(f"{i:>2}! = {result}\n")
