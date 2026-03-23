def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    pass

    nombre = input("Nombre:")
    apellido = input("Apellido:")
    print((nombre + " " + apellido ).lower())
    print((nombre + " " + apellido).title())
    print((nombre + " " + apellido).upper())
    print(("\t" + nombre.lower() + " " + apellido.lower()))
