import requests
import json

url = "https://api.open-meteo.com/v1/forecast?timezone&latitude=28.6353&longitude=77.2250&current_weather&hourly=temperature_2m"

r = requests.get(url)
print(r.status_code)

dict = json.loads(r.text)


def timeread(timenow):
    list = timenow.split("T")
    print(list[0])
    print(list[1])

# print(type(dict))
data_index = 0
while (data_index < 24*7):
    timenow = dict["hourly"]["time"][data_index]
    timeread(timenow)
    temp = dict["hourly"]["temperature_2m"][data_index]
    print(f"Time : {timenow} Temperature: {temp}")
    data_index+=24

