
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

import matplotlib as mpl

import datetime as dt


from datetime import datetime
# import pylab as plt

# plt.rcParams['font.sans-serif'] = ['SimHei']

data_LA = pd.read_csv('https://raw.githubusercontent.com/SolaireOAstora/PythonPlotDemoMaterials/master/LATemperature2019.csv')

data_NY = pd.read_csv('https://raw.githubusercontent.com/SolaireOAstora/PythonPlotDemoMaterials/master/NYTemperature2019.csv')

data_LD = pd.read_csv('ld-nsew.csv')
 
date_LA = data_LA['DATE'].to_numpy()
TAVG_LA = data_LA['TAVG'].to_numpy()

date_LD = data_LD['ymd'].to_numpy()
data_LD = data_LD['data'].to_numpy()

x= [datetime.strptime(str(d), '%Y/%m/%d').date() for d in date_LD]

# print(x)

plt.rcParams['figure.figsize']=(12.0,6.0)
fig = plt.figure()
sub = fig.add_subplot(111)


monthsLoc = mpl.dates.MonthLocator()
weeksLoc = mpl.dates.WeekdayLocator()

sub.scatter(x,data_LD, marker= '8', s=15, color ='green')
sub.set_xlabel(r'$ Date$', fontsize =15)
sub.set_ylabel(r'$ Azimuth $', fontsize =15)

# sub.xaxis.set_major_locator(monthsLoc)
# sub.xaxis.set_minor_locator(weeksLoc)

date2_1 = dt.datetime(2018,1,1)
date2_2 = dt.datetime(2020,10,11)

# bg = dt.datetime.strptime(‘2018-01-01',’%Y-%m-%d')
# ed = dt.datetime.strptime(‘2020-08-01',’%Y-%m-%d')
# print(bg)

#sub.set_ylim([40, 100])
sub.set_xlim([date2_1,date2_2])

plt.savefig('ld-nsew.png')
plt.show()


# nrec = len(TAVG_LA)

# date_LA = np.zeros(nrec, dtype=object)

# for i in range(nrec) :
#     date_LA_str[i] = datetime.strptime(date_LA[i],'%Y-%m-%d') 

# print(date_LA)
