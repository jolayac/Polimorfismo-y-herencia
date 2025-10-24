from especies import Perro, Gato, Pajaro, Oso

class Animal:
    def __init__(self, nombre, especie, alimentacion):
        self.nombre = nombre
        self.especie = especie
        self.alimentacion = alimentacion

    def moverse(self):
        pass

    def hablar(self):
        pass

    def alimentarse(self):
        pass

    @staticmethod
    def ejecutar_programa():
        nombre_perro = input("Ingrese el nombre del perro: ")
        nombre_gato = input("Ingrese el nombre del gato: ")
        nombre_pajaro = input("Ingrese el nombre del pájaro: ")
        nombre_oso = input("Ingrese el nombre del oso: ")

        animales = [
            Perro(nombre_perro),
            Gato(nombre_gato),
            Pajaro(nombre_pajaro),
            Oso(nombre_oso)
        ]

        for animal in animales:
            print(f"\nNombre: {animal.nombre}")
            print(f"Especie: {animal.especie}")
            print(f"Alimentación: {animal.alimentacion}")
            animal.moverse()
            animal.hablar()
            animal.alimentarse()


def main():
    Animal.ejecutar_programa()


if __name__ == "__main__":
    main()


