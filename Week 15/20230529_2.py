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

fname = './111_basej.csv'
print(fname)
region = []
jh = []

with open(fname, "r", encoding='utf-8') as fp:
    strdata = fp.read()
    lines = strdata.strip().split('\n')
    index = 0  # for printing first line
    for line in lines:
        items = csv_split(line)
        
        if items[0] == "30":
            if items[2] not in region:
                index += 1
                region.append(items[2])
                jh.append(1) 
            else:
                jh[region.index(items[2])] += 1

for i in range(len(region)):
    print(f"{region[i]} : {jh[i]:>2} 間")