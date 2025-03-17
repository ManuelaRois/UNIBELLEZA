from datetime import datetime

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
    }
}

def ver_inventario(inventario, usuarios):
    """Muestra el inventario con fechas de vencimiento y aplica descuento si el usuario está registrado."""
    hoy = datetime.today().date()
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
                fecha_venc = datetime.strptime(vencimiento, "%Y-%m-%d").date()
                if fecha_venc < hoy:
                    continue  # Omitir productos vencidos
            print("{:<25} {:<10} {:>10.2f} {:>15}".format(producto, detalles['Cantidad'], precio_con_descuento, vencimiento))
    
    if descuento > 0:
        print("\n¡Se aplicó un descuento del 10% por estar registrado!🩷")
    print("\nNota: Los productos vencidos no se muestran en el inventario.")