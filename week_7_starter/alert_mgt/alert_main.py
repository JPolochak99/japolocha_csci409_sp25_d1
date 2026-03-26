from fastapi import FastAPI, Depends
import httpx
from configuration.config import ServerSettings
from security.auth import authenticate
from configuration.config import Message
from fastapi.responses import JSONResponse

alert_app = FastAPI()

def build_server_config():
    return ServerSettings()

# Dependency to fetch all alerts
async def get_all_alerts(route: str = None, stop: str = None, sconfig:ServerSettings = Depends(build_server_config)):
    params = {}
    if route:
        params["filter[route]"] = route
    if stop:
        params["filter[stop]"] = stop

    async with httpx.AsyncClient() as client: # Define client
        response = await client.get(f"{sconfig.endpoint}/alerts?api_key={sconfig.api_key}", params=params)
        response.raise_for_status()

        if response.status_code == 400:
            return JSONResponse(status_code=400, content={"message": f"Bad Request"}) # Return Error for a 400 response code
        elif response.status_code == 403:
            return JSONResponse(status_code=403, content={"message": f"API Request Forbidden"}) # Return Error for a 403 response code
        elif response.status_code == 429:
            return JSONResponse(status_code=429, content={"message": f"Too Many Requests"}) # Return Error for a 429 response code

        return response.json()

async def get_alert_by_id(alert_id:str, sconfig:ServerSettings = Depends(build_server_config)):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{sconfig.endpoint}/alerts/{alert_id}?api_key={sconfig.api_key}")
        response.raise_for_status()

        if response.status_code == 400:
            return JSONResponse(status_code=400, content={"message": f"Bad Request"})
        elif response.status_code == 403:
            return JSONResponse(status_code=403, content={"message": f"API Request Forbidden"})
        elif response.status_code == 404:
            return JSONResponse(status_code=404, content={"message": f"Route {alert_id} not found"})
        elif response.status_code == 406:
            return JSONResponse(status_code=406, content={"message": f"Not Acceptable"})
        elif response.status_code == 429:
            return JSONResponse(status_code=429, content={"message": f"Too Many Requests"})
        return response.json()

@alert_app.get("/", 
               responses= {400: {"model": Message}, # Display 400 response code in Docs
                           403: {"model": Message}, # Display 403 response code in Docs
                           429: {"model": Message}, # Display 429 response code in Docs
                           })

async def read_alerts(alerts=Depends(get_all_alerts), user: dict = Depends(authenticate)):
    return alerts

@alert_app.get("/{alert_id}", 
               responses = {400: {"model": Message}, #Display 400 response code in Docs
                            403: {"model": Message}, #Display 403 response code in Docs
                            404: {"model": Message}, #Display 404 response code in Docs
                            406: {"model": Message}, #Display 406 response code in Docs
                            429: {"model": Message}, #Display 429 response code in Docs
               })
async def read_alert(alert_id:str, alert=Depends(get_alert_by_id), user: dict = Depends(authenticate)):
    return alert