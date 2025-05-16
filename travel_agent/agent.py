from google.adk.agents import Agent
from google.adk.tools import google_search

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
    tools=[google_search],
)
