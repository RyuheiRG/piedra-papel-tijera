import numpy as np
import time

def piedra_papel_tijera():
    # Las opciones asignadas a lo que vencen
    opciones = {'piedra': 'tijera', 'tijera': 'papel', 'papel': 'piedra'}

    while True:
        # Elección del jugador
        jugador = input("Escribe piedra, papel o tijera: ").lower()
        while jugador not in opciones:
            print("Error al elegir tu movimiento...")
            jugador = input("Escribe piedra, papel o tijera: ").lower()

        # Elección de la computadora
        computadora = np.random.choice(['piedra', 'papel', 'tijera'])

        # Mostrar las selecciones
        time.sleep(0.5)
        print(f"\nHas seleccionado: {jugador}")
        print(f"La computadora ha seleccionado: {computadora}\n")
        time.sleep(1)

        # Determinar el ganador
        if opciones[jugador] == computadora:
            print("Has ganado!!! 🎉")
        elif opciones[computadora] == jugador:
            print("Has perdido :c")
        else:
            print("¡Empate!")

        # Preguntar si desea jugar otra vez
        jugar_otra = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_otra != 's':
            print("¡Gracias por jugar! 🎮")
            break

# Llamar a la función principal
if __name__ == "__main__":
    piedra_papel_tijera()
