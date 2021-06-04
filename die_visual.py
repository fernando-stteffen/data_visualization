import pygal
from die import Die


# Create a D6.
die = Die()


# Make some rolls, and store results in a list
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)
    
    
# Analyze the results.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

    
    
# Visualize the results.
historic = pygal.Bar()

historic.title = "Results of rolling one D6 1000 times."
historic.x_labels = ['1','2','3','4','5','6']
historic.x_title = "Result"
historic.y_title = "Frequency of Result"

historic.add('D6', frequencies)
historic.render_to_file('die_visual.svg')

