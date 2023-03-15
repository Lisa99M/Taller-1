# Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.

x = float(input("Digite un número real: "))
y = float(input("Digite un número real: "))

if y % x == 0:
    print("El número " + str(x) + " es múltiplo de " + str(y))
else:
    print("El número " + str(x) + " no es múltiplo de " + str(y)) 