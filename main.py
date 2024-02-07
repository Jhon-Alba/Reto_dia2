def validar_nombre(nombre):
    return 5 <= len(nombre) <= 50


def validar_apellidos(apellidos):
    return 5 <= len(apellidos) <= 50


def validar_telefono(telefono):
    return len(telefono) == 10 and telefono.isnumeric()


def validar_correo(correo):
    return 5 <= len(correo) <= 50 and "@" in correo and "." in correo


def ingresar_usuario(numero):
    print(f"\nRegistrando usuario: {numero}")
    nombre = input("Ingrese su nombre: ")
    while not validar_nombre(nombre):
        print("El nombre debe tener entre 5 y 50 caracteres.")
        nombre = input("Ingrese su nombre: ")

    apellidos = input("Ingrese sus apellidos: ")
    while not validar_apellidos(apellidos):
        print("Los apellidos deben tener entre 5 y 50 caracteres.")
        apellidos = input("Ingrese sus apellidos: ")

    telefono = input("Ingrese su número de teléfono(10 digitos): ")
    while not validar_telefono(telefono):
        print("El número de teléfono debe tener exactamente 10 dígitos.")
        telefono = input("Ingrese su número de teléfono: ")

    correo = input("Ingrese su correo electrónico: ")
    while not validar_correo(correo):
        print("El correo electrónico debe tener entre 5 y 50 caracteres y ser válido.")
        correo = input("Ingrese su correo electrónico: ")

    return nombre, apellidos, telefono, correo


def main():
    cantidad_usuarios = int(input("¿Cuántos usuarios desea registrar? \n"))
    usuarios = []

    for i in range(1, cantidad_usuarios + 1):
        nombre, apellidos, telefono, correo = ingresar_usuario(i)
        usuarios.append((nombre, apellidos, telefono, correo))

    print("\nUsuarios registrados:")
    for i, usuario in enumerate(usuarios, start=1):
        print(f"\nUsuario {i}")
        print(f"Bienvenido, {usuario[0]}, {usuario[1]}")
        print(f"En breve recibiras un correo a: {usuario[3]}")
        print(f"Usuario registrado, su ID es: {i}")


if __name__ == "__main__":
    main()
