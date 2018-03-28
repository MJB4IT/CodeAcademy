from matplotlib import pyplot as plt

days = [0, 1, 2, 3, 4, 5, 6]
money_spent = [10, 12, 12, 10, 14, 22, 24]
money_earned = [25, 15, 10, 20, 15, 30, 25]

#Show days on x-axis and money_spent on y-axis
plt.plot(days, money_spent, color = 'red', linestyle = '--')
plt.plot(days, money_earned, color = 'green', marker = 's')  #additional point of coverage on graph (green line)
plt.axis([0, 6, 10, 30])  #to zoom
plt.xlabel('Time')
plt.ylabel('Earned')
plt.title('Money Earned and Money Spent Over 6 Days')

plt.show()

print(money_spent)
