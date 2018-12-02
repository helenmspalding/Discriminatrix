import pandas as pd

import numpy as np
# import json


industry = pd.read_csv('Industry.csv')
codenumber= industry["Code"]
sectionrow = industry.loc[codenumber.str.startswith("Secti")].index.values.astype(int)#[0]
# print sectionrow
industrynames = industry["Description"].iloc[sectionrow].tolist()
industrydict = {}
industryaverages = {}

for i in range(len(industrynames)):  #creates dictionary with key = industry and values = codes
    if i == len(sectionrow)-1:
        industrydict['%s' % industrynames[i]] = codenumber[sectionrow[i] + 1:].tolist()
    else:
        industrydict['%s' % industrynames[i]] = codenumber[sectionrow[i]+1:sectionrow[i+1]].tolist()
