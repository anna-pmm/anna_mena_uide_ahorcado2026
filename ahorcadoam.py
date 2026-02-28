# 1. Se crea la lista y aplico random.choice para que elija de manera aleatoria la palabra
import random

def elegir_palabra():
    palabras = ["python", "sistemas", "algoritmo", "bucles", "variable"]
    return random.choice(palabras)

# 2. Establece el inicio del juego para verificar el progreso
def inicializar_progreso(palabra):
    progreso = []
    i = 0
    while i < len(palabra):
        if i == 0 or i == len(palabra) - 1:
            progreso.append(palabra[i])
        else:
            progreso.append("_")
        i = i + 1
    return progreso

def mostrar_progreso(progreso):
    i = 0
    salida = ""
    while i < len(progreso):
        salida = salida + progreso[i] + " "
        i = i + 1
    print(salida)

def actualizar_progreso(palabra, progreso, letra):
    i = 0
    acierto = False
    while i < len(palabra):
        if palabra[i] == letra:
            progreso[i] = letra
            acierto = True
        i = i + 1
    return acierto

def progreso_completo(progreso):
    i = 0
    completo = True
    while i < len(progreso):
        if progreso[i] == "_":
            completo = False
        i = i + 1
    return completo

#3. Inicia el desarrollo para jugar
def jugar():
    palabra = elegir_palabra()
    intentos = 6
    progreso = inicializar_progreso(palabra)

    while intentos > 0 and not progreso_completo(progreso):
        mostrar_progreso(progreso)
        letra = input("Ingrese una letra: ")

        acierto = actualizar_progreso(palabra, progreso, letra)

        if acierto:
            print("Letra correcta")
        else:
            intentos = intentos - 1
            print("Letra incorrecta")
            print("Intentos restantes:", intentos)

    if progreso_completo(progreso):
        mostrar_progreso(progreso)
        print("¡Te salvaste!")
    else:
        print("¡Ahorcado!")
        print("La palabra era:", palabra)

jugar()