# Clase padre
class vehiculos:
    def __init__(self, color, numero_de_ruedas):
        self.color = color
        self.numero_de_ruedas = numero_de_ruedas

    def mostrar_informacion(self):
        print(f"color: {self.color}")
        print(f"N de ruedas: {self.numero_de_ruedas}")


class autos(vehiculos):
    def __init__(self, color, numero_de_ruedas, motor):
        super().__init__(color, numero_de_ruedas)
        self.motor = motor

    def mostrar_informacion(self):
        super().mostrar_informacion()
        print(f"motor: {self.motor}")


auto = autos("Rojo", 4, 3200)
auto.mostrar_informacion()
