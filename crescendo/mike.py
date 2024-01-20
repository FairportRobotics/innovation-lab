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

tba_events(2024)