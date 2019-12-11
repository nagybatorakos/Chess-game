import string

str = input("String: ") # <>={}

num,lower,upper,other = 0,0,0,0
lower_com,upper_com = ["á", "é", "í","ó", "ö", "ő", "ú", "ü", "ű"], ["Á", "É", "Í", "Ó", "Ö", "Ő", "Ú", "Ü", "Ű"]
for i in str.replace(" ", ""):
    if i in string.ascii_lowercase or i in lower_com:
        lower += 1
    elif i in string.ascii_uppercase or i in upper_com:
        upper += 1
    elif i.isdigit():
        num += 1
    else:
        other += 1
print("num = {}\nlower = {}\nupper = {}\nother = {}".format(num, lower, upper, other))


