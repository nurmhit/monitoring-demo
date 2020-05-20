import requests
import graphyte


api_key = 'lcVaF0Mo7yVJGTJNAkWZKOSJZ3ISrKDL'

forecast_site = 'http://dataservice.accuweather.com/forecasts/v1/hourly/1hour/308526'

params = {'apikey': api_key, 'language': 'en-us'}

def get_forecast():
    request = forecast_site
    response = requests.get(request, params).json()
    return {'temp': response[0]['Temperature']['Value']}


def send_forecast(forecast):
    sender = graphyte.Sender("graphite", prefix='weather')
    value = forecast['temp']
    metric_name = "forecast.{}".format('temp')
    print(metric_name, value)
    sender.send(metric_name, value)


def main():
    send_forecast(get_forecast())


if __name__ == '__main__':
    main()
