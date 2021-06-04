import pygal
from die import Die


# Create Dices
die_1 = Die(8)
die_2 = Die(8)
max_result = die_1.num_sides + die_2.num_sides
roll_times = 100000000

# Make some rolls, and store results in a list
results = []
for roll_num in range(roll_times):
    result = die_1.roll() + die_2.roll()
    results.append(result)
    
    
# Analyze the results.
frequencies = []

for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

    
    
# Visualize the results.
historic = pygal.Bar()
str_roll_times = str("{:,}".format(roll_times))
str_d1 = "D" + str(die_1.num_sides)         
str_d2 = "D" + str(die_2.num_sides)    
            
historic.title = ("Results of rolling a " + 
        str_d1 + " and a " + str_d2  + " " +
        str_roll_times + " times.")
        
labels = list(range(2,max_result+1))

historic.x_labels = labels
historic.x_title = "Result"
historic.y_title = "Frequency of Result"

historic.add(str_d1 + "+" + str_d2, frequencies)
historic.render_to_file('die_visual.svg')



