def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"

    print(f"Palabra: {palabra}")
    longitud = len(palabra)
    print(f"Longitud: {longitud}")
    print(f"Primera letra: {palabra[0]}")
    print(f"Ultima letra: {palabra[-1]}")
    palabraRepe = palabra*3
    print(f"Repetida: {palabraRepe}")
    print(f"Decorada: ***{palabra}***")

