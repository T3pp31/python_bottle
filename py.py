import requests


def weather_command():
    base_url = "http://weather.livedoor.com/forecast/websercive/json/v1"
    city_code = "130010"
    url = "{}?city={}".format(base_url, city_code)
    r = requests.get(url)
    weather_data = r.json()
    city = weather_data["location"]["city"]
    label = weather_data["forecasts"][0]["dateLabel"]
    telop = weather_data["forecasts"][0]["telop"]

    response = "{}の{}の天気は「{}」です".format(city, label, telop)
    return response

response = weather_command()
print(response)