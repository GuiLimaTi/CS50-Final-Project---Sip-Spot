import sqlite3

conn = sqlite3.connect("sipspot.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS coffee_shops (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    address TEXT NOT NULL,
    rating REAL NOT NULL,
    work_friendly TEXT NOT NULL,
    service_type TEXT NOT NULL,
    irish_coffee INTEGER NOT NULL,
    opening_time TEXT NOT NULL,
    closing_time TEXT NOT NULL,
    notes TEXT,
    image_filename TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS coffee_prices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    coffee_shop_id INTEGER NOT NULL,
    coffee_type TEXT NOT NULL,
    price REAL NOT NULL,
    FOREIGN KEY (coffee_shop_id) REFERENCES coffee_shops(id)
)
""")

conn.commit()
conn.close()

print("Database and tables created successfully.")
