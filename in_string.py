def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """
    nombre = input()

    ca = "a" in nombre.lower()
    ce = "e" in nombre.lower()
    ci = "i" in nombre.lower()
    co = "o" in nombre.lower()
    cu = "u" in nombre.lower()

    print(f"Contiene a: {ca}")
    print(f"Contiene e: {ce}")
    print(f"Contiene i: {ci}")
    print(f"Contiene o: {co}")
    print(f"Contiene u: {cu}")





    pass
