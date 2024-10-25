import pytest
from datetime import date
from model.usuarios import Usuario
from model.tipo_usuario import TipoDeUsuario  # Importar correctamente el Enum

def test_obtener_uid():
    usuario = Usuario(1, "Juan", "Pérez", "juan@example.com", "juanp", "clave123", date(2000, 1, 1), TipoDeUsuario.Martillero)
    assert usuario.obtener_uid() == 1

def test_obtener_clave():
    usuario = Usuario(2, "Ana", "Gómez", "ana@example.com", "anag", "clave123", date(1995, 5, 15), TipoDeUsuario.Consignatario)
    assert usuario.obtener_clave() == "clave123"

def test_obtener_nombre():
    usuario = Usuario(3, "Luis", "Martínez", "luis@example.com", "luism", "clave123", date(2005, 10, 10), TipoDeUsuario.Pujador)
    assert usuario.obtener_nombre() == "Luis"