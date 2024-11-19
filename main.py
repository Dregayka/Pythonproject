import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '5ad415c0fc9867c314203ae9251e9bfc'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_pokemons = {
    "name": "generate",
    "photo_id": -1
}
response = requests.post(url = f'{URL}/pokemons', headers= HEADER, json= body_pokemons)
print(response.text)
pokemons_id = response.json()['id']
print(pokemons_id)


body_change = {
    "pokemon_id": pokemons_id ,
    "name": 'Pika',
    "photo_id": 2
}
response_change = requests.put(url = f'{URL}/pokemons', headers= HEADER, json= body_change)
print(response_change.text)


body_in_pokeball = {
    "pokemon_id": pokemons_id
}
response_in_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers= HEADER, json= body_in_pokeball)
print(response_in_pokeball.text)