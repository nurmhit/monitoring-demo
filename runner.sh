#!/bin/bash
echo "Starting script"
while true
do
    python3 current_weather.py
    python3 get_forecast.py
    sleep 10
done
