# Search algorithm for recommending cars based on user preferences
from car_data import CARS, COUNTRIES, BODY_TYPES, DRIVETRAINS, FUEL_TYPES, TAGS
from car_data import MAKE, MODEL, COUNTRY, BODY, PRICE, DRIVE, FUEL, SEATS, RELIABILITY, TAGS_IDX

def recommend(wanted_tags, coo, body_type, drivetrain, fuel_type, reliability, max_price):
    results = []
    for car in CARS:
        # Filter out cars that don't meet the basic criteria
        # None means the user has no preference for that filter
        if max_price is not None and int(car[PRICE]) > max_price:
            continue
        if reliability is not None and int(car[RELIABILITY]) < reliability:
            continue

        # Add a score based on how many tags and other criteria match
        # (an empty list means no preference, otherwise the car must match one of the choices)
        score = sum(1 for t in wanted_tags if t in car[TAGS_IDX])
        score += 1 if reliability is not None else 0
        score += 1 if max_price is not None else 0
        score += 1 if car[COUNTRY] in coo else 0
        score += 1 if car[BODY] in body_type else 0
        score += 1 if car[DRIVE] in drivetrain else 0
        score += 1 if car[FUEL] in fuel_type else 0

        # Add the car to the results if it has a positive score
        if score > 0:
            results.append((score, car))

    # Sort based on highest scoring car, provide 5 close competitors
    results.sort(reverse=True, key=lambda r: r[0])
    return results[:5]