from models import Estudiante,Cliente
from shared.json_manager import GestorJSON
e=Estudiante(
    id_estudiante=1,
    nombre="Juan",
    apellido="Pérez",
    email="juan.perez@example.com"
     )
e.agregar_nota("Matemáticas", 85)
gestor = GestorJSON("data/estudiantes.json")
gestor = GestorJSON("data/clientes.json")
gestor.guardar([e.a_diccionario()])

print("¡Estudiante creado y guardado con éxito!")


c=Cliente (
    id_cliente=1,
    nombre="Ana",
    apellido="García",
    email="ana@gamil.com",
    telefono="0994077921",
    ciudad="Guayaquil"      
    
)
    
         