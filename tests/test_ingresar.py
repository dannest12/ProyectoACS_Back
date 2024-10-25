# tests/test_ingresar.py

import pytest
from fastapi.testclient import TestClient
from main import app
from unittest.mock import MagicMock
from services.login import ServicioLogin

# Simulamos el ServicioLogin
app.dependency_overrides[ServicioLogin] = lambda: MagicMock()

client = TestClient(app)

def test_ingresar_correcto():
    # Simulamos un login exitoso
    ServicioLogin.login = MagicMock(return_value=None)  # No lanza excepciones
    response = client.post("/ingresar/", data={"usuario": "test_user", "clave": "test_password"})
    
    assert response.status_code == 200
    assert response.json() == {"status": "ok", "mensaje": "Bienvenido/a, test_user!"}  # Incluimos el mensaje

def test_ingresar_incorrecto():
    # Simulamos un login fallido
    ServicioLogin.login = MagicMock(side_effect=Exception("Credenciales inválidas"))
    response = client.post("/ingresar/", data={"usuario": "test_user", "clave": "wrong_password"})
    
    assert response.status_code == 401
    assert response.json() == {"status": "error", "mensaje": "Credenciales inválidas"}
