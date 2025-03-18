from datetime import datetime

# Diccionario para almacenar el inventario con categorías
inventario = {
    "maquillaje 💄": {
        "lapiz delineador": {"Cantidad": 7, "Precio": 40, "Vencimiento": "2025-08-15"},
        "paleta de sombras": {"Cantidad": 10, "Precio": 250, "Vencimiento": "2026-02-10"},
        "base liquida": {"Cantidad": 5, "Precio": 30, "Vencimiento": "2024-12-30"},
        "iluminador": {"Cantidad": 5, "Precio": 20, "Vencimiento": "2026-05-20"},
        "pestañina": {"Cantidad": 20, "Precio": 17, "Vencimiento": "2025-06-10"},
        "labial mate": {"Cantidad": 15, "Precio": 50, "Vencimiento": "2026-09-15"},
        "corrector liquido": {"Cantidad": 12, "Precio": 35, "Vencimiento": "2025-12-01"},
        "rubor en polvo": {"Cantidad": 8, "Precio": 45, "Vencimiento": "2026-07-18"},
        "primer facial": {"Cantidad": 6, "Precio": 60, "Vencimiento": "2026-03-22"}
    },
    "skincare💆🏻‍♀️": {
        "crema hidratante": {"Cantidad": 20, "Precio": 80, "Vencimiento": "2026-01-20"},
        "serum vitamina C": {"Cantidad": 10, "Precio": 100, "Vencimiento": "2025-11-05"},
        "protector solar SPF 50": {"Cantidad": 15, "Precio": 90, "Vencimiento": "2025-07-15"},
        "tonico facial": {"Cantidad": 12, "Precio": 55, "Vencimiento": "2026-04-10"},
        "agua micelar": {"Cantidad": 18, "Precio": 50, "Vencimiento": "2026-08-05"},
        "aceite limpiador": {"Cantidad": 10, "Precio": 65, "Vencimiento": "2025-09-01"}
    },
    "uñas 💅": {
        "esmalte rojo": {"Cantidad": 20, "Precio": 20, "Vencimiento": "N/A"},
        "esmalte nude": {"Cantidad": 18, "Precio": 25, "Vencimiento": "N/A"},
        "quitaesmalte": {"Cantidad": 15, "Precio": 15, "Vencimiento": "N/A"},
        "lima de uñas": {"Cantidad": 25, "Precio": 10, "Vencimiento": "N/A"}
    },
    "accesorios 💍": {
        "brocha para base": {"Cantidad": 10, "Precio": 35, "Vencimiento": "N/A"},
        "esponja de maquillaje": {"Cantidad": 15, "Precio": 20, "Vencimiento": "N/A"},
        "pinza para cejas": {"Cantidad": 8, "Precio": 15, "Vencimiento": "N/A"},
        "cepillo para pestañas": {"Cantidad": 10, "Precio": 12, "Vencimiento": "N/A"},
        "neceser de maquillaje": {"Cantidad": 5, "Precio": 100, "Vencimiento": "N/A"},
    }
}

# Diccionario para almacenar usuarios registrados con información adicional
usuarios = {}

# Historial de ventas
historial_ventas = []

# REGISTRAR USUARIO
def registrar_usuario(usuarios):
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo electrónico: ")
    telefono = input("Ingrese su número de teléfono: ")
    direccion = input("Ingrese su dirección: ")

    if correo in usuarios:
        print(f"El correo '{correo}' ya está registrado.")
    else:
        usuarios[correo] = {"nombre": nombre, "telefono": telefono, "direccion": direccion}
        print(f"Usuario '{nombre}' registrado correctamente.")

