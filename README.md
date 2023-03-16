# Taller-1 Grupo Attack On Coding
![attack on coding](https://user-images.githubusercontent.com/124607325/225370329-96e3bfc0-d0a4-4adf-bda7-91cd5fc0260f.jpeg)

# Primer punto #
1. Realice el quiz Python Beginner Quiz (20 preguntas) y adjunte pantallazo con el resultado (mínimo 90% bien).
[![2023-03-15-15.png](https://i.postimg.cc/jjJ1dgxn/2023-03-15-15.png)](https://postimg.cc/hJcs207K)

[![2023-03-15-22.png](https://i.postimg.cc/Rh7L82Dr/2023-03-15-22.png)](https://postimg.cc/XBv5B1Wx)

# Segundo punto #
2. Realice un programa que lea tres números reales y determine cuál es el mayor.

### Diagrama de flujo ###
[![](https://mermaid.ink/img/pako:eNqNkk1OwzAQRq8y8qoV6aKwi6AImgYqARvYQNLFKJ62Fokd_AOq0l6MLRfDjQmFCqRGiuRJ3ud5sqdhheLEYjYv1VuxRG3hIckl-OeiN5WiEKoPg8EILjPpKtJqGIMmLCFUx7-qk1DN2sA4QyMWEjW8Yqk04Bc0jLosrLrcDELLcZtMmonp4KOOPe3Y801gky27fiSzhkl2g2BchcAJSmWA-7fWYsv7nT7ew4IMVCS9yosjoBIs6cL_CLrTXipk_-fWd2oN6V8qo32VdKdydbgKrg5QSb9VrrN9j7Pd8bWxg1uLhfN39n9rFjHPVii4H4xmK5Izu6SKchb7JUf9nLNcbjyHzqr7lSxYbLWjiLmao6VE4EJjxeI5lsZ_JS6s0rdh0tqBi1iN8kmpjtl8AoEp1-g?type=png)](https://mermaid.live/edit#pako:eNqNkk1OwzAQRq8y8qoV6aKwi6AImgYqARvYQNLFKJ62Fokd_AOq0l6MLRfDjQmFCqRGiuRJ3ud5sqdhheLEYjYv1VuxRG3hIckl-OeiN5WiEKoPg8EILjPpKtJqGIMmLCFUx7-qk1DN2sA4QyMWEjW8Yqk04Bc0jLosrLrcDELLcZtMmonp4KOOPe3Y801gky27fiSzhkl2g2BchcAJSmWA-7fWYsv7nT7ew4IMVCS9yosjoBIs6cL_CLrTXipk_-fWd2oN6V8qo32VdKdydbgKrg5QSb9VrrN9j7Pd8bWxg1uLhfN39n9rFjHPVii4H4xmK5Izu6SKchb7JUf9nLNcbjyHzqr7lSxYbLWjiLmao6VE4EJjxeI5lsZ_JS6s0rdh0tqBi1iN8kmpjtl8AoEp1-g)

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
# Tercer punto #
3. Realice un programa que lea un número enteros y determine si es par o impar.
###  Diagrama de flujo ### 
![Diagrama de flujo punto 3](https://user-images.githubusercontent.com/124607325/225164100-c29c5ffe-fcb1-4f42-b618-bc0ae9b55476.png)

Se pide que ingrese un número entero.
![Ingresar un numero entero](https://user-images.githubusercontent.com/124607325/225150478-5549a790-0748-44ee-b7fb-10a0c7f51071.png)

El número ingresado se almacena como un entero en la variable n.
![Tercer punto Codigo](https://user-images.githubusercontent.com/124607325/225164326-03c2d08d-aece-4dd3-8168-f97dd510c11e.png)

Si el número n es impar,  se determinará usando n % 2 != 0, que devuelve verdadero si el resto de la división de n entre 2  es cero, e imprime que el número ingresado no es par.
![RESULTADO NUMERO NO PAR](https://user-images.githubusercontent.com/124607325/225151673-45464d1a-d59e-40a8-8303-e387ea1061a5.png)

Si el resultado de la expresión anterior es falso, se imprime un mensaje que indica que el número es par y finaliza el programa
![Resultado numero par](https://user-images.githubusercontent.com/124607325/225151781-53d82469-fee8-4d5a-a1bd-f0295a6c34cc.png)

# Cuarto punto # 
4. Realice un programa que lea dos números reales y determine si el primero es múltiplo del segundo.

4.1. Lo primero que haremos será pedirle al usuario que ingrese dos números reales los cuáles serán guardados en las variables "x" y "y".

![image](https://user-images.githubusercontent.com/124721286/225158538-56d34329-febd-4d5c-8921-2e02b1b2bbdf.png)

4.2.  Para saber si el primer número es múltimplo del segundo, lo que debemos hacer es comprobar si el residuo de dividir el primero por el segundo es igual a cero.

![image](https://user-images.githubusercontent.com/124721286/225160077-f51bc1c0-7cbb-49c3-acc2-cf9aab3c7830.png)

4.3.  Si lo anterior sucede, podremos decir que el primer número ingresado es múltiplo del segundo.

![image](https://user-images.githubusercontent.com/124721286/225160193-4b5f14e0-bb89-403d-9795-4896bacc88b7.png)

4.4. Si por le contrario, el residuo al realizar la división del primero por el segundo es diferente de creo, diremos que el primer número no es múltiplo del segundo.

![image](https://user-images.githubusercontent.com/124721286/225160367-00cbd1ae-b3ba-485c-b878-9f3299fb6b69.png)

4.5. Ejemplo usando los números 5 y 10:

![image](https://user-images.githubusercontent.com/124721286/225160454-3842e637-336c-49ca-b752-6370545e2117.png)

![image](https://user-images.githubusercontent.com/124721286/225160478-086c9a9a-73b8-4dc3-9b13-dd108e984137.png)

![image](https://user-images.githubusercontent.com/124721286/225160504-f8d56fd3-348f-4f92-b36b-76358f994abc.png)

  4.6. Ejemplo usando los números 6 y 21:
  
  ![image](https://user-images.githubusercontent.com/124721286/225160580-111b5f28-0195-466d-8db3-924edbf178cf.png)
  
  ![image](https://user-images.githubusercontent.com/124721286/225160613-5479f83b-739b-499f-9a1e-930651da0a29.png)
  
  ![image](https://user-images.githubusercontent.com/124721286/225160651-545139cb-0e11-4a7a-ac27-6033effe7158.png)

  4.7. Código completo:
  
  ![image](https://user-images.githubusercontent.com/124721286/225160698-8b52941c-d65d-4c49-87b2-b5a511e53abf.png)

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
# Sexto Punto #
6.Escriba un programa que solicite al usuario una letra y determine si es una vocal o una consonante.

6.1. Se pide ingresar una letra y se almacena en la variable "letra".

![INGRESE UNA LETRA](https://user-images.githubusercontent.com/124607325/225466419-34b83e1f-afb0-48fc-97aa-d86707fe5097.png)

6.2. Se verifica si la letra ingresada es una vocal con una serie de declaraciones "if" y "elif" para comprobar si la letra ingresada es una vocal o una consonante.

![Lista de variables letras](https://user-images.githubusercontent.com/124607325/225466808-1e796b2d-994f-4325-968c-ac0446be0cf9.png)

![Lista de variables letras 2](https://user-images.githubusercontent.com/124607325/225466812-41f607d5-5b62-40cd-b858-91314384d5fd.png)

6.3. Si la letra es una vocal, se imprime un mensaje indicando que la letra es una vocal.

![VOCAL](https://user-images.githubusercontent.com/124607325/225466979-56e0f6aa-7f62-4fce-83ac-38bb7eaa0259.png)

6.4. Si la letra es una consonante, se imprime un mensaje indicando que la entrada es una consonante.

![CONSONANTE](https://user-images.githubusercontent.com/124607325/225467043-d49f3db2-4863-4297-a70b-845ff79875cb.png)

6.5. Si la letra no es una consonante ni una vocal, se imprime un mensaje indicando que la entrada no es una letra. y el programa finaliza.

![No es una letra](https://user-images.githubusercontent.com/124607325/225467109-b199aa6e-3c77-4d6d-954a-274e361ab547.png)

# Séptimo punto #
7. Escriba un programa que pida 5 números reales y calcule las siguientes operaciones:

   - El promedio
   - La mediana
   - El promedio multiplicativo (multilplica todos y luego calcula la raíz de la cantidad de operandos)
   - Ordenar los números de forma ascendente
   - Ordenar los números de forma descendente
   - La potencia del mayor número elevado al menor número
   - La raíz cúbica del menor número
   
7.1. Lo primero que haremos será pedirle al usuario que digite cinco números reales los cuales guardaremos en las variables "a", "b", "c", "d" y "e".
   
![image](https://user-images.githubusercontent.com/124721286/225161047-0634ea4a-0fef-42ad-9182-2ef81503515f.png)

7.2. Debido a que gran parte de los items solicitados requieren de que los números ingresados sean ordenados, procederemos a realizar esta acción. Lo primero que haremos será determinar cuál de los números ingresados es el mayor de todos, esto lo conseguimos al realizar la comparación de uno por uno con los demás. Si se cumple la condición de que un número sea mayor que los otros, entonces le asignaremos ese número a la variable "mayor".

![image](https://user-images.githubusercontent.com/124721286/225161397-a9aebde4-0125-43d4-ad8e-d53c4d63bd98.png)

![image](https://user-images.githubusercontent.com/124721286/225161432-b8331ec8-7ec0-44a3-87a3-ed98be125e7b.png)

![image](https://user-images.githubusercontent.com/124721286/225161455-6cb2ef81-3873-4aa1-82ee-71aea7502539.png)

![image](https://user-images.githubusercontent.com/124721286/225161508-651b8585-fdc1-4184-aec1-0429821d4e46.png)

![image](https://user-images.githubusercontent.com/124721286/225161554-275c5b0b-2994-4102-8575-2094694873bb.png)

7.3. Una vez definido cuál es el mayor, procederemos a determinar cuál de los números ingresados es el que le sigue en orden descendente al mayor. Lo anterior lo lograremos si empezamos a comparar los números que no corresponden a mayor con los demás y lo guardaremos en la variable "medio3". Por ejemplo: si determinamos que el número mayor es "a" lo que haremos para determinar "medio3" será comparar "b", "c", "d" y "e" de tal forma que el que sea mayor entre estos se le asignará la variable "medio3". Sin embargo, no podemos olvidar que posiblemente "a" no sea el número mayor, por lo que es candidato a ser "medio3" por lo tanto debemos incluirlo en los casos donde no es el mayor. (Las siguientes imagenes corresponden al ejemplo de cuando a es el mayor, ya que se repite en los demas casos solo que esta vez obviando a sus respectivos mayores)

![image](https://user-images.githubusercontent.com/124721286/225163188-906dd8b7-f023-4899-9d9c-d6565aaa9055.png)

![image](https://user-images.githubusercontent.com/124721286/225162370-d4c5f238-7cb9-40a5-a8cc-1eb9a98dc054.png)

![image](https://user-images.githubusercontent.com/124721286/225162414-f4da9192-476d-4bef-9ee3-f60147b33f2b.png)

![image](https://user-images.githubusercontent.com/124721286/225162439-94528431-73d1-4a0f-a1e9-ef85a1d2a912.png)

7.4. De la misma forma procederemos con el número que le sigue al anterior es decir a "medio3", este lo guardaremos en la variable "medio2". No debemos olvidar que debemos obviar los números "mayor" y "medio3", ya que se supone que estos ya fueron determinados anteriormente. (Las siguientes imagenes corresponden a cuando "b" es "medio3", ya que el procedimiento se repite para los demas casos).

![image](https://user-images.githubusercontent.com/124721286/225163383-a7dde842-07ae-471b-9994-cc017ae44db7.png)

![image](https://user-images.githubusercontent.com/124721286/225163552-f09fa280-36d2-4b92-825a-388c04e482d5.png)

![image](https://user-images.githubusercontent.com/124721286/225163573-3e5f4d0b-8531-4d2c-900b-20446ecab777.png)

7.5. Ahora, lo que debemos hacer es determinar el siguiente número descendente y el menor, estos los guardaremos en las variables "medio1" y "menor" correspondientemente. Para esto, debemos comprarar los dos últimos números que nos faltan (olvidando a "mayor", "medio3" y "medio2") y determinar cuál es el número mayor entre estos. (Las siguientes imagenes corresponden a cuando "c" es "medio2", ya que este procedimiento se repite para los demas casos).

![image](https://user-images.githubusercontent.com/124721286/225163946-f91fc767-12ec-40ce-8423-bf7dd3659e19.png)

7.6. Los pasos 3, 4 y 5 deben repetirse para los distintos casos posibles.

7.7. Una vez ordenados los números, procedemos a solucionar los items que nos están solicitando, en este caso el promedio. Para esto, lo único que debemos hacer es realizar la suma de los números ingresados y el resultado dividirlo entre cinco. El resultado de toda la operación lo guardaremos en la variable "promedio". Luego de haber realizado el cálculo le mostraremos al usuario el resultado.

![image](https://user-images.githubusercontent.com/124721286/225164682-9614a439-f5a0-4724-b059-306277df5c27.png)

7.8. Para la mediana, lo único que debemos hacer es mostrarle el valor de la variable "medio2", puesto que, al haber ordenado de forma previa los números, el número de la mitad correspondería a el valor de "medio2".

![image](https://user-images.githubusercontent.com/124721286/225164905-59f3da54-abb5-420b-81d5-f347d48cca92.png)

7.9. En el siguiente item nos piden calcular el promedio multiplicativo; para esto, lo que debemos hacer es realizar la multiplicación de todos los números ingresados y lo obtenido, elevarlo a la 1/5. El resultado lo guardaremos en la variable "pmult". Una vez hecho esto, le mostraremos al usuario el resultado.

![image](https://user-images.githubusercontent.com/124721286/225165273-8e3a53f8-2156-485f-a5d5-2abdce60ae88.png)

7.10. En el siguiente item nos piden que organicemos los números de forma ascendente. Sin embargo, al tener ya los números ordenados, lo único que deberemos hacer es mostrarle al usuario un mensaje situando como primer número a "menor", seguido de esto a "medio1", luego a "medio2", después "medio3" y por último a "mayor".

![image](https://user-images.githubusercontent.com/124721286/225165806-d7bd98dd-92a5-4dd0-becf-3fb7b146527e.png)

7.11. Luego de haber hecho esto, debemos organizar los números en forma descendente, asi que realizaremos lo mismo que en el paso anterior solo que esta vez el orden sera primero "mayor", el siguiente será "medio3", luego "medio2", seguido de "medio1" y en último lugar posicionaremos a "menor".

![image](https://user-images.githubusercontent.com/124721286/225166099-b2f77a39-fb9b-4ce0-8846-130286ba4132.png)

7.12. El penúltimo item nos pide que elevemos el mayor número al menor número, para esto, simplemente usamos el simbolo de potencia en python, El resultado de esta operación lo guardaremos en la variable "pot", y una vez hecho el cálculo mostraremos el resultado en un mensaje.

![image](https://user-images.githubusercontent.com/124721286/225166432-8cfd9cee-76fa-42a4-9157-60a35a6856c6.png)

7.13. Por último, debemos calcular la raíz cúbica del menor número, así que, usando el símbolo de potencia en python, elevaremos el menor número a la 1/3. Cuando tengamos el resultado, lo guardaremos en la variable "raíz" y le mostraremos el resultado al usuario.

![image](https://user-images.githubusercontent.com/124721286/225166727-13248533-2643-4990-9b1c-2edc041d4ea5.png)

7.14. Ejemplo usando los números 45, 21, 7, 56 y 2.

![image](https://user-images.githubusercontent.com/124721286/225166858-2930a780-da15-4d6e-b9c3-b7dbbce2778c.png)

![image](https://user-images.githubusercontent.com/124721286/225166880-12175733-a113-461d-a39b-016f5170bd19.png)

![image](https://user-images.githubusercontent.com/124721286/225166902-49ca5b6e-0bfb-4e0c-b419-3f3bab5e6cc0.png)

![image](https://user-images.githubusercontent.com/124721286/225166929-d681a313-4517-461f-a191-62fe0d6cf9c3.png)

![image](https://user-images.githubusercontent.com/124721286/225166952-cead5d65-4058-439f-ada6-96b4f12a299d.png)

![image](https://user-images.githubusercontent.com/124721286/225166997-57a8b9e9-d947-4e1e-9b55-e92dffa8d88e.png)

7.15. Código completo
        
        ![image](https://user-images.githubusercontent.com/124721286/225167155-13c0510e-0afa-4376-948b-6a8597f0b79a.png)
        ![image](https://user-images.githubusercontent.com/124721286/225167220-9d57abbc-a512-4cb8-8573-b8f2ebd9a1f4.png)
        ![image](https://user-images.githubusercontent.com/124721286/225167276-59301dad-b08e-415b-9c22-a8c6476c2970.png)
        ![image](https://user-images.githubusercontent.com/124721286/225167311-ca1a1cc0-1ff3-43af-8004-e001b76fc46a.png)
        ![image](https://user-images.githubusercontent.com/124721286/225167352-e08f6d52-072f-48dc-89ac-1f7d2a76c0aa.png)
        ![image](https://user-images.githubusercontent.com/124721286/225167389-4dad3515-ed2d-4e01-a2d8-52ef7cd439c1.png)
        ![image](https://user-images.githubusercontent.com/124721286/225167423-4807aa4b-2f89-4950-a871-eeb1bdef04ba.png)
        ![image](https://user-images.githubusercontent.com/124721286/225167538-0c22d092-6da5-40fe-9724-f93cd88702d7.png)
        ![image](https://user-images.githubusercontent.com/124721286/225167578-241846f0-59cf-457b-b8f9-4ed05e852a06.png)
        ![image](https://user-images.githubusercontent.com/124721286/225167635-055e1879-90ca-409f-a226-044526f1131e.png)
        ![image](https://user-images.githubusercontent.com/124721286/225167681-fc43dcd6-2991-47fb-bbcd-94f0f0a0ef08.png)
        ![image](https://user-images.githubusercontent.com/124721286/225167725-a9a69704-ab4f-4356-9f95-94ec62d109f1.png)
        ![image](https://user-images.githubusercontent.com/124721286/225167842-22feb582-e3d0-482c-bbfa-3b4873753a92.png)
        ![image](https://user-images.githubusercontent.com/124721286/225167914-ef447554-5896-4bb3-b48d-27a41af45688.png)


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

# Noveno Punto #
9. Escriba un programa que reciba el nombre en minúsculas de un país de America y retorne la ciudad capital, si el país no pertenece al continente debe arrojar país no identificado.

9.1. Se solicita al usuario que ingrese el nombre en minúsculas de un país de América.

![Ingresar ](https://user-images.githubusercontent.com/124607325/225161919-6af31f40-5540-4b65-a3a5-6f82c716ee5f.png)

9.2. Se comprueba si el nombre ingresado está en una lista de países americanos utilizando la declaración if Nombre in (...):.

![9 punto](https://user-images.githubusercontent.com/124607325/225161930-f381481f-53d5-45e5-aedc-c6703b1734af.png)

9.3. Si el país está en la lista, el programa imprime un mensaje que indica que el país es de América.

![Lista de paises](https://user-images.githubusercontent.com/124607325/225162628-a3dc8919-8593-4409-85ac-91a4de81b700.png)

![Lista de paises 2](https://user-images.githubusercontent.com/124607325/225162630-6de98076-1f05-43ac-b50a-3e6f91fe5d75.png)

9.4. Se utiliza una serie de declaraciones elif para determinar la capital del país.

![Pais, capital](https://user-images.githubusercontent.com/124607325/225162733-0a3039b9-7d0f-47e1-9d78-c8048f1a58d7.png)

9.5. Si el nombre ingresado no está en la lista de países, el programa imprime un mensaje que indica que el país no se pudo identificar y se finaliza el programa.

![No identificado](https://user-images.githubusercontent.com/124607325/225162747-a61f3671-17e9-4770-b5b1-030ff77d2356.png)

# Décimo punto # 
10. Escriba un programa que dada una distancia calcule:

   - El tiempo que le tomaría a la luz recorrer la distancia.
   - El tiempo que le tomaría al sonido (en el aire) recorrer la distancia.
   - El tiempo que le tomaría al vehiculo comercial más veloz recorrer la distancia.
   - El tiempo que le tomaría a Bolt recorrer la distancia.
   
10.1. Como primer paso le pediremos al usuario que nos digite una distancia en metros. Esta distancia se guardará el la variable "x".

![image](https://user-images.githubusercontent.com/124721286/225168303-e92e9fd8-3140-41b7-bdfd-2ddadf06f15d.png)
      
10.2. Seguido de esto calcularemos el tiempo que le tomaría a la luz recorrer esa distancia. Esto lo haremos dividiendo la distancia "x" entre la velocidad de la luz en metros sobre segundo (299.792.458 m/s). El resultado lo guardaremos en la variable "tluz".

![image](https://user-images.githubusercontent.com/124721286/225168534-92943f2d-8de4-4cac-b351-5ffafea2b058.png)

10.3. Igual que en el paso anterior, calcularemos el tiempo pero esta vez el que le toma al sonido en recorrer la distancia "x" usando, dividiendo la x sobre la velocidad del sonido en metros sobre segundo (343.2 m/s). El resultado lo guardaremos en la variable "tsonido".

![image](https://user-images.githubusercontent.com/124721286/225168993-971fb60e-60d4-4153-9416-f9e189e0dd52.png)

10.4. Para el tiempo que le tomaría al vehículo comercial más caro, repetiremos el proceso de los pasos anterios solo que esta vez usando la velocidad correspondiente en metros sobre segundo (141.111 m(/s). El resultado lo guardaremos en la variable "tvehiculo".

![image](https://user-images.githubusercontent.com/124721286/225169520-c05d1611-16b5-4024-8da9-5a2f58c5b91f.png)

10.5. Ahora, calculamos el tiempo que le tomaria a Usain Bolt recorrer la distancia ingresada, dividiendo la misma entre la velocidad del corredor en metros sobre segundo (12.4 m/s). El resultado lo guardaremos en la variable "tbolt".

![image](https://user-images.githubusercontent.com/124721286/225170041-d724e43e-7608-45b6-b510-69870115e02e.png)

10.6. Cómo paso final le mostraremos al usuario varios mensajes indicando los tiempos calculados para cada caso.

![image](https://user-images.githubusercontent.com/124721286/225170108-6940ccdb-ac4c-4176-bffd-c63052c845db.png)

10.7. Ejemplo usando una distacncia de 100.000.000 metros.

![image](https://user-images.githubusercontent.com/124721286/225170197-29566ae6-8c26-4c5c-b818-d9702f4a16c5.png)

![image](https://user-images.githubusercontent.com/124721286/225170242-3b928fac-f54a-4589-9d97-de25be2142f4.png)
      
### Diagrama de flujo punto 10 ###
   [![](https://mermaid.ink/img/pako:eNo1kc9PgzAUgP8V8k6YMKQtjJZEEzfG9OBJT44dKnSuEdqFFWVb9r_bFXynl_d9eT_yLlDpWkAGu0b_VnveGe89L5Vn42nzomQl9dabzR69hV802nBlhDfcjcLCgaU_eA9eLY8WVpJPbOlY7pumP1s83GPGUobjhE5C7oSVb45ayVo7h8QkxBNfOV745kfsZdU3o4FiFCKEJqdwzto3n7oxI8dh_N9h7ejzppBqWyoIoBVdy2Vtj73cjBLMXrSihMymNe--SyjV1Xq8N_rtpCrITNeLAPpDzY3IJf_qeAvZjjdHWz1wBdkFBshwmoSYURzhlFBGcDIP4AQZoSGL5zRCJMU4pXN2DeCste0QhSyKCImp5UmKSBKAqKXR3ev4C_cSN-HD-bc1rn_SVXdW?type=png)](https://mermaid.live/edit#pako:eNo1kc9PgzAUgP8V8k6YMKQtjJZEEzfG9OBJT44dKnSuEdqFFWVb9r_bFXynl_d9eT_yLlDpWkAGu0b_VnveGe89L5Vn42nzomQl9dabzR69hV802nBlhDfcjcLCgaU_eA9eLY8WVpJPbOlY7pumP1s83GPGUobjhE5C7oSVb45ayVo7h8QkxBNfOV745kfsZdU3o4FiFCKEJqdwzto3n7oxI8dh_N9h7ejzppBqWyoIoBVdy2Vtj73cjBLMXrSihMymNe--SyjV1Xq8N_rtpCrITNeLAPpDzY3IJf_qeAvZjjdHWz1wBdkFBshwmoSYURzhlFBGcDIP4AQZoSGL5zRCJMU4pXN2DeCste0QhSyKCImp5UmKSBKAqKXR3ev4C_cSN-HD-bc1rn_SVXdW)


