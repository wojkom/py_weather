import os

from dotenv import load_dotenv

from src.advisor import ActivityAdvisor
from src.air_quality_api import AirQualityAPI
from src.weather_api import WeatherAPI


def main():
    load_dotenv()
    api_key = os.getenv("OPENWEATHER_API_KEY")
    if not api_key or api_key == "your_api_key_here":
        print(
            "Brak klucza API. Ustaw OPENWEATHER_API_KEY w pliku .env "
            "(wzór znajdziesz w .env.example)."
        )
        return

    city = input("Podaj miasto: ").strip()

    try:
        weather_client = WeatherAPI(api_key)
        air_client = AirQualityAPI()  # symulacja PM2.5 (placeholder)

        weather = weather_client.get_weather(city)
        temp = weather["temperature"]
        description = weather["description"]
        pm25 = air_client.get_pm25(city)

        recommendation = ActivityAdvisor.get_recommendation(temp, pm25)

        print(f"\n--- Wynik dla {city} ---")
        print(f"Pogoda: {description}")
        print(f"Temperatura: {temp}°C")
        print(f"Jakość powietrza (PM2.5): {pm25} µg/m³  [symulacja]")
        print(f"Rekomendacja: {recommendation}")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")


if __name__ == "__main__":
    main()
