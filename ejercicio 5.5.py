A=["Lucas","Mateo","Alexis","Juan"]
B=["Lucas","Herbert","Angel","Mateo","Oscar"]
x=0
lista=[]
for nombre in A:
    if nombre in A and nombre in B:
        print("Nombres de ambos cursos")
        print(nombre)
    if nombre in A and nombre not in B:
        print("Nombre que solo aparecen en la lista A")
        print(nombre)

for i in A:
    for e in B:
        if i not in lista:
            lista.append(i)
            x+=1
        elif e not in lista:
            lista.append(e)
            x+=1


print(f"Hay {x} nombres que no se repiten")
print("Nombres filtrados")
print(lista)