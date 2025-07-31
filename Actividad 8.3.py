def facturar_productos():
    productos = []
    print("Ingrese los productos y sus precios (escriba 'fin' para terminar):")

    while True:
        nombre = input("Nombre del producto: ")
        if nombre.lower() == 'fin':
            break
        try:
            precio = float(input("Precio del producto: "))
            productos.append({"nombre": nombre, "precio": precio})
        except ValueError:
            print("Precio inválido. Intente de nuevo.")

    def calcular_total(lista_precios):
        return sum(item["precio"] for item in lista_precios)

    def aplicar_descuento(total):
        if total > 300:
            return total * 0.90 
        return total

    total_bruto = calcular_total(productos)
    total_final = aplicar_descuento(total_bruto)

    print("\nResumen de factura:")
    for item in productos:
        print(f"{item['nombre']}: Q{item['precio']:.2f}")
    print(f"Total sin descuento: Q{total_bruto:.2f}")
    if total_bruto != total_final:
        print("Descuento aplicado: 10%")
    print(f"Total final: Q{total_final:.2f}")

facturar_productos()
