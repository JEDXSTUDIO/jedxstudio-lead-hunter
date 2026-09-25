import os
import requests

api_key = os.environ.get("GOOGLE_MAPS_API_KEY")

if not api_key:
    raise RuntimeError("GOOGLE_MAPS_API_KEY was not found.")

url = "https://places.googleapis.com/v1/places:searchText"

headers = {
    "Content-Type": "application/json",
    "X-Goog-Api-Key": api_key,
    "X-Goog-FieldMask": (
        "places.displayName,"
        "places.formattedAddress,"
        "places.nationalPhoneNumber,"
        "places.websiteUri"
    ),
}

data = {
    "textQuery": "web design businesses in Port Harcourt, Nigeria"
}

response = requests.post(url, headers=headers, json=data, timeout=30)

if response.status_code != 200:
    raise RuntimeError(
        f"Google Places API error {response.status_code}: {response.text}"
    )

result = response.json()

places = result.get("places", [])

print(f"Found {len(places)} businesses.")

for place in places:
    name = place.get("displayName", {}).get("text", "Unknown")
    address = place.get("formattedAddress", "No address")
    phone = place.get("nationalPhoneNumber", "No phone")
    website = place.get("websiteUri", "No website")

    print("\n--- BUSINESS ---")
    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"Phone: {phone}")
    print(f"Website: {website}")
