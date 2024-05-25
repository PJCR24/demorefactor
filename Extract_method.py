import math
def calcular_areas(radio, largo, ancho):
    # Cálculo del área del círculo
    circle_area = 3.14159 * (radio ** 2)
    print("El área del círculo es: ", circle_area)

    # Cálculo del área del rectángulo
    rectangle_area = largo * ancho
    print("El área del rectángulo es: ", rectangle_area)

# Llamada a la función con algunos valores
calcular_areas(5, 10, 20)