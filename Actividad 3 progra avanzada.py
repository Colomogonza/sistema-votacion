seguir = "sí"

while seguir.lower() == "sí":
    numero = int(input("Ingresa una tabla: "))

    i = 1
    while i <= 10:
        print(f"{numero} x {i} = {numero * i}")
        i += 1

    seguir = input("¿Quieres ver otra tabla? (sí/no): ")
