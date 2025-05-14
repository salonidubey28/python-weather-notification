import requests
from plyer import notification

# Your OpenWeatherMap API key (sign up on OpenWeatherMap to get it)
API_KEY = "a5c37dc4315f9d8760648edfaf8d1d62"

# Step 1: Get the city using your IP address (use the IPInfo API)
ip_info = requests.get("https://ipinfo.io").json()
city = ip_info.get("city", "Unknown")

# Step 2: Fetch weather data from OpenWeatherMap using the API
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Request weather data
response = requests.get(url).json()

# Step 3: Extract the required information from the response
if response.get("cod") != "404":
    # Extract temperature and weather description
    temp = response['main']['temp']
    weather_description = response['weather'][0]['description']
else:
    temp = "N/A"
    weather_description = "N/A"

# Step 4: Prepare the message for the notification
result = f"Current temperature: {temp}°C in {city}\nWeather: {weather_description}"

# Step 5: Show the notification
notification.notify(
    title="Live Weather Update",
    message=result,
    timeout=10
)
