# Juego de adivinanza de números (by Álvaro Santamaría).
# Generaremos un número aleatorio entre 0 y 99, el jugador tiene que adivinarlo.
# Si el intento es fallido, indicará si el número es mayor o menor y continuará el juego, hasta que el jugador adivine el número.
# El programa cuenta los intentos válidos y muestra un mensaje de éxito al adivinar el número.
# Si el intento no es válido (fuera del rango 0-99 o no es un número), se muestra un mensaje de error.

import random

numero_secreto = random.randint(0, 99)
contador_intentos = 0

while True:
    try:
        intento = int(input("Escribe un número entre 0 y 99: "))

        if intento >= 0 and intento <= 99:  # Define como intento válido cualquier número entero entre 0 y 99.
            contador_intentos += 1   # Incrementa el contador de intentos por cada intento válido.

        if intento == numero_secreto:   # Si el intento corresponde con el número, muestra mensaje de éxito y termina el programa. 
            if contador_intentos == 1:
                print(f"¡Enhorabuena! Has acertado el número en {contador_intentos} intento.")
            else:
                print(f"¡Enhorabuena! Has acertado el número en {contador_intentos} intentos.")
            break
        elif intento < 0 or intento > 99:
            print("Por favor, escribe un número entre 0 y 99.")
        elif intento < numero_secreto:
            print("El número es mayor.")
        else:
            print("El número es menor.")
    except ValueError:
        print("Por favor, escribe un número entre 0 y 99.")