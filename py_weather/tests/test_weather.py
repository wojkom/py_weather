from unittest.mock import MagicMock, patch

import pytest

from src.air_quality_api import AirQualityAPI
from src.weather_api import WeatherAPI


@patch("src.weather_api.requests.get")
def test_get_temperature_success(mock_get):
    # Testujemy parsowanie poprawnej odpowiedzi API (bez internetu, z mockiem).
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"main": {"temp": 21.5}}
    mock_get.return_value = mock_response

    api = WeatherAPI("fake-key")
    assert api.get_temperature("Warszawa") == 21.5


@patch("src.weather_api.requests.get")
def test_get_temperature_invalid_city_raises(mock_get):
    # Dla błędnego kodu HTTP (np. 404) oczekujemy kontrolowanego ValueError.
    mock_response = MagicMock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response

    api = WeatherAPI("fake-key")
    with pytest.raises(ValueError):
        api.get_temperature("Miasto-Ktore-Nie-Istnieje")


def test_air_quality_fixed_value():
    # Tryb deterministyczny: stała wartość PM2.5.
    api = AirQualityAPI(fixed_pm25=42.0)
    assert api.get_pm25("Kraków") == 42.0


def test_air_quality_simulated_in_range():
    # Symulacja powinna zwracać float z realistycznego zakresu.
    api = AirQualityAPI()
    value = api.get_pm25("Kraków")
    assert isinstance(value, float)
    assert 5.0 <= value <= 80.0
