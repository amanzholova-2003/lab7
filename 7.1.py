n = int(input())
countries = {}
for i in range(n):
    # Считываем строку вида "Страна: река1, река2, ..."
    country_data = input().split(": ")
    # Разделяем названия рек и сохраняем их в списке
    rivers = country_data[1].split(", ")
    # Записываем название страны и список рек в словарь
    countries[country_data[0]] = rivers

river_names = input().split(", ")

#вывод стран, в которых протекает каждая река
for river_name in river_names:
    for country_name, rivers in countries.items():
        if river_name in rivers:
            print(f"{river_name} протекает в {country_name}")

#проверка наличия реки в словаре
check_river_name = input()
if any(check_river_name in rivers for rivers in countries.values()):
    print(f"Река {check_river_name} присутствует в словаре")
else:
    print(f"Река {check_river_name} отсутствует в словаре")

#добавление новой пары страна-река в словарь
new_country_name, new_river_name = input().split(": ")
if new_country_name in countries:
    countries[new_country_name].append(new_river_name)
else:
    countries[new_country_name] = [new_river_name]

print(countries)