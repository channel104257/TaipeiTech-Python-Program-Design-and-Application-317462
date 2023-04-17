data = ['台', '北', '科', '大', '電', '機', '二', '甲', '劉', '千', '榮']

for i in range(11):
    print(data, sep='')
    for j in range(0, i + 1):
            if i < 10:
                data[j] = data[i + 1]
