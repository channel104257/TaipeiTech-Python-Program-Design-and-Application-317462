def anonymize_name(name: str) -> str:
    if len(name) == 2:
        return name[0] + 'O'
    else:
        return name[0] + 'O' * (len(name) - 2) + name[-1]
   
name = input("輸入名字 : ")     
print(anonymize_name(name))
