'''
Escriba un programa que dada una distancia calcule:

    - El tiempo que le tomaría a la luz recorrer la distancia.
    - El tiempo que le tomaría al sonido (en el aire) recorrer la distancia.
    - El tiempo que le tomaría al vehiculo comercial más veloz recorrer la distancia.
    - El tiempo que le tomaría a Bolt recorrer la distancia.
    
'''
x = float(input("Ingrese una distancia en metros: "))

tluz = x/299792458
tsonido = x/343.2
tvehiculo = x/141.111
tbolt = x/12.4

print("El tiempo que le tomaría en recorrer la distancia "+str(x)+" m a la luz en segundos es: "+str(tluz)+"\n")
print("El tiempo que le tomaría en recorrer la distancia "+str(x)+" m al sonido en segundos es: "+str(tsonido)+"\n")
print("El tiempo que le tomaría en recorrer la distancia "+str(x)+" m al vehículo comercial mas veloz en segundos es: "+str(tvehiculo)+"\n")
print("El tiempo que le tomaría en recorrer la distancia "+str(x)+" m a Usain Bolt en segundos es: "+str(tbolt)+"\n")