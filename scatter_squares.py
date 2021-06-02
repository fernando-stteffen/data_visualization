import matplotlib.pyplot as plot


x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]


plot.scatter(x_values, y_values,  s=100)

# Set chart title and label axes.
plot.title("Square Numbers", fontsize=24)
plot.xlabel("Value", fontsize=14)
plot.ylabel("Square of Value", fontsize=14)


# Set size of tick labels.
plot.tick_params(axis='both', which='major', labelsize=14)

plot.show()
