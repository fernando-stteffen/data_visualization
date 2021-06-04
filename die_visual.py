import pygal
from die import Die


# Create a D6.
die_1 = Die()
die_2 = Die()


# Make some rolls, and store results in a list
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
    
# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(1, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

    
    
# Visualize the results.
historic = pygal.Bar()

historic.title = "Results of rolling two D6 1000 times."
labels = list(range(2,13))

historic.x_labels = labels
historic.x_title = "Result"
historic.y_title = "Frequency of Result"

historic.add('D6 + D6', frequencies)
historic.render_to_file('die_visual.svg')

