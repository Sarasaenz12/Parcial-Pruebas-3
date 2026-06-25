import httpx

BASE_URL = "http://localhost:8001"


def test_flujo_completo_reserva_y_consolidado_financiero():
    payload = {
        "cliente_email": "sistema@correo.com",
        "zona": "General",
        "cantidad": 3,
    }

    response_post = httpx.post(f"{BASE_URL}/reservas/sistema-evento-xyz", json=payload)
    assert response_post.status_code == 201

    response_get = httpx.get(f"{BASE_URL}/reservas/sistema-evento-xyz/resumen")
    assert response_get.status_code == 200

    data = response_get.json()
    assert data["total_recaudado"] == 150_000