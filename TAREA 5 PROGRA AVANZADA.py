reservaciones = []

def registrar_reservacion():
    nombre = input("Nombre del cliente: ")
    numero = input("Número de habitación: ")
    tipo = input("Tipo de habitación (individual, doble, suite): ")
    dias = int(input("Días de estancia: "))
    precio = float(input("Precio total: "))
    reservacion = (nombre, numero, tipo, dias, precio)
    reservaciones.append(reservacion)
    print("✔ Reservación registrada exitosamente.\n")

def mostrar_reservaciones():
    if not reservaciones:
        print("No hay reservaciones registradas.\n")
        return
    print("Reservaciones registradas:")
    for r in reservaciones:
        print(f"Cliente: {r[0]}, Habitación: {r[1]}, Tipo: {r[2]}, Días: {r[3]}, Precio: Q{r[4]:.2f}")
    print()

def buscar_por_nombre():
    nombre_buscado = input("Ingrese el nombre del cliente: ")
    encontrados = [r for r in reservaciones if r[0].lower() == nombre_buscado.lower()]
    if encontrados:
        print("Reservaciones encontradas:")
        for r in encontrados:
            print(f"Cliente: {r[0]}, Habitación: {r[1]}, Tipo: {r[2]}, Días: {r[3]}, Precio: Q{r[4]:.2f}")
    else:
        print("No se encontraron reservaciones con ese nombre.")
    print()

def mostrar_estadisticas():
    total_reservas = len(reservaciones)
    ingreso_total = sum(r[4] for r in reservaciones)
    tipos = {}
    for r in reservaciones:
        tipo = r[2].lower()
        tipos[tipo] = tipos.get(tipo, 0) + 1
    print(f"Total de reservaciones: {total_reservas}")
    print(f"Ingreso total acumulado: Q{ingreso_total:.2f}")
    print("Habitaciones ocupadas por tipo:")
    for tipo, cantidad in tipos.items():
        print(f"  {tipo.capitalize()}: {cantidad}")
    print()

while True:
    print("----- SISTEMA DE RESERVACIONES -----")
    print("1. Registrar reservación")
    print("2. Mostrar todas las reservaciones")
    print("3. Buscar reservación por nombre")
    print("4. Mostrar estadísticas")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_reservacion()
    elif opcion == "2":
        mostrar_reservaciones()
    elif opcion == "3":
        buscar_por_nombre()
    elif opcion == "4":
        mostrar_estadisticas()
    elif opcion == "5":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida.\n")
