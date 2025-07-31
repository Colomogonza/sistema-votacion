datos = {}

nombre = input("Nombre: ").strip()
correo = input("Correo: ").strip()
carnet = input("Carnet: ").strip()

if nombre == "":
    print("Nombre vacío no permitido.")
elif "@" not in correo or "." not in correo:
    print("Correo inválido.")
elif not (carnet.isdigit() and len(carnet) == 7):
    print("Carnet debe tener 7 dígitos numéricos.")
else:
    datos = {"nombre": nombre, "correo": correo, "carnet": carnet}
    print("Datos guardados:", datos)
