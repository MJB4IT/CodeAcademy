import pandas as pd

city_pops = pd.DataFrame([[10, 'Chicago', 5],
                         [35, 'Los Angeles', 8],
                         [40, 'San Francisco', 10],
                         [50, 'Dallas', 4]],
                         columns=['City Number', 'City Name', 'Population in Millions'])

print(city_pops)

print(city_pops.info())