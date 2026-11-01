# Import the car data from the car_data.py file
from car_data import CARS, COUNTRIES, BODY_TYPES, DRIVETRAINS, FUEL_TYPES, TAGS
from car_data import MAKE, MODEL, COUNTRY, BODY, PRICE, DRIVE, FUEL, SEATS, RELIABILITY, TAGS_IDX
from search_algorithm import recommend

# Start out with a simple command-line interface for the user to input their preferences]
print("Welcome to Carmendation!\nThe car reccomendation site made by a car enthusiast!\nLet's find the perfect car for you based on your preferences.")
start = input("Press Enter to start the car recommendation process...")
print("Starting the car recommendation process...")

# Get user preferences
price_range = input("On a scale of 1-5, how much are you willing to spend on a car? (1 = $0-$10k, 2 = $10k-$20k, 3 = $20k-$30k, 4 = $30k-$50k, 5 = $50k+)\nINPUT THE NUMBER: ")
reliability = input("On a scale of 1-5, how important is reliability to you? (1 = not important, 5 = very important)\nINPUT THE NUMBER: ")
body_type = input(f"What body type do you prefer? {BODY_TYPES}\nINPUT THE BODY TYPE: ")
drivetrain = input(f"What drivetrain do you prefer? {DRIVETRAINS}\nINPUT THE DRIVETRAIN: ")
fuel_type = input(f"What fuel type do you prefer? {FUEL_TYPES}\nINPUT THE FUEL TYPE: ")
country_of_origin = input(f"What country of origin do you prefer? {COUNTRIES}\nINPUT THE COUNTRY: ")
wanted_tags = input(f"What tags do you want in your car? (e.g., 'sporty', 'family', 'luxury', 'fast', 'reliable', 'cheap-to-maintain')\nINPUT THE TAGS (comma-separated): ").split(',')


# Recommend to user a car based on their preferences
recommended_cars = recommend(
    wanted_tags=wanted_tags,
    coo=country_of_origin,
    body_type=body_type,
    drivetrain=drivetrain,
    fuel_type=fuel_type,
    reliability=int(reliability),
    max_price=int(price_range),
)

print("\nBased on your preferences, we recommend the following cars:")
for score, car in recommended_cars:
    print(f"{car[MAKE]} {car[MODEL]} - ${car[PRICE]} - Reliability: {car[RELIABILITY]} - Tags: {', '.join(car[TAGS_IDX])}")