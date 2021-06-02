import matplotlib.pyplot as plot

plot.scatter(2, 4, s=200)

# Set chart title and label axes.
plot.title("Square Numbers", fontsize=24)
plot.xlabel("Value", fontsize=14)
plot.ylabel("Square of Value", fontsize=14)


# Set size of tick labels.
plot.tick_params(axis='both', which='major', labelsize=14)

plot.show()
