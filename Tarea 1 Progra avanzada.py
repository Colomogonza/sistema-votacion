letra = input("Ingresa una letra (un solo carácter): ")

if len(letra) == 1 and letra.isalpha():
    if letra in ['A', 'E', 'I', 'O', 'U']:
        print("Vocal mayúscula")
    elif letra in ['a', 'e', 'i', 'o', 'u']:
        print("Vocal minúscula")
    else:
        print("Consonante")
else:
    # Si no es una letra válida
    print("No es una letra válida")
