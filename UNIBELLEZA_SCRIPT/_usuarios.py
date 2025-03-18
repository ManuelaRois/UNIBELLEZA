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
