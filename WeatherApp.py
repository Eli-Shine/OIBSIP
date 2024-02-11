import requests

#API key from openweathermap
api_key = "234fffe3cb09ced84945f29c112e629a"

#take user input for desired city
user_input = input("Please enter your city: ")


try:
    #fetch weather data from API url using requests for the inputted city
    weather_data = requests.get(
    f"http://api.openweathermap.org/data/2.5/weather?q={user_input}&units=metric&APPID={api_key}")
    data = weather_data.json()

    #extract relevant information from the API response
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    weather_description = data['weather'][0]['description']
    country = data['sys']['country']
    coordinates = data['coord']
    min_temp = data['main']['temp_min']
    max_temp = data['main']['temp_max']
    pressure = data['main']['pressure']
    timezone = data['timezone']

    # Print the fetched data
    print("Temperature:", temperature, "degree C")
    print("Humidity:", humidity, "%")
    print("Wind Speed:", wind_speed, "km/h")
    print("Weather Description:", weather_description)
    print("Country:", country)
    print("Coordinates:", coordinates)
    print("Minimum Temperature:", min_temp, "degree C")
    print("Maximum Temperature:", max_temp, "degree C")
    print("Pressure:", pressure, "hPa")
    print("Timezone:", timezone)

except Exception as e:
    print("Error fetching or processing data:", e)


