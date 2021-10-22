from sqlalchemy import Column, Integer, String, DateTime
from db.db_conection import Base, engine

class RolInDB(Base):
    __tablename__ = "rol"
    id = Column((Integer), primary_key=True, unique=True)
    id_rol = Column(String(100))
    fecha = Column(DateTime)
    rol = Column(String(100))
    contador = Column(Integer)

Base.metadata.create_all(bind=engine)
