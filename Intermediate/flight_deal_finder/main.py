from data_manager import DataManager
from IATA_code import city_to_iata
from flights_finder import Flights
from flight_data import find_cheapest_flight
from send_information import NotificationManager
from pprint import pprint
import requests_cache
from datetime import datetime, timedelta

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

################## searches for direct flights ##################
def get_direct_flights():
    flights = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_CODE,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_now,
    )
    return flights

################## searches for indirect flights ##################
def get_indirect_flights():
    flights = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_CODE,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_now,
        is_direct=False,
    )
    return flights


################# Talk to Sheety #################
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
pprint(sheet_data)


############### Getting customer emails ###############
user_data = data_manager.get_customer_emails()
customer_emails = [user['whatIsYourEmail?'] for user in user_data]


################# Set the Dates #################
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_now = datetime.now() + timedelta(days=(30*6))

################# Do a FLIGHT SEARCH #################
flight_search = Flights()
ORIGIN_CITY_CODE = "JFK"

################# SEARCHING ALL DESTINATIONS #################
for destination in sheet_data:
    pprint(f"Getting direct flights for {destination['city']}...")
    direct_flights = get_direct_flights()
    ##################### Showing the cheapest flight #####################
    cheapest_flight = find_cheapest_flight(direct_flights, return_date=six_months_from_now.strftime("%Y-%m-%d"))

    ##################### 
    if cheapest_flight.price == "N/A": 
        pprint(f"No direct flight to {destination["city"]}. Looking for indirect flights...")
        indirect_flights = get_indirect_flights()
        cheapest_flight = find_cheapest_flight(indirect_flights, return_date=six_months_from_now.strftime("%Y-%m-%d"))
        pprint(f"{destination["city"]}: USD {cheapest_flight.price} for indirect flight")

    pprint(f"{destination["city"]}: USD {cheapest_flight.price} for direct flight")


    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        pprint(f"Lower price flight found to {destination["city"]}!")
        data_manager.update_lowest_price(new_price=cheapest_flight.price, object_id=destination["id"])

        ################### Sending an SMS message ###################
        # NotificationManager().send_message(
        #     message=f"Low Price Alert! Only USD {cheapest_flight.price} to fly "
        #             f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
        #             f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        # )
        ################### Sending an EMAIL message ###################
        message = f"Low Price Alert! Only ${cheapest_flight.price} to fly from {destination['city']} "\
                f"to {cheapest_flight.destination_airport}, with {cheapest_flight.stops} stop(s) departing on "\
                f"{cheapest_flight.out_date} and returning on {cheapest_flight.return_date}." 
        
        NotificationManager().send_emails(message=message, customer_emails=customer_emails)
