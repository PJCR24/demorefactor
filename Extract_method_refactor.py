import math
def calcular_circulo_area(radio):
    return 3.14159 * (radio ** 2)

def calcular_rectangulo_area(largo, ancho):
    return largo * ancho

def calcular_areas(radio, largo, ancho):
    circulo_area = calcular_circulo_area(radio)
    print("El área del círculo es: ", circulo_area)

    rectangulo_area = calcular_rectangulo_area(largo, ancho)
    print("El área del rectángulo es: ", rectangulo_area)

# Llamada a la función con algunos valores
calcular_areas(5, 10, 20)