from shared.json_manager import GestorJSON
from models import Cliente, Estudiante


class ClienteController:
    """CRUD genérico. Sirve para cualquier modelo con CAMPOS, OBLIGATORIOS y a_diccionario."""

    MODELO = Cliente
    ARCHIVO = "data/clientes.json"
    CAMPOS_BUSCABLES = ("nombre", "apellido", "email", "telefono", "ciudad")
    _gestor = GestorJSON(ARCHIVO)

    @classmethod
    def _registros(cls):
        return cls._gestor.leer()

    @classmethod
    def emails_registrados(cls, excepto_id=None):
        return {
            r["email"].lower()
            for r in cls._registros()
            if r["id"] != excepto_id
        }

    @classmethod
    def siguiente_id(cls):
        ids = [r["id"] for r in cls._registros()]
        return max(ids) + 1 if ids else 1

    @staticmethod
    def _coincide(registro, termino, campos):
        for campo in campos:
            if termino in str(registro.get(campo, "")).lower():
                return True
        return False

    @classmethod
    def crear(cls, datos):
        try:
            faltantes = [
                campo for campo in cls.MODELO.OBLIGATORIOS
                if not str(datos.get(campo, "")).strip()
            ]
            if faltantes:
                return False, f"Faltan campos obligatorios: {', '.join(faltantes)}"

            email = str(datos.get("email", "")).strip().lower()
            if email in cls.emails_registrados():
                return False, f"El email '{email}' ya está registrado."

            valores = {campo: datos.get(campo, "") for campo in cls.MODELO.CAMPOS}
            objeto = cls.MODELO(cls.siguiente_id(), **valores)

            registros = cls._registros()
            registros.append(objeto.a_diccionario())
            if not cls._gestor.guardar(registros):
                return False, "No se pudo escribir el archivo JSON."

            return True, f"{objeto.nombre_completo} creado con ID {objeto.id}."
        except ValueError as err:
            return False, str(err)

    @classmethod
    def listar(cls):
        return [cls.MODELO.desde_diccionario(r) for r in cls._registros()]

    @classmethod
    def obtener(cls, id_registro):
        for objeto in cls.listar():
            if objeto.id == id_registro:
                return objeto
        return None

    @classmethod
    def buscar(cls, termino):
        termino = str(termino).strip().lower()
        if not termino:
            return []
        return [
            cls.MODELO.desde_diccionario(r)
            for r in cls._registros()
            if cls._coincide(r, termino, cls.CAMPOS_BUSCABLES)
        ]

    @classmethod
    def actualizar(cls, id_registro, cambios):
        try:
            objeto = cls.obtener(id_registro)
            if objeto is None:
                return False, f"No existe un registro con ID {id_registro}."

            if "email" in cambios:
                nuevo = str(cambios["email"]).strip().lower()
                if nuevo in cls.emails_registrados(excepto_id=id_registro):
                    return False, f"El email '{nuevo}' ya pertenece a otro registro."

            for campo, valor in cambios.items():
                if hasattr(objeto, campo) and valor:
                    setattr(objeto, campo, valor)

            registros = cls._registros()
            for i, r in enumerate(registros):
                if r["id"] == id_registro:
                    registros[i] = objeto.a_diccionario()
                    break

            cls._gestor.guardar(registros)
            return True, f"Registro {id_registro} actualizado."
        except ValueError as err:
            return False, str(err)

    @classmethod
    def eliminar(cls, id_registro):
        registros = cls._registros()
        filtrados = [r for r in registros if r["id"] != id_registro]
        if len(registros) == len(filtrados):
            return False, f"No existe un registro con ID {id_registro}."
        cls._gestor.guardar(filtrados)
        return True, f"Registro {id_registro} eliminado."


class EstudianteController(ClienteController):
    """Hereda todo el CRUD. Solo cambia MODELO, ARCHIVO y agrega extras."""

    MODELO = Estudiante
    ARCHIVO = "data/estudiantes.json"
    CAMPOS_BUSCABLES = ("nombre", "apellido", "email", "carnet")
    _gestor = GestorJSON(ARCHIVO)

    @classmethod
    def carnets_registrados(cls, excepto_id=None):
        return {
            r["carnet"].upper()
            for r in cls._registros()
            if r.get("carnet") and r["id"] != excepto_id
        }

    @classmethod
    def crear(cls, datos):
        carnet = str(datos.get("carnet", "")).strip().upper()
        if carnet in cls.carnets_registrados():
            return False, f"El carnet '{carnet}' ya está registrado."
        return super().crear(datos)

    @classmethod
    def actualizar(cls, id_registro, cambios):
        if "carnet" in cambios:
            nuevo = str(cambios["carnet"]).strip().upper()
            if nuevo in cls.carnets_registrados(excepto_id=id_registro):
                return False, f"El carnet '{nuevo}' ya lo usa otro estudiante."
        return super().actualizar(id_registro, cambios)

    @classmethod
    def agregar_nota(cls, id_estudiante, materia, nota):
        try:
            est = cls.obtener(id_estudiante)
            if est is None:
                return False, f"No existe un estudiante con ID {id_estudiante}."
            est.agregar_nota(materia, nota)

            registros = cls._registros()
            for i, r in enumerate(registros):
                if r["id"] == id_estudiante:
                    registros[i] = est.a_diccionario()
                    break
            cls._gestor.guardar(registros)
            return True, f"Nota {nota} agregada a '{materia}' para {est.nombre_completo}."
        except ValueError as err:
            return False, str(err)

    @classmethod
    def materias_ofertadas(cls):
        todas = set()
        for e in cls.listar():
            todas |= e.materias
        return sorted(todas)

    @classmethod
    def materias_en_comun(cls, id_a, id_b):
        a = cls.obtener(id_a)
        b = cls.obtener(id_b)
        if a is None or b is None:
            return None, "Uno o ambos estudiantes no existen."
        return a.materias_en_comun(b), "OK"

    @classmethod
    def estadisticas(cls):
        registros = cls._registros()
        promedios = []
        for r in registros:
            notas = []
            for lista in r.get("notas", {}).values():
                notas.extend(lista)
            if notas:
                promedios.append(sum(notas) / len(notas))
        prom = round(sum(promedios) / len(promedios), 2) if promedios else 0
        aprobados = sum(1 for p in promedios if p >= 14)
        return {
            "total": len(registros),
            "materias": cls.materias_ofertadas(),
            "promedio_general": prom,
            "aprobados": aprobados,
            "reprobados": len(promedios) - aprobados,
        }