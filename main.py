from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Serves the search page itself
@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(request, "index.html")

# Looks up a live flight by callsign (e.g. "NZ102")
@app.get("/flight/{callsign}")
def get_flight(callsign: str):
    callsign = callsign.strip().upper()
    response = requests.get("https://opensky-network.org/api/states/all")
    response.raise_for_status()
    states = response.json().get("states") or []

    # OpenSky returns EVERY live aircraft — loop through to find a matching callsign
    for state in states:
        state_callsign = (state[1] or "").strip().upper()
        if state_callsign == callsign:
            return {
                "callsign": state_callsign,
                "origin_country": state[2],
                "latitude": state[6],
                "longitude": state[5],
                "altitude_m": state[7],
                "velocity_mps": state[9],
                "on_ground": state[8],
            }
    return {"error": "Not found — flight may not be airborne right now"}