import time
def passw():
   password = ""
   sp = int(str(time.time())[len(str(time.time())) - 1])
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
   return password






if __name__ == "__main__":
  print("Пароль",passw())