import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("FLY_SCRAPER_API_KEY")
if not API_KEY:
    raise ValueError("Missing FLY_SCRAPER_API_KEY in .env file.")

# url = "https://fly-scraper.p.rapidapi.com/flights/search"
url = "https://fly-scraper.p.rapidapi.com/searchFlights"  # Try this if it's in the docs
querystring = {
    "origin": "SFO",
    "destination": "BCN",
    "departureDate": "2025-08-15",
    "adults": "1",
    "currency": "USD"
}

headers = {
    "X-RapidAPI-Key": os.getenv("FLY_SCRAPER_API_KEY"),
    "X-RapidAPI-Host": "fly-scraper.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.status_code)
print(response.json())
