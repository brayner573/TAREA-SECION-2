import random

def generar_numero_secreto(minimo, maximo):
    return random.randint(minimo, maximo)

#Definir la función principal del juego
def jugar_adivinanzas():
    print("¡Bienvenido al juego de adivinanzas!")
    minimo = int(input("Ingrese el número mínimo del rango: "))
    maximo = int(input("Ingrese el número máximo del rango: "))
    numero_secreto = generar_numero_secreto(minimo, maximo)
    
    intentos = 0
    historial = []
    limite_intentos = int(input("Ingrese el límite de intentos: "))
#Lógica del juego en un bucle while
    while True:
        suposicion = int(input(f"Adivina un número entre {minimo} y {maximo}: "))
        intentos += 1
        historial.append(suposicion)

        #Comparar la suposición con el número secreto y proporcionar retroalimentación
        if suposicion > numero_secreto:
            print("Demasiado alto")
        elif suposicion < numero_secreto:
            print("Demasiado bajo")
        else:
            print(f"¡Has ganado en {intentos} intentos!")
            print("Historial de suposiciones: ", historial)
            break
#Ejecutar el juego si el script se ejecuta directamente
if __name__ == '__main__':
    jugar_adivinanzas()
