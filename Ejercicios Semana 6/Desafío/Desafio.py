class Persona:
    def __init__(self, nombre, apellido, fecha_de_nacimiento):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_de_nacimiento = fecha_de_nacimiento

    def presentarse(self):
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellido}")
        print(f"Fecha de nacimiento: {self.fecha_de_nacimiento}")


class Estudiante(Persona):
    def __init__(
        self, nombre, apellido, fecha_de_nacimiento, matricula, carrera, semestre
    ):
        super().__init__(nombre, apellido, fecha_de_nacimiento)
        self.matricula = matricula
        self.carrera = carrera
        self.semestre = semestre

    def estudiar(self):
        print(f"")

    def presentarse(self):
        return super().presentarse()


class Profesor(Persona):
    def __init__(
        self, nombre, apellido, fecha_de_nacimiento, numero_empleado, departamento
    ):
        super().__init__(nombre, apellido, fecha_de_nacimiento)
        self.numero_empleado = numero_empleado
        self.departamento = departamento

    def enseñar(self):
        print(f"")

    def presentarse(self):
        return super().presentarse()


class Asignatura:
    def __init__(self, nombre, codigo, creditos):
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos

    def mostrar_información(self):
        print(f"Nombre de Asignatura: {self.nombre}")
        print(f"Codigo: {self.codigo}")
        print(f"Creditos: {self.creditos}")

class Grupo:
    def __init__(self):
