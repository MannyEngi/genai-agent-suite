import os
from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.models.lite_llm import LiteLlm
from dotenv import load_dotenv
from .tools import get_trip_type, get_weather_forecast

load_dotenv()

api_key = os.getenv("OPENWEATHER_API_KEY")

model = LiteLlm(
    model="openrouter/openai/gpt-3.5-turbo",  # Tool-compatible model on OpenRouter
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# === Root Agent ===
root_agent = Agent(
    name="travel_planner",
    model=model,
    description="Travel itinerary planning agent",
    instruction="""
    You are a helpful travel planner. Based on the user's prompt, return a structured daily travel itinerary. 
    The itinerary should consider the location, number of days, and preferences mentioned (e.g., food, culture, adventure).
    
    You also have access to a weather forecast tool. For each location mentioned in the itinerary, 
    call the weather tool and include the current weather forecast in the daily breakdown.

    Format your output as Markdown. Include:
    - A daily breakdown of suggested activities
    - Tips on transportation, meals, or bookings
    """,

    tools=[get_trip_type, get_weather_forecast], 
)