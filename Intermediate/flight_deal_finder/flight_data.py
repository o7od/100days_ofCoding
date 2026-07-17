

class FlightData:
    def __init__(self, price, departing_air, arrival_air, outdate, return_date):
        self.price = price
        self.origin_airport = departing_air
        self.destination_airport = arrival_air
        self.out_date = outdate
        self.return_date = return_date


def find_cheapest_flight(data, return_date):
    if data is None or (not data.get("best_flights") and not data.get("other_flights")):
        print("No flight data")
        return FlightData("N/A", "N/A", "N/A", "N/A", "N/A")
    
    all_flights = data.get("best_flights", []) + data.get("other_flights", [])

    # Data from the first flight on the list
    first_flight = all_flights[0]
    lowest_price = first_flight["price"]
    origin = first_flight["flights"][0]["departure_airport"]["id"]
    destination = first_flight["flights"][-1]["arrival_airport"]["id"]
    out_date = first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]

    # Initalizing FlightData with the first flight for comparison
    cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)

    for flight in all_flights:
        try:
            price = flight["price"]
        except KeyError:
            print("--- No price available for flight. ---")
            continue
        if price < lowest_price: 
            lowest_price = price
            origin = first_flight["flights"][0]["departure_airport"]["id"]
            destination = first_flight["flights"][-1]["arrival_airport"]["id"]
            out_date = first_flight["flights"][0]["departure_airport"]["time"].split(" ")[0]
            cheapest_flight = FlightData(lowest_price, origin, destination, out_date, return_date)
            print(f"Lowest price to {destination} is USD {lowest_price}")
        
    return cheapest_flight

