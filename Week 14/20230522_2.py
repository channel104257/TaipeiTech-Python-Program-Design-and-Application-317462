def binary(n):
    if n <= 1:
        print(n, end='')
    else:
        binary(n // 2)
        print(n % 2, end='')

for i in range(1, 16):
    print(f"{i:>2} -> ", end='')
    binary(i)
    print()
