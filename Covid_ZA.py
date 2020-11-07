# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 10:15:20 2020

@author: Pierre-Henri Rossouw
"""

import pandas as pd

url = 'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide.xlsx'
df_raw = pd.read_excel(url)

df_raw['countriesAndTerritories'].unique()
df = df_raw

df = df[df['countriesAndTerritories']=='South_Africa']

df = df.sort_values(['month', 'deaths' ,'cases'], ascending=[1, 1, 1])

df['month'] = pd.to_datetime(df[['year', 'month' ,'day']])


ax = df.plot(x='month', y = ['cases','deaths'], title = 'Covid Statistics for South Africa', figsize=(10,7), grid=True)
ad = df.plot(x='month', y = 'cases', title = 'Covid Statistics for South Africa in 2020', figsize=(10,7), grid=True)
az = df.plot(x='month', y = 'deaths', title = 'Covid Statistics for South Africa in 2020', figsize=(10,7), grid=True)
