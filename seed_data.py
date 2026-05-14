import sqlite3

conn = sqlite3.connect("sipspot.db")
cursor = conn.cursor()

cursor.execute("DELETE FROM coffee_prices")
cursor.execute("DELETE FROM coffee_shops")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='coffee_prices'")
cursor.execute("DELETE FROM sqlite_sequence WHERE name='coffee_shops'")

coffee_shops = [
    (
        "Cool Hand Coffee Roasters Temple Bar",
        "Crown Alley, Temple Bar, Dublin 2",
        4.7,
        "Yes",
        "Sit-in and takeaway",
        0,
        "08:00",
        "18:00",
        "Coffee roasted in Dublin by the company.",
        "cool-hand.jpg"
    ),
    (
        "Brick Alley Café",
        "25 Essex St E, Temple Bar, Dublin, D02 W560",
        3.9,
        "Yes",
        "Sit-in and takeaway",
        1,
        "09:00",
        "21:00",
        "A central Temple Bar café with a longer opening time and Irish coffee available.",
        "brick-alley.jpg"
    ),
    (
        "The Stage Door Cafe",
        "Apartment 3, 11 Essex St E, Temple Bar, Dublin 2",
        4.7,
        "No",
        "Sit-in and takeaway",
        1,
        "06:00",
        "15:00",
        "Good for breakfast or meeting someone to talk, but not for working.",
        "stage-door.jpg"
    ),
    (
        "Copper + Straw Speciality Coffee",
        "14 - 18 Aston Quay, Temple Bar, Dublin 2, D02 FV38",
        4.8,
        "Yes",
        "Sit-in and takeaway",
        0,
        "07:30",
        "16:00",
        "Customers can choose from a range of origins, processing methods, roast profiles, and varieties, each contributing distinct characteristics to the final cup.",
        "copper-straw.jpg"
    ),
    (
        "Rumi Cafe Temple Bar",
        "1 Scarlet Row, Essex St W, Temple Bar, Dublin 8, D08 RRX6",
        4.9,
        "No",
        "Sit-in and takeaway",
        0,
        "07:30",
        "19:00",
        "Turkish-influenced café known for Turkish coffee and sweet treats like Turkish delight and baklava, better for a relaxed visit than for working.",
        "rumi-cafe.jpg"
    ),
    (
        "The Music Cafe Dublin",
        "Grattan House, 1 Wellington Quay, Temple Bar, Dublin 2, D02 DY95",
        4.3,
        "No",
        "Sit-in and takeaway",
        1,
        "08:30",
        "19:00",
        "We serve brunch and have a great choice of cakes. At least 3 evenings a week we have live music from some of Dublin's finest musicians.",
        "music-cafe.jpg"
    )
]

cursor.executemany("""
INSERT INTO coffee_shops (
    name, address, rating, work_friendly,
    service_type, irish_coffee, opening_time, closing_time, notes, image_filename
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", coffee_shops)

coffee_prices = [
    (1, "Americano", 3.90),
    (1, "Espresso", 3.90),
    (1, "Latte", 4.50),
    (1, "Flat White", 4.30),
    (1, "Cappuccino", 4.50),

    (2, "Americano", 3.15),
    (2, "Espresso", 3.15),
    (2, "Latte", 4.15),
    (2, "Flat White", 3.95),
    (2, "Cappuccino", 4.15),
    (2, "Irish Coffee", 5.50),

    (3, "Americano", 4.00),
    (3, "Espresso", 3.50),
    (3, "Latte", 5.00),
    (3, "Flat White", 4.00),
    (3, "Cappuccino", 5.00),
    (3, "Irish Coffee", 10.95),

    (4, "Americano", 3.70),
    (4, "Espresso", 3.70),
    (4, "Latte", 4.20),
    (4, "Flat White", 4.00),
    (4, "Cappuccino", 4.00),

    (5, "Americano", 3.40),
    (5, "Espresso", 3.00),
    (5, "Latte", 3.70),
    (5, "Flat White", 3.40),
    (5, "Cappuccino", 3.70),

    (6, "Americano", 3.50),
    (6, "Espresso", 3.20),
    (6, "Latte", 4.20),
    (6, "Flat White", 3.90),
    (6, "Cappuccino", 4.20),
    (6, "Irish Coffee", 6.95)
]

cursor.executemany("""
INSERT INTO coffee_prices (coffee_shop_id, coffee_type, price)
VALUES (?, ?, ?)
""", coffee_prices)

conn.commit()
conn.close()

print("Real coffee shop data inserted successfully.")
