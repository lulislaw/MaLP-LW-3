import time
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
        return("true", password)

    else:
        return("false")

def passw():
   password = ""
   sp = int(str(time.time())[len(str(time.time())) - 2])
   if (sp < 7):
      sp = 8
   if (sp < 4):
      sp = 11
   t = 1
   while (t < sp):
      t = t + 1
      a = str(time.time() * t)
      i = int(a[len(a) - 2] + a[len(a) - 1])
      i = i + 33
      if (i > 126):
         i = 125
      if (i < 33):
         i = 32
      password = password + chr(i)
   return(safepass(password))









# Не всегда срабатывет, порой не выводит
if __name__ == "__main__":
    a = 0
    while(not(passw().__contains__("true"))):
        a = a +1
        print(a, "Пароль", passw())
