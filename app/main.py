import os
import sys
from dotenv import load_dotenv

if __package__ in (None, ""):
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from domain.animal import Animal  # Sigue igual, solo base

from presentation.animal_vm import AnimalViewModel
from ui.animal_cli import AnimalCLIView
from data.firebase_service import FirebaseRealtimeService

def main():
    load_dotenv()
    animal_inicial = Animal("Ejemplo", "Animal", "Desconocida")
    storage = None
    try:
        storage = FirebaseRealtimeService(base_path="animals")
    except Exception:
        storage = None
    vm = AnimalViewModel(animal_inicial, storage)
    view = AnimalCLIView(vm)
    view.demo()

if __name__ == "__main__":
    main()