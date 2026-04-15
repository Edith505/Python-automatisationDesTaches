import requests
import os
from dotenv import load_dotenv

def telecharger_donnees():
    #doit être proteger
    load_dotenv()
    cle_api = os.getenv("API_KEY")
    url = "https://api.systeme.interne/v1/export"
    
    en_tetes = {"Authorization": "Bearer " + cle_api}
    reponse = requests.get(url, headers=en_tetes)
    
    if reponse.status_code == 200:
        with open("/var/backups/export.json", "w") as fichier:
            fichier.write(reponse.text)
        print("Exportation terminée.")
    else:
        print("Erreur HTTP :", reponse.status_code)

if __name__ == "__main__":
    telecharger_donnees()
