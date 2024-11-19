import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '8fc0995c4b592b0e4fa589cb2880d028'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '7805'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
      response_get = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
      assert response_get.json()['data'][0]['trainer_name'] == 'Артур'

      