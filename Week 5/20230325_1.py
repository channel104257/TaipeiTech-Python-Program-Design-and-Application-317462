def anonymize_name(name: str):
    if len(name) == 2:
        return name[0] + 'O'
    else:
        return name[0] + 'O' * (len(name) - 2) + name[-1]

with open('C:/Users/chann/Desktop/Python程式設計概論與實作/20230327/Names-50.txt', 'r', encoding='utf-8') as f:
    lines = f.read()

namelist = lines.split('、')

for name in namelist:
    print(anonymize_name(name),'、', sep='', end='')
