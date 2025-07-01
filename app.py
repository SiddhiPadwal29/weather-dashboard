from flask import Flask, render_template, request
import requests
import webbrowser
from threading import Timer
from datetime import datetime

app = Flask(__name__)

API_KEY = '08f79308c0bc933096686b19c26de1fa'  # Replace with your OpenWeatherMap API key
BASE_URL_CURRENT = 'https://api.openweathermap.org/data/2.5/weather?'
BASE_URL_FORECAST = 'https://api.openweathermap.org/data/2.5/forecast?'

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = {}
    forecast_data = []

    if request.method == "POST":
        city = request.form.get("city")
        if city:
            url_current = f"{BASE_URL_CURRENT}q={city}&appid={API_KEY}&units=metric"
            res_current = requests.get(url_current)

            url_forecast = f"{BASE_URL_FORECAST}q={city}&appid={API_KEY}&units=metric"
            res_forecast = requests.get(url_forecast)

            if res_current.status_code == 200 and res_forecast.status_code == 200:
                current = res_current.json()
                forecast = res_forecast.json()

                weather_data = {
                    "city": current["name"],
                    "temperature": current["main"]["temp"],
                    "humidity": current["main"]["humidity"],
                    "description": current["weather"][0]["description"],
                    "icon": current["weather"][0]["icon"],
                    "wind": current["wind"]["speed"]
                }

                for entry in forecast["list"]:
                    if "12:00:00" in entry["dt_txt"]:
                        forecast_data.append({
                            "date": datetime.strptime(entry["dt_txt"], "%Y-%m-%d %H:%M:%S").strftime("%a, %b %d"),
                            "temp": entry["main"]["temp"],
                            "description": entry["weather"][0]["description"],
                            "icon": entry["weather"][0]["icon"]
                        })
            else:
                weather_data["error"] = "City not found or API error. Try again."

    return render_template("index.html", weather=weather_data, forecast=forecast_data)

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == "__main__":
    Timer(1, open_browser).start()
    app.run()
