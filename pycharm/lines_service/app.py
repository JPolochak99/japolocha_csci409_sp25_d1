from fastapi import FastAPI
import requests

API_KEY = "33df77cbf5d4483ab87b3980e0bc913a"
ENDPOINT_URL = "https://api-v3.mbta.com"

app = FastAPI(title="Lines Service")

@app.get("/")
def root():
    return {"service": "Lines Service"}

@app.get("/lines")
def get_lines():
    lines_list = []
    response = requests.get(f"{ENDPOINT_URL}/routes?api_key={API_KEY}")
    lines = response.json()["data"]

    for line in lines:
        lines_list.append({
            "id": line["id"],
            "short_name": line["attributes"]["short_name"],
            "long_name": line["attributes"]["long_name"],
            "color": line["attributes"]["color"],
            "text_color": line["attributes"]["text_color"],
        })

    return {"lines": lines_list}

@app.get("/lines/{line_id}")
def get_line(line_id: str):
    response = requests.get(f"{ENDPOINT_URL}/routes/{line_id}?api_key={API_KEY}")
    line_data = response.json()["data"]

    return {
        "id": line_data["id"],
        "short_name": line_data["attributes"]["short_name"],
        "long_name": line_data["attributes"]["long_name"],
        "color": line_data["attributes"]["color"],
        "text_color": line_data["attributes"]["text_color"],
    }
