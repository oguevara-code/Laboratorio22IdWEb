import requests

url = "https://pokeapi.co/api/v2/pokemon?limit=10"

response = requests.get(url)

data = response.json()

print("Primeros 10 Pokémon:")
for pokemon in data["results"]:
    print("-", pokemon["name"])