# Setting up a database using sqlite3

import sqlite3
import csv

# Connect to the database
conn = sqlite3.connect('herbs.db')
cursor = conn.cursor()

# Step 1: Create the table
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

# Step 2: Read the CSV file and insert data into the table
try:
    with open('herbs_sample.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute("""
            INSERT INTO herbs (
                name, scientific_name, days_to_maturity, humidity_min, humidity_max,
                temperature_min, temperature_max, light_requirements,
                watering_frequency, soil_type, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                row['name'],
                row['scientific_name'],
                int(row['days_to_maturity']),
                int(row['humidity_min']),
                int(row['humidity_max']),
                float(row['temperature_min']),
                float(row['temperature_max']),
                int(row['light_requirements']),
                row['watering_frequency'],
                row['soil_type'],
                row['notes']
            ))
except FileNotFoundError:
    print("Error: The CSV file was not found.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Step 3: Save changes and close connection
    conn.commit()
    conn.close()
    print("Database populated from CSV!")
