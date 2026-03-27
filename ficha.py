def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)


    nombre = input("Ingrese nombre: ")
    email = input("Ingrese email: ")
    nota1 = input("Ingrese nota 1: ")
    nota2 = input("Ingrese nota 2: ")
    nota3 = input("Ingrese nota 3: ")

    nombre = nombre.strip().title()
    email = email.lower()



    print("========================\n    FICHA DEL ALUMNO\n========================")
    print("Nombre: "+ nombre)
    print("Email: "+ email)
    print(f"Caracteres en nombre: {len(nombre.strip())}")

    espacio = nombre.find(" ")
    print(f"Iniciales: {nombre[0]}{nombre[(espacio+1)]}")

    print(f"Usuario: {nombre.lower()[(espacio+1):]}.{nombre.lower()[0:(espacio)]}")

    validez = "@" in email
    print(f"Email valido: {validez}")

    arroba = email.find("@")
    print(f"Dominio: {email[(arroba+1):]}")

    guion = nombre.replace(" ","_")
    print(f"Nombre para archivo: {guion}")


    print(f"Cantidad de a: {nombre.count("a")}")


    print(f"Codigo secreto: {nombre.upper()[::-1]}")

    print("Nota 1: " + nota1)
    print("Nota 2: " + nota2)
    print("Nota 3: " + nota3)
    nota1, nota2, nota3 = int(nota1), int(nota2), int(nota3)
    suma = nota1 + nota2 + nota3
    print("Suma: "+ str(suma))
    promedio = suma / 3
    print("Promedio: "+ str(promedio))
    promedioEnt = suma // 3
    print("Promedio entero: "+ str(promedioEnt))

    print("="*24)


