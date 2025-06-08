import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("FLY_SCRAPER_API_KEY")
BASE_URL = "https://fly-scraper.p.rapidapi.com/flights/search-one-way"
HEADERS = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "fly-scraper.p.rapidapi.com"
}

def search_flights(origin="SFO", destination="BCN", departure_date="2025-08-15", adults="1", currency="USD"):
    """
    Searches for flights using Fly Scraper API.
    Returns a dict with status, error_message, and result.
    """
    if not API_KEY:
        return {
            "status": "error",
            "error_message": "Missing FLY_SCRAPER_API_KEY in .env file.",
            "result": None
        }

    querystring = {
        "originSkyId": "PARI",
        "destinationSkyId": "MSYA"
        # "date": departure_date
        # "date": "2025-06-20"

    }

    try:
        response = requests.get(BASE_URL, headers=HEADERS, params=querystring)
        response.raise_for_status()
        data = response.json()

        print("\n🌐 Raw API Response:\n")
        import json
        print(json.dumps(data, indent=2)) 

        itineraries = data.get("data", {}).get("itineraries", [])
        if not itineraries:
            return {
                "status": "success",
                "error_message": None,
                "result": "No flights found."
            }

        results = []
        for flight in itineraries[:3]:
            price = flight.get("price", {}).get("formatted", "N/A")
            legs = flight.get("legs", [])
            if not legs:
                continue

            departure = legs[0].get("departure", "N/A")
            carriers = legs[0].get("carriers", {}).get("marketing", [])
            airline_names = ", ".join(c.get("name", "Unknown Airline") for c in carriers)

            results.append(f"{airline_names} - {price} - Departs at {departure}")

        return {
            "status": "success",
            "error_message": None,
            "result": "\n".join(results) if results else "No flights found."
        }

    except Exception as e:
        return {
            "status": "error",
            "error_message": str(e),
            "result": None
        }

# Only run if file is executed directly for testing
if __name__ == "__main__":
    result = search_flights()
    if result["status"] == "success":
        print("✅ Flight Search Successful:\n")
        print(result["result"])
    else:
        print("❌ Error Occurred:")
        print(result["error_message"])