import requests
import openmeteo_requests

def get_ip_based_location():
    try:
        response = requests.get('https://ipinfo.io')
        response.raise_for_status()
        data = response.json()
        return data
    except requests.RequestException as e:
        print(f"Error fetching location data: {e}")
        return None

def fetch_weather_data(latitude, longitude):
    om = openmeteo_requests.Client()
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "hourly": ["temperature_2m", "precipitation", "wind_speed_10m"],
        "current": ["temperature_2m", "relative_humidity_2m"]
    }

    responses = om.weather_api("https://api.open-meteo.com/v1/forecast", params=params)
    return responses[0] if responses else None