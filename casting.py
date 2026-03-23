def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    pass

    precio = int(input("Precio:"))
    descuento = float(input("Descuento:"))
    cantidad = int(input("Cantidad:"))
    precio_total = precio - descuento
    
    print(f"Precio: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio con descuento: {precio - descuento}")
    print(f"Total: {precio_total * cantidad}")
casting()