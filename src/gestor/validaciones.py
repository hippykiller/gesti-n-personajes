"""Funciones para pedir y validar datos por consola."""

from collections.abc import Sequence


def pedir_entero(
    mensaje: str, minimo: int | None = None, maximo: int | None = None
) -> int:
    """Pide un entero, con límites opcionales, hasta que sea válido."""
    while True:
        dato = input(mensaje)
        try:
            numero = int(dato)
        except ValueError:
            print("Error, por favor ingrese solo numeros enteros.")
            continue
        if minimo is not None and numero < minimo:
            print(f"Error, el numero debe ser igual o mayor a {minimo}.")
            continue
        if maximo is not None and numero > maximo:
            print(f"Error, el numero debe ser igual o menor a {maximo}.")
            continue
        return numero


def pedir_entero_positivo(mensaje: str) -> int:
    """Pide un entero mayor o igual a 1."""
    return pedir_entero(mensaje, minimo=1)


def pedir_texto(mensaje: str) -> str:
    """Pide un texto no vacío y que no sea solo números."""
    while True:
        texto = input(mensaje).strip()
        if texto == "":
            print("Error, no se puede dejar el campo vacio.")
            continue
        if texto.isdigit():
            print("Error, por favor ingrese un texto, no solo numeros.")
            continue
        return texto


def pedir_opcion(mensaje: str, opciones_validas: Sequence[str]) -> str:
    """Pide una opción que esté dentro de las opciones válidas."""
    while True:
        opcion = input(mensaje).strip()
        if opcion in opciones_validas:
            return opcion
        print(f"Error, por favor ingrese una opcion valida {list(opciones_validas)}.")


def pedir_si_o_no(mensaje: str) -> bool:
    """Pide S o N y devuelve True para S y False para N."""
    while True:
        respuesta = input(mensaje + " (S/N) ").strip().upper()
        if respuesta == "S":
            return True
        if respuesta == "N":
            return False
        print("Error, ingresa solo S o N.")
