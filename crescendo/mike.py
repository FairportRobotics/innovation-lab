import requests
import os
from dotenv import load_dotenv, find_dotenv
import json
import csv

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

def wrangle_match_json(j):
    match_data = {}

    for k,v in j.items():
        if isinstance(v, dict):
            for k2, v2 in v.items():
                match_data[k+"_"+k2] = v2
        else:
            match_data[k] = v
        
    #print(match_data)

    with open('boss.csv','w', newline='') as f:
        w = csv.writer(f)
        w.writerow(match_data.keys())
        w.writerow(match_data.values())
    return None

f = open('boss.json')
data = json.load(f)
f.close()

wrangle_match_json(data)