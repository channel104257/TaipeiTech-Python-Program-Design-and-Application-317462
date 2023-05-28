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

                       
def generate_html_table(school, students):
    table_html = "<table border=1>\n"
    table_html += "    <tr>\n"
    table_html += "        <th>學校名稱</th> <th>學生人數</th>\n"
    table_html += "    </tr>\n"
    
    for i in range(len(school)):
        table_html += "    <tr>\n"
        table_html += "        <td>{}</td> <td>{}</td>\n".format(school[i], students[i])
        table_html += "    </tr>\n"
    
    table_html += "</table>"
    
    return table_html

fname = './111_student.csv'
print(fname)

index_inner = -1
school = []
students = []

with open(fname, "r", encoding='utf-8') as fp:
    strdata = fp.read()
    lines = strdata.strip().split('\n')
    index = 0  # for printing first line
    for line in lines:
        items = csv_split(line)
        
        if items[1] not in school and index != 0:
            index += 1
            index_inner += 1
            school.append(items[1])
            
            if items[4].find(",") != -1:
                items[4] = items[4].replace(",", "")
            students.append(int(items[4])) 
        elif index == 0:
            index += 1
        else:
            if items[4].find(",") != -1:
                items[4] = items[4].replace(",", "")
            students[index_inner] += int(items[4])

# 生成HTML表格
html_table = generate_html_table(school, students)

# 將HTML寫入檔案
with open('result.html', 'w', encoding='utf-8') as file:
    file.write(html_table)

