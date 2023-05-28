def csv_split(msg):
    msgLen = len(msg)
    items = []
    beg = 0
    index = 0
    while index < msgLen:
        if msg[index] == ',':
            items.append(msg[beg:index])
            beg = index + 1
        elif msg[index] == '"':
            beg = index + 1
            while True:
                index += 1
                if msg[index] == '"':
                    items.append(msg[beg:index])
                    beg = index + 2
                    index += 1
                    break
        index += 1
    
    if beg < msgLen:
        items.append(msg[beg:])
    
    return items

fname = './u1_new.csv'
print(fname)
html_table = ""

with open(fname, "r", encoding='utf-8') as fp:
    strdata = fp.read()
    lines = strdata.strip().split('\n')
    
    for line in lines:
        items = csv_split(line)
            
        if len(items[0]) > 2:
            html_table += "<a href=\""
            html_table += items[6]
            html_table += "\"target=_blank>{}</a>".format(items[1])
                
            html_table += "<p>{}-{}</p>\n".format(items[4], items[5])
                
            
                
with open('result.html', 'w', encoding='utf-8') as file:
    file.write(html_table)
