def menu_personalizado():
    print("Bienvenido al generador de menús.")

    def seleccionar_entrada():
        print("Entradas disponibles:")
        opciones = ["Ensalada César", "Sopa de verduras", "Bruschetta"]
        for i, op in enumerate(opciones, 1):
            print(f"{i}. {op}")
        eleccion = int(input("Seleccione una entrada (1-3): "))
        return opciones[eleccion - 1]

    def seleccionar_plato_fuerte():
        print("Platos fuertes disponibles:")
        opciones = ["Pollo al horno", "Pasta Alfredo", "Carne asada"]
        for i, op in enumerate(opciones, 1):
            print(f"{i}. {op}")
        eleccion = int(input("Seleccione un plato fuerte (1-3): "))
        return opciones[eleccion - 1]

    def seleccionar_postre():
        print("Postres disponibles:")
        opciones = ["Flan", "Helado", "Tarta de manzana"]
        for i, op in enumerate(opciones, 1):
            print(f"{i}. {op}")
        eleccion = int(input("Seleccione un postre (1-3): "))
        return opciones[eleccion - 1]

    entrada = seleccionar_entrada()
    plato = seleccionar_plato_fuerte()
    postre = seleccionar_postre()

    print("\nMenú personalizado generado:")
    print(f"Entrada: {entrada}")
    print(f"Plato fuerte: {plato}")
    print(f"Postre: {postre}")

menu_personalizado()
