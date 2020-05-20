FROM python:3.8

RUN apt-get update && apt-get install -y vim curl jq
RUN pip3 install graphyte requests
RUN mkdir /code
COPY current_weather.py /code/current_weather.py
COPY get_forecast.py /code/get_forecast.py
COPY runner.sh /code/runner.sh
WORKDIR /code
CMD  "./runner.sh"
