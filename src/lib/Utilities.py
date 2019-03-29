import os
import json

def getBaseName(team_name):
    partial = {
        "mumbai":"mumbai-indians",
        "Mumbai":"mumbai-indians",
        "hyderabad":"sunrisers-hyderabad",
        "Hyderabad":"sunrisers-hyderabad"
    }
    exact = {
        "MI": "mumbai-indians",
        "SRH": "sunrisers-hyderabad"
    }
    for key in exact.keys():
        if team_name == key:
            return exact[key]
    for key in partial.keys():
        if key in team_name:
            return partial[key]

def getSquad(team_name):
    folder = "../../web-data/squads/"
    squad_files = []
    for (dirpath, dirnames, filenames) in os.walk(folder):
        squad_files = filenames
    squad = [x for x in squad_files if team_name in x][0]
    with open(folder+squad) as f:
        squad = json.load(f)
    squad = squad["stats"]["content"]
    return squad
