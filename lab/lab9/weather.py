from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="kolkata"):

    if not bool(city.strip()):
        city = "kolkata"

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'

    weather_data = requests.get(request_url).json()
    if weather_data['cod'] == 200:
        return weather_data
    else:
        return False


if __name__ == "__main__":
    print('\n*** Get Current Weather ***\n')

    city = input("\nPlease enter a city: ")

    weather_data = get_current_weather(city)

    if (weather_data):
        pprint(weather_data)
    else:
        pprint("city not found")
