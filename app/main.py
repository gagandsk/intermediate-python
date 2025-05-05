import utils

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

def run():
    keys, values = utils.get_population()
    print(keys, values)


    country = input('Que país desea buscar? ')
    result = utils.population_by_country(data, country)
    print(result)
    
#si es ejecutado desde la terminal, que ejecute el metodo 'run'
if __name__ == '__main__':
    run()