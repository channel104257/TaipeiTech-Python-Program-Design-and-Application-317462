info_input = input("請輸入身高(cm)及體重(kg)並以空格隔開 : ")
info = info_input.split()

BMI = float(info[1]) / (float(info[0]) / 100) ** 2

print(f'{BMI:.1f}')