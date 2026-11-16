import os
import sys

# Parche de rutas para que Python encuentre la carpeta src/gestor
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from gestor.models.item import Item, cargar_items_de_json, guardar_items_en_json

print("=== 1. PROBANDO VALIDACIONES DE LA CLASE ITEM ===")
try:
    # Creamos un ítem válido
    item1 = Item(id_item=1, nombre="Poción de Vida", tipo="Consumible", cantidad=5)
    print(f"¡Ítems creado correctamente! -> {item1}")
    
    # Probamos lanzar un error a propósito (cantidad negativa)
    print("Probando cantidad negativa (debe saltar error):")
    item_invalido = Item(id_item=2, nombre="Escudo", tipo="Armadura", cantidad=-3)
except ValueError as e:
    print(f" [ÉXITO] El programa frenó el error correctamente: {e}")


print("\n=== 2. PROBANDO GUARDAR EN JSON ===")
# Creamos una lista de ítems de prueba
lista_para_guardar = [
    Item(1, "Espada Corta", "Arma", 1),
    Item(2, "Poción de Maná", "Consumible", 3),
    Item(3, "Casco de Cuero", "Armadura", 1)
]

# Guardamos en la carpeta data/items.json
guardar_items_en_json(lista_para_guardar, "data/items.json")


print("\n=== 3. PROBANDO CARGAR DESDE JSON ===")
# Leemos los datos del archivo que acabamos de crear
lista_recuperada = cargar_items_de_json("data/items.json")

print(f"Se cargaron {len(lista_recuperada)} ítems del archivo:")
for it in lista_recuperada:
    print(f" - {it}")