def get_fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * get_fac(n-1)

for i in range(1, 26):
    factorial = get_fac(i)
    print(f"{i}! = {factorial}")

