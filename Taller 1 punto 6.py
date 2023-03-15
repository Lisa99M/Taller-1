#6. Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante.

letra = input("Ingrese una letra  ")

if letra in ('a', 'e', 'i', 'o', 'u'):
    print("La letra " + str(letra) + " ingresada es una vocal.")
elif letra in ('b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'):
    print("La letra " + str(letra) +" ingresada es una consonante.")
else:
    print("La entrada " + str(letra) + " ingresada no es una letra") 