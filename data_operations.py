from openmeteo_sdk.Variable import Variable

def extract_location_info(location_data):
    if 'loc' in location_data:
        coordinates = location_data['loc'].split(',')
        latitude = round(float(coordinates[0]), 4)
        longitude = round(float(coordinates[1]), 4)
        city = location_data.get('city', '')
        print(f"City: {city}")
        return latitude, longitude, city
    else:
        print("Location coordinates not found in the data.")
        return None, None, None

def extract_weather_info(response):
    if response:
        print(f"Coordinates: {response.Latitude():.4f}\u00b0N {response.Longitude():.4f}\u00b0E")
        
        current = response.Current()
        current_variables = list(map(lambda i: current.Variables(i), range(0, current.VariablesLength())))
        
        current_temperature_2m = next(filter(lambda x: x.Variable() == Variable.temperature and x.Altitude() == 2, current_variables))
        current_relative_humidity_2m = next(filter(lambda x: x.Variable() == Variable.relative_humidity and x.Altitude() == 2, current_variables))
        
        temperature = f"{current_temperature_2m.Value():.1f}"
        print(f"Current temperature: {temperature}")
        print(f"Current relative humidity: {current_relative_humidity_2m.Value():.1f}")
        
        return temperature
    return None