class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def obtener_nota(self):
        return self.nota
def calcular_promedio(estudiantes):
    if not estudiantes:
        return 0

    promedio = sum(estudiante.obtener_nota() for estudiante in estudiantes) / len(estudiantes)
    return promedio
estudiantes = [
    Estudiante("Juan", 85),
    Estudiante("Ana", 90),
    Estudiante("Luis", 78)
]
promedio = calcular_promedio(estudiantes)
print("El promedio de notas es:", promedio)