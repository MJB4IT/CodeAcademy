import pandas as pd
import numpy as np

orders = pd.read_csv('inventory.csv')
print(orders.head(12))

most_expensive = orders.price.max()
num_products = orders.product_type.nunique()
print('The most expensive pair costs ' + str(most_expensive))
print('Number of product types is ' + str(num_products))

pricey_products = orders.groupby('product_type').price.max()  # aggregate function calculation

print(pricey_products)
print(type(pricey_products))

# Use lambda for more complex statistical functions.  Below calcs the 25th percentile
cheap_products = orders.groupby('product_type').price.apply(lambda mb: np.percentile(mb, 25)).reset_index()
print(cheap_products)

product_grouping = orders.groupby(['product_type', 'product_description']).id.count().reset_index()
print(product_grouping)

product_pivot = product_grouping.pivot(columns ='product_description',
                                       index = 'product_type',
                                       values = 'id').reset_index()
print(product_pivot)
