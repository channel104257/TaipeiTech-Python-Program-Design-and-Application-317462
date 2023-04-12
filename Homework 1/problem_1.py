print("攝氏與華氏轉換:\n1) 攝氏轉華氏(C -> F)\n2) 華氏轉攝氏(F -> C)")
situ = int(input("您的選擇:"))

if situ == 1:
    tempC = int(input("請輸入攝氏溫度:"))
    tempF = 9 * tempC / 5 + 32
    print(f'{tempF:.1f}')
    
if situ == 2:
    tempF = int(input("請輸入華氏溫度:"))
    tempC = (tempF - 32) * 5 / 9
    print(f'{tempC:.1f}')
