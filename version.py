# Thanks to atlas academy for this script!
# All credits to atlas
# Github: github.com/atlasacademy
# Website: atlasacademy.io
# Api: api.atlasacademy.io
# Apps: apps.atlasacademy.io

import re
import time
import requests
import json5
import json
import httpx

def get_version(region: str):
    fate_region = "NA"
    endpoint = ""

    if fate_region == "NA":
        endpoint += "https://raw.githubusercontent.com/O-Isaac/FGO-VerCode-extractor/refs/heads/next/na.json"
    else:
        endpoint += "https://raw.githubusercontent.com/O-Isaac/FGO-VerCode-extractor/refs/heads/next/jp.json"

    response = requests.get(endpoint).text
    response_data = json.loads(response)

    return response_data['appVer']
