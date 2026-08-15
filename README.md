# Flight Status Tracker

A live flight-tracking dashboard that looks up any aircraft's real-time position, altitude, and speed by callsign, pulling from OpenSky Network's public ADS-B feed.

<img width="623" height="504" alt="image" src="https://github.com/user-attachments/assets/da72fbc0-991e-4baa-b5a1-191e982e315f" />


## What it does
Search any aircraft callsign (e.g.UAL888) to see its live latitude/longitude, altitude, ground speed, and flight status, sourced directly from real-time ADS-B transponder data.


## Stack
FastAPI (backend), Jinja2 (templating), vanilla JS (frontend), OpenSky Network API (live aviation data)

## Run locally
\`\`\`
pip install -r requirements.txt
uvicorn main:app --reload
\`\`\`
Then open `http://127.0.0.1:8000`
