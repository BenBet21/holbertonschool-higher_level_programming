#!/usr/bin/env python3
from urllib.parse import urlparse

url = input("Entrez une URL : ")
parsed_url = urlparse(url)
port = parsed_url.port

print(f"Le numéro de port est : {port}")

protocole = parsed_url.scheme
nom_domaine = parsed_url.hostname
port = parsed_url.port
chemin = parsed_url.path

# Afficher les résultats
print(f"Protocole : {protocole}")
print(f"Nom de domaine : {nom_domaine}")
if port:
    print(f"Port : {port}")
else:
    print("Port : non spécifié, utilise le port par défaut")
print(f"Chemin : {chemin}")