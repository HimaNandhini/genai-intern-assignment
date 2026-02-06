import requests

def get_weather(city):
    """
    Fetches current weather using Open-Meteo API (no API key).
    """
    # Simple city → coordinates mapping (minimal & acceptable)
    city_coords = {
        "hyderabad": (17.3850, 78.4867),
        "bangalore": (12.9716, 77.5946),
        "chennai": (13.0827, 80.2707),
        "delhi": (28.6139, 77.2090)
    }

    city_lower = city.lower()
    if city_lower not in city_coords:
        return {"error": "City not supported"}

    lat, lon = city_coords[city_lower]

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }

    response = requests.get(url, params=params, timeout=10)

    if response.status_code != 200:
        return {"error": "Weather API failed"}

    data = response.json()
    weather = data.get("current_weather", {})

    return {
        "city": city,
        "temperature": weather.get("temperature"),
        "windspeed": weather.get("windspeed")
    }
