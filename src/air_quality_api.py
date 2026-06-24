import random


class AirQualityAPI:
    """Dostawca danych o jakości powietrza (PM2.5).

    UWAGA: to świadomy PLACEHOLDER / SYMULACJA. Zwracana wartość PM2.5 nie
    pochodzi z prawdziwego pomiaru — jest losowana z realistycznego zakresu.

    Aby podpiąć realne dane, wystarczy zaimplementować w `get_pm25` zapytanie
    HTTP do jednego z serwisów, zachowując ten sam interfejs metody:
      - OpenWeather Air Pollution API (ten sam klucz co pogoda, po lat/lon),
      - OpenAQ (https://openaq.org),
      - Airly (https://airly.org).
    Reszta aplikacji (advisor, main) nie wymaga wtedy żadnych zmian.
    """

    # Realistyczny zakres stężeń PM2.5 w µg/m³ (od czystego powietrza po smog).
    _MIN_PM25 = 5.0
    _MAX_PM25 = 80.0

    def __init__(self, fixed_pm25: float | None = None):
        """fixed_pm25: jeśli podane, `get_pm25` zawsze zwróci tę wartość
        (wygodne w testach i do deterministycznych demonstracji)."""
        self.fixed_pm25 = fixed_pm25

    def get_pm25(self, city: str | None = None) -> float:
        """Zwraca (symulowane) stężenie PM2.5 w µg/m³.

        Argument `city` jest przyjmowany dla zgodności z przyszłym realnym API,
        ale w wersji symulowanej nie wpływa na wynik.
        """
        if self.fixed_pm25 is not None:
            return self.fixed_pm25
        return round(random.uniform(self._MIN_PM25, self._MAX_PM25), 1)
