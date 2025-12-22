countries_info = [
    {
        'name': 'Германия',
        'capital': 'Берлин',
        'region': 'Европа',
        'population': 83,
        'area': 357.4
    }
]
def get_capital_by_name(name):
    for c in countries_info:
        if c['name'] == name:
            return c['capital']
    return 'Страна не найдена'
