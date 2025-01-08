# # Setting up a database using sqlite3

# import sqlite3

# # Connect to SQLite database (or create it if it doesn't exist)
# conn = sqlite3.connect('herbs.db')
# cursor = conn.cursor()

# # Create the 'herbs' table
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS herbs (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     scientific_name TEXT,
#     days_to_maturity INTEGER,
#     preferred_humidity TEXT,
#     preferred_temperature TEXT,
#     light_requirements TEXT,
#     watering_frequency TEXT,
#     soil_type TEXT,
#     notes TEXT
# )
# ''')

# # Save changes and close the connection
# conn.commit()
# conn.close()

# print("Database and table created successfully!")

import sqlite3
import csv

# Connect to the database
conn = sqlite3.connect('herbs.db')
cursor = conn.cursor()

# Read the CSV file
try: 
    with open('herbs_sample.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS herbs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                scientific_name TEXT,
                days_to_maturity INTEGER,
                humidity_min INTEGER,
                humidity_max INTEGER,
                temperature_min REAL,
                temperature_max REAL,
                light_requirements INTEGER, -- 1 = Full sun, 2 = Partial sun, 3 = Shade
                watering_frequency TEXT,
                soil_type TEXT,
                notes TEXT
            );
            """)

    # Save changes and close connection
    conn.commit()
    conn.close()

    print("Database populated from CSV!")
except: 
    print("File not found")


# import sqlite3

# # Establish a connection to SQLite database (or create it if it doesn't exist)
# connection = sqlite3.connect("herbs.db")
# cursor = connection.cursor()

# # Create a table with the updated schema
# cursor.execute("""
# CREATE TABLE IF NOT EXISTS herbs (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     name TEXT NOT NULL,
#     scientific_name TEXT,
#     days_to_maturity INTEGER,
#     humidity_min INTEGER,
#     humidity_max INTEGER,
#     temperature_min REAL,
#     temperature_max REAL,
#     light_requirements INTEGER, -- 1 = Full sun, 2 = Partial sun, 3 = Shade
#     watering_frequency TEXT,
#     soil_type TEXT,
#     notes TEXT
# );
# """)

# # Sample data to insert into the table
# herbs = [
#     ("Basil", "Ocimum basilicum", 60, 40, 60, 18.0, 24.0, 1, "Daily", "Loamy", "Great for companion planting."),
#     ("Mint", "Mentha", 90, 60, 70, 10.0, 30.0, 2, "Keep soil moist", "Rich, well-drained", "Can spread aggressively."),
#     ("Thyme", "Thymus vulgaris", 75, 30, 50, 18.0, 28.0, 1, "Weekly", "Sandy, well-drained", "Avoid overwatering."),
#     ("Rosemary", "Salvia rosmarinus", 120, 40, 60, 15.0, 25.0, 1, "Bi-weekly", "Sandy, well-drained", "Prune regularly to encourage growth."),
#     ("Cilantro", "Coriandrum sativum", 50, 50, 70, 10.0, 20.0, 2, "Keep soil moist", "Loamy", "Bolts quickly in hot weather.")
# ]

# # Insert sample data into the table
# cursor.executemany("""
# INSERT INTO herbs (
#     name, scientific_name, days_to_maturity, humidity_min, humidity_max,
#     temperature_min, temperature_max, light_requirements, watering_frequency, soil_type, notes
# ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
# """, herbs)

# # Commit changes and close the connection
# connection.commit()
# connection.close()