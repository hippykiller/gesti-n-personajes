#validaciones.py
#Autor: Gabriel Benitez Ibarola - Tarea 2: validaciones
#este archivo evita que el programa se rompa por un dato mal ingesado.

def pedir_entero(mensaje, minimo= None, maximo= None):
    while True:
        dato= input(mensaje)
        try:
            numero= int(dato)
            if minimo is not None and numero < minimo:
                print(f"Error, el numero debe ser igual o mayor a {minimo}.")
                continue
            if maximo is not None and numero > maximo:
                print(f"Error, el numero debe ser igual o menor a {maximo}.")
                continue
            return numero 
        except ValueError:
            print(f"Error, por favor ingrese solo numeros enteros.")

def pedir_entero_positivo(mensaje):
    return pedir_entero(mensaje, minimo=1)

def pedir_texto(mensaje):
    while True:
        texto= input(mensaje).strip()
        if texto=="":
            print(f"Error, no se puede dejar el campo vacio.")
            continue
        if texto.isdigit():
            print(f"Error, por favor ingrese un texto, no solo numeros.")
            continue
        return texto

def pedir_opcion(mensaje,opciones_validas):
    while True:
        opcion= input(mensaje).strip()
        if opcion in opciones_validas:
            return opcion
        print(f"Error, por favor ingrese una opcion valida {opciones_validas}.")


def pedir_si_o_no(mensaje):
    while True:
        respuesta= input(mensaje + "(S/N)").strip().upper()
        if respuesta == "S":
            return True
        if respuesta == "N":
            return False
        print(f"Error, ingresa solo S o N.")

        