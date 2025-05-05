import utils

keys, values = utils.get_population()
print(keys, values)
print(utils.A)

data = [
    {
        'Country': 'Colombia',
        'Population': 300
    },
    {
        'Country': 'Bolivia',
        'Population': 400
    },
    {
        'Country': 'Ecuador',
        'Population': 500
    },
    {
        'Country': 'España',
        'Population': 600
    }
]

country = input('Que país desea buscar? ')
result = utils.population_by_country(data, country)
print(result)