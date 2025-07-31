def registro_pacientes():
    pacientes = []

    def agregar_paciente(nombre, edad, diagnostico):
        pacientes.append({
            "nombre": nombre,
            "edad": edad,
            "diagnostico": diagnostico
        })
        print(f"Paciente '{nombre}' registrado correctamente.")

    def buscar_paciente(nombre):
        for paciente in pacientes:
            if paciente["nombre"].lower() == nombre.lower():
                print(f"Nombre: {paciente['nombre']}")
                print(f"Edad: {paciente['edad']}")
                print(f"Diagnóstico: {paciente['diagnostico']}")
                return
        print(f"No se encontró al paciente '{nombre}'.")

    while True:
        print("\n1. Agregar paciente")
        print("2. Buscar paciente")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            edad = input("Edad: ")
            diagnostico = input("Diagnóstico: ")
            agregar_paciente(nombre, edad, diagnostico)

        elif opcion == "2":
            nombre = input("Ingrese el nombre del paciente a buscar: ")
            buscar_paciente(nombre)

        elif opcion == "3":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción inválida.")

registro_pacientes()
