import csv

# 開啟 CSV 檔案
with open('StudentScore.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)
    
# 印出原始資料
print("原始資料:")
for row in data:
    print(row)
    
# 轉換成績部分為整數
for row in data:
    for i in range(2, len(row)):
        row[i] = int(row[i])

# 計算總分並插入在成績之前
for row in data:
    total = sum(score for score in row[2:])
    row.insert(2, total)

# 印出插入總分後的結果
print("\n填入總分的結果:")
for row in data:
    print(row)
