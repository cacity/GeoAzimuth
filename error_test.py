import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np 
from datetime import datetime 

data = pd.read_csv('https://raw.githubusercontent.com/SolaireOAstora/PythonPlotDemoMaterials/master/NYTemperature2019.csv')

data_str = data['DATE'].to_numpy()
TMIN = data['TMIN'].to_numpy()
TMAX = data['TMAX'].to_numpy()
TAVG = data['TAVG'].to_numpy()

nrec = len(TAVG)
 
dt_str_arr = np.zeros(nrec, dtype = object)

yday_arr = np.zeros(nrec, dtype = int)
month_arr = np.zeros(nrec, dtype = int)


for i in range(nrec):
    dt = datetime.strptime(data_str[i], '%Y-%m-%d')
    dt_str_arr[i]= dt.strftime('%b-%d')

    dt_struct = dt.timetuple()
    yday_arr[i] = dt_struct.tm_yday
    month_arr[i] = dt_struct.tm_mon

    print(yday_arr)
    print(month_arr)


# print(dt_str_arr)

yerr = np.zeros([2,nrec])

yerr[0,:] = TAVG - TMIN
yerr[1,:] = TMAX -TAVG


fig = plt.figure(figsize= [8,5])
sub =fig.add_subplot(111)

sub.errorbar(np.arange(0,7), TAVG[0:7],yerr[:,0:7])

sub.set_xticks(np.arange(0,7))
sub.set_xticklabels(data_str[0:7])

sub.set_xlabel('Date', fontsize = 15)
sub.set_ylabel('Temperature of NY', fontsize=15)
plt.show()