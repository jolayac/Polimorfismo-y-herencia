from presentation.animal_vm import AnimalViewModel


class AnimalCLIView:
    """Vista CLI: suscribe a observables y expone loop de demo."""

    def __init__(self, vm: AnimalViewModel):
        self.vm = vm
        self.vm.info.subscribe(self._render_info)
        self.vm.error.subscribe(self._render_error)
        self.vm.mensaje.subscribe(self._render_mensaje)

    def _render_info(self, animal):
        if animal:
            print(f"Animal actual: {animal._nombre} ({animal._especie})")

    def _render_error(self, err):
        if err:
            print(f"[ERROR] {err}")

    def _render_mensaje(self, msg):
        if msg:
            print(f"[INFO] {msg}")

    def demo(self):
        print("=== Enciclopedia Interactiva de Animales (MVVM + Firebase) ===")
        print("Comandos: new <tipo> <nombre> | show | save | load <nombre> | del <nombre> | list | h | q")
        while True:
            try:
                entrada = input("> ").strip()
            except EOFError:
                break
            if not entrada:
                continue
            if entrada.lower() == "q":
                break
            if entrada.lower() in ("h", "help"):
                print("Comandos: new <tipo> <nombre> (tipo: perro/gato/pajaro/oso) | show | save | load <nombre> | del <nombre> | list | q")
                continue
            partes = entrada.split()
            cmd = partes[0].lower()
            if cmd == "new" and len(partes) >= 3:
                tipo = partes[1]
                nombre = partes[2]
                self.vm.crear_animal(tipo, nombre)
            elif cmd == "show":
                self.vm.mostrar_acciones()
            elif cmd == "save":
                self.vm.guardar()
            elif cmd == "load" and len(partes) == 2:
                self.vm.cargar(partes[1])
            elif cmd == "del" and len(partes) == 2:
                self.vm.eliminar(partes[1])
            elif cmd == "list":
                items = self.vm.listar()
                if not items:
                    print("(sin animales)")
                else:
                    for k, v in items.items():
                        print(f"- {k}: {v}")
            else:
                print("Comando no reconocido. Escribe 'h' para ayuda.")
