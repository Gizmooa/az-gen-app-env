import json

def write_appsettings_json(data: dict, path: str = "appsettings.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
