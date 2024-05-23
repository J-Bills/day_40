from pprint import pprint
import requests

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.destination_endpoint = 'https://api.sheety.co/35a0e869c1dfb499093623a9fe14a4ea/flightDeals/prices'

    def get_destination_data(self):
        response = requests.get(url=self.destination_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{self.destination_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)
