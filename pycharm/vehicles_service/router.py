from fastapi import FastAPI
import httpx

API_KEY = "33df77cbf5d4483ab87b3980e0bc913a"
ENDPOINT_URL = "https://api-v3.mbta.com"

app = FastAPI(title="Vehicles Service")

@app.get("/")
def root():
    return {"service": "Vehicles Service"}

@app.get("/vehicles")
async def get_vehicles(route: str = None, stop: str = None):
    params = {"api_key": API_KEY}
    if route:
        params["filter[route]"] = route
    if stop:
        params["filter[stop]"] = stop

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/vehicles", params=params)
        response.raise_for_status()
        return response.json()

@app.get("/vehicles/{vehicle_id}")
async def get_vehicle(vehicle_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/vehicles/{vehicle_id}?api_key={API_KEY}")
        response.raise_for_status()
        return response.json()
