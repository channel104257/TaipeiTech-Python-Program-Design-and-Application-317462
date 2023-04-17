if input1.isdigit():
    sort_array = []
    sum = 0
     
    for i in input1:
        sort_array.append(int(i))
        sum += int(i)
         
    sort_array.sort()
     
    print(sort_array)
    print('總和為 :', sum, ',最小值為 :', sort_array[0], ',最大值為 :', sort_array[4])
else:
    print('輸入數值錯誤')
