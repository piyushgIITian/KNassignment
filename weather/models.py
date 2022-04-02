from utils import app
import requests


@app.route("/weather", methods=["GET"])
def weather(lat=23,lon=123):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=b4f6f5bf33ff9a68b09e7c324196b9fc'

    r = requests.get(url).json()

    return f"<h1>{r}</h1>"