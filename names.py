def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    nombre_apellido = f'{nombre} {apellido}'

    print(nombre_apellido.lower())
    print(nombre_apellido.title())
    print(nombre_apellido.upper())
    print(f"\t{nombre_apellido.lower()}")



