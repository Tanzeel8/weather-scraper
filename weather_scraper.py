import os
import time
from datetime import datetime

import requests
import pandas as pd
from dotenv import load_dotenv

# Load the API key from the .env file
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    raise SystemExit("❌ API key not found. Add OPENWEATHER_API_KEY to your .env file.")

CITIES = ["Islamabad,PK", "Lahore,PK", "Karachi,PK", "Multan,PK", "Peshawar,PK"]
URL = "https://api.openweathermap.org/data/2.5/weather"

# Output folder
os.makedirs("output", exist_ok=True)


def get_weather(city):
    """Fetch the current weather of one city. Returns a dict or None."""
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(URL, params=params, timeout=20)

    if response.status_code != 200:
        print(f"❌ {city}: failed (status {response.status_code})")
        return None

    data = response.json()
    return {
        "City": data["name"],
        "Temperature (°C)": data["main"]["temp"],
        "Feels Like (°C)": data["main"]["feels_like"],
        "Humidity (%)": data["main"]["humidity"],
        "Condition": data["weather"][0]["description"].title(),
        "Checked At": datetime.now().strftime("%Y-%m-%d %H:%M"),
    }


rows = []
for city in CITIES:
    result = get_weather(city)
    if result:
        rows.append(result)
        print(f"✅ {city}: done")
    time.sleep(0.5)  # polite delay between requests

if rows:
    df = pd.DataFrame(rows)

    # Save as CSV (utf-8-sig so Excel shows the degree sign correctly)
    df.to_csv("output/weather.csv", index=False, encoding="utf-8-sig")

    # Save as Excel
    df.to_excel("output/weather.xlsx", index=False, engine="openpyxl")

    print(f"✅ Saved {len(df)} cities to output/weather.csv and output/weather.xlsx")
else:
    print("❌ No weather data collected. Check your API key and internet connection.")
