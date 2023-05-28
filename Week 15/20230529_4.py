import re

phones = "0930654321, 0924-135-246, 0922  132456, 0938 258-369, 0933"

# 移除空格和其他非數字字符
phones = re.sub(r'\D', '', phones)

# 將手機號碼按照指定格式進行拆分和格式化
formatted_phones = [phones[i:i+4] + ' ' + phones[i+4:i+7] + '-' + phones[i+7:i+10] for i in range(0, len(phones), 10)]

# 列印結果
for phone in formatted_phones:
    print(phone)
