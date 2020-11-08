# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 10:15:20 2020

@author: Pierre-Henri Rossouw

Global Covid-19 Statistics from the ECDC

"""

import pandas as pd

x=input("What countries data would you like to get? ")

url = 'https://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide.xlsx'
df_raw = pd.read_excel(url)

df_raw['countriesAndTerritories'].unique()
df = df_raw

df = df[df['countriesAndTerritories']==x]

df = df.sort_values(['month', 'deaths' ,'cases'], ascending=[1, 1, 1])

df['month'] = pd.to_datetime(df[['year', 'month' ,'day']])


ax = df.plot(x='month', y = ['cases','deaths'], title = 'Covid Statistics for '+x, figsize=(10,5), grid=True)
ay = df.plot(x='month', y = 'cases', title = 'Covid Statistics for '+x, figsize=(10,5), grid=True)
az = df.plot(x='month', y = 'deaths', title = 'Covid Statistics for'+x, figsize=(10,5), grid=True)