# VER INVENTARIO
def ver_inventario(inventario, usuarios):
    hoy = datetime.now().date()
    correo_usuario = input("Ingrese su correo electrónico (o presione Enter si no está registrado): ")
    descuento = 0.10 if correo_usuario in usuarios else 0

    print("\n--- Inventario ---")
    for categoria, productos in inventario.items():
        print(f"\n📌 Categoría: {categoria.capitalize()}")
        print("{:<25} {:<10} {:>10} {:>15}".format("Producto", "Cantidad", "$Precio", "Vencimiento"))
        for producto, detalles in productos.items():
            precio_con_descuento = detalles['Precio'] * (1 - descuento)
            vencimiento = detalles.get("Vencimiento", "N/A")
            if vencimiento != "N/A":
                try:
                    fecha_venc = datetime.strptime(vencimiento, "%Y-%m-%d").date()
                    if fecha_venc < hoy:
                        continue  # Omitir productos vencidos
                except ValueError:
                    print(f"Error en la fecha de vencimiento del producto '{producto}'. Formato incorrecto.")
                    continue
            else:
                vencimiento = "Sin vencimiento"
            print("{:<25} {:<10} {:>10.2f} {:>15}".format(producto, detalles['Cantidad'], precio_con_descuento, vencimiento))

    if descuento > 0:
        print("\n¡Se aplicó un descuento del 10% por estar registrado!🩷")
    print("\nNota: Los productos vencidos no se muestran en el inventario.")

# REGISTRAR VENTA
def registrar_venta(inventario, usuarios):
    producto = input("Ingrese el nombre del producto vendido: ").lower()
    for categoria, productos in inventario.items():
        if producto in productos:
            try:
                cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
                if cantidad_vendida < 0:
                    print("La cantidad vendida no puede ser negativa.")
                    return
                if cantidad_vendida > productos[producto]["Cantidad"]:
                    print(f"No hay suficiente inventario para esta venta. Solo hay {productos[producto]['Cantidad']} unidades disponibles.")
                    return
                productos[producto]["Cantidad"] -= cantidad_vendida
                total = cantidad_vendida * productos[producto]["Precio"]
                fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Solicitar el correo del usuario que realizó la compra
                correo_usuario = input("Ingrese el correo electrónico del usuario que realizó la compra: ")
                if correo_usuario in usuarios:
                    nombre_usuario = usuarios[correo_usuario]["nombre"]
                    telefono_usuario = usuarios[correo_usuario]["telefono"]
                    direccion_usuario = usuarios[correo_usuario]["direccion"]
                else:
                    nombre_usuario = "Usuario no registrado"
                    telefono_usuario = "N/A"
                    direccion_usuario = "N/A"

                # Agregar el usuario al registro de ventas
                historial_ventas.append({
                    "Producto": producto,
                    "Cantidad": cantidad_vendida,
                    "Total": total,
                    "Fecha": fecha,
                    "Usuario": nombre_usuario,
                    "Correo": correo_usuario,
                    "Telefono": telefono_usuario,
                    "Direccion": direccion_usuario
                })
                print(f"Venta registrada: {cantidad_vendida} x '{producto}' = ${total:.2f} (Vendido por: {nombre_usuario}, Teléfono: {telefono_usuario}, Dirección: {direccion_usuario})")
                return
            except ValueError:
                print("Cantidad inválida. Por favor, ingrese un número entero.")
                return
    print("Producto no encontrado.")

# AGREGAR PRODUCTO
def agregar_producto(inventario):
    categoria = input("Ingrese la categoría del producto: ").lower()
    producto = input("Ingrese el nombre del producto: ").lower()
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        precio = float(input("Ingrese el precio del producto: "))
    except ValueError:
        print("Entrada inválida. Por favor, ingrese números válidos.")
        return
    vencimiento = input("Ingrese la fecha de vencimiento del producto (YYYY-MM-DD) o 'N/A' si no aplica: ")

    if categoria not in inventario:
        inventario[categoria] = {}
    inventario[categoria][producto] = {"Cantidad": cantidad, "Precio": precio, "Vencimiento": vencimiento}
    print(f"Producto '{producto}' agregado correctamente en la categoría '{categoria}'.")

