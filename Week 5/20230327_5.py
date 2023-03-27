import random as rand

with open('C:/Users/chann/Desktop/Python程式設計概論與實作/20230327/Names-50.txt', 'r', encoding='utf-8') as f:
    lines = f.read()

namelist = lines.split('、')
name_score = []

for name in namelist:
    a = rand.randint(0, 100)
    b = rand.randint(0, 100)
    c = rand.randint(0, 100)
    name_temp = [name, a, b, c, format((a + b + c ) / 3, '.2f')]
    name_score.append(name_temp)
    
for data in name_score:
    print(data)