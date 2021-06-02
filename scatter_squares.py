import matplotlib.pyplot as plot


x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]


plot.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolor='none',  s=40)

# Set chart title and label axes.
plot.title("Square Numbers", fontsize=24)
plot.xlabel("Value", fontsize=14)
plot.ylabel("Square of Value", fontsize=14)


# Set the range ofr each exis.
plot.axis([0, 1100, 0, 1100000])

# Set size of tick labels.
plot.tick_params(axis='both', which='major', labelsize=14)

plot.show()
