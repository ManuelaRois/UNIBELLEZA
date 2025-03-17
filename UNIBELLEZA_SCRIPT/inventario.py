from datetime import datetime
from _usuarios import usuarios  # Importar el diccionario de usuarios

# Diccionario para almacenar el inventario con categorías
inventario = {
    "maquillaje": {
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
    "skincare": {
        "crema hidratante": {"Cantidad": 20, "Precio": 80, "Vencimiento": "2026-01-20"},
        "serum vitamina C": {"Cantidad": 10, "Precio": 100, "Vencimiento": "2025-11-05"},
        "protector solar SPF 50": {"Cantidad": 15, "Precio": 90, "Vencimiento": "2025-07-15"},
        "tonico facial": {"Cantidad": 12, "Precio": 55, "Vencimiento": "2026-04-10"},
        "agua micelar": {"Cantidad": 18, "Precio": 50, "Vencimiento": "2026-08-05"},
        "aceite limpiador": {"Cantidad": 10, "Precio": 65, "Vencimiento": "2025-09-01"}
    },
    "uñas": {
        "esmalte rojo": {"Cantidad": 20, "Precio": 20, "Vencimiento": "N/A"},
        "esmalte nude": {"Cantidad": 18, "Precio": 25, "Vencimiento": "N/A"},
        "quitaesmalte": {"Cantidad": 15, "Precio": 15, "Vencimiento": "N/A"},
        "lima de uñas": {"Cantidad": 25, "Precio": 10, "Vencimiento": "N/A"}
    },
    "accesorios": {
        "brocha para base": {"Cantidad": 10, "Precio": 35, "Vencimiento": "N/A"},
        "esponja de maquillaje": {"Cantidad": 15, "Precio": 20, "Vencimiento": "N/A"},
        "pinza para cejas": {"Cantidad": 8, "Precio": 15, "Vencimiento": "N/A"},
        "cepillo para pestañas": {"Cantidad": 10, "Precio": 12, "Vencimiento": "N/A"},
        "neceser de maquillaje": {"Cantidad": 5, "Precio": 100, "Vencimiento": "N/A"},
    }
}

# Historial de ventas
historial_ventas = []

# Registrar venta
def registrar_venta():
    producto = input("Ingrese el nombre del producto vendido: ").lower()
    for categoria, productos in inventario.items():
        if producto in productos:
            try:
                cantidad_vendida = int(input("Ingrese la cantidad vendida: "))
                if cantidad_vendida < 0:
                    print("La cantidad vendida no puede ser negativa.")
                    return
                if cantidad_vendida > productos[producto]["Cantidad"]:
                    print("No hay suficiente inventario para esta venta.")
                    return
                productos[producto]["Cantidad"] -= cantidad_vendida
                total = cantidad_vendida * productos[producto]["Precio"]
                fecha = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

                # Solicitar el correo del usuario que realiza la venta
                correo_usuario = input("Ingrese el correo electrónico del usuario que realiza la venta: ")
                if correo_usuario in usuarios:
                    nombre_usuario = usuarios[correo_usuario]
                else:
                    nombre_usuario = "Usuario no registrado"

                # Agregar el usuario al registro de ventas
                historial_ventas.append({
                    "Producto": producto,
                    "Cantidad": cantidad_vendida,
                    "Total": total,
                    "Fecha": fecha,
                    "Usuario": nombre_usuario
                })
                print(f"Venta registrada: {cantidad_vendida} x '{producto}' = ${total:.2f} (Vendido por: {nombre_usuario})")
                return
            except ValueError:
                print("Cantidad inválida.")
                return
    print("Producto no encontrado.")

# Ver historial de ventas
def ver_historial_ventas():
    if not historial_ventas:
        print("No hay ventas registradas.")
        return

    print("\n--- Historial de Ventas ---")
    print("{:<20} {:<10} {:<10} {:<20} {:<20}".format("Producto", "Cantidad", "Total", "Fecha", "Usuario"))
    for venta in historial_ventas:
        print("{:<20} {:<10} {:<10.2f} {:<20} {:<20}".format(
            venta['Producto'], venta['Cantidad'], venta['Total'], venta['Fecha'], venta['Usuario']
        ))
