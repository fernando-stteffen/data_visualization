import pygal
from pygal.style import LightColorizedStyle, RotateStyle
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

# Group the countries into three populations levels

populations_level_1, populations_level_2, populations_level_3, = {}, {}, {}

for country_code, population in countrycode_populations.items():
    
    if population < 10000000:
        populations_level_1[country_code] = population
    elif population < 1000000000:
        populations_level_2[country_code] = population
    else:
        populations_level_3[country_code] = population
        
print(
    len(populations_level_1), 
    len(populations_level_2), 
    len(populations_level_3)
)



world_map_style = RotateStyle('#336699', base_style=LightColorizedStyle)
world_map = pygal.maps.world.World(style=world_map_style)
world_map.title = "World population in 2010, by country"
world_map.add('0-10m', populations_level_1)
world_map.add('10m-1b', populations_level_2)
world_map.add('>1b', populations_level_3)

world_map.render_to_file('world_population.svg')
            

