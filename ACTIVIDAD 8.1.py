def evaluar_estudiantes():
    estudiantes = []

    print("Ingrese datos de al menos 3 estudiantes.")
    while len(estudiantes) < 3:
        nombre = input("Nombre del estudiante: ")
        notas = input("Ingrese las notas separadas por comas (ej. 70,80,90): ")
        lista_notas = [float(n) for n in notas.split(",")]
        estudiantes.append((nombre, lista_notas))

    def promedio(notas):
        return sum(notas) / len(notas)

    def resultado(prom):
        return "Aprobado" if prom >= 61 else "Reprobado"

    print("\nResumen de Evaluación:")
    for nombre, notas in estudiantes:
        prom = promedio(notas)
        estado = resultado(prom)
        print(f"{nombre} | Promedio: {prom:.2f} | Resultado: {estado}")
        
evaluar_estudiantes()
