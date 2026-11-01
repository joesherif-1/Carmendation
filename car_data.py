# ---------------------------------------------------------------
# car_data.py
# ---------------------------------------------------------------
# Each car is a list in this order:
#   0 make   1 model   2 country   3 body_type   4 price_tier
#   5 drivetrain   6 fuel   7 seats   8 reliability   9 tags (list)
#
# price_tier (rough cost of a decent recent used example, USD):
#   1 = under ~$12k    2 = $12-25k    3 = $25-45k
#   4 = $45-80k        5 = $80k+
# reliability: 1 (temperamental) to 5 (bulletproof)
# ---------------------------------------------------------------

FIELDS = ["make", "model", "country", "body_type", "price_tier",
          "drivetrain", "fuel", "seats", "reliability", "tags"]

MAKE, MODEL, COUNTRY, BODY, PRICE, DRIVE, FUEL, SEATS, RELIABILITY, TAGS_IDX = range(10)

COUNTRIES = ["USA", "UK", "Germany", "Italy", "Japan", "South Korea"]

BODY_TYPES = ["Sedan", "Coupe", "Hatchback", "Convertible", "SUV", "Truck", "Wagon"]

DRIVETRAINS = ["FWD", "RWD", "AWD", "4WD"]

FUEL_TYPES = ["Gas", "Hybrid", "Electric"]

TAGS = [
    "first-car", "project-car", "daily-driver", "reliable", "cheap-to-maintain",
    "fuel-efficient", "fun-to-drive", "sporty", "fast", "supercar", "track-ready",
    "drift-friendly", "tuner-friendly", "lightweight", "luxury", "comfortable",
    "family", "spacious", "off-road", "towing", "rugged", "compact", "electric",
    "hybrid", "manual-available", "v8", "turbo", "rotary", "collector", "status",
    "classic-style", "tech-heavy", "expensive-to-maintain",
]

