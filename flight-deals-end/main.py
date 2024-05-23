from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
#from notification_manager import NotificationManager
from sheety import Sheety
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
#notification_manager = NotificationManager()
users = Sheety()
users.get_user_data()

ORIGIN_CITY_IATA = "LON"
def main():
    print('Welcome to Jamal\'s Flight Club')
    print('We find the best flight deals and email you.')
    user_first_name = input('What is your first name?\n').lower()
    user_last_name = input('What is your last name?\n').lower()
    user_email = input('What is your email?\n').lower()
    user_email2 = input('Type your email again\n').lower()

    while user_email != user_email2:
        print('Your emails did not match. Input again:\n')
        user_email = input('What is your email?\n')
        user_email2 = input('Type your email again\n')


    for acc in users.users_data.values():
        if user_email != acc[0]['email']:
            users.add_user_info(user_first_name, user_last_name, user_email)
        else:
            print("That user already exists")



    # if sheet_data[0]["iataCode"] == "":
    #     for row in sheet_data:
    #         row["iataCode"] = flight_search.get_destination_code(row["city"])
    #     data_manager.destination_data = sheet_data
    #     data_manager.update_destination_codes()

    # tomorrow = datetime.now() + timedelta(days=1)
    # six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

    # for destination in sheet_data:
    #     flight = flight_search.check_flights(
    #         ORIGIN_CITY_IATA,
    #         destination["iataCode"],
    #         from_time=tomorrow,
    #         to_time=six_month_from_today
    #     )
    #     if flight.price < destination["lowestPrice"]:
    #         notification_manager.send_sms(
    #             message=f"Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
    #         )
