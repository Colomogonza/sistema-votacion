productos=["Jamon", "Cereal", "Queso", "Jugo", "Sopa"]
while True:
    print("Menu")
    print("1.Agregar un nuevo producto")
    print("2.Eliminar un producto")
    print("3.Mostrar los productos")
    print("4.Salir")
    x=int(input("Seleccione una opcion: "))
    if x==1:
        producto=str(input("Ingrese el nombre del producto: "))
        productos.append(producto)
        print("Producto agregado correctamente")
    if x==2:
        if len(productos)==0:
            print("La lista no tiene productos")
        else:
            for i,nombre in enumerate(productos):
                print(f"{i}: {nombre}")            
        eliminar=str(input("Seleccione el producto a eliminar de la lista: "))
        if eliminar in productos:
            productos.remove(eliminar)
            print("Producto eliminado correctamente")
        else:
            print("El producto no se encuentra dentro de la lista\nVuelva a intentarlo")
    if x==3:
        if len(productos)==0:
            print("La lista esta vacia")
        else:
            print("Lista de productos")
            productos.sort()
            for i,nombre in enumerate(productos):
                print(f"{i}: {nombre}")
    if x==4:
        break