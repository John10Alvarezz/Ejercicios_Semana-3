class rectangulo:
    def __init__(self, longitud, ancho):
        self.longitud = longitud
        self.ancho = ancho

    def calcularArea(self):
        return self.longitud * self.ancho

    def calcularPerimetro(self):
        return self.ancho * 2 + self.longitud * 2

    def cambiarLongitud(self, nueva_longitud):
        self.longitud = nueva_longitud

    def cambiarAncho(self, nuevo_ancho):
        self.ancho = nuevo_ancho


valor_longitud = 7
valor_ancho = 5
mi_rectangulo = rectangulo(valor_longitud, valor_ancho)

area = mi_rectangulo.calcularArea()
print("El área del rectangulo es: ", area)

perimetro = mi_rectangulo.calcularPerimetro()
print("El perímetro del rectangulo es: ", perimetro)
