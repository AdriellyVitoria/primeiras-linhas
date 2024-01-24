#Entradas int
a , b , c = map(int , input().split())
#Calculo
if a > b and a > c:
    print(f"{a} eh o maior")
elif b > a and b > c:
    print(f"{b} eh o maior")
else:
    print(f"{c}eh o maior")