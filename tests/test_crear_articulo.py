import pytest
from unittest.mock import MagicMock
from model.database import BaseDeDatos
from services.articulos import ServicioArticulos
from model.usuarios import Consignatario

def test_agregar_articulo_correcto():
    # Mock de la base de datos
    db_mock = MagicMock(spec=BaseDeDatos)
    servicio = ServicioArticulos(db_mock)

    # Mock de consignatario
    consignatario_mock = MagicMock(spec=Consignatario)
    consignatario_mock.obtener_uid.return_value = 1
    db_mock.Usuarios.buscar_consignatario_por_uid.return_value = consignatario_mock
    db_mock.Articulos.crear.return_value = None  # Simular éxito en creación

    # Agregar un artículo
    servicio.agregar("Título de Prueba", "Descripción de Prueba", 100, 1)

    # Verificar que se haya llamado a la creación del artículo
    db_mock.Articulos.crear.assert_called_once_with("Título de Prueba", "Descripción de Prueba", 100, consignatario_mock)

def test_agregar_articulo_con_titulo_invalido():
    # Mock de la base de datos
    db_mock = MagicMock(spec=BaseDeDatos)
    servicio = ServicioArticulos(db_mock)

    # Probar que se lanza la excepción
    with pytest.raises(ValueError, match=servicio.TITULO_INVALIDO):
        servicio.agregar("", "Descripción de Prueba", 100, 1)

