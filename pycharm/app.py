from fastapi import FastAPI, Depends
import requests
import httpx

API_KEY = "33df77cbf5d4483ab87b3980e0bc913a" # Fill in with your API Key
ENDPOINT_URL = "https://api-v3.mbta.com/" # DO NOT CHANGE THIS

app = FastAPI() # Initialize the end point

@app.get("/") # Create a default route
def read_root():
    return {"message": "Welcome to my FastAPI Application!"}

# Get a list of all routes
@app.get("/routes")
def get_routes():
    routes_list = list()
    response = requests.get(ENDPOINT_URL+f"/routes?&api_key={API_KEY}") # Send a request to the endpoint
    # Convert the response to json and extract the data key
    routes = response.json()["data"]
    for route in routes:
        # Loop through all routes extracting relevant information
        routes_list.append({
            "id": route["id"],
            "type": route["type"],
            "color": route["attributes"]["color"],
            "text_color": route["attributes"]["text_color"],
            "description": route["attributes"]["description"],
            "long_name": route["attributes"]["long_name"],
            "type": route["attributes"]["type"],
        })
    # Return the routes_list in JSON format
    return {"routes": routes_list}

# Get information on a specific route
@app.get("/routes/{route_id}")
def get_route(route_id: str):
    response = requests.get(ENDPOINT_URL + f"/routes/{route_id}?api_key={API_KEY}") # Send a request to the endpoint
    # Convert the response to json and extract the data key
    route_data = response.json()["data"]
    # Extract the relevant data
    route = {
        "id": route_data["id"],
        "type": route_data["type"],
        "color": route_data["attributes"]["color"],
        "text_color": route_data["attributes"]["text_color"],
        "description": route_data["attributes"]["description"],
        "long_name": route_data["attributes"]["long_name"],
        "type": route_data["attributes"]["type"],
    }
    # Return the data to the user
    return {"routes": route}

@app.get("/lines")
def get_lines():
    lines_list = list()
    response = requests.get(ENDPOINT_URL+f"/routes?&api_key={API_KEY}") # Send a request to the endpoint
    # Convert the response to json and extract the data key
    lines = response.json()["data"]
    for line in lines:
        # Loop through all routes extracting relevant information
        lines_list.append({
            "id": line["id"],
            "text_color": line["attributes"]["text_color"],
            "short_name": line["attributes"]["short_name"],
            "long_name": line["attributes"]["long_name"],
            "color": line["attributes"]["color"],
        })
    # Return the routes_list in JSON format
    return {"routes": lines_list}

@app.get("/lines/{line_id}")
def get_line(line_id: str):
    response = requests.get(ENDPOINT_URL + f"/routes/{line_id}?api_key={API_KEY}") # Send a request to the endpoint
    # Convert the response to json and extract the data key
    line_data = response.json()["data"]
    # Extract the relevant data
    route = {
        "id": line_data["id"],
        "text_color": line_data["attributes"]["text_color"],
        "short_name": line_data["attributes"]["short_name"],
        "long_name": line_data["attributes"]["long_name"],
        "color": line_data["attributes"]["color"],
    }
    # Return the data to the user
    return {"line": route}


#--------------------------------------------- Week 4 --------------------------------------------------------
# Dependency to fetch all alerts
async def get_all_alerts(route: str = None, stop: str = None):
    params = {}
    if route:
        params["filter[route]"] = route
    if stop:
        params["filter[stop]"] = stop

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/alerts/", params=params)
        response.raise_for_status()
        return response.json()

# Dependency to fetch a specific alert by ID
async def get_alert_by_id(alert_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/alerts/{alert_id}?api_key={API_KEY}")
        response.raise_for_status()
        return response.json()
@app.get("/alerts")
async def read_alerts(route: str = None, stop: str = None, alerts=Depends(get_all_alerts)):
    return alerts

@app.get("/alerts/{alert_id}")
async def read_alert(alert_id: str, alert=Depends(get_alert_by_id)):
    return alert



# --------------------------- Vehicles ---------------------------------
async def get_all_vehicles(route: str = None, stop: str = None):
    params = {"api_key": API_KEY}
    if route:
        params["filter[route]"] = route
    if stop:
        params["filter[stop]"] = stop

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/vehicles", params=params)
        response.raise_for_status()
        return response.json()

# Dependency to fetch a specific alert by ID
async def get_vehicle_by_id(vehicle_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/vehicles/{vehicle_id}?api_key={API_KEY}")
        response.raise_for_status()
        return response.json()
@app.get("/vehicles")
async def read_vehicles(route: str = None, stop: str = None, vehicles=Depends(get_all_vehicles)):
    return vehicles

@app.get("/vehicles/{vehicle_id}")
async def read_vehicle(vehicle_id: str, vehicle=Depends(get_vehicle_by_id)):
    return vehicle