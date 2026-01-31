import datetime
import requests
import sys

from Lesson8.Homework.WatherForecast import WeatherForecast

weather_forecast = WeatherForecast()


date_input = input("Enter a date: (YYYY-MM-DD) or press enter for tomorrow: ").strip()

if date_input =="":
    searched_date = datetime.date.today() + datetime.timedelta(days=1)
else:
    try:
        searched_date = datetime.datetime.strptime(date_input, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYY-mm-dd.")
        sys.exit()

searched_date = searched_date.strftime("%Y-%m-%d")
print(f"Checking weather for: {searched_date}")

if searched_date in weather_forecast:
    print("Result loaded from file (no API call).")
    precip = weather_forecast[searched_date]

else:
    print("Fetching data from API...")

URL = f"https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&daily=rain_sum&start_date={searched_date}&end_date={searched_date}"
response = requests.get(URL)
result = response.json()

precip = result["daily"]["rain_sum"][0]

weather_forecast[searched_date] = precip


if precip > 0:
    print(f"It will rain on {searched_date}. Precipitation: {precip} mm")
elif precip == 0:
    print(f"It will not rain on {searched_date}.")

else:
    print("I don't know.")