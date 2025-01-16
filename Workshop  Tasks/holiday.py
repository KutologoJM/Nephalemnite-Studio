"""
Name: holiday.py
hard_coded values:
    price_per_night = 800
    daily_rental_cost = 500


tasks: calculate plane cost, hotel cost, car rental cost

user inputs:
    city_flight: city they will fly to
    num_nights: number of nights staying in hotel
    rental_days: number of days car will be rented for

functions:
    hotel_cost: arg(num_nights) returns hotel cost
    plane_cost: arg(city_flights) returns flight cost
        (hint: use if-elif-else statements in
        the function to retrieve a price based on the chosen city).
    car_rental_cost: arg(rental_days) returns total car rental cost
    holiday_cost: args(hotel_cost; plane_cost; car_rental)
        objective: return total cost of holiday through calling previous functions

secondary task:
    print out details in a readable format
    error handling
"""

available_destinations = ["Usa", "China", "Europe", "Japan"]

print("""Hello, what city would you like to fly to?
• USA
• China
• Europe
• Japan""")
while True:
    city_flight = input("Destination: ").capitalize()
    if city_flight in available_destinations:
        break
    else:
        print("Please choose from the given options")
        continue

while True:
    try:
        num_nights = int(input("How many nights will you be staying at the hotel?\n"))
    except ValueError:
        print("Please enter a number")
    else:
        break
while True:
    try:
        rental_days = int(input("Lastly how many days will you be renting a car for?\n"))
    except ValueError:
        print("Please enter a number")
    else:
        break


def hotel_cost():
    price_per_night = 800
    total_hotel_cost = num_nights * price_per_night
    return total_hotel_cost


def plane_cost():
    total_plane_cost = 0
    if city_flight == "Usa":
        total_plane_cost = 18000
    elif city_flight == "China":
        total_plane_cost = 11100
    elif city_flight == "Europe":
        total_plane_cost = 9000
    elif city_flight == "Japan":
        total_plane_cost = 9000
    return total_plane_cost


def car_rental_cost():
    daily_rental_cost = 500
    total_rental_cost = rental_days * daily_rental_cost
    return total_rental_cost


def holiday_cost():
    total_hotel_cost = hotel_cost()
    total_plane_cost = plane_cost()
    total_rental_cost = car_rental_cost()

    total_holiday_cost = total_hotel_cost + total_plane_cost + total_rental_cost
    print(f"\n'Itinerary'\n"
          f"Destination: {city_flight}\n"
          f"Hotel rental period: {num_nights} days. Hotel cost: R{total_hotel_cost}\n"
          f"Car rental period: {rental_days} days. Rental cost: R{total_rental_cost}\n"
          f"All in all your holiday will cost R{total_holiday_cost}.")


holiday_cost()
