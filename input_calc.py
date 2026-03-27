def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """

    base = input()

    print("Base: " + str(base))

    altura = input()

    print("Altura: " + str(altura))


    area = int(base) * int(altura)
    print("Area: " + str(area))

    perimetro = 2*(int(base) + int(altura))

    print("Perimetro: " + str(perimetro))

    pass
