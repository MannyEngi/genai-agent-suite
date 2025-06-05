import requests
import os
from google.adk.agents import Agent
from google.adk.tools import google_search
from dotenv import load_dotenv

load_dotenv()
print(f"DEBUG: API Key = {os.getenv('OPENWEATHER_API_KEY')}")

api_key = os.getenv("OPENWEATHER_API_KEY")

def get_trip_type (prompt: str) -> dict:
    """
    Classify the type of trip based on the user's input. 
    Returns one of: business, leisure, romantic, or adventure.
    """
    prompt_lower = prompt.lower()
    if any (word in prompt_lower for word in ["meeting", "conference", "client", "work", "business"]):
        trip_type = "business"
    if any (word in prompt_lower for word in ["honeymoon", "couple", "romantic", "date", "partner"]):
        trip_type= "romantic"
    if any (word in prompt_lower for word in ["meeting", "conference", "client", "work", "business"]):
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

# === Root Agent ===
root_agent = Agent(
    name="travel_planner",
    model="gemini-2.0-flash",
    description="Travel itinerary planning agent",
    instruction="""
    You are a helpful travel planner. Based on the user's prompt, return a structured daily travel itinerary. 
    The itinerary should consider the location, number of days, and preferences mentioned (e.g., food, culture, adventure).
    Format your output as Markdown. Include:
    - A daily breakdown of suggested activities
    - Tips on transportation, meals, or bookings
    """,
    # tools=[google_search],
    tools=[google_search, get_trip_type, get_weather_forecast], 
)

if __name__ == "__main__":
    # Simple test
    print(get_weather_forecast("Barcelona"))
