# =========================
# Clase base Animal
# =========================
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        pass

    def moverse(self):
        pass


# =========================
# Clase Mamifero
# =========================
class Mamifero(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} ruge como mamífero")

    def moverse(self):
        print(f"{self.nombre} camina sobre tierra")


# =========================
# Clase Ave
# =========================
class Ave(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} canta como ave")

    def moverse(self):
        print(f"{self.nombre} vuela por el cielo")


# =========================
# Clase Habitat (Composición)
# =========================
class Habitat:
    def __init__(self, nombre):
        self.nombre = nombre
        self.animales = []

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def simular_dia(self):
        print(f"Simulación diaria en el hábitat {self.nombre}")
        for animal in self.animales:
            animal.hacer_sonido()
            animal.moverse()


# =========================
# Ejecución
# =========================
habitat_sabana = Habitat("Sabana")

leon = Mamifero("León")
aguila = Ave("Águila")

habitat_sabana.agregar_animal(leon)
habitat_sabana.agregar_animal(aguila)

habitat_sabana.simular_dia()
