employees = [
    {'фамилия': 'Иванов', 'возраст': 25, 'военнообязанный': True},
    {'фамилия': 'Петров', 'возраст': 30, 'военнообязанный': False},
    {'фамилия': 'Сидоров', 'возраст': 22, 'военнообязанный': True},
]

military = [e for e in employees if e['военнообязанный']]
min_age_military = min(e['возраст'] for e in military)
youngest_military = next(e for e in military if e['возраст'] == min_age_military)
print('Фамилия самого младшего военнообязанного:', youngest_military['фамилия'])

max_age_military = max(e['возраст'] for e in military)
oldest_military = [e for e in military if e['возраст'] == max_age_military]
print('Фамилии самых старших военнообязанных:', [e['фамилия'] for e in oldest_military])

non_military = [e for e in employees if not e['военнообязанный']]
max_age_non_military = max(e['возраст'] for e in non_military)
oldest_non_military = [e for e in non_military if e['возраст'] == max_age_non_military]
print('Фамилии самых старших невоеннообязанных:', [e['фамилия'] for e in oldest_non_military])
