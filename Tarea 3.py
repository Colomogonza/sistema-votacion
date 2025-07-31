productos = {}  

while True:
    personas = input("Nombre del cliente (salir para terminar): ")
    if personas.lower() == "salir":
        break 
    else:
        while True:
            productos = input("Ingrese el producto (fin para salir): ")
            if productos.lower() == "fin":
                print("Factura final: ")
                break