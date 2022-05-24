def mediana(a,b,c):
    return (a+b+c-max(a,b,c)-min(a,b,c))

x = float(input())
y = float(input())
z = float(input())

print(mediana(x,y,z))