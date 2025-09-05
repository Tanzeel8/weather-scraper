import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()   #  .env file load 
API_KEY = os.getenv("OPENWEATHER_API_KEY")  # OpenWeatherMap API key load from .env

CITY = "Islamabad,PK"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

# Output folder
if not os.path.exists("output"):
    os.makedirs("output")

# API request
response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    weather_data = {
        "City": data["name"],
        "Temperature (°C)": data["main"]["temp"],
        "Feels Like (°C)": data["main"]["feels_like"],
        "Humidity (%)": data["main"]["humidity"],
        "Condition": data["weather"][0]["description"].title(),
    }

    df = pd.DataFrame([weather_data])

    # Save as CSV
    df.to_csv("output/weather.csv", index=False)

    # Save as Excel
    df.to_excel("output/weather.xlsx", index=False, engine="openpyxl")

    print("✅ Weather data saved to output/weather.csv and output/weather.xlsx")
    
else:
    print("❌ Failed to fetch weather data. Check API key or city name.")
