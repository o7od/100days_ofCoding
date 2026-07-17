from Sheety import Sheety_api
from IATA_code import city_to_iata
from flights_finder import Flights
from send_information import Sms_sender


### What do we need ###
# 1. Searching existing data from sheety api
# 2. Searching google flights api to get all of the prices from now until 6 months 
# 3. Comparing it with existing data 
# 4. Sending an sms message 


def find_cheapest_flight():
    flight_deals = flight_finder.find_deals()
    cheapest_price = 10000
    for each_flight in flight_deals:
        if cheapest_price > each_flight["price"]:
            cheapest_price = each_flight["price"]
            cheapest_flight = {
                "city": each_flight["name"],
                "price": each_flight["price"],
                "airport_code": each_flight["arrival_airport_code"],
                "outbound_date": each_flight["outbound_date"],
            }
    return cheapest_flight


departure_id = input("Which city are you flying from? ").capitalize()

# Our objects to control sheety api, flight_deals finder and 
data = Sheety_api()
flight_finder = Flights(departing_air=city_to_iata[departure_id])
msg = Sms_sender()

# Once we find the chepeast flight, we post it in our google sheets and send a SMS or whatsapp message
cheap_flight = find_cheapest_flight()
data.post(cheap_flight)
text = f"We found a cheap flight to {cheap_flight['city']} for only ${cheap_flight['price']}. The flight is currently scheduled for {cheap_flight['outbound_date']}"
msg.send_message(text)

