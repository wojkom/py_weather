from src.advisor import ActivityAdvisor


def test_recommendation_high_smog():
    # Wysoki smog ma priorytet niezależnie od temperatury.
    result = ActivityAdvisor.get_recommendation(20.0, 65.0)
    assert result == "Zostań w domu. Jakość powietrza jest bardzo zła!"


def test_recommendation_cold_weather():
    # Czyste powietrze, ale niska temperatura.
    result = ActivityAdvisor.get_recommendation(-5.0, 10.0)
    assert "Zimno!" in result


def test_recommendation_perfect_weather():
    # Idealne warunki pogodowe.
    result = ActivityAdvisor.get_recommendation(18.0, 5.0)
    assert result == "Idealna pogoda na aktywność na świeżym powietrzu!"


def test_recommendation_hot_weather():
    # Wysoka temperatura przy czystym powietrzu.
    result = ActivityAdvisor.get_recommendation(30.0, 10.0)
    assert "Gorąco!" in result
