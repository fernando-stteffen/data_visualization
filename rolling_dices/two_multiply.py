import pygal
from die import Die


def get_str_d(dice):
    return "D" + str(die_1.num_sides)


# Configs
die_1 = Die()
die_2 = Die()
roll_times = 1000000

# Constants
num_dices = 2
max_result = die_1.num_sides * die_2.num_sides
min_result = 1


# Calcuating
results = []
for roll_num in range(roll_times):
    result = die_1.roll()
    result *= die_2.roll()
    results.append(result)


# Labels to plot and count frequency
labels = list(range(min_result, max_result+1))

# Merge results
frequencies = []
for value in labels:
    frequency = results.count(value)
    frequencies.append(frequency)


# Visualize the results.
chart = pygal.Bar()

str_roll_times = str("{:,}".format(roll_times))
str_d1 = get_str_d(die_1)         
str_d2 = get_str_d(die_2)

chart.title = "Results of rolling a "
chart.title += str_d1 + " and a " + str_d2
chart.title += " " + str_roll_times + " times."

chart.x_labels = labels
chart.x_title = "Results"
chart.y_title =  " Frequency "

chart.add(str_d1 + "*" + str_d2, frequencies)
chart.render_to_file('die_visual.svg')



