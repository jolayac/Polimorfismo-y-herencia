from .observable import Observable
from domain.animal import Animal
from domain.perro import Perro  # Nuevo import
from domain.gato import Gato  # Nuevo import
from domain.pajaro import Pajaro  # Nuevo import
from domain.oso import Oso  # Nuevo import
from data.firebase_service import FirebaseRealtimeService

class AnimalViewModel:
    """ViewModel: expone estado y comandos para la vista."""

    def __init__(self, animal: Animal, storage: FirebaseRealtimeService | None = None):
        self._animal = animal
        self._storage = storage

        # Observables para UI
        self.info = Observable(None)
        self.error = Observable(None)
        self.mensaje = Observable(None)

    # --- Comandos ---
    def crear_animal(self, tipo, nombre):
        try:
            self.error.value = None
            if tipo.lower() == "perro":
                self._animal = Perro(nombre)
            elif tipo.lower() == "gato":
                self._animal = Gato(nombre)
            elif tipo.lower() == "pajaro":
                self._animal = Pajaro(nombre)
            elif tipo.lower() == "oso":
                self._animal = Oso(nombre)
            else:
                raise ValueError("Tipo de animal no reconocido\nTipos: perro/gato/pajaro/oso")
            self.info.value = self._animal  # Actualiza observable
            self.mensaje.value = f"Animal {nombre} creado ({tipo})."
        except Exception as exc:
            self.error.value = str(exc)

    def mostrar_acciones(self):
        try:
            self.error.value = None
            self._animal.describir()
            self._animal.moverse()
            self._animal.hablar()
            self._animal.alimentarse()
            self.mensaje.value = "Acciones mostradas."
        except Exception as exc:
            self.error.value = str(exc)

    # --- CRUD en Firebase ---
    def guardar(self):
        """Guarda el animal actual en RTDB por nombre."""
        if not self._storage:
            self.error.value = "Storage no configurado"
            return
        try:
            key = self._animal._nombre
            self._storage.create(key, self._animal.to_dict())
            self.mensaje.value = f"Animal {key} guardado"
        except Exception as exc:
            self.error.value = str(exc)

    def cargar(self, nombre):
        if not self._storage:
            self.error.value = "Storage no configurado"
            return
        try:
            data = self._storage.read(nombre)
            if not data:
                self.error.value = "No encontrado"
                return
            self._animal = Animal.from_dict(data)
            self.info.value = self._animal
            self.mensaje.value = f"Animal {nombre} cargado"
        except Exception as exc:
            self.error.value = str(exc)

    def eliminar(self, nombre):
        if not self._storage:
            self.error.value = "Storage no configurado"
            return
        try:
            self._storage.delete(nombre)
            self.mensaje.value = f"Animal {nombre} eliminado"
        except Exception as exc:
            self.error.value = str(exc)

    def listar(self):
        if not self._storage:
            self.error.value = "Storage no configurado"
            return {}
        try:
            return self._storage.list_all()
        except Exception as exc:
            self.error.value = str(exc)
            return {}