# =========================
# Clase base: Cuenta
# =========================
class Cuenta:
    def __init__(self, numero, saldo):
        self.numero = numero
        self.saldo = saldo

    def depositar(self, monto):
        if monto > 0:
            self.saldo += monto
        else:
            print("El monto a depositar debe ser positivo")

    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo -= monto
        else:
            print("Fondos insuficientes")

    def mostrar_saldo(self):
        return self.saldo


# =========================
# Cuenta de Ahorros
# =========================
class CuentaAhorros(Cuenta):
    def __init__(self, numero, saldo, tasa_interes):
        super().__init__(numero, saldo)
        self.tasa_interes = tasa_interes

    def aplicar_interes(self):
        interes = self.saldo * self.tasa_interes
        self.saldo += interes


# =========================
# Cuenta Corriente
# =========================
class CuentaCorriente(Cuenta):
    def __init__(self, numero, saldo, limite_sobregiro):
        super().__init__(numero, saldo)
        self.limite_sobregiro = limite_sobregiro

    def retirar(self, monto):
        if monto <= self.saldo + self.limite_sobregiro:
            self.saldo -= monto
        else:
            print("Se excede el límite de sobregiro permitido")


# =========================
# Clase Cliente (Composición)
# =========================
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def mostrar_saldo_total(self):
        total = 0
        for cuenta in self.cuentas:
            total += cuenta.mostrar_saldo()
        return total


# =========================
# Ejecución del sistema
# =========================
cliente1 = Cliente("Carlos Pérez")

cuenta_ahorros = CuentaAhorros("AH-001", 1000, 0.05)
cuenta_corriente = CuentaCorriente("CC-001", 500, 300)

cliente1.agregar_cuenta(cuenta_ahorros)
cliente1.agregar_cuenta(cuenta_corriente)

cuenta_ahorros.aplicar_interes()
cuenta_corriente.retirar(700)

print("Saldo en cuenta de ahorros:", cuenta_ahorros.mostrar_saldo())
print("Saldo en cuenta corriente:", cuenta_corriente.mostrar_saldo())
print("Saldo total del cliente:", cliente1.mostrar_saldo_total())
