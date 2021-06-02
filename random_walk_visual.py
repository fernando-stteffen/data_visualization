import matplotlib.pyplot as plot

from random_walk import RandomWalk


# Keep making new walks
while True:
    # Make a random walk, and plot the points
    rw = RandomWalk()
    rw.fill_walk()

    plot.scatter(rw.x_values, rw.y_values, s=15)
    plot.show()
    
    keep_running = input("Make another walk? (y/n): ")
    while keep_running != 'y' and keep_running != 'n':
        keep_running = input("Make another walk? (y/n): ")
    
    if keep_running == 'n':
        break
