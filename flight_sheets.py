from os import environ
import requests
from dotenv import load_dotenv
load_dotenv("F:\Python Practice\Day 39 - cheap Flight tickets\My Codes\.env")

SHEET_ENDPOINT = 'https://api.sheety.co/2dca02d4e378c2d952f05b165121bdf3/flightDetails/sheet1'
BEARER_TOKEN = 'sd5d5g5sdgsdG5AS'

bearer_header = {
            "Authorization":f"Bearer {BEARER_TOKEN}"
        }

class Sheet:
    def __init__(self):
        self.city_list = []
        self.data = {}
    def get_sheet_data(self):
        response = requests.get(SHEET_ENDPOINT, headers=bearer_header)
        self.data = response.json()['sheet1']
        return self.data

    def get_city_names(self):
        for part in self.data:
            city_name = part['city']
            self.city_list.append(city_name)
        return self.city_list
    
    def update_iata_code(self,code, city):
        for cit in self.data:
            if city == cit['city']:
                new_data = {
                    "sheet1":{
                        "iataCode":code
                    }
                }
                id = cit['id']
                response = requests.put(url=f'{SHEET_ENDPOINT}/{id}', headers=bearer_header, json=new_data)



    







