import requests
import os
from dotenv import load_dotenv, find_dotenv
import json

load_dotenv(find_dotenv())

headers = { "X-TBA-Auth-Key": os.environ.get("TBA_API_KEY") }

def tba_events(year: int):
    response = requests.get(f"https://www.thebluealliance.com/api/v3/events/{year}", headers)
    with open(f"events_{year}.json", "wb") as f:
        f.write(response.content)

def tba_matches(event_key: str):
    response = requests.get(f"https://www.thebluealliance.com/api/v3/event/{event_key}/matches", headers)
    with open(f"matches_{event_key}.json", "wb") as f:
        f.write(response.content)

def tba_event_teams(event_key: str):
    response = requests.get(f"https://www.thebluealliance.com/api/v3/event/{event_key}/teams", headers)
    with open(f"event_teams_{event_key}.json", "wb") as f:
        f.write(response.content)

tba_event_teams("2023nyro")