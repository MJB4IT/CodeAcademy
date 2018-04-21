import pandas as pd

pv = pd.read_csv('cust.csv')

print(pv.head())

print(
    pv.groupby('Page Visited')\
      .First_Name.count()\
      .reset_index()\
      .rename(columns = {'First_Name': 'Number of Visitors'})
)