import streamlit as st
import requests

API_KEY = "2606f769271b8d545fe3458b2b72ed9f"
API_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

def main():
    st.title('Weather Checker Application')

    city = st.text_input('Enter city name:')
    if city:
        weather_data = get_weather(city)
        if weather_data:
            st.write(f"Weather in {city}:")
            st.write(f"Temperature: {weather_data['main']['temp']}°C")
            st.write(f"Description: {weather_data['weather'][0]['description']}")
            st.write(f"Humidity: {weather_data['main']['humidity']}%")
            st.write(f"Wind Speed: {weather_data['wind']['speed']} m/s")
        else:
            st.write("Failed to retrieve weather data. Please try again.")

if __name__ == "__main__":
    main()
