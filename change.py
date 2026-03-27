def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.
    """

    print("Ingresar gasto:")
    gasto = input()
    print(float(gasto))

    print("Dinero recibido")
    dinero_recibido = input()
    print(dinero_recibido)

    vuelto = float(dinero_recibido) - float(gasto)
    vuelto_pesos = int(vuelto)
    vuelto_centavos = int(round((vuelto - vuelto_pesos) * 100))

    print()
    print("Vuelto")
    print()

    print(f"Pesos:")
    print(vuelto_pesos)
    print(f"Centavos:")
    print(vuelto_centavos)

