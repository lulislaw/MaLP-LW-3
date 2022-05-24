baseprice = 4
floatprice = 0.25
distanceplus = 140

def cost(distance):
    return (baseprice + (((distance*1000) // distanceplus) * floatprice))

dist = float(input())

print(cost(dist))