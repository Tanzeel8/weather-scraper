# Weather Data Scraper (OpenWeatherMap API)

A Python script that fetches the current weather of a city from the
[OpenWeatherMap API](https://openweathermap.org/api) and saves it to CSV and Excel files.

## Features
- Fetches temperature, "feels like" temperature, humidity and weather condition
- Reads the API key safely from a `.env` file (never stored in the code)
- Handles failed requests with a clear message
- Saves the result to CSV and Excel

## Tools used
Python, Requests, pandas, openpyxl, python-dotenv

## Setup
1. Get a free API key from [OpenWeatherMap](https://home.openweathermap.org/users/sign_up).
2. Clone this repository:
   ```bash
   git clone https://github.com/Tanzeel8/weather-scraper.git
   cd weather-scraper
   ```
3. Install the libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project folder (see `.env.example`):
   ```
   OPENWEATHER_API_KEY=your_api_key_here
   ```
5. Run the script:
   ```bash
   python weather_scraper.py
   ```

## Output
The script creates an `output` folder with `weather.csv` and `weather.xlsx`.
A sample is included in [`sample_output.csv`](sample_output.csv).

| City | Temperature (°C) | Feels Like (°C) | Humidity (%) | Condition |
|------|------------------|-----------------|--------------|-----------|
| Islamabad | 29.91 | 35.06 | 71 | Overcast Clouds |

## License
MIT
