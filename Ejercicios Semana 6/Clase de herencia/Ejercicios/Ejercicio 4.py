class Reserva:
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha):
        self.nombre_del_pasajero = nombre_del_pasajero
        self.numero_de_vuelo = numero_de_vuelo
        self.fecha = fecha

    def mostrar_detalle(self):
        print("Detalles de su Reserva:")
        print(f"Nombre del pasajero: {self.nombre_del_pasajero}")
        print(f"Numero de vuelo: {self.numero_de_vuelo}")
        print(f"Fecha: {self.fecha}")


class ReservaEconomica(Reserva):
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha, colacion):
        super().__init__(nombre_del_pasajero, numero_de_vuelo, fecha)
        self.colacion = colacion

    def mostrar_detalle(self):
        super().mostrar_detalle()
        print(f"Colacion: {self.colacion}")


class ReservaBusiness(Reserva):
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha, comida):
        super().__init__(nombre_del_pasajero, numero_de_vuelo, fecha)
        self.comida = comida

    def mostrar_detalle(self):
        super().mostrar_detalle()
        input(f"Comida: {self.comida}")


class ReservaPrimeraClase(Reserva):
    def __init__(self, nombre_del_pasajero, numero_de_vuelo, fecha, sala_vip):
        super().__init__(nombre_del_pasajero, numero_de_vuelo, fecha)
        self.sala_vip = sala_vip

    def mostrar_detalle(self):
        super().mostrar_detalle()
        input(f"Sala de VIP: {self.sala_vip}")


nombre_del_pasajero = input("Ingrese su Nombre: ")
numero_de_vuelo = input("Ingrese el numero de vuelo: ")
fecha = input("Ingrese la fecha del vuelo: ")
tipo_de_reserva = input(
    "Ingrese el tipo de vuelo que desea reservar (Economica, Business o Primera Clase): "
)
if tipo_de_reserva == "Economica":
    colacion = input("¿Deseas agregar una colacion? (SI/NO): ")
    reserva = ReservaEconomica(nombre_del_pasajero, numero_de_vuelo, fecha, colacion)

elif tipo_de_reserva == "Business":
    comida = input("¿Desea agregar comida? (SI/NO): ")
    reserva = ReservaBusiness(nombre_del_pasajero, numero_de_vuelo, fecha, comida)

elif tipo_de_reserva == "Primera Clase":
    sala_vip = input("¿Tiene acceso a la sala VIP? (SI/NO): ")
    reserva = ReservaPrimeraClase(nombre_del_pasajero, numero_de_vuelo, fecha, sala_vip)

else:
    print("Se ha producido un error")

print()
if hasattr(reserva, "mostrar_detalle"):
    reserva.mostrar_detalle()
