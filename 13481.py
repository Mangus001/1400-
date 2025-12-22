def get_capital(country):
    return countries.get(country, 'Страна не найдена')

def get_country_by_capital(capital):
    for country, city in countries.items():
        if city == capital:
            return country
    return 'Город не найден'
