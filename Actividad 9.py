biblioteca = []

def agregar_libros(*titulos):
    for titulo in titulos:
        libro = {
            "titulo": titulo,
            "autor": "Sin asignar",
            "genero": "Sin asignar",
            "anio": None
        }
        biblioteca.append(libro)
    print(f"{len(titulos)} libro(s) agregado(s) a la biblioteca.")

def asignar_detalles(titulo, autor, genero, anio):
    for libro in biblioteca:
        if libro["titulo"].lower() == titulo.lower():
            libro["autor"] = autor
            libro["genero"] = genero
            libro["anio"] = anio
            print(f"Detalles asignados a '{titulo}'.")
            return
    print(f"Libro '{titulo}' no encontrado.")

def mostrar_biblioteca():
    if not biblioteca:
        print("La biblioteca está vacía.")
        return

    print("\nCatálogo de libros:")
    for libro in biblioteca:
        print(f"Título: {libro['titulo']}")
        print(f"Autor: {libro['autor']}")
        print(f"Género: {libro['genero']}")
        print(f"Año: {libro['anio']}")
        print("-" * 30)

def buscar_libros(**filtros):
    resultados = biblioteca

    if "genero" in filtros:
        resultados = [l for l in resultados if l["genero"].lower() == filtros["genero"].lower()]
    if "autor" in filtros:
        resultados = [l for l in resultados if l["autor"].lower() == filtros["autor"].lower()]
    if "año_max" in filtros:
        resultados = [l for l in resultados if l["anio"] is not None and l["anio"] <= filtros["año_max"]]

    if resultados:
        print("\nLibros encontrados:")
        for libro in resultados:
            print(f"{libro['titulo']} | {libro['autor']} | {libro['genero']} | {libro['anio']}")
    else:
        print("No se encontraron libros con esos filtros.")

        
agregar_libros("Cien años de soledad", "El principito", "Don Quijote")

asignar_detalles("El principito", "Antoine de Saint-Exupéry", "Ficción", 1943)
asignar_detalles("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", 1967)

mostrar_biblioteca()

buscar_libros(genero="Ficción", año_max=2000)


