def simplevalue(n):
    a = int(n)
    simple = 0
    while(simple == 0):
        k = 0
        for i in range(a):
            i = i + 1
            if (a % i == 0):
                k = k + 1
        if (k > 2):
            a = a + 1
        else:
            return a, "Простое"
            simple = 1
            break


o = int(input())
print(simplevalue(o))