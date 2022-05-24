def safepass(password):
    bigc = 0
    smallc = 0
    intc = 0
    for i in range(len(password)):

        if(ord(password[i]) < 33 or ord(password[i]) > 126):
            return("error 0")
            break
        if(ord(password[i]) > 64) and (ord(password[i]) < 91):
            bigc = bigc + 1
        if (ord(password[i]) > 96) and (ord(password[i]) < 123):
            smallc = smallc + 1
        if (ord(password[i]) > 47) and (ord(password[i]) < 58):
            intc = intc + 1
    if((len(password) > 7) and (bigc > 0) and (smallc > 0) and (intc > 0)):
        return("true")
    else:
        return("false", "Пароль не надежный")







if __name__ == "__main__":
    print("Введите пароль:")
    p = str(input())
    print(safepass(p))