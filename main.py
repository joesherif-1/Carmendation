# Import the car data from the car_data.py file
from car_data import CARS, COUNTRIES, BODY_TYPES, DRIVETRAINS, FUEL_TYPES, TAGS
from car_data import MAKE, MODEL, COUNTRY, BODY, PRICE, DRIVE, FUEL, SEATS, RELIABILITY, TAGS_IDX
from search_algorithm import recommend

# Start out with a simple command-line interface for the user to input their preferences
print("Welcome to Carmendation!\nThe car recommendation site made by a car enthusiast!\nLet's find the perfect car for you based on your preferences.")
input("Press Enter to start the car recommendation process...")
print("Starting the car recommendation process...")

# Get user preferences
def get_user_preferences():
    price_range = input("On a scale of 1-5, how much are you willing to spend on a car? (1 = $0-$10k, 2 = $10k-$20k, 3 = $20k-$30k, 4 = $30k-$50k, 5 = $50k+) or press enter if you have no preference\nINPUT THE NUMBER: ")
    while price_range not in ['1', '2', '3', '4', '5'] and price_range != "":
        print("Invalid input. Please enter a number between 1 and 5.")
        price_range = input("On a scale of 1-5, how much are you willing to spend on a car? (1 = $0-$10k, 2 = $10k-$20k, 3 = $20k-$30k, 4 = $30k-$50k, 5 = $50k+) or press enter if you have no preference\nINPUT THE NUMBER: ")

    reliability = input("On a scale of 1-5, how important is reliability to you? (1 = not important, 5 = very important) or press enter if you have no preference\nINPUT THE NUMBER: ")
    while reliability not in ['1', '2', '3', '4', '5'] and reliability != "":
        print("Invalid input. Please enter a number between 1 and 5.")
        reliability = input("On a scale of 1-5, how important is reliability to you? (1 = not important, 5 = very important) or press enter if you have no preference\nINPUT THE NUMBER: ")

    valid_body_types = [body.lower() for body in BODY_TYPES]
    while True:
        raw_body_type = input(f"What body type do you prefer? {BODY_TYPES}\n Seperate by commas if you have multiple preferences\n or press enter if you have no preference\nINPUT THE BODY TYPE: ")
        body_type = [bt.strip() for bt in raw_body_type.split(',') if bt.strip()]
        if not body_type:
            print("No body type entered. Proceeding without any specific body type preference.")
            break
        if all(bt in valid_body_types for bt in body_type):
            break
        print("Invalid input. Please choose a body type from the list.")

    valid_drivetrains = [drivetrain.lower() for drivetrain in DRIVETRAINS]
    while True:
        raw_drivetrain = input(f"What drivetrain do you prefer? {DRIVETRAINS}\n Seperate by commas if you have multiple preferences\n or press enter if you have no preference\nINPUT THE DRIVETRAIN: ")
        drivetrain = [dt.strip() for dt in raw_drivetrain.split(',') if dt.strip()]
        if not drivetrain:
            print("No drivetrain entered. Proceeding without any specific drivetrain preference.")
            break
        if all(dt in valid_drivetrains for dt in drivetrain):
            break
        print("Invalid input. Please choose a drivetrain from the list.")

    valid_fuel_types = [fuel.lower() for fuel in FUEL_TYPES]
    while True:
        raw_fuel_type = input(f"What fuel type do you prefer? {FUEL_TYPES}\n Seperate by commas if you have multiple preferences\n or press enter if you have no preference\nINPUT THE FUEL TYPE: ")
        fuel_type = [ft.strip() for ft in raw_fuel_type.split(',') if ft.strip()]
        if not fuel_type:
            print("No fuel type entered. Proceeding without any specific fuel type preference.")
            break
        if all(ft in valid_fuel_types for ft in fuel_type):
            break
        print("Invalid input. Please choose a fuel type from the list.")

    valid_countries = [country.lower() for country in COUNTRIES]
    while True:
        raw_country = input(f"What country of origin do you prefer? {COUNTRIES}\n Seperate by commas if you have multiple preferences\n or press enter if you have no preference\nINPUT THE COUNTRY: ")
        country_of_origin = [co.strip() for co in raw_country.split(',') if co.strip()]
        if not country_of_origin:
            print("No country of origin entered. Proceeding without any specific country preference.")
            break
        if all(co in valid_countries for co in country_of_origin):
            break
        print("Invalid input. Please choose a country from the list.")

    valid_tags = [tag.lower() for tag in TAGS]
    while True:
        raw_tags = input(f"What tags do you want in your car? {TAGS}\nINPUT THE TAGS (comma-separated, or press Enter for none): ")
        wanted_tags = [t.strip().lower() for t in raw_tags.split(',') if t.strip()]
        if not wanted_tags:
            print("No tags entered. Proceeding without any specific tags.")
            break
        if all(t in valid_tags for t in wanted_tags):
            break
        print("Invalid input. Please choose tags from the list.")
    return price_range, reliability, body_type, drivetrain, fuel_type, country_of_origin, wanted_tags

# Recommend to user a car based on their preferences
price_range, reliability, body_type, drivetrain, fuel_type, country_of_origin, wanted_tags = get_user_preferences()
recommended_cars = recommend(
    wanted_tags=wanted_tags,
    coo=country_of_origin,
    body_type=body_type,
    drivetrain=drivetrain,
    fuel_type=fuel_type,
    reliability=int(reliability) if reliability else None,
    max_price=int(price_range) if price_range else None,
)

formatted_price = {
    1: "$0-$10k",
    2: "$10k-$20k",
    3: "$20k-$30k",
    4: "$30k-$50k",
    5: "$50k+"
}

if not recommended_cars:
    print("\nSorry, no cars matched your preferences. Try loosening some of them.")
else:
    print("\nBased on your preferences, we recommend the following cars:")
for _, car in recommended_cars:
    print(f"{car[MAKE]} {car[MODEL]} - {formatted_price.get(int(car[PRICE]), car[PRICE])} - Reliability: {car[RELIABILITY]} - Tags: {', '.join(car[TAGS_IDX])}")