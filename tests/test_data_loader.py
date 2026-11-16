from src.gestor.services.data_loader import cargar_base_datos

def test_cargar_base_datos():
    datos = cargar_base_datos()
    assert isinstance(datos, dict)
    assert len(datos) > 0
