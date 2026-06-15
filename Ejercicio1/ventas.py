ventas = []

def registrar_ventas():
    fecha = input("Ingrese la fecha de la venta (dd/mm/yyyy): ")
    producto = input("Ingrese el nombre del producto vendido: ")
    cantidad = int(input("Ingrese la cantidad vendida: "))
    precio_unitario = float(input("Ingrese el precio unitario del producto: "))
    total_venta = cantidad * precio_unitario

    print("Producto agregado exitosamente.")

