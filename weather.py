import requests

# WeatherAPI key
WEATHER_API_KEY = '29ee40b8f7bb4a4490621150260402'  # TODO: Replace with your own WeatherAPI key

def get_weather(city):
    # TODO: Build the API request URL using the base API endpoint, the API key, and the city name provided by the user.
    
    #                  base API endpoint                                          API key              city name
    apirequestURL = "http://api.weatherapi.com/v1/forecast.json" + "?key=" + WEATHER_API_KEY + "&q=" + city
    
    print("API Request URL: " + apirequestURL)
    # TODO: Make the HTTP request to fetch weather data using the 'requests' library.
    
    response = requests.get(apirequestURL)

    # TODO: Handle HTTP status codes:
    # - Check if the status code is 200 (OK), meaning the request was successful.
    # - If not 200, handle common errors like 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), and any other relevant codes.

    if response.status_code == 200:
        # TODO: Parse the JSON data returned by the API. Extract and process the following information:

        data = response.json()

        # - Current temperature in Fahrenheit

        tempF = data["current"]["temp_f"]

        # - The "feels like" temperature

        tempFeels = data["current"]["feelslike_f"]

        # - Weather condition (e.g., sunny, cloudy, rainy)

        weatherCon = data["current"]["condition"]["text"]

        # - Humidity percentage

        humidityPer = data["current"]["humidity"]

        # - Wind speed and direction

        windSpeed = data["current"]["wind_mph"]
        windDirection = data["current"]["wind_dir"]

        # - Atmospheric pressure in mb

        atmPressure = data["current"]["pressure_mb"]

        # - UV Index value

        uvIndex = data["current"]["uv"]

        # - Cloud cover percentage

        cloudPercentage = data["current"]["cloud"]

        # - Visibility in miles

        visibMiles = data["current"]["vis_miles"]

        # TODO: Display the extracted weather information in a well-formatted manner.
        print(f"Weather data for {city}...")
        print(f"Temperature(Farenheit): {tempF}")
        print(f"Temperature(Feels like): {tempFeels}")
        print(f"Weather Condition: {weatherCon}")
        print(f"Humidity Percentage: {humidityPer}")
        print(f"Wind Speed: {windSpeed}")
        print(f"Wind Direction: {windDirection}")
        print(f"Atmospheric Pressure(mb): {atmPressure}")
        print(f"UV Index Value: {uvIndex}")
        print(f"Cloud Percentage: {cloudPercentage}")
        print(f"Visibility(Miles): {visibMiles}")

    else:
        # TODO: Implement error handling for common status codes. Provide meaningful error messages based on the status code.
        print(f"Error: {response.status_code}. Something went wrong.")
        #prints the error meaning for status code 400
        if(response.status_code == 400):
            print(f"Bad Request")
        #prints the error meaning for status code 401
        if(response.status_code == 401):
            print(f"Unauthorized")
        #prints the error meaning for status code 404
        if(response.status_code == 404):
            print(f"Bad Response")
        

if __name__ == '__main__':
    # TODO: Prompt the user to input a city name.
    cityInput = input("Please input a city name: ")


    # TODO: Call the 'get_weather' function with the city name provided by the user.
    get_weather(cityInput)
    pass
