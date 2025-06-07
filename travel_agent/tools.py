# tools.py
import os
import requests

def get_trip_type(prompt: str) -> dict:
    """
    Classify the type of trip based on the user's input.
    Returns one of: business, leisure, romantic, or adventure.
    """
    prompt_lower = prompt.lower()

    if any(word in prompt_lower for word in ["meeting", "conference", "client", "work", "business"]):
        trip_type = "business"
    elif any(word in prompt_lower for word in ["honeymoon", "couple", "romantic", "date", "partner"]):
        trip_type = "romantic"
    elif any(word in prompt_lower for word in ["hike", "explore", "adventure", "outdoors", "thrill"]):
        trip_type = "adventure"
    else:
        trip_type = "leisure"

    return {
        "status": "success",
        "error_message": None,
        "result": trip_type,
    }

def get_weather_forecast(city: str) -> dict:
    """
    Get the weather forecast for a city using OpenWeatherMap API.
    Returns a short weather description and temperature in Celsius.
    """
    api_key = os.getenv("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200 or "weather" not in data:
            return {"status": "error", "error_message": data.get("message", "API error"), "result": None}

        weather_desc = data["weather"][0]["description"]
        temp = data["main"]["temp"]

        return {
            "status": "success",
            "error_message": None,
            "result": f"In {city}, it’s currently {weather_desc} with a temperature of {temp}°C."
        }

    except Exception as e:
        return {"status": "error", "error_message": str(e), "result": None}
