from pydantic import BaseModel

class OtroRolInAdd(BaseModel):
    id_rol: str
    otro_rol: str

class OtroRolOut(BaseModel):
    id_rol: str
    otro_rol: str

    class Config:
        orm_mode = True