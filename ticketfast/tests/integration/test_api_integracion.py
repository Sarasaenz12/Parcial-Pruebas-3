from src.database.models import ReservaDB


def test_crear_reserva_persiste_en_base_de_datos(client_con_bd, db_session):
    payload = {
        "cliente_email": "test@correo.com",
        "zona": "VIP",
        "cantidad": 2,
    }

    response = client_con_bd.post("/reservas/concierto-2026", json=payload)

    assert response.status_code == 201

    reserva_guardada = (
        db_session.query(ReservaDB)
        .filter(ReservaDB.evento_id == "concierto-2026")
        .first()
    )

    assert reserva_guardada is not None
    assert reserva_guardada.cliente_email == "test@correo.com"