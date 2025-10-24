from carnivoro import Carnivoro
from herbivoro import Herbivoro
from omnivoro import Omnivoro

class Perro(Carnivoro):
    def __init__(self, nombre):
        super().__init__(nombre, "Perro")

    def moverse(self):
        print(f"{self.nombre} camina sobre cuatro patas.")

    def hablar(self):
        print(f"{self.nombre}:¡Guau Guau!")


class Gato(Carnivoro):
    def __init__(self, nombre):
        super().__init__(nombre, "Gato")

    def moverse(self):
        print(f"{self.nombre} camina sobre cuatro patas.")

    def hablar(self):
        print(f"{self.nombre} dice: Miauuu.")


class Pajaro(Herbivoro):
    def __init__(self, nombre):
        super().__init__(nombre, "Pájaro")

    def moverse(self):
        print(f"{self.nombre} vuela con sus alas.")

    def hablar(self):
        print(f"{self.nombre}: Pío pío.")


class Oso(Omnivoro):
    def __init__(self, nombre):
        super().__init__(nombre, "Oso")

    def moverse(self):
        print(f"{self.nombre} camina en cuatro patas, aunque a veces en dos.")

    def hablar(self):
        print(f"{self.nombre}:GRRRRR.")