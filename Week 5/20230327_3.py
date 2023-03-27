msg = "早安的英文是Good morning, milk則是牛奶"
chinese = ""
others = ""

for character in msg:
    if ord(character) >= 20000:
        chinese += character
    else:
        others += character
        
print("chinese:", chinese)
print("others:", others)