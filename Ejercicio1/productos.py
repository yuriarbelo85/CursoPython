


def agregar_producto(productos):

    producto = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))

    producto = {"nombre": producto, "precio": precio}
    productos.append(producto)

    print("Producto agregado exitosamente.")


def ver_productos(productos):

    if not productos:
        print("No hay productos en el listado.")

    else:
        for producto in productos:
            print(f"Nombre del Producto: {producto['nombre']}, Precio MXN: {producto['precio']}")


def buscar_productos(productos):
    
    nombre_producto = input("Ingrese el nombre del producto a buscar: ")

    for producto in productos:
        if producto["nombre"].lower() == nombre_producto.lower():
            print(f"Producto encontrado: Nombre del Producto: {producto['nombre']}, Precio MXN: {producto['precio']}")
            break
    else:
        print("Producto no encontrado.")

def modificar_producto(productos):
    
    nombre_producto = input("Ingrese el nombre del producto a modificar: ")

    for producto in productos:
        if producto["nombre"].lower() == nombre_producto.lower():
            nuevo_nombre = input("Ingrese el nuevo nombre del producto: ")
            nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
            producto["nombre"] = nuevo_nombre
            producto["precio"] = nuevo_precio
            print("Producto modificado exitosamente.")
            break
    else:
        print("Producto no encontrado.")


def eliminar_producto(productos):
    
    nombre_producto = input("Ingrese el nombre del producto a eliminar: ")

    for producto in productos:
        if producto["nombre"].lower() == nombre_producto.lower():
            productos.remove(producto)
            print("Producto eliminado exitosamente.")
            break
    else:
        print("Producto no encontrado.")    
