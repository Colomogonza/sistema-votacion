nombre = input("Ingrese un nombre: ")
try:
    nota = float(input("Ingrese una nota de 0 a 100: "))
    if nota < 0 or nota > 100:
        print("Error: La nota debe estar entre 0 y 100.")
        exit()
except ValueError:
    print("Error: Debe ingresar un número válido para la nota.")
    exit()

try:
    asistencia = float(input("Ingrese el porcentaje de asistencia de 0 a 100: "))
    if asistencia < 0 or asistencia > 100:
        print("Error: El porcentaje de asistencia debe estar entre 0 y 100.")
        exit()
except ValueError:
    print("Error: Debe ingresar un número válido para la asistencia.")
    exit()


if nota >= 70 and asistencia >= 80:
    estado = "Aprobado"
elif nota >= 70 and asistencia < 80:
    estado = "Reprobado por asistencia"
elif nota < 70 and asistencia >= 80:
    estado = "Reprobado por nota"
else:
    estado = "Reprobado por ambas razones"

if nota >= 90:
    calificación = "A"
elif nota >= 80:
    calificación = "B"
elif nota >= 70:
    calificación = "C"
elif nota >= 60:
    calificación = "D"
else:
    calificación = "F" 

print("Resultado")
print(f"- {estado}")
print(f"- calificación: {calificación}")
