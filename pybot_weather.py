import requests

def weather_command():
    base_url="http://weather.livedoor.com/forecast/webservice/json/v1"
    city_code = "130010"
    url="{}?city={}".format(base_url,city_code)
    weather_data = requests.get(url).json()

    city=weather_data['location']['city']
    label = weather_data['forecasts'][0]['dateLabel']
    telop = weather_data['forecasts'][0]['telop']
    description = weather_data["description"]["text"]
  
    response ="{}の{}の天気は「{}」です\n詳細はこちら→{}".format(city,label,telop,description)
    return response
