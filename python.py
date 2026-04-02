import requests
from datetime import datetime

now = datetime.now()

resultat = ""

response = requests.get("https://www.cegeplimoilou.ca", timeout=5)

if response.status_code == 200:
    resultat = f"[{now}] OK - Site actif"
else:
    resultat = f"[{now}] - Site inactif (code {response.status_code})"


with open("data.txt", "a") as file:
    file.write(resultat + "\n")