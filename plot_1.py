import numpy as np
import matplotlib.pyplot as plt 

# x=np.linspace(0,10,1001)
# y1=x
# y2=100-x

# fig = plt.figure()
# sub=fig.add_subplot(111)
# sub.plot(x, y1, label=r'$y=x$')


# sub.set_xlabel(r'$X$',fontsize=15)
# sub.set_ylabel(r'$Y$',fontsize=15,color='C0')
# sub.tick_params(which='both', axis='y', colors='C0')
# sub.legend(loc='center left')

# sub2=sub.twinx()
# sub2.plot(x, y2, label=r'$y=100-x$', color='C1')
# sub2.legend(loc='center right')
# sub2.set_ylabel(r'$Y2$',fontsize=15,color='C1')
# sub2.tick_params(which='both', axis='y', colors='C1')

x = np.linspace(0,1,101)
y = np.cos(2 * np.pi * x)
fig=plt.figure()
sub=fig.add_subplot(111)
sub.plot(x,y)
# sub.axvspan(0.25,0.75, color='yellow', alpha=0.5,label='$y \leg 0$')
# sub.legend()

x1=np.linspace(0.25,0.75,100)
y1=np.cos(2 * np.pi * x1)
y2=y1-0.25
  
sub.text(0.5,0.2, r'$y=\cos (2 \pi x)$',fontsize=15, 
    color='r', ha='center', va='center', transform=sub.transAxes,
    rotation =60, bbox= dict(edgecolor='g',facecolor='None', linestyle='--', linewidth=1.5))

# sub.fill_between(x1,y1,y2, color='yellow', alpha=0.5)


sub.axhline(y=0,color='k',linewidth=0.5)

sub.set_xlabel(r'$x$',fontsize=15)
sub.set_ylabel(r'$y$',fontsize =15)





plt.show()
