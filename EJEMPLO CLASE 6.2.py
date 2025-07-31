usuarios = {
    "129431203": {"nombre": "Luis González", "Correo": "luis.correo.com"}

}
busqueda = input("Buscar por nombre o correo:   ").strip().lower()

encontrados = {}

for carnet, datos in usuarios.items():
    nombre = datos["nombre"].lower()
    correo = datos["correo"].lower()
    if busqueda in nombre or busqueda in correo:
        encontrados[carnet] = datos

if encontrados:
    print("Coincidencias encontradas: ")
    for c, info in encontrados.items():
        print(f"{c}: {info}")
    else:
        print("No se encontraron coincidencias")