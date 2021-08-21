# Calcula el área de un círculo en base al radio proporcionado
# por el usuario.

# 1. Leer el valor del radio del usuario (entrada estándar)
# 2. Calcular el área del círculo
# 3. Imprimir el área en la pantalla (salida estándar)
#
# A = Pi x radio^2
PI = 3.14159

radio_str = input("Humano, dame el valor del radio =")
radio = float(radio_str)
area = PI * radio ** 2
print("El área del círculo es:", area)
