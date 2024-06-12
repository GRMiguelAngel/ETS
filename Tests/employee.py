class Empleado:
    def __init__(self, nombre, apellidos, salario):
        self.nombre=nombre
        self.apellidos=apellidos
        self.salario=salario
    def aumentar_salario(self):
        self.salario += 1000