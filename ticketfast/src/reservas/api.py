from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from src.database.config import get_db, engine
from src.database.models import Base
from src.database.repositorio import ReservasRepositorio
from pydantic import BaseModel

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ReservaInput(BaseModel):
    cliente_email: str
    zona: str
    cantidad: int


@app.post("/reservas/{evento_id}", status_code=201)
def crear_reserva(evento_id: str, reserva: ReservaInput, db: Session = Depends(get_db)):
    if reserva.zona not in ["VIP", "General"]:
        raise HTTPException(status_code=400, detail="Zona invalida")
    if reserva.cantidad < 1:
        raise HTTPException(status_code=400, detail="Cantidad invalida")

    repo = ReservasRepositorio(db)
    nueva_reserva = repo.guardar_reserva(evento_id, reserva.cliente_email, reserva.zona, reserva.cantidad)
    return {"mensaje": "Reserva creada con exito", "reserva_id": nueva_reserva.id}


@app.get("/reservas/{evento_id}/resumen", status_code=200)
def obtener_resumen(evento_id: str, db: Session = Depends(get_db)):
    repo = ReservasRepositorio(db)
    total_recaudado = repo.calcular_total_evento(evento_id)
    return {"evento_id": evento_id, "total_recaudado": total_recaudado}