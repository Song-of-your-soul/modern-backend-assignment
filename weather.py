import datetime as dt
import requests

with open("api_key.txt", "r") as file:
    API_KEY = file.read()
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
city = input("In what city do you want to check the temperature?")

url = BASE_URL + "appid=" + API_KEY + "&q=" + city

response = requests.get(url).json()

print(response)

# def temp_kelvin_to_celsius(kelvin: float) -> float:
#     return (kelvin - 272.15)


# temp_kelvin = response["main"]["temp"]
# temp_celsius = round(temp_kelvin_to_celsius(temp_kelvin), 1)

# print(f"The temperature in {city} is {temp_celsius} °C")

# def check_temperature(city: str) -> None:
