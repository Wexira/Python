import pyowm

owm = pyowm.OWM('49877e0901f8715065b4e76841918c56',
                language="ru")  # You MUST provide a valid API key

place = input("В каком городе/стране?: ")

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place(place)
w = observation.get_weather()

temp = w.get_temperature('celsius')[
    "temp"]  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}

print("В городе " + place + " сейчас " + w.get_detailed_status())
print("Температура сейчас в районе " + str(temp))

if temp < 10:
    print("Сейчас ппц как холодно, одевайся как танк!")
elif temp < 20:
    print("Сейчас холодно, оденься потеплее.")
else:
    print("Температура норм, одевай что угодно")
