import csv
from matplotlib import pyplot as plot
from datetime import datetime

filename = 'death_valley_2014.csv'


# Import data from file

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    

# Plot data.
fig = plot.figure(dpi=128, figsize=(20,6))
plot.plot(dates, highs, c='red', alpha=0.5)
plot.plot(dates, lows, c='blue', alpha=0.5)
plot.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format Plot
plot.title("Daily high  and low temperatures - 2014\n Death Valley, CA", fontsize=24)
plot.xlabel('', fontsize=16)
fig.autofmt_xdate()
plot.ylabel('Temperature (F)', fontsize=16)
plot.tick_params(axis='both', which='major', labelsize=16)


plot.show()
