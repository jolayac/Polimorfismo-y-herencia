# Proyecto: Enciclopedia Interactiva de Animales con Herencia y Polimorfismo en Python

> Basado en [AccessModifiresPython](https://github.com/jolayac/AccessModifiersPython)

- **Autores:**
    - Juan Sebastián Olaya Castaneda
    - Juan Camilo Paez Guaspud
- **Tutores:**
    - Nestor German Bolivar Pulgarin
    - GrokAI

Este proyecto es una pequeña enciclopedia interactiva donde puedes crear, mostrar y guardar información sobre animales como perros, gatos, pájaros y osos. Usa una interfaz en la terminal para interactuar con los animales, y opcionalmente guarda datos en una RTDB.

## Prerequisitos

```
firebase-admin
python-dotenv
```

Para instalarlos, escriba en la terminal:
```
pip install -r requirements.txt
```

Esto instala las librerías necesarias para la base de datos (opcional) y manejo de variables de entorno.

## Ejecutar
```
python -m app.main
```
o
```
python app/main.py
```

Esto inicia la interfaz en la terminal. Si usas Firebase, configura un archivo `.env` en la carpeta principal con tus credenciales (ver cómo abajo).

## Uso de la Interfaz (CLI)

Comandos: new <tipo> <nombre> | show | save | load <nombre> | del <nombre> | list | h | q

- **Comandos disponibles** (escribe `h` para ver ayuda en cualquier momento):
  - `new <tipo> <nombre>`: Crea un nuevo animal. Tipos disponibles: perro, gato, pajaro, oso. Ejemplo: `new gato Motas`.
  - `show`: Muestra las acciones del animal actual (descripción, moverse, hablar, alimentarse).
  - `save`: Guarda el animal actual en la base de datos (usa el nombre como clave).
  - `load <nombre>`: Carga un animal guardado por su nombre.
  - `del <nombre>`: Elimina un animal de la base de datos por su nombre.
  - `list`: Lista todos los animales guardados.
  - `h` o `help`: Muestra la lista de comandos.
  - `q`: Salir.

### Ejemplos de Uso y Salidas

1. Crear un animal:
   ```
   > new gato Motas
   Animal actual: Motas (Gato)
   [INFO] Animal Motas creado (gato).
   ```

2. Mostrar acciones:
   ```
   > show
   Soy Motas, un Gato de tipo Carnívoro.
   Motas camina sobre cuatro patas.
   Motas: Miauuu.
   Motas come carne o alimentos de animales.
   [INFO] Acciones mostradas.
   ```

3. Guardar y listar:
   ```
   > save
   [INFO] Animal Motas guardado
   > list
   - Motas: {'alimentacion': 'Carnívoro', 'especie': 'Gato', 'nombre': 'Motas'}
   ```

4. Cargar un animal:
   ```
   > load Motas
   Animal actual: Motas (Gato)
   [INFO] Animal Motas cargado
   ```

5. Eliminar:
   ```
   > del Motas
   [INFO] Animal Motas eliminado
   ```

Si no hay Firebase configurado, comandos como `save` mostrarán `[ERROR] Storage no configurado`.

## Conceptos Clave: Herencia y Polimorfismo
La herencia permite que una clase "hija" (como Perro) copie y modifique características de una clase "padre" (como Animal). Por ejemplo, todos los animales heredan métodos como moverse(), pero Perro lo cambia para "camina sobre cuatro patas".

El polimorfismo hace que el mismo método funcione diferente según el tipo de animal. Cuando llamas mostrar_acciones(), un gato "miaula" y un pájaro "pía", aunque usas el mismo código. Esto hace el programa flexible sin repetir instrucciones.

## Firebase (opcional)
Para guardar/cargar animales en la nube, configura `.env` con:
  ```
  FIREBASE_DB_URL = "https://tu-proyecto.firebaseio.com"
  FIREBASE_CREDENTIALS_JSON = "ruta/a/tu/credenciales.json"  # O el JSON completo
  ```
  Si no, el proyecto funciona localmente (en memoria).
