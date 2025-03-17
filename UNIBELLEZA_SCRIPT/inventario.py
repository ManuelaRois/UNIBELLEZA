inventario = {
    "maquillaje": {
        "lapiz delineador": {"Cantidad": 7, "Precio": 40},
        "paleta de sombras": {"Cantidad": 10, "Precio": 250},
        "base liquida": {"Cantidad": 5, "Precio": 30},
        "iluminador": {"Cantidad": 5, "Precio": 20},
        "pestañina": {"Cantidad": 20, "Precio": 17},
        "labial mate": {"Cantidad": 15, "Precio": 50},
        "corrector liquido": {"Cantidad": 12, "Precio": 35},
        "rubor en polvo": {"Cantidad": 8, "Precio": 45},
        "primer facial": {"Cantidad": 6, "Precio": 60}
    },
    "skincare": {
        "crema hidratante": {"Cantidad": 20, "Precio": 80},
        "serum vitamina C": {"Cantidad": 10, "Precio": 100},
        "protector solar SPF 50": {"Cantidad": 15, "Precio": 90},
        "tonico facial": {"Cantidad": 12, "Precio": 55},
        "agua micelar": {"Cantidad": 18, "Precio": 50},
        "aceite limpiador": {"Cantidad": 10, "Precio": 65}
    },
    "uñas": {
        "esmalte rojo": {"Cantidad": 20, "Precio": 20},
        "esmalte nude": {"Cantidad": 18, "Precio": 25},
        "quitaesmalte": {"Cantidad": 15, "Precio": 15},
        "lima de uñas": {"Cantidad": 25, "Precio": 10}
    },
    "accesorios": {
        "brocha para base": {"Cantidad": 10, "Precio": 35},
        "esponja de maquillaje": {"Cantidad": 15, "Precio": 20},
        "pinza para cejas": {"Cantidad": 8, "Precio": 15},
        "cepillo para pestañas": {"Cantidad": 10, "Precio": 12},
        "neceser de maquillaje": {"Cantidad": 5, "Precio": 100}
    }
}

def ver_inventario(usuarios):
    correo_usuario = input("Ingrese su correo electrónico (o presione Enter si no está registrado): ")
    descuento = 0.10 if correo_usuario in usuarios else 0

    print("\n--- Inventario ---")
    for categoria, productos in inventario.items():
        print(f"\n📌 Categoría: {categoria.capitalize()}")
        print("{:<25} {:<10} {:>10}".format("Producto", "Cantidad", "$Precio"))
        for producto, detalles in productos.items():
            precio_con_descuento = detalles['Precio'] * (1 - descuento)
            print("{:<25} {:<10} {:>10.2f}".format(producto, detalles['Cantidad'], precio_con_descuento))

    if descuento > 0:
        print("\n¡Se aplicó un descuento del 10% por estar registrado!🩷")

def buscar_producto():
    producto = input("Ingrese el nombre del producto a buscar: ").lower()
    encontrado = False

    for categoria, productos in inventario.items():
        if producto in productos:
            detalles = productos[producto]
            print(f"\n--- Detalles de '{producto}' ---")
            print(f"Categoría: {categoria.capitalize()}")
            print(f"Cantidad: {detalles['Cantidad']}")
            print(f"Precio: ${detalles['Precio']:.2f}")
            encontrado = True
            break
    
    if not encontrado:
        print(f"El producto '{producto}' no existe en el inventario.")

def agregar_producto():
    categoria = input("Ingrese la categoría: ").lower()
    if categoria not in inventario:
        print("Categoría inválida.")
        return

    producto = input("Ingrese el nombre del producto: ").lower()
    if producto in inventario[categoria]:
        print("El producto ya existe.")
        return
    
    try:
        cantidad = int(input("Ingrese la cantidad: "))
        precio = float(input("Ingrese el precio unitario: "))
        if cantidad < 0 or precio < 0:
            raise ValueError
    except ValueError:
        print("La cantidad y el precio deben ser valores positivos.")
        return

    inventario[categoria][producto] = {"Cantidad": cantidad, "Precio": precio}
    print(f"Producto '{producto}' agregado correctamente.")

def actualizar_cantidad():
    producto = input("Ingrese el nombre del producto: ").lower()
    for categoria, productos in inventario.items():
        if producto in productos:
            nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
            productos[producto]['Cantidad'] = nueva_cantidad
            print(f"Cantidad de '{producto}' actualizada a {nueva_cantidad}.")
            return
    print(f"El producto '{producto}' no existe en el inventario.")

def actualizar_precio():
    producto = input("Ingrese el nombre del producto: ").lower()
    for categoria, productos in inventario.items():
        if producto in productos:
            nuevo_precio = float(input("Ingrese el nuevo precio: "))
            productos[producto]['Precio'] = nuevo_precio
            print(f"Precio de '{producto}' actualizado a ${nuevo_precio:.2f}.")
            return
    print(f"El producto '{producto}' no existe en el inventario.")

def eliminar_producto():
    producto = input("Ingrese el nombre del producto: ").lower()
    for categoria, productos in inventario.items():
        if producto in productos:
            del productos[producto]
            print(f"Producto '{producto}' eliminado.")
            return
    print(f"El producto '{producto}' no existe en el inventario.")
