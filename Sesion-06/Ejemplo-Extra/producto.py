import json
import sqlite3

# Definición de constantes
NOMBRE_JSON = "productos.json"
NOMBRE_CSV = "productos.csv"


class Producto():
    """ Define los objetos de tipo Producto """
    def __init__(self, id_, nombre, cantidad, precio):
        """ constructor de la clase """
        self.id = id_
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    @property
    def subtotal(self):
        """ Calcula el subtotal en tiempo real """
        return self.cantidad * self.precio
    
    def __str__(self):
        """ Representación en str de un Producto """
        return f"({self.id}) {self.nombre}"

    def to_dict(self):
        """ Regresar en diccionario el Producto """
        return {
            "id": self.id,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio,
        }

# Funciones a nivel módulo
def imprimir_productos(productos):
    """ Imprime en la salida estándar la lista de productos """
    # Considerar que: productos -> [prod1, prod2, ...]
    print()
    print("Lista de productos")
    print("-" * 20)
    for p in productos:  # p es de tipo Producto()
        print(p)
    print("-" * 20)

def agrega_producto(productos):
    """ 
    Lee los datos de un productos desde el usuario y lo
    agrega a la lista de productos.
    """
    print()
    id_str = input("Escribe el id del producto: ")
    id_ = int(id_str)
    nombre = input("Escrime el nombre del producto: ")
    cantidad_str = input("Escribe la cantidad del producto: ")
    cantidad = int(cantidad_str)
    precio_str = input("Escribe el precio unitario del producto: ")
    precio = float(precio_str)

    producto = Producto(id_, nombre, cantidad, precio)
    productos.append(producto)
    print("Producto agregado correctamente!")
    print()

def elimina_producto(productos):
    """ Elimina un producto de la lista """
    print()
    id_str = input("Escribe el id del producto a eliminar: ")
    id_ = int(id_str)
    # Vamos a buscar el id en la lisra de productos
    producto_encontrado = False
    for producto in productos:
        if producto.id == id_:
            producto_encontrado = True
            break
    if producto_encontrado:
        productos.remove(producto)
        print("El producto ha sido eliminado")
    else:
        print("El id de producto no existe en la lista!")
    print()

def exportar_a_json(productos):
    """ Exporta la lista de producto a un archivo en formato JSON """
    productos_exportar = [p.to_dict() for p in productos]
    with open(NOMBRE_JSON, "w") as arch_txt:
        json.dump(productos_exportar, arch_txt, indent=4)
    print("Los productos han sido exportados de forma correcta!")
    print()

def importar_de_json():
    """ Importa la lista de productos desde un archivo en formato JSON """
    with open(NOMBRE_JSON) as arch_txt:
        datos = json.load(arch_txt)

    productos = []
    for p in datos:  # p es de tipo dict
        producto = Producto(
            p["id"],
            p["nombre"],
            p["cantidad"],
            p["precio"]
        )
        productos.append(producto)

    return productos
