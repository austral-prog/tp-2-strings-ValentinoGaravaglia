def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""

    precio = input()

    print("Precio: "+precio)

    descuento = input()

    print("Descuento: "+descuento)

    precio_descuento = int(precio) - float(descuento)

    print("Precio con descuento: " + str(precio_descuento))

    cantidad = input()

    total = precio_descuento * int(cantidad)

    print("Total: " + str(total))







