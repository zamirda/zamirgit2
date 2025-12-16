# =========================
# Clase Producto
# =========================
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio


# =========================
# Clase Cliente base
# =========================
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def obtener_descuento(self):
        return 0.0


# =========================
# Cliente Premium (Herencia)
# =========================
class ClientePremium(Cliente):
    def obtener_descuento(self):
        return 0.15


# =========================
# Clase Pedido (Composición)
# =========================
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def calcular_total(self):
        subtotal = 0
        for producto in self.productos:
            subtotal += producto.precio

        descuento = subtotal * self.cliente.obtener_descuento()
        total = subtotal - descuento
        return total


# =========================
# Ejecución
# =========================
cliente1 = Cliente("Ana")
cliente2 = ClientePremium("Luis")

producto1 = Producto("Teclado", 100)
producto2 = Producto("Mouse", 50)

pedido = Pedido(cliente2)
pedido.agregar_producto(producto1)
pedido.agregar_producto(producto2)

print("Total del pedido:", pedido.calcular_total())
