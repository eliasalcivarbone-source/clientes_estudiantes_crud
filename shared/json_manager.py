import json  # Permite leer y escribir datos en formato JSON.
import os    # Permite trabajar con archivos y carpetas.

class GestorJSON:
    def __init__(self, ruta_archivo):
        # Se guarda la ubicación del archivo JSON.
        self.ruta_archivo = ruta_archivo
        # Se asegura de que la carpeta donde irá el archivo exista.
        self._asegurar_directorio()

    def _asegurar_directorio(self):
        # Obtiene la carpeta que contiene la ruta del archivo.
        directorio = os.path.dirname(self.ruta_archivo)
        # Si hay una carpeta y todavía no existe, la crea.
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio, exist_ok=True)

    def leer(self):
        # Si el archivo no existe, devuelve una lista vacía.
        if not os.path.exists(self.ruta_archivo):
            return []
        try:
            # Abre el archivo para leerlo usando caracteres UTF-8.
            with open(self.ruta_archivo, "r", encoding="utf-8") as f:
                # Convierte el contenido JSON en datos de Python.
                return json.load(f)
        # Si el JSON está mal escrito o hay un error de archivo,
        # devuelve una lista vacía.
        except (json.JSONDecodeError, OSError):
            return []

    def guardar(self, datos):
        try:
            # Abre el archivo para escribir; si no existe, lo crea.
            with open(self.ruta_archivo, "w", encoding="utf-8") as f:
                # Convierte los datos de Python a JSON y los guarda.
                # ensure_ascii=False conserva letras como ñ y tildes.
                # indent=4 ordena el texto para que sea fácil de leer.
                json.dump(datos, f, ensure_ascii=False, indent=4)
            # Indica que el guardado terminó correctamente.
            return True
        # Si ocurre un error al escribir, indica que falló.
        except OSError:
            return False