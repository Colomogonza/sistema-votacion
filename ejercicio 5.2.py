estudiantes = [("Juan", 70.), ("Pablo", 60), ("Manuel", 90), ("Pedro", 55)]

total_notas= 0
for nombre, notas in (estudiantes):
    total_notas += notas
promedio = total_notas / len(estudiantes)
print(f"el promedio de notas es {promedio}")

nombre_mas_alto, nota_mas_alta = estudiantes[0]
nombre_mas_bajo, nota_mas_baja = estudiantes[0]
for nombre, nota in estudiantes:
    total_notas += nota
    if nota > nota_mas_alta:
        nota_mas_alta = nota
        nombre_mas_alto = nombre
    if nota < nota_mas_baja:
        nota_mas_baja = nota
        nombre_mas_bajo = nombre
print("Nota más alta:", nota_mas_alta, "obtenida por", nombre_mas_alto)
print("Nota más baja:", nota_mas_baja, "obtenida por", nombre_mas_bajo)

for nombre, notas in estudiantes:
    if notas > 60:
        print(f"{nombre} aprobo con {notas}")
    else:
        print(f"{nombre} perdio con {notas}")

