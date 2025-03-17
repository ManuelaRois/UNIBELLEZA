from inventario import (
    agregar_producto,
    ver_inventario,
    actualizar_cantidad,
    actualizar_precio,
    eliminar_producto,
    buscar_producto
)
from _usuarios import registrar_usuario, usuarios
from menu import mostrar_menu
from datetime import datetime

def verificar_vencimiento(producto, inventario):
    """Verifica si un producto está vencido antes de procesarlo."""
    for categoria, productos in inventario.items():
        if producto in productos:
            vencimiento = productos[producto].get("Vencimiento")
            if vencimiento:
                fecha_venc = datetime.strptime(vencimiento, "%Y-%m-%d").date()
                if fecha_venc < datetime.today().date():
                    print(f"⚠️ El producto '{producto}' está vencido y no puede ser vendido ni actualizado.")
                    return False
    return True

# Inicializar inventario como un diccionario vacío
inventario = {}

def main():
    while True:
        mostrar_menu()
        opcion = input("\n👉 Seleccione una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_inventario(inventario, usuarios)
        elif opcion == "3":
            producto = input("Ingrese el nombre del producto a actualizar: ").lower()
            if verificar_vencimiento(producto, inventario):
                actualizar_cantidad()
        elif opcion == "4":
            producto = input("Ingrese el nombre del producto a actualizar precio: ").lower()
            if verificar_vencimiento(producto, inventario):
                actualizar_precio()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            buscar_producto()
        elif opcion == "7":
            registrar_usuario()
        elif opcion == "8":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()