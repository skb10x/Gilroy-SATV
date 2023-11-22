Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
... import json
... 
... def get_temperature(api_key, city, country):
...     url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country}&appid={api_key}&units=metric"
...     response = requests.get(url)
...     data = response.json()
... 
...     if "main" in data:
...         return data["main"]["temp"]
... 
...     return None
... 
... api_key = input("be31db6602e1819b4c7cfd6ce7685bbd")
... city = "Buenos Aires"
... country = "AR"
... 
... temperature = get_temperature(api_key, city, country)
... print(temperature)
