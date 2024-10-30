import requests

TOKEN = 'sdg5sd5g5s5dgs5d5'
SHEET_ENDPOINT = 'https://api.sheety.co/2dca02d4e378c2d952f05b165121bdf3/users/sheet1'
bearer_header = {
                "Authorization":f"Bearer {TOKEN}"
            }


class UserSheet:
    
    def add_user():

        firstname = input("What is your first name ?")
        lastname = input("What is your last name ?")
        emailid = input("What is your email ?")

        new_data = {
            "sheet1":{
                'firstName': firstname,
                'lastName': lastname,
                'email': emailid 
            }
        }

        response = requests.post(url=SHEET_ENDPOINT, headers=bearer_header, json=new_data)

        print('Congrats You are in the Flight Club !!!!')
    
    def get_users():
        response = requests.get(url=SHEET_ENDPOINT, headers=bearer_header)
        data = response.json()['sheet1']
        return data








