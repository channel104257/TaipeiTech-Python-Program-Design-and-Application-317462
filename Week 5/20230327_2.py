for i in range(32, 128):
    print(i, ":\'", chr(i), '\' ', end=' ')
    if i % 10 == 1:
        print()