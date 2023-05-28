def binary8(n):
    if n == 0:
        return '00000000'  # 若 n 為 0，直接回傳八個 0
    else:
        binary = bin(n)[2:]  # 使用內建函式 bin() 取得二進位表示法，並去除前綴 '0b'
        return '0' * (8 - len(binary)) + binary

# 測試 1 到 15 的二進位轉換結果
for i in range(1, 16):
    binary = binary8(i)
    print(f'{i:>2} -> {binary}')

