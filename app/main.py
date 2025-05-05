import utils
import read_csv
import charts

def run():
    
  data = read_csv.read_csv('data_set2.csv')
  data = list(filter(lambda item : item['Continent'] == 'Europe',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)
    
  '''
  country = input('Type Country => ')

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_pie_chart(labels, values)
  '''
    
#si es ejecutado desde la terminal, que ejecute el metodo 'run'
if __name__ == '__main__':
    run()