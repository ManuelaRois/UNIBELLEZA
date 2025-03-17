from inventario import registrar_venta, ver_historial_ventas, inventario
from _usuarios import registrar_usuario, usuarios
from menu import mostrar_menu
from datetime import datetime

def main():
    while True:
        mostrar_menu()
        opcion = input("\n👉 Seleccione una opción: ")
        if opcion == "1":
            # Agregar producto (esto lo puedes añadir después)
            pass
        elif opcion == "2":
            # Ver inventario (esto lo puedes añadir después)
            pass
        elif opcion == "7":
            registrar_usuario()
        elif opcion == "8":
            registrar_venta()
        elif opcion == "9":
            ver_historial_ventas()
        elif opcion == "10":
            print("👋 Saliendo del sistema...¡Gracias por visitarnos! 💖")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
