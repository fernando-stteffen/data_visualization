import matplotlib.pyplot as plot


x_values = [1, 2, 3, 4, 5]
y_values = [1, 8, 27, 64, 125]


plot.scatter(x_values, y_values, c='green', s=40)
plot.title("Cubic Numbers", fontsize=24)

plot.xlabel("Value", fontsize=14)
plot.ylabel("Value Cubic", fontsize=14)

plot.show()

x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]


plot.scatter(x_values, y_values, c=y_values, cmap=plot.cm.Greens, s=40)

plot.title("Cubic Numbers", fontsize=24)
plot.xlabel("Value", fontsize=14)
plot.ylabel("Value Cubic", fontsize=14)

plot.axis([0, 5000, 0, 5000**3])
plot.tick_params(axis='both', which='major', labelsize=14)

plot.show()
