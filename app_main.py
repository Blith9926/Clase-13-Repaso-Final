
import os 
from Gestion_ventas import ingresar_ventas
from analisi_ventas import analizar_ventas

def limpiar_pantalla():

    """Limpia la pantalla de la consola"""
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def menu():
    while True:
        limpiar_pantalla()
        print("\n 🛒 Menú Principal")
        print("1️⃣ Ingresar nuevas ventas")
        print("2️⃣ Analizar nuevas ventas(Requiere el archivo de ventas en formato CSV)")
        print("3️⃣ Salir")
        
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ingresar_ventas()
        elif opcion == "2":
            analizar_ventas()
        elif opcion == "3":
            print("¡Gracias por usar el sistema de gestión de ventas! ¡Hasta luego! 👋")
            break
        else:
            print("❌ Opción no válida. Por favor, seleccione una opción del menú.")
        input("Presione Enter para continuar...")


        

if __name__ == "__main__":
    print("Bienvenido al sistema de gestion de ventas artesanales!")
    menu()