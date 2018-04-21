import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())

views_by_plat = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(views_by_plat)

ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()
print(ad_clicks)

clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
print(clicks_by_source)

clicks_pivot = clicks_by_source.pivot(
  columns = 'is_click',
  index = 'utm_source',
  values = 'user_id').reset_index()
print(clicks_pivot)

clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[True] + clicks_pivot[False])
print(clicks_pivot)

ads_shown_by_group = ad_clicks.groupby('experimental_group').user_id.count().reset_index()
ads_shown_by_group.columns = ['Group', 'Number of Ads Shown']
print(ads_shown_by_group)

ab_click_perc = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
print(ab_click_perc)