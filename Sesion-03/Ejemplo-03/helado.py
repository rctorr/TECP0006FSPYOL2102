import os

# Definición de funciones
def borrar_terminal():
    """ Borra la terminal """
    os.system("clear")  # Linux y Mac
    # os.system("cls")  # Windows

def imprime_toppings(menu):
    """ Imprime la lista de opciones de toppings """
    print()
    print("-" * 25)
    print(f"{menu[0][0]}. {menu[0][1]}")
    print(f"{menu[1][0]}. {menu[1][1]}")
    print(f"{menu[2][0]}. {menu[2][1]}")
    print(f"{menu[3][0]}. {menu[3][1]}")
    print("-" * 25)

def lee_respuesta():
    """ Leer las opción elegida por el usuario """
    opcion_str = input("Elige el topping: ")
    opcion = int(opcion_str)
    return opcion

def imprime_precio(opcion):
    """ Imprime el precio del Helado en base al valor de la opcion """
    if opcion == 1:
        precio = 19
    elif opcion == 2:
        precio = 25
    elif opcion == 3:
        precio = 22
    elif opcion == 4:
        precio = 28
    else:
        precio = 0

    if precio == 0:
        print("El Helado elegido no existe!")
    else:
        # print("El valor del helado es ${:.2f} M.N.".format(precio))
        print(f"El valor del helado es ${precio:.2f} M.N.")


def main():
    """ Función principal del programa """

    # 1. Imprimir la lista de opciones en la pantalla
    # 2. Leer la opción elegida por el usuario
    # 3. En base a la opción del usuario imprimir el valor del helado
    menu = (
        (1, "Helado con oreo"),     # 0
        #0  1
        (2, "Helado con m&m"),      # 1
        (3, "Helado con fresas"),   # 2
        (4, "Helado con brownie"),  # 3
    )
    borrar_terminal()
    imprime_toppings(menu)
    opcion = lee_respuesta()
    imprime_precio(opcion)

# Para validar si este script es el programa principal
if __name__ == "__main__":
    main()

