class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def sonido(self):
        print(f"Nombre del animal: {self.nombre}")
        print(f"Edad: {self.edad}")


class Perro(Animal):
    def __init__(self, nombre, edad, sonido_perro):
        super().__init__(nombre, edad)
        self.sonido_perro = sonido_perro

    def sonido(self):
        super().sonido()
        print(f"Sonido que emite: {self.sonido_perro}\n")


class Gato(Animal):
    def __init__(self, nombre, edad, sonido_gato):
        super().__init__(nombre, edad)
        self.sonido_gato = sonido_gato

    def sonido(self):
        super().sonido()
        print(f"Sonido que emite: {self.sonido_gato}\n")


class Pajaro(Animal):
    def __init__(self, nombre, edad, sonido_pajaro):
        super().__init__(nombre, edad)
        self.sonido_pajaro = sonido_pajaro

    def sonido(self):
        super().sonido()
        print(f"Sonido que emite: {self.sonido_pajaro}")


perro = Perro("perro", 5, "Guau-Guau")
gato = Gato("gato", 3, "Miau-Miau")
pajaro = Pajaro("pajaro", 2, "Pio-pio")

animal = [perro, gato, pajaro]
for i in animal:
    i.sonido()
