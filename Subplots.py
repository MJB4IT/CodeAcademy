from matplotlib import pyplot as plt

months = range(12)
temps = [60, 70, 90, 85, 77, 90, 88, 92, 78, 85, 91, 79]
flight_prices = [450, 525, 800, 790, 910, 820, 800, 850, 715, 875, 1025, 715]

plt.subplot(1, 2, 1)         #1st plot in a figure with 1 row and 2 columns
plt.plot(months, temps)

plt.subplot(1, 2, 2)      #2nd plot in a figure with 1 row and 3 columns will display to the right of the initial plot
plt.plot(temps, flight_prices, marker='o')    #'o' makes this a scatter plot

plt.show()

