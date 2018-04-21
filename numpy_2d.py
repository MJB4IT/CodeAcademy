import numpy as np

multi_array = [[1, 5, 10],
               [2, 4, 6],
               [3, 6, 9]]

#print(multi_array)

new_array = np.array(multi_array)
#print(new_array)

second_column = new_array[:,1]
#print(second_column)

third_row = new_array[2:,]
#print(third_row)

middle_element = new_array[1,1] #should be 4
print(middle_element)

bottom_right = new_array[2,2]      #should be 9
print(bottom_right)

third_column = new_array[:,2]
print(third_column)

bottom_two_third_column = new_array[1:,2]
print(bottom_two_third_column)