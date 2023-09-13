class Empleado:
    def __init__(self, nombre, edad, salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def describir_rol(self):
        print(
            f"Mi nombre es {self.nombre}, tengo {self.edad} años, mi sueldo es {self.salario}"
        )


class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento

    def describir_rol(self):
        super().describir_rol()
        print(f"y trabajo en el depattamento de {self.departamento}")


class Ingeniero(Empleado):
    def __init__(self, nombre, edad, salario, especialidad):
        super().__init__(nombre, edad, salario)
        self.especialidad = especialidad

    def describir_rol(self):
        super().describir_rol()
        print(f"y me especializo en el area de {self.especialidad}")


class Asistente(Empleado):
    def __init__(self, nombre, edad, salario, tarea):
        super().__init__(nombre, edad, salario)
        self.tarea = tarea

    def describir_rol(self):
        super().describir_rol()
        print(f"y mi labor es {self.tarea}")


gerente = Gerente("Patricio", 40, "$1.100.000", "Ventas")
gerente.describir_rol()
print()
ingeniero = Ingeniero("Neymar", 29, "$1.500.000", "Informatica")
ingeniero.describir_rol()
print()
asistente = Asistente("Fabricio", 24, "$600.000", "Agendar visitas")
asistente.describir_rol()
