class Animal:
    """
    Clase base para animales. Usa polimorfismo para métodos.
    """
    def __init__(self, nombre, especie, alimentacion):
        self._nombre = nombre  # Protegido
        self._especie = especie
        self._alimentacion = alimentacion

    def describir(self):
        print(f"Soy {self._nombre}, un {self._especie} de tipo {self._alimentacion}.")

    def moverse(self):
        print(f"{self._nombre} se mueve de alguna manera.")

    def hablar(self):
        print(f"{self._nombre} hace un sonido.")

    def alimentarse(self):
        print(f"{self._nombre} se alimenta de algo.")

    # Serialización para DB
    def to_dict(self):
        return {
            "nombre": self._nombre,
            "especie": self._especie,
            "alimentacion": self._alimentacion,
        }

    @classmethod
    def from_dict(cls, data):
        nombre = data.get("nombre")
        especie = data.get("especie")
        alimentacion = data.get("alimentacion", "Desconocida")
        # Imports locales: solo aquí, para evitar ciclo
        if especie == "Perro":
            from .perro import Perro
            return Perro(nombre)
        elif especie == "Gato":
            from .gato import Gato
            return Gato(nombre)
        elif especie == "Pajaro":
            from .pajaro import Pajaro
            return Pajaro(nombre)
        elif especie == "Oso":
            from .oso import Oso
            return Oso(nombre)
        else:
            return cls(nombre, especie, alimentacion)