# Diccionario para almacenar usuarios
usuarios = {}

def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo electrónico: ")

    if correo in usuarios:
        print(f"⚠️ El correo '{correo}' ya está registrado.")
    else:
        usuarios[correo] = nombre
        print(f"✅ Usuario '{nombre}' registrado correctamente.")