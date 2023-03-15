#Programa para calcular el mayor de tres números reales

a: float = input("inserte valor de a")
b: float = input("inserte valor de b")
c: float = input("inserte valor de c")

if a>b>c or a>c>b:
    print("El mayor número es " + str(a))
elif b>a>c or b>c>a:
    print("El mayor número es " + str(b))
else:
    print("El mayor número es " + str(c))