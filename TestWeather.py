import requests

print("------------------------------------------------")
city = input("Введите город (Пример: Kyiv): ")
appid = "a0d60f299cee3a1d0f3e7950a2649389"

data = (requests.get("http://api.openweathermap.org/data/2.5/weather", params = {'q': city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})).json()
print("------------------------------------------------")
print(data)
print("------------------------------------------------")
print("Погода для города: " + city)
print("------------------------------------------------")
print("Погодные условия:", data["weather"][0]["description"])
print("Текущая температура:", int(data["main"]["temp"]))
print("Минимальная температура на сегодня:", data["main"]["temp_min"])
print("Максимальная температура на сегодня:", data["main"]["temp_max"])
print("Давление: " + str(data["main"]["pressure"]) + " мм. ртутного столбика")
print("Влажность: " + str(data["main"]["humidity"]) + "%")
print("Скорость ветра: " + str(data["wind"]["speed"]) + " км/ч")
print("------------------------------------------------")
