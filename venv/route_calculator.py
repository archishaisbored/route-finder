import requests

# OpenRouteService API Key
API_KEY = "5b3ce3597851110001cf6248d2ef251be0264bc6a3fa272e4beb849b"

def get_route(start, end):
    # API URL for driving directions
    url = "https://api.openrouteservice.org/v2/directions/driving-car/geojson"
    
    # API request headers
    headers = {
        "Authorization": API_KEY,
        "Content-Type": "application/json"
    }
    
    # API request payload (note: API expects [lon, lat], so we swap start/end order)
    payload = {
        "coordinates": [[start[1], start[0]], [end[1], end[0]]],
        "format": "geojson"
    }
    
    # Fetch route data
    response = requests.post(url, json=payload, headers=headers)
    data = response.json()
    
    # Extract coordinates if route exists
    if "features" in data and len(data["features"]) > 0:
        route_coords = data["features"][0]["geometry"]["coordinates"]
        # Convert [lon, lat] to [lat, lon] for consistency with your input
        return [(lat, lon) for lon, lat in route_coords]
    else:
        raise ValueError("No route found or invalid API response")

# For testing (optional)
if __name__ == "__main__":
    start = [49.41461, 8.681495]  # [lat, lon]
    end = [49.420318, 8.687872]    # [lat, lon]
    route = get_route(start, end)
    print(route)