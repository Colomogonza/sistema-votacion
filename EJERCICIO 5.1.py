productos = ["Jamon", "Cereal", "Queso", "Jugo", "Sopa"]
print("Lista inicial de productos:", productos)

nuevo_producto = input("¿Qué producto deseas agregar? ")
productos.append(nuevo_producto)
print(f"'{nuevo_producto}' ha sido agregado.")


eliminar_producto = input("¿Qué producto deseas eliminar? ")
if eliminar_producto in productos:
    productos.remove(eliminar_producto)
    print(f"'{eliminar_producto}' ha sido eliminado.")
else:
    print(f"'{eliminar_producto}' no está en la lista.")

productos.sort()

print("Lista final de productos ordenados:")
print(productos)
