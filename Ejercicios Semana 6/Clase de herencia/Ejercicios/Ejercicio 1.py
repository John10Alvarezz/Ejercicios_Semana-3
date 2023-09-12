class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_detalle(self):
        print(f"nombre: {self.nombre}")
        print(f"precio: {self.precio}")
        print(f"categoria: {self.categoria}")


class Electronico(Producto):
    def __init__(self, nombre, precio, categoria, unidades):
        super().__init__(nombre, precio, categoria)
        self.unidades = unidades

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Unidades disponibles: {self.unidades}")


class Alimeticio(Producto):
    def __init__(self, nombre, precio, categoria, paquetes):
        super().__init__(nombre, precio, categoria)
        self.paquetes = paquetes

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"N de paquetes: {self.paquetes}")


class Vestimenta(Producto):
    def __init__(self, nombre, precio, categoria, color):
        super().__init__(nombre, precio, categoria)
        self.color = color

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Color: {self.color}")


electronico = Electronico("Lavadora", "$120.000", "Linea Blanca", 5)
electronico.mostrar_detalle()
print()
alimenticio = Alimeticio("Arroz", "$7.000", "Alimentos", 2)
alimenticio.mostrar_detalle()
print()
vestimenta = Vestimenta("Pantalones", "$12.000", "Ropa", "Rojo")
vestimenta.mostrar_detalle()
