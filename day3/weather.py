import requests

woeid = 1132599

url = f'https://www.metaweather.com/api/location/{woeid}/'

response = requests.get(url).json()

weather =response['consolidated_weather'][2]['weather_state_name']

print(f'서울의 모레 날씨는 {weather}로 예상됩니다.')