import requests

class Sheety:

    def __init__(self):
        self.user_endpoint = 'https://api.sheety.co/35a0e869c1dfb499093623a9fe14a4ea/flightDeals/users'
        self.users_data = {}

    def get_user_data(self):
        response = requests.get(url=self.user_endpoint)
        data = response.json()
        self.users_data = data
        return self.users_data

    def add_user_info(self, firstname, lastname, email):        
        new_data = {
            "user": {
                "firstName": firstname,
                "lastName": lastname,
                "email": email
            }
        }
        response = requests.post(url=f"{self.user_endpoint}", json=new_data)
        
        print(response.text)