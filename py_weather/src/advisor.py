class ActivityAdvisor:
    """Czysta logika biznesowa — silnik decyzji o aktywności.

    Odizolowana od bibliotek zewnętrznych i sieci, dzięki czemu jest
    w pełni testowalna offline (Single Responsibility Principle).
    """

    @staticmethod
    def get_recommendation(temperature: float, smog_level: float) -> str:
        """Generuje rekomendację na podstawie temperatury (°C)
        i poziomu smogu (PM2.5 w µg/m³)."""
        if smog_level > 50.0:
            return "Zostań w domu. Jakość powietrza jest bardzo zła!"
        if temperature < 0:
            return "Zimno! Ubierz się ciepło na spacer."
        elif temperature > 25:
            return "Gorąco! Pamiętaj o wodzie i unikaj pełnego słońca."
        else:
            return "Idealna pogoda na aktywność na świeżym powietrzu!"
