from bs4 import BeautifulSoup
import requests
import pandas as pd
import io
import codecs
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path


pd.options.mode.chained_assignment = None  # default='warn'

import statsmodels.api as sm


# +
achat = pd.read_csv('csv/tableau_achat.csv')
data = pd.read_csv('csv/tableau_final.csv')

data['Date'] = pd.to_datetime(data.Date)
data['Date'] = data['Date'].dt.strftime('%m/%Y')

for el in data.variable.unique():
    for elt in achat.variable.unique():
        data_el = data[data['variable'] == el]
        data_achat = achat[achat['variable'] == elt]
        data_el['value']= pd.to_numeric(data_el['value'])
        data_achat['value'] = pd.to_numeric(data_achat['value'])
        data_el_array = data_el['value'].to_numpy()
        data_achat_array = data_achat['value'].to_numpy()
        correl = sm.tsa.stattools.ccf(data_el_array, data_achat_array, adjusted=False)
        plt.figure()
        plt.title('Correlation ' + el + ' avec ' + elt)
        plt.xlabel('lag (month)')
        plt.ylabel('coefficient de correlation')
        plt.plot(range(len(correl)), correl)
    
