import random
INTENTOS_FIJOS = 5
ultimo_modo = None
ultimo_resultado = None
ultima_palabra = None
Mostradas=[]

def mostrar_palabra(palabra, adivinadas):
    resultado = ""
    for letra in palabra:
        if letra in adivinadas:
            resultado += letra + " "
        else:
            resultado += "_ "
    return resultado.strip()

def un_jugador():
    global ultimo_modo, ultimo_resultado, ultima_palabra
    intentos = INTENTOS_FIJOS
    palabras = ["manzana", "jenga", "comandante", "palabra", "trama"]
    palabra = random.choice(palabras)
    adivinadas = []
    print("\n--- MODO UN JUGADOR ---")
    print(mostrar_palabra(palabra, adivinadas))
    while intentos > 0:
        letra = input("Ingresa una letra: ")
        if letra in adivinadas:
            print("Ya ingresaste esa letra.")
            continue
        adivinadas.append(letra)
        if letra in palabra:
            print("Correcto!")
        else:
            intentos -= 1
            print("Incorrecto. Te quedan", intentos, "intentos.")
        print("Palabra:", mostrar_palabra(palabra, adivinadas))
        if "_" not in mostrar_palabra(palabra, adivinadas):
            print("¡Ganaste! La palabra era:", palabra)
            ultimo_modo = "Un jugador"
            ultimo_resultado = "Ganó"
            ultima_palabra = palabra
            Mostradas.append(palabra)
            return
    print("¡Perdiste! La palabra era:", palabra)
    ultimo_modo = "Un jugador"
    ultimo_resultado = "Perdió"
    ultima_palabra = palabra
    
def contra_computadora():
    global ultimo_modo, ultimo_resultado, ultima_palabra
    intentos = INTENTOS_FIJOS
    palabra = input("\nEscribe una palabra para que la computadora la adivine: ")
    adivinadas = []
    abecedario = list("abcdefghijklmnopqrstuvwxyz")
    print("\n--- MODO CONTRA LA COMPUTADORA ---")
    print(mostrar_palabra(palabra, adivinadas))

    while intentos > 0 and len(abecedario) > 0:
        letra = random.choice(abecedario)
        abecedario.remove(letra)
        print("\nComputadora: ¿La palabra tiene la letra", letra, "?")
        respuesta = input("Responde (si o no): ")
        while respuesta != "si" and respuesta != "no":
                respuesta = input("Responde (si o no): ")
        if respuesta == "si":
              adivinadas.append(letra)
              print("Correcto!")
        if respuesta == "no":
              intentos -= 1
              print("Incorrecto. Intentos restantes:", intentos)
        print("Palabra:", mostrar_palabra(palabra, adivinadas))
        if "_" not in mostrar_palabra(palabra, adivinadas):
            print("La computadora ganó. La palabra era:", palabra)
            ultimo_modo = "Contra computadora"
            ultimo_resultado = "Computadora ganó"
            ultima_palabra = palabra
            Mostradas.append(palabra)
            return
    print("La computadora perdió. La palabra era:", palabra)
    ultimo_modo = "Contra computadora"
    ultimo_resultado = "Computadora perdió"
    ultima_palabra = palabra

def multijugador():
    global ultimo_modo, ultimo_resultado, ultima_palabra
    intentos = INTENTOS_FIJOS
    jugador1 = input("\nNombre del Jugador 1: ")
    jugador2 = input("Nombre del Jugador 2: ")
    palabra = input(jugador1 + ", escribe la palabra: ")
    adivinadas = []
    print("\n--- MODO MULTIJUGADOR ---")
    print(jugador2, "debe adivinar la palabra.")
    print(mostrar_palabra(palabra, adivinadas))

    while intentos > 0:
        letra = input(jugador2 + ", ingresa una letra: ")
        if letra in adivinadas:
            print("Ya ingresaste esa letra.")
            continue
        adivinadas.append(letra)
        if letra in palabra:
            print("Correcto!")
        else:
            intentos -= 1
            print("Incorrecto. Te quedan", intentos, "intentos.")
        print("Palabra:", mostrar_palabra(palabra, adivinadas))
        if "_" not in mostrar_palabra(palabra, adivinadas):
            print("¡", jugador2, "ganó! La palabra era:", palabra)
            ultimo_modo = "Multijugador"
            ultimo_resultado = jugador2 + " ganó"
            ultima_palabra = palabra
            Mostradas.append(palabra)
            return
    print("¡", jugador2, "perdió! La palabra era:", palabra)
    ultimo_modo = "Multijugador"
    ultimo_resultado = jugador2 + " perdió"
    ultima_palabra = palabra

def ver_estadisticas():
    if ultimo_modo is None:
        print("\nNo hay estadísticas aún.")
    else:
        print("\n--- ESTADÍSTICAS ---")
        print("Modo:", ultimo_modo)
        print("Resultado:", ultimo_resultado)
        print("Palabra:", ultima_palabra)

def reglas():
    print("\n===Reglas====")
    print("1. Leer las ordenes")
    print("2. disfrutar")

def menu():
    while True:
        print("\n=== JUEGO DEL AHORCADO ===")
        print("1. Jugar")
        print("2. Reglas")
        print("3. estadisticas")
        print("4. Palabras adivinadas")
        print("5. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            submenu()
        elif opcion == "2":
            reglas()
        elif opcion == "3":
            ver_estadisticas()
        elif opcion == "4":
            print("Palabras ya usadas: ", Mostradas)
        elif opcion == "5":
            print("Gracias por jugar!")
            break
        else:
            print("Opción inválida.")

def submenu():
    while True:
        print("\n===Modos de juego===")
        print("1. Solo jugador")
        print("2. Contra la computadora")
        print("3. Multijugador")
        print("4. Volver a menu principal")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            un_jugador()
        elif opcion == "2":
            contra_computadora()
        elif opcion == "3":
            multijugador()
        elif opcion == "4":
            break
        else:
            print("Opción inválida.")

menu()