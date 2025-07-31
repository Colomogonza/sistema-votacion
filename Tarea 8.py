def biblioteca():
    libros = []

    def agregar_libro():
        titulo = input("Título del libro: ")
        autor = input("Autor: ")
        try:
            anio = int(input("Año de publicación: "))
            libros.append({"titulo": titulo, "autor": autor, "anio": anio})
            print("Libro agregado correctamente.")
        except ValueError:
            print("Año inválido. Intenta de nuevo.")

    def buscar_libros():
        print("Buscar por:")
        print("1. Autor")
        print("2. Año")
        opcion = input("Opción: ")
        if opcion == "1":
            autor = input("Nombre del autor: ")
            encontrados = [libro for libro in libros if libro["autor"].lower() == autor.lower()]
        elif opcion == "2":
            try:
                anio = int(input("Año de publicación: "))
                encontrados = [libro for libro in libros if libro["anio"] == anio]
            except ValueError:
                print("Año inválido.")
                return
        else:
            print("Opción no válida.")
            return

        if encontrados:
            print("Libros encontrados:")
            for libro in encontrados:
                print(f"{libro['titulo']} | {libro['autor']} | {libro['anio']}")
        else:
            print("No se encontraron libros con ese criterio.")

    def mostrar_libros():
        if not libros:
            print("No hay libros registrados.")
        else:
            print("Listado de libros:")
            for libro in libros:
                print(f"{libro['titulo']} | {libro['autor']} | {libro['anio']}")

    while True:
        print("\n1. Agregar libro")
        print("2. Buscar libros")
        print("3. Mostrar todos los libros")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            buscar_libros()
        elif opcion == "3":
            mostrar_libros()
        elif opcion == "4":
            print("Saliendo del sistema de biblioteca.")
            break
        else:
            print("Opción inválida.")

biblioteca()
