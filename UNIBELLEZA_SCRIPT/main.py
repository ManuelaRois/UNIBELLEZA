
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

def main():
    while True:
        mostrar_menu()
        opcion = input("\n👉 Seleccione una opción: ")
        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            ver_inventario(usuarios)   # ✅ Ahora `usuarios` está importado correctamente
        elif opcion == "3":
            actualizar_cantidad()
        elif opcion == "4":
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
