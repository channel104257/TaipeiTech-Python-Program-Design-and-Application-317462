# 引用 python decimal 模組
from decimal import Decimal

# 取輸入為Decimal
num = Decimal(input('please enter a number : '))

# 利用 divmod 函式，將 num 除以 1 取出 商(integer_part) 及 餘數(decimal_part)
integer_part, decimal_part = divmod(num, 1)

print("整數 :", integer_part)
print("小數 :", decimal_part)