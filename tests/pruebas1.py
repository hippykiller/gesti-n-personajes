import os
import sys
sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
)
from gestor.validaciones import (
    pedir_entero,
    pedir_entero_positivo,
    pedir_opcion,
    pedir_si_o_no,
    pedir_texto,
)
print("--- INICIANDO PRUEBAS DE VALIDACIONES ---")

# 1. La que ya probaste y funcionó
print("\n[1] Probando pedir_entero:")
numero = pedir_entero("Ingrese un numero entero: ")
print(f"¡Funcionó! El número ingresado es: {numero}")

# 2. Probar pedir_entero_positivo
print("\n[2] Probando pedir_entero_positivo:")
num_positivo = pedir_entero_positivo("Ingrese un número entero positivo: ")
print(f"¡Funcionó! El positivo ingresado es: {num_positivo}")

# 3. Probar pedir_texto
print("\n[3] Probando pedir_texto:")
texto = pedir_texto("Ingrese un texto (sin vacíos ni solo números): ")
print(f"¡Funcionó! El texto ingresado es: '{texto}'")

# 4. Probar pedir_opcion
print("\n[4] Probando pedir_opcion:")
opcion = pedir_opcion(
    "Elija una opción (a, b, c): ", opciones_validas=["a", "b", "c"]
)
print(f"¡Funcionó! Opción elegida: '{opcion}'")

# 5. Probar pedir_si_o_no
print("\n[5] Probando pedir_si_o_no:")
respuesta = pedir_si_o_no("¿Te gusta este sistema?")
print(f"¡Funcionó! Resultado booleano: {respuesta}")

print("\n¡Todas las pruebas finalizaron!")

