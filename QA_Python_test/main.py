import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8fc0995c4b592b0e4fa589cb2880d028'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}

body_create = {
        "name": "generate",
        "photo_id": -1
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)
print(response_create.status_code) 

message = response_create.json()['message']
changed_pokemon = response_create.json()['id']
print(message)

name_change = {
    "pokemon_id": changed_pokemon,
    "name": "Котюзер",
    "photo_id": -1
 }

response_create = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = name_change)
print(response_create.text)
print(response_create.status_code)

message = response_create.json()['message']
print(message)


cath = {
     "pokemon_id": changed_pokemon
     }

response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = cath)
print(response_create.text)
print(response_create.status_code)

message = response_create.json()['message']
print(message)