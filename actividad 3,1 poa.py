grupos = {}  

while True:
    grupo = input("Grupo(Escribe salir para terminar): ")
    if grupo.lower() == "salir":
        break

    estudiantes = []
    while True:
        estudiante = input("Nombre del estudiante (escribe fin para terminar): ")
        if estudiante.lower() == "fin":
            break
        estudiantes.append(estudiante)
    
    grupos[grupo] = estudiantes

print("Resumen de grupos y estudiantes:")
for grupo, lista in grupos.items():
    print(f"{grupo}: {', '.join(lista)}")

