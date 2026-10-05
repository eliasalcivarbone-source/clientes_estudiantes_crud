class Cliente:
    CAMPOS = ("nombre", "apellido", "email", "telefono", "ciudad")
    OBLIGATORIOS = ("nombre", "apellido", "email", "telefono", "ciudad")
    def __init__(self, id_cliente, nombre, apellido, email, telefono, ciudad):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.telefono = telefono
        self.ciudad = ciudad

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, valor):
        self._id_cliente = int(valor)

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = valor.strip().title()

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, valor):
        if not valor or not valor.strip():
            raise ValueError("El apellido no puede estar vacío.")
        self._apellido = valor.strip().title()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        v = valor.strip().lower()
        if "@" not in v or "." not in v:
            raise ValueError(f"El email '{valor}' no tiene un formato válido.")
        self._email = v

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self, valor):
        self._telefono = valor.strip()

    @property
    def ciudad(self):
        return self._ciudad

    @ciudad.setter
    def ciudad(self, valor):
        self._ciudad = valor.strip().title()

    @property
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"

    def a_diccionario(self):
        return {
            "id": self.id_cliente,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "email": self.email,
            "telefono": self.telefono,
            "ciudad": self.ciudad
        }

    @classmethod
    def desde_diccionario(cls, d):
        return cls(
            id_cliente=d["id"],
            nombre=d["nombre"],
            apellido=d["apellido"],
            email=d["email"],
            telefono=d["telefono"],
            ciudad=d["ciudad"]
        )


class Estudiante:
    CAMPOS = ("nombre", "apellido", "email", "carnet")
    OBLIGATORIOS = ("nombre", "apellido", "email", "carnet")
    NOTA_MINIMA = 0
    NOTA_MAXIMA = 20
    total_creados = 0

    def __init__(self, id_estudiante, nombre, apellido, email, carnet,
                 notas=None, materias=None):
        self.__id = id_estudiante
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.carnet = carnet
        self.__notas = dict(notas) if notas else {}
        self.__materias = set(materias) if materias else set()
        Estudiante.total_creados += 1

    @staticmethod
    def limpiar(texto):
        return str(texto).strip()

    @staticmethod
    def es_nota_valida(nota):
        return isinstance(nota, (int, float)) and \
            Estudiante.NOTA_MINIMA <= nota <= Estudiante.NOTA_MAXIMA

    @property
    def id(self):
        return self.__id

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        valor = Estudiante.limpiar(valor)
        if not valor:
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = valor.title()

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, valor):
        valor = Estudiante.limpiar(valor)
        if not valor:
            raise ValueError("El apellido no puede estar vacío.")
        self.__apellido = valor.title()

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        valor = Estudiante.limpiar(valor)
        if "@" not in valor or "." not in valor:
            raise ValueError("El email debe contener '@' y '.'.")
        self.__email = valor.lower()

    @property
    def carnet(self):
        return self.__carnet

    @carnet.setter
    def carnet(self, valor):
        valor = Estudiante.limpiar(valor).upper()
        if len(valor) < 4:
            raise ValueError("El carnet debe tener al menos 4 caracteres.")
        self.__carnet = valor

    @property
    def materias(self):
        return set(self.__materias)

    @property
    def notas(self):
        return self.__notas

    @property
    def nombre_completo(self):
        return f"{self.__nombre} {self.__apellido}"

    @property
    def promedio(self):
        todas = []
        for lista in self.__notas.values():
            todas.extend(lista)
        return round(sum(todas) / len(todas), 2) if todas else 0.0

    @property
    def estado(self):
        return "Aprobado" if self.promedio >= 14 else "Reprobado"

    def inscribir_materia(self, materia):
        materia = Estudiante.limpiar(materia).title()
        if not materia:
            raise ValueError("La materia no puede estar vacía.")
        self.__materias.add(materia)
        return materia

    def agregar_nota(self, materia, nota):
        if not Estudiante.es_nota_valida(nota):
            raise ValueError(
                f"La nota debe estar entre {Estudiante.NOTA_MINIMA} y {Estudiante.NOTA_MAXIMA}."
            )
        materia = self.inscribir_materia(materia)
        self.__notas.setdefault(materia, []).append(float(nota))

    def materias_en_comun(self, otro):
        return self.__materias & otro.materias

    def a_diccionario(self):
        return {
            "id": self.__id,
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "email": self.__email,
            "carnet": self.__carnet,
            "notas": self.__notas,
            "materias": sorted(self.__materias),
        }

    @classmethod
    def desde_diccionario(cls, datos):
        return cls(
            datos["id"],
            datos["nombre"],
            datos["apellido"],
            datos["email"],
            datos["carnet"],
            notas=datos.get("notas", {}),
            materias=set(datos.get("materias", [])),
        )

    def __str__(self):
        return f"[{self.__carnet}] {self.nombre_completo} - Promedio: {self.promedio} ({self.estado})"