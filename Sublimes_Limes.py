from matplotlib import pyplot as plt

# Variables for the project
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]


# Sets figure size to width 12 and height 8
plt.figure(figsize=(12, 8))

# Left subplot charting area of 1 row, 2 columns
ax1 = plt.subplot(1, 2, 1)
plt.title('Number of Customer Visits')     #title of left subplot

x_values = range(len(months))
plt.plot(x_values, visits_per_month, marker = 'o')

plt.xlabel('Months')
plt.ylabel('Number of Visits')

ax1.set_xticks(x_values)
ax1.set_xticklabels(months)

# Right subplot charting area
bx1 = plt.subplot(1, 2, 2)
plt.title('Monthly Sales of Limes by Type')        #title of right subplot

# Number of each type of lime sold
plt.plot(x_values, key_limes_per_month, color = 'green')
plt.plot(x_values, persian_limes_per_month, color = 'orange')
plt.plot(x_values, blood_limes_per_month, color = 'red')


bx1.set_xticks(x_values)
bx1.set_xticklabels(months)

bx1.legend(['Key Limes', 'Persian Limes', 'Blood Limes'], loc = 1)


plt.subplots_adjust(wspace = 0.35, bottom = 0.2)

# Show the subplots
plt.show()

# Save the figure
plt.savefig('sublimes_project.png')