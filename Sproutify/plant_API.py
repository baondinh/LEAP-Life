import sqlite3
import openai
import os

# Generate text
# client = OpenAI()
client = openai.OpenAI(
    api_key = os.environ.get("OPEN_API_KEY"),
)

# # OpenAI API key
# openai.api_key = "your_openai_api_key"

# Function to query the database and fetch plant details
def get_plant_data(plant_name):
    # Connect to the SQLite database
    connection = sqlite3.connect("herbs.db")
    cursor = connection.cursor()
    
    # Query the database for the plant
    cursor.execute("SELECT * FROM herbs WHERE name = ?", (plant_name,))
    plant_data = cursor.fetchone()
    
    # Close the database connection
    connection.close()
    
    return plant_data

# Function to generate growing tips using OpenAI
def generate_growing_tips(plant_data):
    # Check if plant data exists
    if not plant_data:
        return f"Sorry, I couldn't find any data for the plant '{plant_data}' in the database."
    
    # Unpack plant data
    (
        _,  # ID
        name,
        scientific_name,
        days_to_maturity,
        humidity_min,
        humidity_max,
        temperature_min,
        temperature_max,
        light_requirements,
        watering_frequency,
        soil_type,
        notes
    ) = plant_data

    # Map light requirements to descriptive terms
    light_mapping = {1: "Full sun", 2: "Partial sun", 3: "Shade"}
    light_description = light_mapping.get(light_requirements, "Unknown")

    # Create a prompt for the OpenAI API
    prompt = f"""
    Provide expert gardening tips for growing {name} ({scientific_name}). The plant has the following growing conditions:
    - Days to maturity: {days_to_maturity} days
    - Preferred humidity: {humidity_min}% to {humidity_max}%
    - Preferred temperature: {temperature_min}°C to {temperature_max}°C
    - Light requirements: {light_description}
    - Watering frequency: {watering_frequency}
    - Preferred soil type: {soil_type}

    Additional notes: {notes}

    Write the tips in a clear, friendly, and professional tone.
    """

    # Use the OpenAI API to generate tips
    response = client.chat.completions.create(
        model="gpt-4o", 
        messages=[
        {"role": "developer", "content": "You are a helpful assistant."},
        {"role": "user", "content": prompt}
        ],
        max_tokens=300,
        temperature=0.7
    )

    # Return the generated tips
    return response.choices[0].message.content
    # return response["choices"][0]["text"].strip()

# Main code to generate tips for a specific plant
if __name__ == "__main__":
    plant_name = input("Enter the name of the plant: ")  # Example: Basil
    plant_data = get_plant_data(plant_name)
    
    if plant_data:
        tips = generate_growing_tips(plant_data)
        print("\nGrowing Tips:\n")
        print(tips)
    else:
        print(f"Sorry, no data found for the plant '{plant_name}'.")