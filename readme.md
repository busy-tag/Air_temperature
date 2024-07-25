# Air_temperature

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)

## Introduction

The Air Temperature script fetches the current temperature based on your IP address, retrieves the weather data from the Open Meteo API, and generates an image displaying the location and temperature. This image is updated every 10 minutes.

### Project Purpose

The main goal of this project is to:

- Retrieve location data based on the user's IP address.
- Fetch current weather data using the Open Meteo API.
- Generate an image with the location and current temperature.
- Update the image every 10 minutes to reflect the latest weather data.

## Prerequisites

To run this script, ensure you have the following installed:

- Python 3.x
- Required Python packages: `requests`, `openmeteo_requests`, `Pillow`
- An active internet connection to fetch location and weather data.

## Installation
 
  To get started with this Python script, follow these steps:

1. Clone the repository:
   First, clone the repository from GitHub to your local machine.
   ```
   git clone https://github.com/busy-tag/Air_temperature.git
   cd Air_temperature
	```
2. Use `pip` to install the necessary packages:
	```
	pip install requests
	pip install openmeteo_requests
	pip install Pillow
	```
3. Ensure the font file (`MontserratBlack-3zOvZ.ttf`) is in the project directory.
	
## Configuration

The script provides several customizable parameters:
 
• **Drive Letter:** Prompted input for the drive letter where the Busy Tag device is located (e.g., `D`).

• **Text Content:** Displays location and temperature data.

• **Font Size and Colors:** Predefined but can be modified in the script.

## Usage
1. **Execute the script:**
You can run the script from the command line:
```
python main.py
```
2. **Provide Drive Letter:**
   
    The script will prompt you to enter the drive letter assigned to the Busy Tag device. Enter the letter (e.g., `D`) and press Enter.
         
3. **Script Operation:**

	The script will fetch the current location based on the user's IP address, retrieve the weather data from the Open Meteo API, and generate an image (air_temperature.png) displaying the location and current temperature. This process will repeat every 10 minutes.
	
4. **Output:**
	
	The generated image will be saved in the specified directory (e.g., D:) and will be updated every 10 minutes.

### Example

After running the script, you should see output similar to this in your terminal:
```
Please enter the drive letter assigned to Busy Tag device (e.g., D): D
City: YourCity
Coordinates: 12.3456°N 78.9101°E
Current temperature: 21.5
Current relative humidity: 60.0
Waiting for 10 minutes before next update...
```

And an image (air_temperature.png) will be saved in the specified directory (e.g., `D:`), displaying the following information:
```
Location
YourCity
Temperature
21.5°C
```

Sample:

![Image](/Air_temperature_sample.png){width=240 height=280}

### Troubleshooting ###

If you encounter any issues, ensure:

All Python packages are installed correctly.

The font file (`MontserratBlack-3zOvZ.ttf`) is present in the project directory.

You have an active internet connection.

The drive letter is correct and the Busy Tag device is connected.

For any additional help, please open an issue in the repository or contact the maintainer.
