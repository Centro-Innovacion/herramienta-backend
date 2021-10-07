from typing import List

from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from db.db_conection import get_db

from db.cita_proyecto_db import Cita_ProyectoInDB
from models.cita_proyecto_models import Cita_ProyectoInAdd, Cita_ProyectoOut

router = APIRouter()

@router.post("/proyecto/crear/",response_model=Cita_ProyectoOut)
async def register_citas_proyectos(new_cita_proyecto: Cita_ProyectoInAdd, db: Session = Depends(get_db)):
    cita_proyecto_in_db = Cita_ProyectoInDB(**new_cita_proyecto.dict())
    db.add(cita_proyecto_in_db)
    db.commit()
    db.refresh(cita_proyecto_in_db)
    return cita_proyecto_in_db

