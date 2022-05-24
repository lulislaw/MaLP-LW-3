arr = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh","twelfth"]

def intb(intt):
    b = int(intt)
    if(b >= 1) and (b <= 12):
        return arr[b-1]
    else:
        return ""

if __name__ == "__main__":
    for i in range(12):
        print(i + 1, arr[i])

    a = int(input())
    print(intb(a))

