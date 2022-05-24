def simpleint(t):
    k = 0
    a = int(t)
    for i in range (a):
        i = i + 1
        if(a % i == 0):
            k = k + 1
    if(k > 2):
        return("false")
    else:
        return ("true")






if __name__ == "__main__":
    b = int(input())
    print(simpleint(b))