# Segundo punto #
2. Realice un programa que lea tres números reales y determine cuál es el mayor.

En primer lugar se le pedirá al usuario asignar valor a cada una de las variables (a, b y c) que serán almacenadas como flotantes. 
[![Insertando-valores.png](https://i.postimg.cc/QCjswYK5/Insertando-valores.png)](https://postimg.cc/34fPDBBJ)

Se realizan las correspondientes comparaciones a partir de los valores insertados y se establece una alternativa de mensaje para cada situación. 
[![Ejemplo-con-5-78-y-3.png](https://i.postimg.cc/QtQh6ZCh/Ejemplo-con-5-78-y-3.png)](https://postimg.cc/ftRGLFYr)

Código completo:

```
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
```

# Quinto punto #
5. Realice un programa que lea tres números reales y determine si la suma de los dos primeros es mayor, menor o igual que el tercer número.

Igualmente el programa inicia pidiéndole al usuario asignar valor a las variables (numero1, numero2, y numero3) que fueron declaradas como flotantes. Se realiza la suma de los dos primeros números y se establece un mensaje para cada una de las posibles situaciones al comparar el resultado con el tercer valor. 
[![Ejemplo-con-16-4-y-20.png](https://i.postimg.cc/L8mSsbxb/Ejemplo-con-16-4-y-20.png)](https://postimg.cc/HVvRZBDw)

Codigo completo:

```
# Programa que lee tres números reales y determina si la suma de los dos primeros es mayor, menor o igual que el tercer número.

numero1: float
numero1 = float(input("Insertar valor de numero1"))
numero2: float
numero2 = float(input("Insertar valor de numero2"))
numero3: float
numero3 = float(input("Insertar valor de numero3"))

if numero1+numero2 < numero3:
    print("La suma de los dos primeros números es menor que el tercero")
elif numero1+numero2 > numero3:
    print("La suma de los dos primeros números es mayor que el tercero")
else:
    print("La suma de los dos primeros números es igual que el tercero")
```

# Octavo punto #
8. Escriba un programa al que se le ingrese la frecuencia de una onda en hz y como salida arroje en que parte del espectro electromagnético se encuentra.

El usuario debe insertar el valor de la frecuencia para el cuál se desea conocer el espectro electromagnético. Dicha variable es previamented declarada y almacenada como un valor flotante. 

En el programa se establecen los diferentes casos de clasificación dentro del espectro electromagnético de acuerdo a los valores de frecuencia. Si la condición no se cumple se pasa a la siguiente, hasta que se establesca una condicón verdadera y entonces el programa arrojará el mensaje correspondiente.

Ejemplo: Para una frecuencia de 67e17:
[![Rayos-x-67e17.png](https://i.postimg.cc/j5TM4HPL/Rayos-x-67e17.png)](https://postimg.cc/hJC8S7CB)

Para una frecuencia de 589e8:
[![microondas-589e8.png](https://i.postimg.cc/s27nW6Bk/microondas-589e8.png)](https://postimg.cc/Y42fKxzR)

Los valores de frecuencia asignados a los diferentes espectros electromagnéticos fueron tomados de [la vieja confiable](https://es.wikipedia.org/wiki/Espectro_electromagn%C3%A9tico "la vieja confiable") 

[![Espectro-Tabloid.jpg](https://i.postimg.cc/m2cxgFfK/Espectro-Tabloid.jpg)](https://postimg.cc/crNkDCJc)

```

# Programa al que se le ingresa la frecuencia de una onda en hz y como salida arroja en que parte del espectro electromagnético se encuentra.
frecuencia: float
frecuencia = float(input("Agregar el valor de la frecuencia en Hz, usar notación científica si es necesario: "))


if frecuencia >= 1e19 :
    print("Rayos gamma")
elif frecuencia >= 30e15 and frecuencia < 30000e15 :
    print("Rayos X")
elif frecuencia >= 790e12 and frecuencia < 30e15 : 
    print("Radiación ultravioleta")
elif frecuencia >= 430e12 and frecuencia < 790e12 :
    print("Espectro visible de la luz")
elif frecuencia >= 300e9 and frecuencia < 430e12 : 
    print("Espectro infrarrojo")
elif frecuencia >= 300e6 and frecuencia < 300e9 : 
    print("Radiación de microondas")
elif frecuencia >= 300e6 and frecuencia < 10e9 :
    print("Ondas de radio de ultra alta frecuencia")
elif frecuencia >= 30e6 and frecuencia > 300e6 :
    print("Ondas de radio de muy alta frecuencia")
elif frecuencia >= 1e6 and frecuencia < 30e6 :
    print("Onda corta de radio")
elif frecuencia >= 300e3 and frecuencia < 1e6 :
    print("Onda media de radio")
elif frecuencia >= 30e3 and frecuencia < 300e3 :
    print("Onda larga de radio")
else:
    frecuencia >= 3 and  frecuencia < 30e3
    print("Onda de radio de muy baja frecuencia")

```
