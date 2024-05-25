def obtener_descuento(precio):
    return precio * 0.1

def calcular_precio_final(precio):
    discount = obtener_descuento(precio)
    return precio - discount

# Llamada a la función con algunos valores
precio_final = calcular_precio_final(100)
print("El precio final es: ", precio_final)
