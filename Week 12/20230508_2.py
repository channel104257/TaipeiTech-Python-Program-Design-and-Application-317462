def markline(length=15, mark='-'):
    print('\n', mark*length, sep='')
    
def csv_split(msg):
    msgLen = len(msg)
    items = []
    beg = 0
    index = 0
    while(index < msgLen):
        if msg[index] == ',':
            items.append(msg[beg:index])
            beg = index + 1
        elif msg[index] == '"':
            beg = index + 1
            while(True):
                index += 1
                if (msg[index] == '"'):
                    items.append(msg[beg:index])
                    beg = index + 2
                    index += 1
                    break;
        index += 1
        
    if beg < msgLen:  # index已過了字串結尾！
        items.append(msg[beg:])
    elif beg >= msgLen and msg[-1]!='"':  # 結束是: ',' or '"'。 
        items.append(msg[beg:])

    return items


fname = ['./108_student.csv', './109_student.csv', './110_student.csv', './111_student.csv']

student_category = ['日 博士', '日 碩士', '日 四技', '日 五專', '職 碩士', '修 四技', '修 二技']
student_number = []
field = [8,9]  # 指定欄位的索引值。

for file in fname:
    #print(file)

    with open(file, "r", encoding='utf-8') as fp:
        strdata = fp.read()
        lines = strdata.strip().split('\n')
        index = 0  # for printing first line
        temp = []
    
        for line in lines:
            items = csv_split(line)
        
            if items[1] == '國立臺北科技大學':
                index += 1
                for f in field:
                    if items[f-1].find(",") != -1:
                        items[f-1] = items[f-1].replace(",", "")
                    if items[f-1] == ' -' or items[f-1] == '-':
                        items[f-1] = 0
                    
                temp.append(int(items[field[0] - 1]) + int(items[field[1] - 1]))
                #print(int(items[field[0] - 1]) + int(items[field[1] - 1]))
                #markline() 
                
    field = [field[0] + 2, field[1] + 2]
    student_number.append(temp)
        

for category in student_category:
    print(category , end=',')
markline()

i = 108

for student_grade in student_number:
    print(str(i) + "學年")
    i += 1
    for student in student_grade:
        print(student , sep='', end=',')
    markline()