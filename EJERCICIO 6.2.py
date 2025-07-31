frase = input("Escribe una frase: ").lower()
palabras = frase.split()

conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

print("Palabras usadas:", len(palabras))
print("Repetición de palabras:")
for palabra, cantidad in conteo.items():
    print(f"{palabra}: {cantidad}")
