import requests

API_KEY = '7336babd2ce61f8563de4fb7f514319f'

city_name = input('Enter a City Name: ')

API_URL = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
try:
    response = requests.get(API_URL).json()

    todays_weather = response['weather'][0]['description']

    print(f"Today Weather Seems Like:  {todays_weather} ")
except requests.exceptions.ConnectionError:
    print("Un Expected error !! Check Your Internet or may be server down")
except:
    print("Please provide valid city name")
