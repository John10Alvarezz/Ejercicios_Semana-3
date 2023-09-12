import math #Importamos math para usar "pi"

class Circulo:
    def __init__(self, radio): 
        self.radio = radio
    
    def calcularArea(self):
        return math.pi * self.radio ** 2
    
    def calcularPerimetro(self):
        return 2 * math.pi * self.radio
    
    def cambiarRadio(self, nuevo_radio):
        self.radio = nuevo_radio

radio_inicial = 6
calcular_circulo = Circulo(radio_inicial)
# Mostramos el área del círculo
area = calcular_circulo.calcularArea()
print("EL área del círculo es: ", area)
# Mostramos el perímetro del círculo
perimetro = calcular_circulo.calcularPerimetro()
print("El perímetro del círculo es: ", perimetro)
