# -*- coding: utf-8 -*-
# +

from bs4 import BeautifulSoup
import requests
import pandas as pd
import io
import codecs
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
import os
import statsmodels.api as sm

pd.options.mode.chained_assignment = None  # default='warn'

#on recupere les données extraites
achat = pd.read_csv('data_extraite/tableau_achat.csv')
data = pd.read_csv('data_extraite/tableau_final.csv')

#on met au bon format de date
data['Date'] = pd.to_datetime(data.Date)
data['Date'] = data['Date'].dt.strftime('%m/%Y')

print('analyse de correlation croisée et tracé dans results')
for el in data.variable.unique():
    print('analyse pour : ' + el)
    os.makedirs('results/Correlations avec '+ el.replace('/', '_'), exist_ok=True)
    for elt in achat.variable.unique():
        #on selectionne les donnees apres 2020
        data_el = data[data['variable'] == el]
        data_el = data_el[data_el['Date'].str[3:].astype(int)>=2020]
        data_achat = achat[achat['variable'] == elt]
        data_achat = data_achat[data_achat['Date'].str[3:].astype(int)>=2020]
        #on convertit string en float 
        data_el['value']= pd.to_numeric(data_el['value'])
        data_achat['value'] = pd.to_numeric(data_achat['value'])
        #on convertit les tableaux en array pour analyse
        data_el_array = data_el['value'].to_numpy()
        data_achat_array = data_achat['value'].to_numpy()
        #analyse de correlation croisee
        correl = sm.tsa.stattools.ccf(data_el_array, data_achat_array, adjusted=False)
        #tracé et enregistrement
        plt.figure()
        plt.title('Correlation ' + el + ' avec ' + elt)
        plt.xlabel('lag (month)')
        plt.ylabel('coefficient de correlation')
        plt.plot(range(len(correl)), correl)
        plt.savefig("results/Correlations avec " +el.replace('/', '_') + '/' + elt.replace('/', '_') + ".png")
print('analyse de correlation croisée et tracé dans results : fini')

