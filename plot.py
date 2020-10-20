import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

df = pd.read_excel('./ld.xlsx',sheet_name='Sheet2')

fig =plt.figure()

sub=fig.add_subplot(111)
# sub.plot(df['starDate'],df['NW'])
# sub.scatter(df['starDate'],df['NW'],s=10)

sub.plot(df['x'],df['y'],linewidth=3, linestyle=':')

sub.set_xlim([0.2,0.8])
sub.set_ylim([0.3, 1.0])

sub.set_xlabel(r'$X$',fontsize=16)
sub.set_ylabel(r'$Y$',fontsize=16)
sub.set_title(r'Plot 1',fontsize=20)

plt.show()

plt.close(fig)

