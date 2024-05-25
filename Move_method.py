class Empleado:
    def __init__(self, nombre, salario, departamento):
        self.nombre = nombre
        self.salario = salario
        self.departamento = departamento

    def calcular_presupuesto_departamento(self):
        return sum(empleado.salario for empleado in self.departamento.empleados)

class Departamento:
    def __init__(self, nombre):
        self.nombre = nombre
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)
        empleado.departamento = self

# Crear departamento y empleados
dept = Departamento("Desarrollo")
emp1 = Empleado("Alice", 50000, dept)
emp2 = Empleado("Bob", 60000, dept)
dept.agregar_empleado(emp1)
dept.agregar_empleado(emp2)

# Calcular presupuesto del departamento
print(emp1.calcular_presupuesto_departamento())