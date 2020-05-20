import requests
import graphyte


api_key = 'lcVaF0Mo7yVJGTJNAkWZKOSJZ3ISrKDL'

site = 'http://dataservice.accuweather.com/currentconditions/v1/308526'

params = {'apikey': api_key, 'language': 'en-us'}

def get_forecast():
    response = requests.get(site, params).json()
    return {'temp': response[0]['Temperature']['Imperial']['Value']}


def send_forecast(forecast):
    sender = graphyte.Sender("graphite", prefix='weather')
    value = forecast["temp"]
    metric_name = "current.{}".format("temp")
    print(metric_name, value)
    sender.send(metric_name, value)


def main():
    send_forecast(get_forecast())


if __name__ == '__main__':
    main()
