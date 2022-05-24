fisrtcost = 10.95
othercost = 2.95

def allcost(count):
    if(count > 0):
        return (fisrtcost + ((count - 1)*othercost))
    else:
        return 0

a = int(input())
print(allcost(a))