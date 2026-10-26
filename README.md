# Weather Data Scraper (OpenWeatherMap API)

A Python script that fetches the current weather of 5 Pakistani cities from the
[OpenWeatherMap API](https://openweathermap.org/api) and saves it to CSV and Excel files.

## Features
- Collects the weather of 5 cities (Islamabad, Lahore, Karachi, Multan, Peshawar) in one file
- Fetches temperature, "feels like" temperature, humidity, weather condition and the time of the check
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

| City | Temperature (°C) | Feels Like (°C) | Humidity (%) | Condition | Checked At |
|------|------------------|-----------------|--------------|-----------|------------|
| Islamabad | 17.48 | 16.85 | 60 | Clear Sky | 2026-10-26 06:47 |
| Lahore | 18.18 | 17.78 | 66 | Clear Sky | 2026-10-26 06:47 |
| Karachi | 22.51 | 21.81 | 38 | Clear Sky | 2026-10-26 06:47 |
| Multan | 20.07 | 19.65 | 58 | Clear Sky | 2026-10-26 06:48 |
| Peshawar | 16.07 | 15.4 | 64 | Clear Sky | 2026-10-26 06:48 |

## License
MIT
