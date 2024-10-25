from fastapi.testclient import TestClient
from unittest.mock import MagicMock, patch  # Asegúrate de importar patch
from main import app  # Importa la instancia de FastAPI desde tu archivo main
from services.usuarios import ServicioUsuario

def test_registrar_correcto():
    # Mock del servicio de registro
    servicio_mock = MagicMock(spec=ServicioUsuario)
    servicio_mock.agregar = MagicMock(return_value=None)  # Simular que no hay excepciones

    # Reemplaza el servicio en el controlador
    with patch('controller.usuario.ServicioUsuario', return_value=servicio_mock):
        client = TestClient(app)

        # Simula la solicitud de registro
        response = client.post("/registrar/", data={
            "nombre": "Juan",
            "apellido": "Pérez",
            "email": "juan@example.com",
            "usuario": "juanp",
            "clave": "clave123",
            "nacimiento": "2000-01-01"
        })

        # Verifica la respuesta
        assert response.status_code == 200
        assert response.json() == {"status": "ok", "mensaje": "La cuenta ha sido creada correctamente"}

