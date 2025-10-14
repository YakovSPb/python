# Словари 

countries = {
    'code': 'RU',
    'name': 'Russion',
    'population': 144
}


# countries = dict(
#     code = 'RU',
#     name = 'Russion',
#     population = 144
# )

print(dict)

for key, value in countries.items(): 
    print(key, ' - ', value)

# удаление
# countries.clear()
# countries.pop('name')

# print(countries.get('code'))


person = {
    'user_1': {
        'first_name': 'Jon',
        'last_name': 'Marley',
        'age': 45,
        'address': ['r.Москва', 'ул. Крин', '45'],
        'grades': {'math': 5, 'physics': 3}

    },
    'user_2':{

    }
}

print(person['user_1']['address'][1])