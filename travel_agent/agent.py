from google.adk.agents import Agent
from google.adk.tools import google_search

def get_trip_type (prompt: str) -> dict:
    """
    Classify the type of trip based on the user's input. 
    Returns one of: business, leisure, romantic, or adventure.
    """
    prompt_lower = promot.lower()
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
    tools=[get_trip_type], 
)
