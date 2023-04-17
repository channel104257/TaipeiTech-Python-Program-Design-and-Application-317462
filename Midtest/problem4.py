import random as rand

namestr = '楊美君;陳心怡;蕭建智;沈嘉鳳;錢紫鑫;徐盈君;李政祥;王雅婷;阮宏喜;甄佳穎'
namelist = namestr.split(';')

data = []
#print(len(namelist))
for i in range(len(namelist)):
    temp = []
    
    temp_str = '電機二甲-' + f'{i + 1:0>3}'
    temp.append(temp_str)
    
    temp.append(namelist[i])
    
    for i in range(3):
        temp.append(rand.randint(50, 99))
    
    data.append(temp)

for i in data:
    print(i)   
    
print('\n')
    
for i in data:
    temp_a = i[2]
    temp_b = i[3]
    temp_c = i[4]
    #sum = data[i][2] + data[i][3] + data[i][4]
    sum = temp_a + temp_b + temp_c
    i.insert(2, sum)
    
for i in data:
    print(i)
