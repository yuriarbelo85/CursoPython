
ventas = []

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

    ventas.append(venta)

    print("Venta registrada correctamente.")