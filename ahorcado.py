import random
palabras = ["manzana", "jenga", "comandante", "palabra", "trama"]
palabra = random.choice(palabras)
adivinada = ""
intentos = 5
print("¡Juego del Ahorcado!")
print("Adivina la palabra.")
while intentos > 0:
    letra = input("Ingresa una letra: ")

    if letra in palabra:
        adivinada =adivinada+letra
        print("¡Correcto!")
    else:
        intentos =intentos-1
        print("Incorrecto. Te quedan", intentos, "intentos.")

    mostrada = ""
    for letra in palabra:
        if letra in adivinada:
            mostrada =mostrada+letra
        else:
            mostrada =mostrada+"_"
    print("Palabra:", mostrada)

    if "_" not in mostrada:
        print("¡Ganaste! La palabra era:", palabra)
        break

if intentos == 0:
    print("¡Perdiste! La palabra era:", palabra)
