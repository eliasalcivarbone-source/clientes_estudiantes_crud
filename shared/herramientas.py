import os


def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def imprimir_titulo(texto):
    print("\n" + "=" * 50)
    print(f"   {texto.upper()}")
    print("=" * 50)


def imprimir_exito(mensaje):
    print(f"\n[✓] {mensaje}")


def imprimir_error(mensaje):
    print(f"\n[ERROR] {mensaje}")


def imprimir_info(mensaje):
    print(f"\n[i] {mensaje}")

def confirmar(pregunta):
    respuesta = input(f"{pregunta} (s/n): ").strip().lower()
    return respuesta in ("s", "si", "sí", "y", "yes")