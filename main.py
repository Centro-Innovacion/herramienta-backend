from fastapi import Depends, FastAPI

from routers.entidad_router import router as router_entidad
from routers.solicitud_router import router as router_solicitud
from routers.home_router import router as router_home
from routers.cita_reunion_router import router as router_cita_reunion
from routers.cita_capacitacion_router import router as router_cita_capacitacion
from routers.cita_charla_router import router as router_cita_charla
from routers.cita_proyecto_router import router as router_cita_proyecto
from routers.otro_rol_router import router as router_otro_rol

app = FastAPI()
from fastapi.middleware.cors import CORSMiddleware

origins = [
"http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
"http://localhost", "http://localhost:8080", "http://localhost:8081"
]

app.add_middleware(
CORSMiddleware, allow_origins=origins,
allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

app.include_router(router_entidad)
app.include_router(router_solicitud)
app.include_router(router_home)
app.include_router(router_cita_reunion)
app.include_router(router_cita_capacitacion)
app.include_router(router_cita_charla)
app.include_router(router_cita_proyecto)
app.include_router(router_otro_rol)