def get_population(country_dict):
  #keys = ['col', 'bol']
  #values = [300, 400]
  population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
   }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values 

def population_by_country(data, country):
  result = list(filter(lambda item: item['Country/Territory'] == country, data))
  return result

def get_perc_world(data):
  perc_world = {
    item['Country/Territory']: item['World Population Percentage'] for item in data
  }
  labels = perc_world.keys()
  values = perc_world.values()
  #labels = list(map(lambda x : x['Country/Territory'], data))
  #values = list(map(lambda y : y['World Population Percentage'], data))
  return labels, values 