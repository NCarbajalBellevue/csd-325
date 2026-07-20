# Name: Natalia Carbajal
# Date: 7/19/2026
# Assignment: Module 9.2
# Purpose: Connect to the Open-Meteo API, test the connection,
# print the JSON response, and display a formatted JSON response.

import requests
import json

# Create a formatted string of the Python JSON object
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# API endpoint for current weather in Riverside, CA
url = "https://api.open-meteo.com/v1/forecast?latitude=33.98&longitude=-117.37&current=temperature_2m,wind_speed_10m"

# Send a GET request to the API
response = requests.get(url)

# Test the connection
print("Status Code:", response.status_code)

# Print the response with no formatting
print("\nUnformatted Response:")
print(response.json())

# Print the response with formatting
print("\nFormatted Response:")
jprint(response.json())