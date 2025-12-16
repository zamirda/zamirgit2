# =========================
# Clase base Vehiculo
# =========================
class Vehiculo:
    def __init__(self, placa, marca, tarifa_base):
        self.placa = placa
        self.marca = marca
        self.tarifa_base = tarifa_base

    def calcular_tarifa_diaria(self):
        return self.tarifa_base


# =========================
# Clase Coche
# =========================
class Coche(Vehiculo):
    def __init__(self, placa, marca, tarifa_base, automatico):
        super().__init__(placa, marca, tarifa_base)
        self.automatico = automatico

    def calcular_tarifa_diaria(self):
        if self.automatico:
            return self.tarifa_base + 20
        return self.tarifa_base


# =========================
# Clase Camion
# =========================
class Camion(Vehiculo):
    def __init__(self, placa, marca, tarifa_base, capacidad_carga):
        super().__init__(placa, marca, tarifa_base)
        self.capacidad_carga = capacidad_carga

    def calcular_tarifa_diaria(self):
        return self.tarifa_base + (self.capacidad_carga * 5)


# =========================
# Clase Agencia (Composición)
# =========================
class Agencia:
    def __init__(self, nombre):
        self.nombre = nombre
        self.flota = []

    def agregar_vehiculo(self, vehiculo):
        self.flota.append(vehiculo)

    def cotizar_alquiler(self, dias):
        print(f"Cotización de alquiler por {dias} días:")
        for vehiculo in self.flota:
            costo = vehiculo.calcular_tarifa_diaria() * dias
            print(f"Vehículo {vehiculo.placa}: {costo}")


# =========================
# Ejecución
# =========================
agencia = Agencia("Alquiler Express")

coche1 = Coche("ABC123", "Toyota", 100, True)
camion1 = Camion("XYZ789", "Volvo", 150, 10)

agencia.agregar_vehiculo(coche1)
agencia.agregar_vehiculo(camion1)

agencia.cotizar_alquiler(3)
