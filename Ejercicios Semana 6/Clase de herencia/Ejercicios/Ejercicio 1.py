class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    # metodo
    def mostrar_detalle(self):
        print(f"nombre: {self.nombre}")
        print(f"precio: {self.precio}")
        print(f"categoria: {self.categoria}")


class Electronico(Producto):
    def __init__(self, nombre, precio, categoria, unidades):
        super().__init__(nombre, precio, categoria)
        self.unidades = unidades

    def mostrar_detalle(self):
        print("Producto Electronico:")
        super().mostrar_detalle()
        print(f"Unidades disponibles: {self.unidades}\n")


class Alimeticio(Producto):
    def __init__(self, nombre, precio, categoria, paquetes):
        super().__init__(nombre, precio, categoria)
        self.paquetes = paquetes

    def mostrar_detalle(self):
        print("Producto Alimenticio:")
        super().mostrar_detalle()
        print(f"N de paquetes: {self.paquetes}\n")


class Vestimenta(Producto):
    def __init__(self, nombre, precio, categoria, color):
        super().__init__(nombre, precio, categoria)
        self.color = color

    def mostrar_detalle(self):
        print("Producto de vestir:")
        super().mostrar_detalle()
        print(f"Color: {self.color}")


# Instancias de cada objeto
electronico = Electronico("Lavadora", "$120.000", "Linea Blanca", 5)
print()
alimenticio = Alimeticio("Arroz", "$7.000", "Alimentos", 2)
vestimenta = Vestimenta("Pantalones", "$12.000", "Ropa", "Rojo")

productos = [electronico, alimenticio, vestimenta]
for i in productos:
    i.mostrar_detalle()
