import json
import subprocess
from time import sleep
import requests

with open("config.json", "r") as file:
    config = json.load(file)

cooldown = config["cooldown"]
url = config["request_url"]

def check_connection():
    try:
        response = requests.get(url, timeout=config["request_timeout"])
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False

while True:
    if check_connection():
        subprocess.run(config["run"])
        quit()
    sleep(cooldown)
