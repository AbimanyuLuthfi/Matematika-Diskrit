pip install pmdarima

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import mean_squared_error
from matplotlib import pyplot
import pmdarima as pm
from google.colab import drive
drive.mount('/content/drive')
import warnings
warnings.filterwarnings("ignore")

source = '/content/drive/MyDrive/Matdis/owid-covid-data.csv'
datacovid = pd.read_csv(source)

datacovid.info()
indonesia = datacovid[datacovid['location'] == 'Indonesia']                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
Mexico = datacovid[datacovid['location'] == 'Mexico']
Germany = datacovid[datacovid['location'] == 'Germany']
Colombia = datacovid[datacovid['location'] == 'Colombia']

IND = indonesia[indonesia['date'] >= '2021-06-01']
MEX = Mexico[Mexico['date'] >= '2021-06-01']
DEU = Germany[Germany['date'] >= '2021-06-01']
COL = Colombia[Colombia['date'] >= '2021-06-01']

plt.plot(IND['date'], IND['total_deaths'])
plt.plot(MEX['date'], MEX['total_deaths'])
plt.plot(DEU['date'], DEU['total_deaths'])
plt.plot(COL['date'], COL['total_deaths'])
plt.legend(['Indonesia', 'Mexico', 'Germany', 'Colombia'])
plt.show()
