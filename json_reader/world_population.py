import pygal
import json
from countries_code import get_country_code


# Load data
filename = "population_data.json"

with open(filename) as f:
    population_data = json.load(f)
    

# Print the 2010 population for each country.
countrycode_populations = {}
for population in population_data:
    if population['Year'] == '2010':
        country_name = population['Country Name']
        population_total = int(float(population['Value']))
        code = get_country_code(country_name)
        if code:
            countrycode_populations[code] = population_total
        

world_map = pygal.maps.world.World()
world_map.title = "World population in 2010, by country"
world_map.add('2010', countrycode_populations)

world_map.render_to_file('world_population.svg')
            

