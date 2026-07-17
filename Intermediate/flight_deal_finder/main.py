from data_manager import DataManager
from IATA_code import city_to_iata
from flights_finder import Flights
from flight_data import find_cheapest_flight
from send_information import Sms_sender
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

################# Talk to Sheety #################
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
pprint(sheet_data)

################# Set the Dates #################
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_now = datetime.now() + timedelta(days=(30*6))

################# Do a FLIGHT SEARCH #################
flight_search = Flights()
ORIGIN_CITY_CODE = "JFK"

################# SEARCHING ALL DESTINATIONS #################
for destination in sheet_data:
    pprint(f"Getting flights for {destination['city']}...")
    flights = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_CODE,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_now,
    )

    ##################### Showing the cheapest flight #####################
    cheapest_flight = find_cheapest_flight(flights, return_date=six_months_from_now.strftime("%Y-%m-%d"))
    pprint(f"{destination["city"]}: USD {cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        pprint(f"Lower price flight found to {destination["city"]}!")
        data_manager.update_lowest_price(new_price=cheapest_flight.price, object_id=destination["id"])

        ################### Sending an SMS message ###################
        Sms_sender().send_message(
            message=f"Low Price Alert! Only USD {cheapest_flight.price} to fly "
                    f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, "
                    f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        )
