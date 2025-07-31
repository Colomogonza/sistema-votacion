registro = {}

for i in range(3):
    nombre = input("Nombre: ").strip().title()
    carnet = input("Carnet: ").strip()
    correo = input("Correo: ").strip().lower()

    if "@" not in correo or "." not in correo:
        print("Correo, invalido. Intenge de nuevo ")
        continue

    registro[carnet] = {
        "nombre": nombre,
        "correo": correo    
                }
print("REGISTRO NOTAS")
for carnet, datos in registro.items():
    print(f"{carnet} + {datos}")
