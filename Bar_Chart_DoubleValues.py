from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 = [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]
sales3 = [100, 36, 57, 68, 88, 105]

# Code below can be used for as many additional bars as needed
n = 1  # This is our first dataset (out of 3)
t = 3 # Number of datasets i.e. sales1 & sales2 & sales3
d = 6 # Number of sets of bars 6 values per list
w = 0.8 # Width of each bar
store1 = [t*element + w*n for element
             in range(d)]

plt.bar(store1, sales1)

n = 2  # This is our second dataset (out of 3)
t = 3 # Number of datasets i.e. sales1 & sales2 & sales3
d = 6 # Number of sets of bars
w = 0.8 # Width of each bar
store2 = [t*element + w*n for element
             in range(d)]

plt.bar(store2, sales2)


# Show the bar chart containing 3 bars representing each store
plt.show()