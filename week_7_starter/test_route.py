from fastapi.testclient import TestClient
from requests.auth import HTTPBasicAuth

import app

client = TestClient(app.app)

auth = HTTPBasicAuth('admin', 'password123') # Create a HTTPBasicAuth login
bad_auth = HTTPBasicAuth('admin', 'badpassword')

# test unauthorized route
def test_read_main_route_unauthorized_nologin():
    response = client.get("/routes")
    assert response.status_code == 401 # Check for unauthorized status code

# Test unauthorized route
def test_read_main_route_unauthorized_bad_credentials():
    response = client.get("/routes", auth=bad_auth)
    assert response.status_code == 401 # check for unauthorized status code

# Test unauthorized route
def test_read_main_route_authorized():
    response = client.get("/routes", auth=auth)
    assert response.status_code == 200 # check for authorized status code

def test_read_route_content():
    response = client.get("/routes/Red", auth=auth)
    route = response.json().get("route") # Fetch route details from json response
    assert response.status_code == 200 #check status code is 200 ok

    #verify route details
    assert route.get("id") == 'Red'
    assert route.get("type") == 1
    assert route.get("color") == 'DA291C'
    assert route.get("text_color") == 'FFFFFF'
    assert route.get("description") == 'Rapid Transit'
    assert route.get("long_name") == 'Red Line'

def test_read_route_not_found():
    route_id = "Chauncey"
    response = client.get(f"/routes/{route_id}", auth=auth)
    assert response.status_code == 404
    print(response.json())
    assert response.json().get("message") == f"Route {route_id} not found"



# ------------------- Lines -----------------------
def test_read_main_lines_unauthorized_nologin():
    response = client.get("/lines")
    assert response.status_code == 401 # Check for unauthorized status code

# Test unauthorized route
def test_read_main_lines_unauthorized_bad_credentials():
    response = client.get("/lines", auth=bad_auth)
    assert response.status_code == 401 # check for unauthorized status code

# Test unauthorized route
def test_read_main_lines_authorized():
    response = client.get("/lines", auth=auth)
    assert response.status_code == 200 # check for authorized status code

def test_read_lines_content():
    response = client.get("/lines/Red", auth=auth)
    route = response.json().get("line") # Fetch route details from json response
    assert response.status_code == 200 #check status code is 200 ok

    #verify route details
    assert route.get("id") == 'Red'
    assert route.get("type") == 1
    assert route.get("color") == 'DA291C'
    assert route.get("text_color") == 'FFFFFF'
    assert route.get("description") == 'Rapid Transit'
    assert route.get("long_name") == 'Red Line'

def test_read_line_not_found():
    line_id = "Chauncey"
    response = client.get(f"/lines/{line_id}", auth=auth)
    assert response.status_code == 404
    print(response.json())
    assert response.json().get("message") == f"Line {line_id} not found"


# ------------------------- Vehicles ------------------------
def test_read_main_vehicles_unauthorized_nologin():
    response = client.get("/vehicles")
    assert response.status_code == 401 # Check for unauthorized status code

# Test unauthorized route
def test_read_main_vehicles_unauthorized_bad_credentials():
    response = client.get("/vehicles", auth=bad_auth)
    assert response.status_code == 401 # check for unauthorized status code

# Test unauthorized route
def test_read_main_vehicles_authorized():
    response = client.get("/vehicles", auth=auth)
    assert response.status_code == 200 # check for authorized status code

def test_read_vehicles_content():
    response = client.get("/vehicles/Red", auth=auth)
    route = response.json().get("vehicle") # Fetch route details from json response
    assert response.status_code == 200 #check status code is 200 ok

    #verify route details
    assert route.get("id") == 'Red'
    assert route.get("type") == 1
    assert route.get("color") == 'DA291C'
    assert route.get("text_color") == 'FFFFFF'
    assert route.get("description") == 'Rapid Transit'
    assert route.get("long_name") == 'Red Line'

def test_read_route_not_found():
    vehicle_id = "Chauncey"
    response = client.get(f"/vehicle/{vehicle_id}", auth=auth)
    assert response.status_code == 404
    print(response.json())
    assert response.json().get("message") == f"Vehicle {vehicle_id} not found"


# ------------- Alerts ------------------
def test_read_alerts_content():
    response = client.get("/alerts/Red", auth=auth)
    route = response.json().get("alerts") # Fetch route details from json response
    assert response.status_code == 200 #check status code is 200 ok

    #verify route details
    assert route.get("id") == 'Red'
    assert route.get("type") == 1
    assert route.get("color") == 'DA291C'
    assert route.get("text_color") == 'FFFFFF'
    assert route.get("description") == 'Rapid Transit'
    assert route.get("long_name") == 'Red Line'

def test_read_route_not_found():
    alert_id = "Chauncey"
    response = client.get(f"/vehicle/{alert_id}", auth=auth)
    assert response.status_code == 404
    print(response.json())
    assert response.json().get("message") == f"Alert {alert_id} not found"