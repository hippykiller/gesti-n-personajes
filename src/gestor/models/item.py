
import json
import os

class Item:
    def __init__(self, id_item, nombre, tipo, cantidad):
        self.id_item = id_item
        self.nombre = nombre
        self.tipo = tipo
        self.cantidad = cantidad

    @property
    def id_item(self):
        return self._id_item

    @id_item.setter
    def id_item(self, nuevo_id):
        if isinstance(nuevo_id, int) and nuevo_id >= 1:
            self._id_item = nuevo_id
        else:
            raise ValueError("El ID del ítem debe ser un número entero positivo mayor o igual a 1.")

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if isinstance(nuevo_nombre, str) and nuevo_nombre.strip():
            self._nombre = nuevo_nombre.strip()
        else:
            raise ValueError("El nombre del ítem debe ser un texto no vacío.")

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, nuevo_tipo):
        if isinstance(nuevo_tipo, str) and nuevo_tipo.strip():
            self._tipo = nuevo_tipo.strip()
        else:
            raise ValueError("El tipo del ítem debe ser un texto no vacío.")

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, nueva_cantidad):
        if isinstance(nueva_cantidad, int) and nueva_cantidad >= 0:
            self._cantidad = nueva_cantidad
        else:
            raise ValueError("La cantidad debe ser un número entero mayor o igual a 0.")

    def a_diccionario(self):
        """Convierte el ítem a un diccionario para guardarlo en JSON."""
        return {
            "id_item": self.id_item,
            "nombre": self.nombre,
            "tipo": self.tipo,
            "cantidad": self.cantidad
        }

    @classmethod
    def de_diccionario(cls, datos):
        """Reconstruye un objeto Item desde un diccionario de JSON."""
        return cls(
            id_item=datos["id_item"],
            nombre=datos["nombre"],
            tipo=datos["tipo"],
            cantidad=datos["cantidad"]
        )

    def __str__(self):
        return f"[{self.id_item}] {self.nombre} ({self.tipo}) - Cant: {self.cantidad}"


# --- Funciones de Persistencia (JSON) ---

def guardar_items_en_json(lista_items, ruta_archivo="data/items.json"):
    """Guarda la lista de ítems en un archivo JSON dentro de data/."""
    os.makedirs(os.path.dirname(ruta_archivo), exist_ok=True)
    datos = [item.a_diccionario() for item in lista_items]
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
    print(f"¡Ítems guardados con éxito en {ruta_archivo}!")


def cargar_items_de_json(ruta_archivo="data/items.json"):
    """Carga los ítems desde el archivo JSON si existe."""
    if not os.path.exists(ruta_archivo):
        return []
    try:
        with open(ruta_archivo, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            return [Item.de_diccionario(d) for d in datos]
    except Exception as e:
        print(f"Error al cargar el archivo JSON de ítems: {e}")
        return []

        