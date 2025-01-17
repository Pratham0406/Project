import requests

API_KEY = "fd774f37aae060def4e1c48b75450b1c"

def get_weather(destination, travel_dates):
    # Simple example to fetch weather
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={destination}&appid={API_KEY}")
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temp = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
        return {"weather": weather, "temp": temp}
    else:
        return {"error": "Could not fetch weather"}

def generate_packing_list(destination, travel_dates, activities):
    weather_info = get_weather(destination, travel_dates)
    if 'error' in weather_info:
        return ["Error fetching weather data. Please try again."]
    
    packing_list = []
    temp = weather_info["temp"]
    
    # Base packing list based on temperature
    if temp < 10:
        packing_list.extend(["Warm jacket", "Sweaters", "Gloves"])
    elif 10 <= temp <= 20:
        packing_list.extend(["Light jacket", "Jeans", "Long-sleeve shirts"])
    else:
        packing_list.extend(["T-shirts", "Shorts", "Sunscreen"])
    
    # Add items based on activities
    if "hiking" in activities:
        packing_list.extend(["Hiking boots", "Water bottle", "First aid kit"])
    if "beach" in activities:
        packing_list.extend(["Swimsuit", "Towel", "Flip-flops"])
    if "formal" in activities:
        packing_list.extend(["Formal attire", "Dress shoes"])
    
    return packing_list
