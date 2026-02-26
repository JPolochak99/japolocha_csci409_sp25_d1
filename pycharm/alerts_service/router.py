from fastapi import APIRouter, Depends, HTTPException
import httpx
from fastapi.security import HTTPBasicCredentials

from security.secure import http_basic, authenticate
from repositories.login_repository import LoginRepository
from database import sess_db

API_KEY = "33df77cbf5d4483ab87b3980e0bc913a"
ENDPOINT_URL = "https://api-v3.mbta.com"

router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"]
)

@router.get("/")
def root():
    return {"service": "Alerts Service"}


@router.get("/alerts")
async def get_alerts(
    route: str = None,
    stop: str = None,
    credentials: HTTPBasicCredentials = Depends(http_basic),
    sess = Depends(sess_db)
):
    loginrepo = LoginRepository(sess)
    account = loginrepo.get_all_login_username(credentials.username)

    if not authenticate(credentials, account):
        raise HTTPException(status_code=400, detail="Incorrect credentials")

    params = {"api_key": API_KEY}
    if route:
        params["filter[route]"] = route
    if stop:
        params["filter[stop]"] = stop

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/alerts", params=params)
        response.raise_for_status()
        return response.json()


@router.get("/alerts/{alert_id}")
async def get_alert(
    alert_id: str,
    credentials: HTTPBasicCredentials = Depends(http_basic),
    sess = Depends(sess_db)
):
    loginrepo = LoginRepository(sess)
    account = loginrepo.get_all_login_username(credentials.username)

    if not authenticate(credentials, account):
        raise HTTPException(status_code=400, detail="Incorrect credentials")

    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/alerts/{alert_id}?api_key={API_KEY}")
        response.raise_for_status()
        return response.json()