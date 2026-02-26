from fastapi import FastAPI
from route_service.router import router as routes_router
from lines_service.router import router as lines_router
from alerts_service.router import router as alerts_router
from vehicles_service.router import router as vehicles_router
from security.router import router as auth_router

app = FastAPI(title="MBTA Gateway")

@app.get("/")
def read_root():
    return {"message": "Welcome to MBTA Gateway"}

app.include_router(routes_router)
app.include_router(lines_router)
app.include_router(alerts_router)
app.include_router(vehicles_router)