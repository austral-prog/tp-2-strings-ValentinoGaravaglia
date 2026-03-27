from gettext import find


def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
    Linea 2
    Linea 3"""

    print("Strip: " + nombre.strip())
    print("Lstrip: " + nombre.lstrip())
    print("Rstrip: " + nombre.rstrip())


    print("Upper: " + frase.upper())
    print("Lower: " + frase.lower())
    print("Title: " + frase.title())

    Find = frase.find("gran")

    print(f"Find: {Find}")

    Cambio = frase.replace("programacion", "desarrollo")
    print(f"Replace: {Cambio}")

    contar = frase.count("a")
    print(f"Count: {contar}")

    PinF = "Python" in frase
    print(f"Contiene Python: {PinF}")

    JinF = "Java" in frase
    print(f"Contiene Java: {JinF}")

    slicing = frase[0:6]
    print(f"Slice: {slicing}")
    print(f"Paso: {slicing[::2]}")


    print(f"Reverso: {slicing[::-1]}")


    print(f"Formato: {nombre.strip()} sabe {slicing}")


    print(f"{multilinea.replace("    ", "")}")






