import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 
from datetime import datetime

data_LA = pd.read_csv('LATemperature2019.csv')
# data_NY = pd.read_csv('https://raw.githubusercontent.com/SoNYireOAstora/PythonPlotDemoMaterials/master/NYTemperature2019.csv')

print(data_LA)

# process NY data
# date_NYS=data_NY['DATE']
# DATA_NYS=data_NY['DATE']

# date_LA = data_LA['DATE'].to_numpy()
# TAVG_LA = data_LA['TAVG'].to_numpy()


# print(date_LA)
# print(TAVE_LA)


# nrec = len(TAVG_LA)
# date_LA=np.zeros(nrec, dtype= object)

# for i in range(nrec):
#     date_LA[i] = datetime.strptime(date_LA[i],'%Y-%m-%d')
 
# print(date_LA)

# doy_LA = np.zeros(nrec)
# for i in range(nrec):
#     doy_LA_str[i] = data_LA_str[i].timetuple().tm_yday


# print(doy_NY)

# plt.scatter(data_LA_str,TAVG_LA, s=50)
# plt.show()

# sort the data according to time

# argsort_idx = np.argsort(doy_LA)

# doy_LA = doy_LA(argsort_idx)
# TAVG_LA = TAVG_LA(argsort_idx)



# data_NY_str=data_NY['DATE'].to_numpy()
# TAVG_NY = data_NY['TAVG'].to_numpy()


# nrec = len(TAVG_NY)
# data_NY=np.zeros(nrec, dtype= object)

# for i in range(nrec):
#     data_NY_str[i] = datetime.strptime(data_NY_str[i],'%Y-%m-%d')
 

# doy_NY = np.zeros(nrec)
# for i in range(nrec):
#     doy_NY[i] = data_NY_str[i].timetuple().tm_yday

# argsort_idx = np.argsort(doy_NY)

# doy_NY=doy_NY(argsort_idx)
# TAVG_NY = TAVG_NY(argsort_idx)

# # plot -------------------------
# fig = plt.figure()

# sub = fig.add_subplot(111)

# sub.plot(TAVG_LA,TAVG_NY)

# sub.set_xlabel(r'$Temperature of LA', fontsize =15)
# sub.set_ylabel(r'$Temperature of NY', fontsize =15)

# plt.show()
