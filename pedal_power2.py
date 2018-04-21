import pandas as pd

inventory = pd.read_csv('inventory.csv')
print(inventory.head(10))

staten_island = inventory.head(10)
product_request = staten_island['product_description']

#select all rows from location Brookly with product_type of seeds
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]
print(seed_request)

inventory['in_stock'] = inventory.quantity.apply(lambda s: 'True' if s > 0 else 'False')

inventory['total_value'] = inventory['price'] * inventory['quantity']

combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda, axis=1)
print(inventory)