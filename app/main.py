import utils
import read_csv
import charts



def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))
  country =  input('Type Country => ')

  #if country == 'World':
  labels, values = utils.get_perc_world(data)
  charts.generate_pie_chart(labels, values)

  
  #else:
  result = utils.population_by_country(data, country)
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)

 #'''


###Permite controlar la ejecucion
if __name__ == '__main__':
  run()
