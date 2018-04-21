import numpy as np

cupcakes = np.array([2, 0.75, 2, 1, 0.5])
print(cupcakes)

recipes = np.genfromtxt('recipes.csv', delimiter = ',')
print(recipes)

eggs = recipes[:,2]
print(eggs)

print(recipes[:,2] == 1)    #gives you a True False boolean for each value based on the condition
#print('new', new_var)

cookies = recipes[2]
print(cookies)

