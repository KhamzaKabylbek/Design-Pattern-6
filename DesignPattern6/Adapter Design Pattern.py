from abc import ABC, abstractmethod

class WeatherData:
    def __init__(self, temperature, humidity, wind_speed):
        self.temperature = temperature
        self.humidity = humidity
        self.wind_speed = wind_speed

class WeatherAPI(ABC):
    @abstractmethod
    def get_weather_data(self):
        pass

class OpenWeatherMapAPI(WeatherAPI):
    def get_weather_data(self):
        return {
            'temp': 20,
            'humidity': 60,
            'wind_speed': 10
        }

class WeatherAdapter:
    def __init__(self, weather_api):
        self.weather_api = weather_api

    def get_weather_data(self):
        api_data = self.weather_api.get_weather_data()
        temperature = api_data['temp']
        humidity = api_data['humidity']
        wind_speed = api_data['wind_speed']
        return WeatherData(temperature, humidity, wind_speed)

if __name__ == "__main__":
    open_weather_map_api = OpenWeatherMapAPI()
    weather_adapter = WeatherAdapter(open_weather_map_api)

    weather_data = weather_adapter.get_weather_data()

    print("Temperature:", weather_data.temperature)
    print("Humidity:", weather_data.humidity)
    print("Wind Speed:", weather_data.wind_speed)
