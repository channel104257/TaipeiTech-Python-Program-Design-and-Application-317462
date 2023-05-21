import csv

# 開啟 CSV 檔案
with open('StudentScore.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

# 印出轉換前後的資料型態和內容
print("原始資料型態:")
for row in data:
    print(row)

# 轉換成績部分為整數
for row in data:
    for i in range(2, len(row)):
        row[i] = int(row[i])

print("\n字串分數轉換成int後的型態:")
for row in data:
    print(row)