# ACTUALIZAR CANTIDAD DE PRODUCTO
def actualizar_cantidad(inventario):
    categoria = input("Ingrese la categoría del producto: ").lower()
    producto = input("Ingrese el nombre del producto: ").lower()
    if categoria in inventario and producto in inventario[categoria]:
        try:
            nueva_cantidad = int(input("Ingrese la nueva cantidad del producto: "))
            if nueva_cantidad < 0:
                print("La cantidad no puede ser negativa.")
                return
            inventario[categoria][producto]["Cantidad"] = nueva_cantidad
            print(f"Cantidad del producto '{producto}' actualizada a {nueva_cantidad}.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
    else:
        print("Producto no encontrado en el inventario.")

# ACTUALIZAR PRECIO DE PRODUCTO
def actualizar_precio(inventario):
    categoria = input("Ingrese la categoría del producto: ").lower()
    producto = input("Ingrese el nombre del producto: ").lower()
    if categoria in inventario and producto in inventario[categoria]:
        try:
            nuevo_precio = float(input("Ingrese el nuevo precio del producto: "))
            if nuevo_precio < 0:
                print("El precio no puede ser negativo.")
                return
            inventario[categoria][producto]["Precio"] = nuevo_precio
            print(f"Precio del producto '{producto}' actualizado a {nuevo_precio}.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido.")
    else:
        print("Producto no encontrado en el inventario.")

# ELIMINAR PRODUCTO
def eliminar_producto(inventario):
    categoria = input("Ingrese la categoría del producto: ").lower()
    producto = input("Ingrese el nombre del producto: ").lower()
    if categoria in inventario and producto in inventario[categoria]:
        del inventario[categoria][producto]
        print(f"Producto '{producto}' eliminado de la categoría '{categoria}'.")
    else:
        print("Producto no encontrado en el inventario.")

# BUSCAR PRODUCTO
def buscar_producto(inventario):
    producto = input("Ingrese el nombre del producto a buscar: ").lower()
    encontrado = False
    for categoria, productos in inventario.items():
        if producto in productos:
            detalles = productos[producto]
            print(f"Producto encontrado en la categoría '{categoria}': {detalles}")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado en el inventario.")

# VER HISTORIAL DE VENTAS
def ver_historial_ventas():
    if not historial_ventas:
        print("No hay ventas registradas.")
        return

    print("\n--- Historial de Ventas ---")
    print("{:<20} {:<10} {:<10} {:<20} {:<20} {:<25} {:<20}".format("Producto", "Cantidad", "Total", "Fecha", "Usuario", "Correo", "Teléfono", "Dirección"))
    for venta in historial_ventas:
        print("{:<20} {:<10} {:<10.2f} {:<20} {:<20} {:<25} {:<20}".format(
            venta['Producto'], venta['Cantidad'], venta['Total'], venta['Fecha'], venta['Usuario'], venta['Correo'], venta['Telefono'], venta['Direccion']
        ))

# MOSTRAR MENÚ
def mostrar_menu():
    print("\n--- Menú de Inventario ---")
    print("1. Agregar producto")
    print("2. Ver inventario")
    print("3. Actualizar cantidad de producto")
    print("4. Actualizar precio de producto")
    print("5. Eliminar producto")
    print("6. Buscar producto")
    print("7. Registrar usuario")
    print("8. Registrar venta")
    print("9. Ver historial de ventas")
    print("10. Salir")

# DICCIONARIO DE FUNCIONES
opciones = {
    '1': lambda: agregar_producto(inventario),
    '2': lambda: ver_inventario(inventario, usuarios),
    '3': lambda: actualizar_cantidad(inventario),
    '4': lambda: actualizar_precio(inventario),
    '5': lambda: eliminar_producto(inventario),
    '6': lambda: buscar_producto(inventario),
    '7': lambda: registrar_usuario(usuarios),
    '8': lambda: registrar_venta(inventario, usuarios),
    '9': lambda: ver_historial_ventas()
}

# EJECUTAR MENÚ
def main():
    print("¡Bienvenido al sistema de gestión de inventario! 💄✨")
    print("Aquí podrás gestionar tu inventario, registrar ventas, usuarios y mucho más.\n")
    
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción: ")
        if opcion == "10":
            print("Saliendo del sistema...¡Gracias por visitarnos 💋!")
            break
        if opcion in opciones:
            opciones[opcion]()  # Ejecuta la función correspondiente
        else:
            print("❌ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
