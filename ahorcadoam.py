palabra = "python"
intentos = 6  
# 6 errores = 6 partes del cuerpo del ahorcado

while intentos > 0:
    letra = input("Ingrese una letra: ")

    # Validación: si la letra está entre p,y,t,h,o,n es correcta caso contrario refleja un intento menos
    if (letra == "p" or letra == "y" or letra == "t" or
        letra == "h" or letra == "o" or letra == "n"):
        print("Letra correcta")
    else:
        intentos = intentos - 1
        print("Letra incorrecta")

# Al salir del bucle, significa que intentos ya no es mayor que 0
print("Ahorcado!")