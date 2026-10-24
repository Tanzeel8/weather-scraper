import os
import requests
import pandas as pd
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise SystemExit("❌ API key not found. Add OPENWEATHER_API_KEY to your .env file.")

CITY = "Islamabad,PK"
URL = "https://api.openweathermap.org/data/2.5/weather"
PARAMS = {"q": CITY, "appid": API_KEY, "units": "metric"}

# Output folder
os.makedirs("output", exist_ok=True)

# API request
response = requests.get(URL, params=PARAMS, timeout=20)

if response.status_code == 200:
    data = response.json()
    weather_data = {
        "City": data["name"],
        "Temperature (°C)": data["main"]["temp"],
        "Feels Like (°C)": data["main"]["feels_like"],
        "Humidity (%)": data["main"]["humidity"],
        "Condition": data["weather"][0]["description"].title(),
    }

    df = pd.DataFrame([weather_data])

    # Save as CSV (utf-8-sig so Excel shows the degree sign correctly)
    df.to_csv("output/weather.csv", index=False, encoding="utf-8-sig")

    # Save as Excel
    df.to_excel("output/weather.xlsx", index=False, engine="openpyxl")

    print("✅ Weather data saved to output/weather.csv and output/weather.xlsx")
else:
    print(f"❌ Failed to fetch weather data (status {response.status_code}). Check API key or city name.")
