lista=[]
while True:
    print("Menu")
    print("1.Ver la lista de tareas")
    print("2.Marcar una como completada")
    print("3.Agregar una nueva")
    print("4.Salir")
    x=int(input("Seleccione una opcion:"))
    if x==1:
        lista
        if len(lista)==0:
            print("La lista de tareas esta vacia")
        else:
            print("Lista de tareas")
            print(lista)
    elif x==2:
        if len(lista)==0:
            print("No hay elementos en la lista")
        else:
            for i,tarea in enumerate(lista):
                print(f"{i}: {tarea}")
            f=int(input("Ingrese el numero de tarea que ya completo: "))
            lista.pop(f)
            print("Tarea eliminada correctamente")
            
    elif x==3:
        y=input("Ingrese su nueva tarea: ")
        lista.append(y)
    elif x==4:
        break