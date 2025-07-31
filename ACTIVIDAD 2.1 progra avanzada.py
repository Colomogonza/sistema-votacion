print("PERSONA 1")
nombre1 = input("Ingrese un nombre: ")
edad1 = int(input("Ingrese una edad: "))
color1 = input("Ingrese un color: ").lower()
pregunta1 = input("¿Le gusta programar? (Si/No): ").lower()

print("PERSONA 2")
nombre2 = input("Ingrese otro nombre: ")
edad2 = int(input("Ingrese otra edad: "))
color2 = input("Ingrese otro color: ")
pregunta2 = input("¿Le gusta programar? (Si/No): ").lower()

puntos = 0

if abs(edad1 - edad2) <= 5:
    puntos += 1
if color1 == color2:
    puntos += 1
if pregunta1 == "si" and pregunta2 == "si":
    puntos += 1

print("Resultados")
print(f"- {nombre1} y {nombre2}")
print(f"- Compatibilidad: {puntos}/3")

if puntos == 3:
    print("Compatibilidad total")
elif puntos == 2:
    print("Compatibles")
elif puntos == 1:
    print("Compatibilidad baja")
else:
    print("Nada compatibles")