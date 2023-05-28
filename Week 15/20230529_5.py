fname = './names-10000.txt'

with open(fname, 'r', encoding='utf-8') as file:
    names = file.read().split(', ')
    zhange_count = 0

    for name in names:
        surname = name[0]  # 姓氏位于名字的第一个字符
        if surname == '張':
            zhange_count += 1

    print("姓張的人數：", zhange_count)
