from controller import ClienteController, EstudianteController
from shared.herramientas import (
    imprimir_titulo, imprimir_exito, imprimir_error, imprimir_info
)


class ClienteView:
    @staticmethod
    def listar():
        imprimir_titulo("Lista de Clientes")
        clientes = ClienteController.listar()
        if not clientes:
            print("No hay clientes registrados.")
            return
        print(f"{'ID':<5} | {'Nombre Completo':<25} | {'Email':<25} | {'Teléfono':<12} | {'Ciudad'}")
        print("-" * 80)
        for c in clientes:
            print(f"{c.id_cliente:<5} | {c.nombre_completo:<25} | {c.email:<25} | {c.telefono:<12} | {c.ciudad}")

    @staticmethod
    def buscar():
        imprimir_titulo("Buscar Cliente")
        try:
            id_c = int(input("Ingrese el ID del cliente: "))
            cliente = ClienteController.obtener(id_c)
            if cliente:
                print(f"\nID:       {cliente.id_cliente}")
                print(f"Nombre:   {cliente.nombre_completo}")
                print(f"Email:    {cliente.email}")
                print(f"Teléfono: {cliente.telefono}")
                print(f"Ciudad:   {cliente.ciudad}")
            else:
                imprimir_error(f"No existe un cliente con ID {id_c}.")
        except ValueError:
            imprimir_error("El ID debe ser un número entero.")

    @staticmethod
    def crear():
        imprimir_titulo("Registrar Cliente")
        datos = {
            "nombre": input("Nombre: "),
            "apellido": input("Apellido: "),
            "email": input("Email: "),
            "telefono": input("Teléfono: "),
            "ciudad": input("Ciudad: "),
        }
        exito, resultado = ClienteController.crear(datos)
        if exito:
            imprimir_exito(resultado)
        else:
            imprimir_error(resultado)

    @staticmethod
    def actualizar():
        imprimir_titulo("Actualizar Cliente")
        try:
            id_c = int(input("Ingrese el ID del cliente a modificar: "))
            cliente = ClienteController.obtener(id_c)
            if not cliente:
                imprimir_error(f"No se encontró cliente con ID {id_c}.")
                return
            print(f"\nModificando: {cliente.nombre_completo} (Enter para conservar actual)")

            nom = input(f"Nuevo Nombre [{cliente.nombre}]: ").strip()
            ape = input(f"Nuevo Apellido [{cliente.apellido}]: ").strip()
            em = input(f"Nuevo Email [{cliente.email}]: ").strip()
            tel = input(f"Nuevo Teléfono [{cliente.telefono}]: ").strip()
            ciu = input(f"Nueva Ciudad [{cliente.ciudad}]: ").strip()

            cambios = {}
            if nom: cambios["nombre"] = nom
            if ape: cambios["apellido"] = ape
            if em: cambios["email"] = em
            if tel: cambios["telefono"] = tel
            if ciu: cambios["ciudad"] = ciu

            if not cambios:
                print("\n[!] No se realizaron cambios.")
                return

            exito, resultado = ClienteController.actualizar(id_c, cambios)
            if exito:
                imprimir_exito(resultado)
            else:
                imprimir_error(resultado)
        except ValueError:
            imprimir_error("El ID debe ser un número entero.")

    @staticmethod
    def eliminar():
        imprimir_titulo("Eliminar Cliente")
        try:
            id_c = int(input("Ingrese el ID a eliminar: "))
            if input(f"¿Confirmar eliminación del ID {id_c}? (s/n): ").strip().lower() == "s":
                exito, msj = ClienteController.eliminar(id_c)
                if exito:
                    imprimir_exito(msj)
                else:
                    imprimir_error(msj)
            else:
                print("\nOperación cancelada.")
        except ValueError:
            imprimir_error("El ID debe ser un número entero.")


