import pandas as pd

mb = pd.read_csv('customers.csv')

print(mb.head())

mb.columns = ['Customer Id', 'First Name', 'Last Name', 'Address', 'City', 'State', 'Zip', 'Gender']

print(mb)

mb['Salutation'] = mb.Gender.apply(lambda s: 'Mr.' if s == 'M' else 'Ms.')  #checks the gender column and applies value based on it's contents

print(mb)