CARS = [
    # ========================= USA =========================
    ["Ford", "Mustang GT", "USA", "Coupe", 3, "RWD", "Gas", 4, 3, ["fun-to-drive", "sporty", "fast", "v8", "manual-available", "tuner-friendly", "project-car", "classic-style"]],
    ["Ford", "F-150", "USA", "Truck", 3, "4WD", "Gas", 5, 3, ["towing", "rugged", "spacious", "family", "daily-driver"]],
    ["Ford", "Focus ST", "USA", "Hatchback", 2, "FWD", "Gas", 5, 3, ["fun-to-drive", "turbo", "manual-available", "tuner-friendly", "first-car", "sporty"]],
    ["Ford", "Fiesta ST", "USA", "Hatchback", 2, "FWD", "Gas", 5, 3, ["fun-to-drive", "turbo", "manual-available", "tuner-friendly", "first-car", "compact", "lightweight"]],
    ["Ford", "Bronco", "USA", "SUV", 3, "4WD", "Gas", 5, 3, ["off-road", "rugged", "tuner-friendly", "family", "classic-style"]],
    ["Ford", "Explorer", "USA", "SUV", 3, "AWD", "Gas", 7, 3, ["family", "spacious", "comfortable", "towing"]],
    ["Chevrolet", "Camaro SS", "USA", "Coupe", 3, "RWD", "Gas", 4, 3, ["fast", "v8", "sporty", "manual-available", "tuner-friendly", "fun-to-drive"]],
    ["Chevrolet", "Corvette Stingray (C7)", "USA", "Coupe", 4, "RWD", "Gas", 2, 3, ["fast", "v8", "sporty", "track-ready", "fun-to-drive", "status", "manual-available"]],
    ["Chevrolet", "Silverado 1500", "USA", "Truck", 3, "4WD", "Gas", 5, 3, ["towing", "rugged", "spacious", "daily-driver"]],
    ["Chevrolet", "Malibu", "USA", "Sedan", 2, "FWD", "Gas", 5, 3, ["comfortable", "fuel-efficient", "daily-driver", "first-car"]],
    ["Chevrolet", "Bolt EV", "USA", "Hatchback", 2, "FWD", "Electric", 5, 3, ["electric", "fuel-efficient", "cheap-to-maintain", "first-car", "compact", "daily-driver"]],
    ["Chevrolet", "Tahoe", "USA", "SUV", 4, "4WD", "Gas", 8, 3, ["family", "spacious", "towing", "comfortable"]],
    ["Dodge", "Challenger R/T", "USA", "Coupe", 3, "RWD", "Gas", 5, 3, ["v8", "fast", "classic-style", "comfortable", "fun-to-drive"]],
    ["Dodge", "Charger R/T", "USA", "Sedan", 3, "RWD", "Gas", 5, 3, ["v8", "fast", "family", "spacious", "comfortable"]],
    ["Jeep", "Wrangler", "USA", "SUV", 3, "4WD", "Gas", 5, 2, ["off-road", "rugged", "project-car", "tuner-friendly", "classic-style"]],
    ["Jeep", "Grand Cherokee", "USA", "SUV", 3, "4WD", "Gas", 5, 2, ["family", "comfortable", "off-road", "towing", "spacious"]],
    ["Tesla", "Model 3", "USA", "Sedan", 3, "RWD", "Electric", 5, 4, ["electric", "fast", "fuel-efficient", "cheap-to-maintain", "daily-driver", "tech-heavy"]],
    ["Cadillac", "CTS-V", "USA", "Sedan", 3, "RWD", "Gas", 5, 3, ["v8", "fast", "luxury", "sporty", "manual-available"]],

    # ========================= UK =========================
    ["Mini", "Cooper", "UK", "Hatchback", 2, "FWD", "Gas", 4, 3, ["first-car", "compact", "fun-to-drive", "classic-style", "daily-driver"]],
    ["Mini", "Cooper S", "UK", "Hatchback", 2, "FWD", "Gas", 4, 3, ["turbo", "fun-to-drive", "tuner-friendly", "compact", "sporty", "manual-available"]],
    ["Land Rover", "Defender", "UK", "SUV", 4, "4WD", "Gas", 5, 2, ["off-road", "rugged", "status", "classic-style", "expensive-to-maintain"]],
    ["Land Rover", "Discovery", "UK", "SUV", 3, "4WD", "Gas", 7, 2, ["off-road", "family", "spacious", "towing", "expensive-to-maintain"]],
    ["Land Rover", "Range Rover Sport", "UK", "SUV", 4, "4WD", "Gas", 5, 2, ["luxury", "off-road", "fast", "status", "comfortable", "expensive-to-maintain"]],
    ["Land Rover", "Range Rover Evoque", "UK", "SUV", 3, "AWD", "Gas", 5, 2, ["luxury", "compact", "status", "expensive-to-maintain"]],
    ["Jaguar", "F-Type", "UK", "Coupe", 4, "RWD", "Gas", 2, 2, ["sporty", "fast", "luxury", "status", "expensive-to-maintain"]],
    ["Jaguar", "XF", "UK", "Sedan", 3, "RWD", "Gas", 5, 2, ["luxury", "comfortable", "expensive-to-maintain"]],
    ["Jaguar", "F-Pace", "UK", "SUV", 3, "AWD", "Gas", 5, 2, ["luxury", "family", "comfortable", "expensive-to-maintain"]],
    ["Aston Martin", "Vantage", "UK", "Coupe", 5, "RWD", "Gas", 2, 2, ["luxury", "fast", "v8", "status", "expensive-to-maintain"]],
    ["Bentley", "Continental GT", "UK", "Coupe", 5, "AWD", "Gas", 4, 2, ["luxury", "fast", "status", "comfortable", "expensive-to-maintain"]],
    ["Rolls-Royce", "Ghost", "UK", "Sedan", 5, "AWD", "Gas", 5, 2, ["luxury", "comfortable", "status", "spacious", "expensive-to-maintain"]],
    ["McLaren", "570S", "UK", "Coupe", 5, "RWD", "Gas", 2, 2, ["supercar", "fast", "turbo", "track-ready", "status", "expensive-to-maintain"]],
    ["Lotus", "Elise", "UK", "Convertible", 3, "RWD", "Gas", 2, 3, ["lightweight", "track-ready", "fun-to-drive", "sporty", "project-car", "manual-available"]],
    ["Lotus", "Evora", "UK", "Coupe", 4, "RWD", "Gas", 4, 3, ["sporty", "fun-to-drive", "track-ready", "manual-available", "lightweight"]],
    ["MG", "MG4 EV", "UK", "Hatchback", 2, "RWD", "Electric", 5, 3, ["electric", "fuel-efficient", "first-car", "family", "daily-driver", "cheap-to-maintain"]],
    ["Caterham", "Seven", "UK", "Convertible", 3, "RWD", "Gas", 2, 3, ["lightweight", "track-ready", "fun-to-drive", "project-car", "sporty", "manual-available"]],

    # ======================= GERMANY =======================
    ["Volkswagen", "Golf GTI", "Germany", "Hatchback", 2, "FWD", "Gas", 5, 3, ["fun-to-drive", "turbo", "manual-available", "tuner-friendly", "daily-driver", "first-car", "sporty"]],
    ["Volkswagen", "Golf R", "Germany", "Hatchback", 3, "AWD", "Gas", 5, 3, ["fast", "turbo", "tuner-friendly", "daily-driver", "manual-available", "sporty"]],
    ["Volkswagen", "Jetta", "Germany", "Sedan", 2, "FWD", "Gas", 5, 3, ["first-car", "fuel-efficient", "daily-driver", "comfortable"]],
    ["Volkswagen", "ID.4", "Germany", "SUV", 3, "RWD", "Electric", 5, 3, ["electric", "family", "spacious", "fuel-efficient", "tech-heavy"]],
    ["Audi", "A3", "Germany", "Sedan", 2, "FWD", "Gas", 5, 3, ["luxury", "compact", "daily-driver", "first-car"]],
    ["Audi", "A4", "Germany", "Sedan", 3, "AWD", "Gas", 5, 3, ["luxury", "comfortable", "daily-driver", "turbo"]],
    ["Audi", "TT", "Germany", "Coupe", 3, "AWD", "Gas", 4, 3, ["sporty", "turbo", "tuner-friendly", "fun-to-drive", "classic-style"]],
    ["Audi", "R8", "Germany", "Coupe", 5, "AWD", "Gas", 2, 3, ["supercar", "fast", "status", "expensive-to-maintain"]],
    ["Audi", "Q5", "Germany", "SUV", 3, "AWD", "Gas", 5, 3, ["family", "luxury", "comfortable", "daily-driver"]],
    ["Audi", "RS6 Avant (C7)", "Germany", "Wagon", 4, "AWD", "Gas", 5, 3, ["fast", "v8", "turbo", "family", "spacious", "luxury", "status", "tuner-friendly", "expensive-to-maintain"]],
    ["BMW", "528i (F10)", "Germany", "Sedan", 2, "RWD", "Gas", 5, 3, ["luxury", "comfortable", "spacious", "turbo", "daily-driver", "expensive-to-maintain"]],
    ["BMW", "535i (F10)", "Germany", "Sedan", 2, "RWD", "Gas", 5, 3, ["luxury", "comfortable", "spacious", "turbo", "fast", "tuner-friendly", "manual-available", "daily-driver"]],
    ["BMW", "550i (F10)", "Germany", "Sedan", 2, "RWD", "Gas", 5, 2, ["luxury", "fast", "v8", "turbo", "comfortable", "spacious", "status", "tuner-friendly", "expensive-to-maintain"]],
    ["BMW", "M5 (F10)", "Germany", "Sedan", 4, "RWD", "Gas", 5, 2, ["fast", "v8", "turbo", "sporty", "track-ready", "luxury", "spacious", "status", "manual-available", "tuner-friendly", "expensive-to-maintain"]],
    ["BMW", "328i (F30)", "Germany", "Sedan", 2, "RWD", "Gas", 5, 3, ["first-car", "daily-driver", "fun-to-drive", "turbo", "manual-available", "fuel-efficient", "comfortable", "tuner-friendly"]],
    ["BMW", "335i (F30)", "Germany", "Sedan", 2, "RWD", "Gas", 5, 3, ["fast", "turbo", "fun-to-drive", "sporty", "tuner-friendly", "manual-available", "drift-friendly", "project-car"]],
    ["BMW", "340i (F30)", "Germany", "Sedan", 3, "RWD", "Gas", 5, 4, ["fast", "turbo", "fun-to-drive", "sporty", "manual-available", "tuner-friendly", "daily-driver", "luxury"]],
    ["BMW", "3 Series Touring (F31)", "Germany", "Wagon", 2, "RWD", "Gas", 5, 3, ["family", "spacious", "daily-driver", "turbo", "luxury", "tuner-friendly"]],
    ["BMW", "M3 (F80)", "Germany", "Sedan", 4, "RWD", "Gas", 5, 3, ["fast", "sporty", "track-ready", "turbo", "manual-available", "tuner-friendly", "drift-friendly", "status"]],
    ["BMW", "M4 (F82)", "Germany", "Coupe", 4, "RWD", "Gas", 4, 3, ["fast", "sporty", "track-ready", "turbo", "manual-available", "tuner-friendly", "drift-friendly", "status"]],
    ["BMW", "435i (F32)", "Germany", "Coupe", 3, "RWD", "Gas", 4, 3, ["sporty", "turbo", "fun-to-drive", "tuner-friendly", "manual-available", "luxury", "daily-driver"]],
    ["BMW", "M235i / M240i (F22)", "Germany", "Coupe", 3, "RWD", "Gas", 4, 3, ["fun-to-drive", "fast", "turbo", "sporty", "compact", "drift-friendly", "tuner-friendly", "manual-available", "project-car"]],
    ["BMW", "M2 (F87)", "Germany", "Coupe", 4, "RWD", "Gas", 4, 3, ["fast", "sporty", "track-ready", "turbo", "compact", "manual-available", "drift-friendly", "tuner-friendly", "fun-to-drive"]],
    ["BMW", "M135i (F20)", "Germany", "Hatchback", 2, "RWD", "Gas", 5, 3, ["fun-to-drive", "fast", "turbo", "compact", "drift-friendly", "tuner-friendly", "manual-available", "project-car"]],
    ["BMW", "640i (F12/F13)", "Germany", "Coupe", 3, "RWD", "Gas", 4, 3, ["luxury", "comfortable", "status", "turbo", "expensive-to-maintain"]],
    ["BMW", "750i (F01)", "Germany", "Sedan", 2, "RWD", "Gas", 5, 2, ["luxury", "comfortable", "spacious", "v8", "turbo", "status", "tech-heavy", "expensive-to-maintain"]],
    ["BMW", "X3 (F25)", "Germany", "SUV", 2, "AWD", "Gas", 5, 3, ["family", "daily-driver", "spacious", "comfortable", "luxury"]],
    ["BMW", "X5 (F15)", "Germany", "SUV", 3, "AWD", "Gas", 5, 3, ["family", "luxury", "spacious", "towing", "comfortable"]],
    ["Mercedes-Benz", "C-Class", "Germany", "Sedan", 3, "RWD", "Gas", 5, 3, ["luxury", "comfortable", "daily-driver", "status"]],
    ["Mercedes-Benz", "E-Class", "Germany", "Sedan", 4, "RWD", "Gas", 5, 3, ["luxury", "comfortable", "spacious", "status"]],
    ["Mercedes-Benz", "G-Class", "Germany", "SUV", 5, "4WD", "Gas", 5, 2, ["off-road", "rugged", "status", "luxury", "expensive-to-maintain"]],
    ["Mercedes-Benz", "AMG GT", "Germany", "Coupe", 5, "RWD", "Gas", 2, 2, ["supercar", "fast", "v8", "turbo", "track-ready", "status", "expensive-to-maintain"]],
    ["Porsche", "911 Carrera", "Germany", "Coupe", 5, "RWD", "Gas", 4, 4, ["sporty", "fast", "track-ready", "status", "manual-available", "collector", "fun-to-drive"]],
    ["Porsche", "718 Cayman", "Germany", "Coupe", 4, "RWD", "Gas", 2, 4, ["sporty", "fun-to-drive", "track-ready", "manual-available", "turbo"]],
    ["Porsche", "Macan", "Germany", "SUV", 4, "AWD", "Gas", 5, 3, ["sporty", "luxury", "family", "status", "daily-driver"]],
    ["Porsche", "Taycan", "Germany", "Sedan", 5, "AWD", "Electric", 4, 3, ["electric", "fast", "luxury", "status", "tech-heavy"]],

    # ========================= ITALY =========================
    ["Fiat", "500", "Italy", "Hatchback", 1, "FWD", "Gas", 4, 2, ["first-car", "compact", "fuel-efficient", "classic-style"]],
    ["Fiat", "500 Abarth", "Italy", "Hatchback", 2, "FWD", "Gas", 4, 2, ["fun-to-drive", "turbo", "tuner-friendly", "compact", "manual-available", "sporty", "first-car"]],
    ["Fiat", "Panda", "Italy", "Hatchback", 1, "FWD", "Gas", 5, 3, ["first-car", "compact", "fuel-efficient", "cheap-to-maintain", "daily-driver"]],
    ["Alfa Romeo", "Giulia", "Italy", "Sedan", 3, "RWD", "Gas", 5, 2, ["sporty", "fun-to-drive", "luxury", "turbo", "classic-style", "daily-driver"]],
    ["Alfa Romeo", "Giulia Quadrifoglio", "Italy", "Sedan", 4, "RWD", "Gas", 5, 2, ["fast", "turbo", "sporty", "track-ready", "manual-available", "status", "expensive-to-maintain"]],
    ["Alfa Romeo", "Stelvio", "Italy", "SUV", 3, "AWD", "Gas", 5, 2, ["sporty", "luxury", "family", "turbo"]],
    ["Alfa Romeo", "4C", "Italy", "Coupe", 4, "RWD", "Gas", 2, 2, ["lightweight", "sporty", "track-ready", "turbo", "collector", "expensive-to-maintain"]],
    ["Maserati", "Ghibli", "Italy", "Sedan", 4, "RWD", "Gas", 5, 2, ["luxury", "comfortable", "status", "turbo", "expensive-to-maintain"]],
    ["Maserati", "GranTurismo", "Italy", "Coupe", 4, "RWD", "Gas", 4, 2, ["luxury", "v8", "fast", "status", "classic-style", "expensive-to-maintain"]],
    ["Ferrari", "488 GTB", "Italy", "Coupe", 5, "RWD", "Gas", 2, 3, ["supercar", "fast", "turbo", "track-ready", "status", "collector", "expensive-to-maintain"]],
    ["Ferrari", "Roma", "Italy", "Coupe", 5, "RWD", "Gas", 4, 3, ["luxury", "fast", "turbo", "v8", "status", "comfortable", "expensive-to-maintain"]],
    ["Lamborghini", "Huracan", "Italy", "Coupe", 5, "AWD", "Gas", 2, 3, ["supercar", "fast", "status", "track-ready", "expensive-to-maintain"]],
    ["Lamborghini", "Urus", "Italy", "SUV", 5, "AWD", "Gas", 5, 3, ["fast", "status", "luxury", "family", "turbo", "v8", "expensive-to-maintain"]],
    ["Lancia", "Delta Integrale", "Italy", "Hatchback", 4, "AWD", "Gas", 5, 2, ["collector", "turbo", "classic-style", "fun-to-drive", "track-ready", "expensive-to-maintain"]],

    # ========================= JAPAN =========================
    ["Toyota", "Corolla", "Japan", "Sedan", 2, "FWD", "Gas", 5, 5, ["first-car", "reliable", "cheap-to-maintain", "fuel-efficient", "daily-driver"]],
    ["Toyota", "Yaris", "Japan", "Hatchback", 1, "FWD", "Gas", 5, 5, ["first-car", "reliable", "cheap-to-maintain", "fuel-efficient", "compact"]],
    ["Toyota", "Camry", "Japan", "Sedan", 2, "FWD", "Gas", 5, 5, ["reliable", "comfortable", "family", "cheap-to-maintain", "daily-driver", "fuel-efficient"]],
    ["Toyota", "Prius", "Japan", "Hatchback", 2, "FWD", "Hybrid", 5, 5, ["hybrid", "fuel-efficient", "reliable", "cheap-to-maintain", "daily-driver", "first-car"]],
    ["Toyota", "RAV4", "Japan", "SUV", 3, "AWD", "Gas", 5, 5, ["family", "reliable", "daily-driver", "spacious", "cheap-to-maintain"]],
    ["Toyota", "Land Cruiser", "Japan", "SUV", 4, "4WD", "Gas", 7, 5, ["off-road", "reliable", "rugged", "towing", "family", "status"]],
    ["Toyota", "Hilux", "Japan", "Truck", 3, "4WD", "Gas", 5, 5, ["rugged", "reliable", "off-road", "towing", "cheap-to-maintain"]],
    ["Toyota", "GR86", "Japan", "Coupe", 3, "RWD", "Gas", 4, 4, ["fun-to-drive", "sporty", "drift-friendly", "track-ready", "manual-available", "tuner-friendly", "lightweight"]],
    ["Toyota", "GR Supra", "Japan", "Coupe", 4, "RWD", "Gas", 2, 4, ["fast", "turbo", "sporty", "tuner-friendly", "track-ready", "manual-available"]],
    ["Toyota", "Supra (A80)", "Japan", "Coupe", 5, "RWD", "Gas", 4, 3, ["collector", "turbo", "tuner-friendly", "fast", "project-car", "manual-available"]],
    ["Toyota", "MR2 Spyder (W30)", "Japan", "Convertible", 2, "RWD", "Gas", 2, 4, ["first-car", "project-car", "lightweight", "fun-to-drive", "sporty", "manual-available", "tuner-friendly", "track-ready", "cheap-to-maintain"]],
    ["Toyota", "RAV4 Hybrid", "Japan", "SUV", 3, "AWD", "Hybrid", 5, 5, ["hybrid", "fuel-efficient", "reliable", "cheap-to-maintain", "family", "spacious", "daily-driver"]],
    ["Toyota", "AE86 (Levin/Trueno)", "Japan", "Coupe", 3, "RWD", "Gas", 4, 3, ["drift-friendly", "project-car", "lightweight", "classic-style", "collector", "manual-available"]],
    ["Honda", "Civic", "Japan", "Sedan", 2, "FWD", "Gas", 5, 5, ["first-car", "reliable", "cheap-to-maintain", "fuel-efficient", "daily-driver", "tuner-friendly"]],
    ["Honda", "Civic Type R", "Japan", "Hatchback", 4, "FWD", "Gas", 5, 4, ["fast", "turbo", "track-ready", "sporty", "manual-available", "fun-to-drive", "tuner-friendly"]],
    ["Honda", "Civic (EG/EK)", "Japan", "Hatchback", 1, "FWD", "Gas", 4, 4, ["project-car", "tuner-friendly", "first-car", "lightweight", "manual-available", "cheap-to-maintain", "track-ready"]],
    ["Honda", "Accord", "Japan", "Sedan", 2, "FWD", "Gas", 5, 5, ["reliable", "comfortable", "family", "cheap-to-maintain", "daily-driver", "spacious"]],
    ["Honda", "CR-V", "Japan", "SUV", 3, "AWD", "Gas", 5, 5, ["family", "reliable", "spacious", "daily-driver", "fuel-efficient"]],
    ["Honda", "S2000", "Japan", "Convertible", 3, "RWD", "Gas", 2, 4, ["sporty", "fun-to-drive", "track-ready", "manual-available", "collector", "lightweight", "tuner-friendly"]],
    ["Honda", "NSX (NA1/NA2)", "Japan", "Coupe", 5, "RWD", "Gas", 2, 4, ["supercar", "collector", "track-ready", "manual-available", "status", "lightweight"]],
    ["Honda", "Fit/Jazz", "Japan", "Hatchback", 1, "FWD", "Gas", 5, 5, ["first-car", "compact", "cheap-to-maintain", "fuel-efficient", "reliable", "spacious"]],
    ["Nissan", "350Z", "Japan", "Coupe", 2, "RWD", "Gas", 2, 3, ["drift-friendly", "project-car", "tuner-friendly", "fun-to-drive", "manual-available", "sporty", "first-car"]],
    ["Nissan", "370Z", "Japan", "Coupe", 3, "RWD", "Gas", 2, 3, ["drift-friendly", "project-car", "tuner-friendly", "fun-to-drive", "manual-available", "sporty"]],
    ["Nissan", "Z (RZ34)", "Japan", "Coupe", 4, "RWD", "Gas", 2, 3, ["turbo", "sporty", "fast", "manual-available", "fun-to-drive", "tuner-friendly"]],
    ["Nissan", "GT-R (R35)", "Japan", "Coupe", 5, "AWD", "Gas", 4, 3, ["supercar", "fast", "turbo", "tuner-friendly", "track-ready"]],
    ["Nissan", "Skyline GT-R (R34)", "Japan", "Coupe", 5, "AWD", "Gas", 4, 3, ["collector", "turbo", "tuner-friendly", "fast", "track-ready", "manual-available"]],
    ["Nissan", "Silvia/240SX (S13-S15)", "Japan", "Coupe", 3, "RWD", "Gas", 4, 3, ["drift-friendly", "project-car", "tuner-friendly", "turbo", "manual-available", "lightweight", "classic-style"]],
    ["Nissan", "Patrol", "Japan", "SUV", 4, "4WD", "Gas", 7, 4, ["off-road", "rugged", "towing", "family", "spacious", "reliable"]],
    ["Nissan", "Leaf", "Japan", "Hatchback", 1, "FWD", "Electric", 5, 3, ["electric", "first-car", "cheap-to-maintain", "fuel-efficient", "daily-driver"]],
    ["Mazda", "MX-5 Miata", "Japan", "Convertible", 2, "RWD", "Gas", 2, 5, ["fun-to-drive", "lightweight", "track-ready", "drift-friendly", "tuner-friendly", "manual-available", "first-car", "project-car", "reliable"]],
    ["Mazda", "Mazda3", "Japan", "Hatchback", 2, "FWD", "Gas", 5, 4, ["first-car", "reliable", "fuel-efficient", "daily-driver", "manual-available", "comfortable"]],
    ["Mazda", "CX-5", "Japan", "SUV", 3, "AWD", "Gas", 5, 4, ["family", "reliable", "daily-driver", "spacious", "comfortable"]],
    ["Mazda", "RX-7 (FD)", "Japan", "Coupe", 4, "RWD", "Gas", 4, 2, ["rotary", "collector", "turbo", "track-ready", "tuner-friendly", "drift-friendly", "lightweight", "project-car", "manual-available"]],
    ["Mazda", "RX-8", "Japan", "Coupe", 2, "RWD", "Gas", 4, 2, ["rotary", "project-car", "fun-to-drive", "drift-friendly", "manual-available", "sporty"]],
    ["Subaru", "WRX", "Japan", "Sedan", 3, "AWD", "Gas", 5, 3, ["fast", "turbo", "fun-to-drive", "tuner-friendly", "manual-available", "daily-driver", "sporty"]],
    ["Subaru", "WRX STI", "Japan", "Sedan", 3, "AWD", "Gas", 5, 3, ["fast", "turbo", "track-ready", "tuner-friendly", "manual-available", "sporty"]],
    ["Subaru", "BRZ", "Japan", "Coupe", 3, "RWD", "Gas", 4, 4, ["fun-to-drive", "lightweight", "drift-friendly", "track-ready", "manual-available", "tuner-friendly", "sporty"]],
    ["Subaru", "Forester", "Japan", "SUV", 3, "AWD", "Gas", 5, 4, ["family", "reliable", "daily-driver", "spacious"]],
    ["Subaru", "Outback", "Japan", "Wagon", 3, "AWD", "Gas", 5, 4, ["family", "reliable", "spacious", "comfortable", "daily-driver"]],
    ["Mitsubishi", "Lancer Evolution X", "Japan", "Sedan", 3, "AWD", "Gas", 5, 3, ["fast", "turbo", "track-ready", "tuner-friendly", "manual-available", "sporty", "collector"]],
    ["Mitsubishi", "Pajero/Montero", "Japan", "SUV", 3, "4WD", "Gas", 7, 4, ["off-road", "rugged", "family", "reliable", "towing"]],
    ["Suzuki", "Jimny", "Japan", "SUV", 2, "4WD", "Gas", 4, 4, ["off-road", "compact", "rugged", "cheap-to-maintain", "first-car", "tuner-friendly", "fun-to-drive"]],
    ["Suzuki", "Swift Sport", "Japan", "Hatchback", 2, "FWD", "Gas", 5, 4, ["fun-to-drive", "lightweight", "first-car", "manual-available", "compact", "fuel-efficient", "cheap-to-maintain"]],
    ["Lexus", "IS 350", "Japan", "Sedan", 3, "RWD", "Gas", 5, 5, ["luxury", "reliable", "sporty", "comfortable", "daily-driver"]],
    ["Lexus", "ES", "Japan", "Sedan", 3, "FWD", "Gas", 5, 5, ["luxury", "comfortable", "reliable", "family"]],
    ["Lexus", "RX", "Japan", "SUV", 3, "AWD", "Gas", 5, 5, ["luxury", "family", "reliable", "comfortable"]],
    ["Lexus", "LX 570", "Japan", "SUV", 5, "4WD", "Gas", 8, 5, ["luxury", "off-road", "reliable", "status", "towing", "spacious"]],
    ["Lexus", "LC 500", "Japan", "Coupe", 5, "RWD", "Gas", 4, 5, ["luxury", "v8", "fast", "status", "comfortable"]],

    # ===================== SOUTH KOREA =====================
    ["Hyundai", "Elantra", "South Korea", "Sedan", 2, "FWD", "Gas", 5, 4, ["first-car", "fuel-efficient", "daily-driver", "cheap-to-maintain", "comfortable"]],
    ["Hyundai", "Elantra N", "South Korea", "Sedan", 3, "FWD", "Gas", 5, 3, ["fun-to-drive", "turbo", "manual-available", "sporty", "tuner-friendly", "track-ready"]],
    ["Hyundai", "Veloster N", "South Korea", "Hatchback", 3, "FWD", "Gas", 4, 3, ["fun-to-drive", "turbo", "manual-available", "sporty", "tuner-friendly", "track-ready"]],
    ["Hyundai", "Genesis Coupe", "South Korea", "Coupe", 2, "RWD", "Gas", 4, 3, ["drift-friendly", "project-car", "tuner-friendly", "manual-available", "first-car", "sporty", "turbo"]],
    ["Hyundai", "Tucson", "South Korea", "SUV", 2, "AWD", "Gas", 5, 4, ["family", "daily-driver", "spacious", "comfortable", "cheap-to-maintain"]],
    ["Hyundai", "Santa Fe", "South Korea", "SUV", 3, "AWD", "Gas", 7, 4, ["family", "spacious", "comfortable", "daily-driver"]],
    ["Hyundai", "Ioniq 5", "South Korea", "SUV", 3, "AWD", "Electric", 5, 4, ["electric", "family", "fast", "tech-heavy", "spacious", "fuel-efficient"]],
    ["Kia", "Rio", "South Korea", "Sedan", 1, "FWD", "Gas", 5, 4, ["first-car", "cheap-to-maintain", "fuel-efficient", "compact", "daily-driver"]],
    ["Kia", "Forte", "South Korea", "Sedan", 2, "FWD", "Gas", 5, 4, ["first-car", "fuel-efficient", "daily-driver", "comfortable", "cheap-to-maintain"]],
    ["Kia", "Soul", "South Korea", "Hatchback", 2, "FWD", "Gas", 5, 4, ["first-car", "compact", "spacious", "daily-driver", "fuel-efficient"]],
    ["Kia", "Stinger GT", "South Korea", "Sedan", 3, "RWD", "Gas", 5, 3, ["fast", "turbo", "sporty", "fun-to-drive", "drift-friendly", "comfortable", "tuner-friendly"]],
    ["Kia", "Sportage", "South Korea", "SUV", 2, "AWD", "Gas", 5, 4, ["family", "daily-driver", "spacious", "cheap-to-maintain"]],
    ["Kia", "Telluride", "South Korea", "SUV", 3, "AWD", "Gas", 8, 4, ["family", "spacious", "comfortable", "towing"]],
    ["Kia", "EV6", "South Korea", "SUV", 3, "AWD", "Electric", 5, 4, ["electric", "fast", "tech-heavy", "family", "fuel-efficient"]],
    ["Genesis", "G70", "South Korea", "Sedan", 3, "RWD", "Gas", 5, 4, ["luxury", "sporty", "fun-to-drive", "turbo", "manual-available", "comfortable"]],
    ["Genesis", "G80", "South Korea", "Sedan", 4, "RWD", "Gas", 5, 4, ["luxury", "comfortable", "spacious", "status"]],
    ["Genesis", "GV70", "South Korea", "SUV", 3, "AWD", "Gas", 5, 4, ["luxury", "family", "sporty", "comfortable"]],
]


# ---------------------------------------------------------------
# Sanity check: catches typos in tags, countries, body types, etc.
# Run this file directly to verify the data.
# ---------------------------------------------------------------
if __name__ == "__main__":
    for car in CARS:
        label = f"{car[MAKE]} {car[MODEL]}"
        assert len(car) == len(FIELDS), f"{label}: wrong number of fields"
        assert car[COUNTRY] in COUNTRIES, f"{label}: bad country"
        assert car[BODY] in BODY_TYPES, f"{label}: bad body type"
        assert car[DRIVE] in DRIVETRAINS, f"{label}: bad drivetrain"
        assert car[FUEL] in FUEL_TYPES, f"{label}: bad fuel type"
        assert 1 <= car[PRICE] <= 5, f"{label}: bad price tier"
        assert 1 <= car[RELIABILITY] <= 5, f"{label}: bad reliability"
        for tag in car[TAGS_IDX]:
            assert tag in TAGS, f"{label}: unknown tag '{tag}'"
    print(f"All {len(CARS)} cars check out.")