import pandas as pd

inventory = pd.read_csv('inventory.csv')
print(inventory.head(10))       #print out first 10 rows of the dataframe

chicago = inventory.head(10)

inventory['in_stock'] = inventory.quantity.apply(lambda q: 'True' if q > 0 else 'False') #new column(in_stock)

inventory['total_value'] = inventory['quantity'] * inventory['price']

gary_seeds = [(inventory.location == 'Gary') & (inventory.product_type == 'seeds')]
print(gary_seeds)
