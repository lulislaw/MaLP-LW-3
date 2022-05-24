import math


def gipo(kat1, kat2):
    return math.sqrt(kat1**2+kat2**2)


a = int(input())
b = int(input())

print(gipo(a,b))