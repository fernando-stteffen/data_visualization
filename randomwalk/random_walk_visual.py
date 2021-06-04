import matplotlib.pyplot as plot

from random_walk import RandomWalk


# Keep making new walks
while True:
    # Make a random walk, and plot the points
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    # Set the size of the plotting window
    # ~ plot.figure(figsize=(20,12))

    point_numbers = list(range(rw.num_points))
    plot.scatter(rw.x_values, rw.y_values, c=point_numbers, 
                 cmap=plot.cm.Blues, edgecolors='none', s=1)
    
    # Mark the first and last points
    plot.scatter(0, 0, c='green', edgecolors='none', s=100)
    plot.scatter(rw.x_values[-1], rw.y_values[-1], c='red', 
                 edgecolors='none', s=100)
                 
    # Remove the axes.
    plot.axis('off')
    
    plot.show()
    
    keep_running = input("Make another walk? (y/n): ")
    while keep_running != 'y' and keep_running != 'n':
        keep_running = input("Make another walk? (y/n): ")
    
    if keep_running == 'n':
        break
