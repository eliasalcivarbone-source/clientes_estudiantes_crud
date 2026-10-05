from views import ClienteView, EstudianteView
from shared.herramientas import imprimir_titulo, imprimir_error


def menu_clientes():
    while True:
        imprimir_titulo("Sistema de Gestión de Clientes")
        print("1. Listar clientes")
        print("2. Buscar cliente por ID")
        print("3. Registrar nuevo cliente")
        print("4. Actualizar cliente")
        print("5. Eliminar cliente")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            ClienteView.listar()
        elif opcion == "2":
            ClienteView.buscar()
        elif opcion == "3":
            ClienteView.crear()
        elif opcion == "4":
            ClienteView.actualizar()
        elif opcion == "5":
            ClienteView.eliminar()
        elif opcion == "0":
            break
        else:
            imprimir_error("Opción inválida.")


def menu_estudiantes():
    while True:
        imprimir_titulo("Sistema de Gestión de Estudiantes")
        print("1. Listar estudiantes")
        print("2. Buscar estudiante por ID")
        print("3. Registrar nuevo estudiante")
        print("4. Actualizar estudiante")
        print("5. Eliminar estudiante")
        print("6. Agregar nota a estudiante")
        print("7. Ver materias ofertadas")
        print("8. Ver materias en común entre dos estudiantes")
        print("9. Ver estadísticas")
        print("0. Volver al menú principal")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            EstudianteView.listar()
        elif opcion == "2":
            EstudianteView.buscar()
        elif opcion == "3":
            EstudianteView.crear()
        elif opcion == "4":
            EstudianteView.actualizar()
        elif opcion == "5":
            EstudianteView.eliminar()
        elif opcion == "6":
            EstudianteView.agregar_nota()
        elif opcion == "7":
            EstudianteView.materias_ofertadas()
        elif opcion == "8":
            EstudianteView.materias_en_comun()
        elif opcion == "9":
            EstudianteView.estadisticas()
        elif opcion == "0":
            break
        else:
            imprimir_error("Opción inválida.")


def main():
    while True:
        imprimir_titulo("Sistema General")
        print("1. Gestionar Clientes")
        print("2. Gestionar Estudiantes")
        print("0. Salir")

        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            menu_clientes()
        elif opcion == "2":
            menu_estudiantes()
        elif opcion == "0":
            print("\n¡Hasta luego!")
            break
        else:
            imprimir_error("Opción inválida.")


if __name__ == "__main__":
    main()