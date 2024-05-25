class Estudiante:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def obtener_nota(self):
        return self.nota

def calcular_promedio(estudiantes):
    total_notas = 0
    numero_estudiantes = 0

    for estudiante in estudiantes:
        nota = estudiante.obtener_nota()
        total_notas += nota
        numero_estudiantes += 1

    if numero_estudiantes == 0:
        return 0

    promedio = total_notas / numero_estudiantes
    return promedio

estudiantes = [
    Estudiante("Juan", 85),
    Estudiante("Ana", 90),
    Estudiante("Luis", 78)
]

promedio = calcular_promedio(estudiantes)
print("El promedio de notas es: ", promedio)
