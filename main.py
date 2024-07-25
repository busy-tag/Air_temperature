import time
from API_operations import get_ip_based_location, fetch_weather_data
from data_operations import extract_location_info, extract_weather_info
from image_operations import create_text_to_image, generate_image

def get_drive_letter():
    while True:
        drive_letter = input("Please enter the drive letter assigned to Busy Tag device (e.g., D): ").strip().upper()
        if len(drive_letter) == 1 and drive_letter.isalpha():
            return drive_letter
        else:
            print("Invalid drive letter. Please enter a single letter (e.g., D).")

def main(drive_letter):
    location_data = get_ip_based_location()
    if not location_data:
        print("Could not get location data.")
        return

    latitude, longitude, city = extract_location_info(location_data)
    if latitude is None:
        return

    response = fetch_weather_data(latitude, longitude)
    temperature = extract_weather_info(response)
    
    if temperature is not None:
        generate_image(city, temperature, drive_letter)

if __name__ == "__main__":
    drive_letter = get_drive_letter()
    while True:
        main(drive_letter)
        print("Waiting for 10 minutes before next update...")
        time.sleep(600)