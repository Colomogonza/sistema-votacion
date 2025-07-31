usuarios = {}

while True:
    nombre = input("Nombre: ")
    correo = input("Correo: ").strip().lower()

    if correo in usuarios:
        print("Correo ya registrado.")
    else:
        usuarios[correo] = nombre
        print("Usuario registrado.")

    continuar = input("¿Registrar otro? (s/n): ")
    if continuar.lower() != "s":
        break

print("\nUsuarios registrados:")
for c, n in usuarios.items():
    print(f"{n} - {c}")
