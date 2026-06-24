
import json

lista_ventas = []

def cargar_ventas():

    global lista_ventas

    try:
        with open("ventas.json", "r") as archivo:
            lista_ventas = json.load(archivo)

    except FileNotFoundError:
        lista_ventas = []

def ver_ventas():

    if not lista_ventas:
        print("No hay ventas registradas.")
        return

    for venta in lista_ventas:
        print(
            f"Fecha: {venta['fecha']}, "
            f"Producto: {venta['producto']}, "
            f"Cantidad: {venta['cantidad']}, "
            f"Precio Unitario: {venta['precio_unitario']}, "
            f"Total: {venta['total_venta']}"
        )

def guardar_ventas():

    with open("ventas.json", "w") as archivo:
        json.dump(lista_ventas, archivo, indent=4)


def find_productos(productos, nombre_producto):

    for producto in productos:
        if producto["nombre"].lower() == nombre_producto.lower():
            return producto

    return None


def registrar_ventas(productos):

    fecha = input("Ingrese la fecha de la venta (dd/mm/yyyy): ")
    nombre_producto = input("Ingrese el nombre del producto vendido: ")

    producto = find_productos(productos, nombre_producto)

    if producto is None:
        print("Producto no encontrado.")
        return

    cantidad = int(input("Ingrese la cantidad vendida: "))

    precio_unitario = producto["precio"]
    total_venta = cantidad * precio_unitario

    venta = {
        "fecha": fecha,
        "producto": nombre_producto,
        "cantidad": cantidad,
        "precio_unitario": precio_unitario,
        "total_venta": total_venta
    }

    lista_ventas.append(venta)
    guardar_ventas()
    print("Venta registrada correctamente.")