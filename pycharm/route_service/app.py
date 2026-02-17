from fastapi import FastAPI
import requests

API_KEY = "33df77cbf5d4483ab87b3980e0bc913a"
ENDPOINT_URL = "https://api-v3.mbta.com"

app = FastAPI(title="Routes Service")

@app.get("/")
def root():
    return {"service": "Routes Service"}

@app.get("/routes")
def get_routes():
    routes_list = []
    response = requests.get(f"{ENDPOINT_URL}/routes?api_key={API_KEY}")
    routes = response.json()["data"]

    for route in routes:
        routes_list.append({
            "id": route["id"],
            "type": route["attributes"]["type"],
            "color": route["attributes"]["color"],
            "text_color": route["attributes"]["text_color"],
            "description": route["attributes"]["description"],
            "long_name": route["attributes"]["long_name"],
        })

    return {"routes": routes_list}

@app.get("/routes/{route_id}")
def get_route(route_id: str):
    response = requests.get(f"{ENDPOINT_URL}/routes/{route_id}?api_key={API_KEY}")
    route_data = response.json()["data"]

    return {
        "id": route_data["id"],
        "type": route_data["attributes"]["type"],
        "color": route_data["attributes"]["color"],
        "text_color": route_data["attributes"]["text_color"],
        "description": route_data["attributes"]["description"],
        "long_name": route_data["attributes"]["long_name"],
    }
