# Search algorithm for recommending cars based on user preferences
from car_data import CARS, COUNTRIES, BODY_TYPES, DRIVETRAINS, FUEL_TYPES, TAGS
from car_data import MAKE, MODEL, COUNTRY, BODY, PRICE, DRIVE, FUEL, SEATS, RELIABILITY, TAGS_IDX

def recommend(wanted_tags, coo, body_type, drivetrain, fuel_type, reliability, max_price):
    results = []
    for car in CARS:
        # Filter out cars that don't meet the basic criteria
        if int(car[PRICE]) > max_price:
            continue
        if int(car[RELIABILITY]) < reliability:
            continue

        # Add a score based on how many tags and other criteria match
        score = sum(1 for t in wanted_tags if t in car[TAGS_IDX])
        score += 1 if int(car[RELIABILITY]) >= reliability else 0
        score += 1 if int(car[PRICE]) <= max_price else 0
        score += 1 if car[COUNTRY] == coo else 0
        score += 1 if car[BODY] == body_type else 0
        score += 1 if car[DRIVE] == drivetrain else 0
        score += 1 if car[FUEL] == fuel_type else 0

        # Add the car to the results if it has a positive score
        if score > 0:
            results.append((score, car))

    # Sort based on highest scoring car, provide 5 close competitors
    results.sort(reverse=True, key=lambda r: r[0])
    return results[:5]