import datetime as dt
import requests
import typer

app = typer.Typer()
today = dt.date.today()


@app.command()
def weather_forecast(city):
    with open("api_key.txt", "r") as file:
        API_KEY = file.read()
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city

    response = requests.get(url).json()

    if response["cod"] == "404":
        print(f"Sorry there is no such city as {city}")
        return

    if response["cod"] == "400":
        print(f"Perhaps you forget to fill in the city you search")
        return

    temp_kelvin = response["main"]["temp"]
    temp_celsius = round(temp_kelvin_to_celsius(temp_kelvin), 1)

    print(
        f"Today is {today}. The temperature in {city} is {temp_celsius} °C")


def temp_kelvin_to_celsius(kelvin: float) -> float:
    return (kelvin - 272.15)


if __name__ == "__main__":
    app()