class EstudianteView:
    @staticmethod
    def listar():
        imprimir_titulo("Lista de Estudiantes")
        estudiantes = EstudianteController.listar()
        if not estudiantes:
            print("No hay estudiantes registrados.")
            return
        print(f"{'ID':<5} | {'Nombre Completo':<25} | {'Email':<25} | {'Carnet':<12} | {'Prom':<6} | {'Estado'}")
        print("-" * 100)
        for e in estudiantes:
            print(f"{e.id:<5} | {e.nombre_completo:<25} | {e.email:<25} | {e.carnet:<12} | {e.promedio:<6} | {e.estado}")

    @staticmethod
    def buscar():
        imprimir_titulo("Buscar Estudiante")
        try:
            id_e = int(input("Ingrese el ID del estudiante: "))
            e = EstudianteController.obtener(id_e)
            if e:
                print(f"\nID:       {e.id}")
                print(f"Nombre:   {e.nombre_completo}")
                print(f"Email:    {e.email}")
                print(f"Carnet:   {e.carnet}")
                print(f"Promedio: {e.promedio}")
                print(f"Estado:   {e.estado}")
                print(f"Materias: {', '.join(sorted(e.materias)) or 'ninguna'}")
            else:
                imprimir_error(f"No existe un estudiante con ID {id_e}.")
        except ValueError:
            imprimir_error("El ID debe ser un número entero.")

    @staticmethod
    def crear():
        imprimir_titulo("Registrar Estudiante")
        datos = {
            "nombre": input("Nombre: "),
            "apellido": input("Apellido: "),
            "email": input("Email: "),
            "carnet": input("Carnet: "),
        }
        exito, resultado = EstudianteController.crear(datos)
        if exito:
            imprimir_exito(resultado)
        else:
            imprimir_error(resultado)

    @staticmethod
    def actualizar():
        imprimir_titulo("Actualizar Estudiante")
        try:
            id_e = int(input("Ingrese el ID del estudiante a modificar: "))
            e = EstudianteController.obtener(id_e)
            if not e:
                imprimir_error(f"No se encontró estudiante con ID {id_e}.")
                return
            print(f"\nModificando: {e.nombre_completo} (Enter para conservar actual)")

            nom = input(f"Nuevo Nombre [{e.nombre}]: ").strip()
            ape = input(f"Nuevo Apellido [{e.apellido}]: ").strip()
            em = input(f"Nuevo Email [{e.email}]: ").strip()
            car = input(f"Nuevo Carnet [{e.carnet}]: ").strip()

            cambios = {}
            if nom: cambios["nombre"] = nom
            if ape: cambios["apellido"] = ape
            if em: cambios["email"] = em
            if car: cambios["carnet"] = car

            if not cambios:
                print("\n[!] No se realizaron cambios.")
                return

            exito, resultado = EstudianteController.actualizar(id_e, cambios)
            if exito:
                imprimir_exito(resultado)
            else:
                imprimir_error(resultado)
        except ValueError:
            imprimir_error("El ID debe ser un número entero.")

    @staticmethod
    def eliminar():
        imprimir_titulo("Eliminar Estudiante")
        try:
            id_e = int(input("Ingrese el ID a eliminar: "))
            if input(f"¿Confirmar eliminación del ID {id_e}? (s/n): ").strip().lower() == "s":
                exito, msj = EstudianteController.eliminar(id_e)
                if exito:
                    imprimir_exito(msj)
                else:
                    imprimir_error(msj)
            else:
                print("\nOperación cancelada.")
        except ValueError:
            imprimir_error("El ID debe ser un número entero.")

    @staticmethod
    def agregar_nota():
        imprimir_titulo("Agregar Nota")
        try:
            id_e = int(input("Ingrese el ID del estudiante: "))
            materia = input("Materia: ").strip()
            nota = float(input("Nota (0-20): "))
            exito, msj = EstudianteController.agregar_nota(id_e, materia, nota)
            if exito:
                imprimir_exito(msj)
            else:
                imprimir_error(msj)
        except ValueError:
            imprimir_error("El ID debe ser entero y la nota un número.")

    @staticmethod
    def materias_ofertadas():
        imprimir_titulo("Materias Ofertadas")
        materias = EstudianteController.materias_ofertadas()
        if not materias:
            print("Aún no hay materias registradas.")
        else:
            for m in materias:
                print(f"  • {m}")

    @staticmethod
    def materias_en_comun():
        imprimir_titulo("Materias en Común")
        try:
            id_a = int(input("ID del primer estudiante: "))
            id_b = int(input("ID del segundo estudiante: "))
            comunes, msj = EstudianteController.materias_en_comun(id_a, id_b)
            if comunes is None:
                imprimir_error(msj)
            elif not comunes:
                imprimir_info("No tienen materias en común.")
            else:
                imprimir_info(f"Materias en común: {', '.join(sorted(comunes))}")
        except ValueError:
            imprimir_error("Los IDs deben ser números enteros.")

    @staticmethod
    def estadisticas():
        imprimir_titulo("Estadísticas de Estudiantes")
        datos = EstudianteController.estadisticas()
        print(f"  Estudiantes registrados : {datos['total']}")
        print(f"  Materias distintas      : {len(datos['materias'])} -> {', '.join(datos['materias'])}")
        print(f"  Promedio general        : {datos['promedio_general']}")
        print(f"  Aprobados               : {datos['aprobados']}")
        print(f"  Reprobados              : {datos['reprobados']}")cls