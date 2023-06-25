import requests
import datetime

def get_sun_times(city, country):
    response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?key=28494129f07d453cbc7200536232506&q={city},{country}&days=1")
    data = response.json()
    sunrise = data['forecast']['forecastday'][0]['astro']['sunrise']
    sunset = data['forecast']['forecastday'][0]['astro']['sunset']
    return sunrise, sunset

city = input("Please enter city name: ")
country = input("Please enter country name: ")

sunrise, sunset = get_sun_times(city, country)
print(f"In {city}, {country}, sunrise is at {sunrise} and sunset is at {sunset}.")

