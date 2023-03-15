frecuencia = float(input("Agregar el valor de la frecuencia en Hz: "))


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