from matplotlib import pyplot as plt
import numpy as np

top_vacation_destinations = ['Cairo', 'Paris', 'Rome', 'Dubai', 'London', 'Other']
vacation_destination_freqs = [55, 120, 200, 180, 95, 75]

plt.pie(vacation_destination_freqs, autopct='%0.2f%%')  #will show percentages out to 2 decimal as ex. 5.10%
plt.axis('equal')
plt.legend(top_vacation_destinations)

plt.show()