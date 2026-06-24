import requests


class WeatherAPI:
    """Klient HTTP do OpenWeatherMap.

    Odpowiada wyłącznie za komunikację z zewnętrznym API pogodowym
    oraz parsowanie odpowiedzi (Single Responsibility Principle).
    """

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"

    def _fetch(self, city: str) -> dict:
        """Wysyła zapytanie do API i zwraca surowe dane JSON.

        Rzuca kontrolowany ValueError, jeśli API zwróci kod inny niż 200
        (np. 404 dla nieistniejącego miasta, 401 dla błędnego klucza).
        """
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric",
        }
        response = requests.get(self.base_url, params=params)
        if response.status_code != 200:
            raise ValueError(f"Nie udało się pobrać danych dla miasta: {city}")
        return response.json()

    def get_temperature(self, city: str) -> float:
        """Pobiera aktualną temperaturę dla podanego miasta w stopniach Celsjusza."""
        data = self._fetch(city)
        return data["main"]["temp"]

    def get_weather(self, city: str) -> dict:
        """Pobiera temperaturę oraz tekstowy opis pogody dla podanego miasta."""
        data = self._fetch(city)
        return {
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
        }
