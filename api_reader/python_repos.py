import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS



# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
response = requests.get(url)
print("Status code:", response.status_code)

response_dictionary = response.json()


# Process results.
print("Total repositories:", response_dictionary['total_count'])


# Explore information about the repositories.
repositories_dictionaries = response_dictionary['items']

names, stars = [], []




print("\nSelected information about first repository:")
for repository_dict in repositories_dictionaries:
    names.append(repository_dict['name'])
    stars.append(repository_dict['stargazers_count'])
    
    
chart_style = LS('#333366', base_style=LCS)

chart_config = pygal.Config()
chart_config.x_label_rotation = 45
chart_config.show_legend = False
chart_config.title_font_size = 24
chart_config.label_font_size = 14
chart_config.major_label_font_size = 18
chart_config.truncate_label = 15
chart_config.show_y_guides = False
chart_config.width = 1000





chart = pygal.Bar(chart_config, style=chart_style)
chart.title = "Most-starred Python projects on Github"
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')

