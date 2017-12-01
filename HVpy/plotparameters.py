import numpy as np
import matplotlib.pyplot as plt
import matlab.engine
a=[0]*5
x=[0]*5
y=[0]*5
eng = matlab.engine.start_matlab()
eng.cd('/Users/siqilu/Documents/MATLAB/HoverV')
for i in range(5) :
    a[i]=eng.trycomputehv(i+6,nargout=2)
eng.quit()
for i in range(5) :
    x[i]=np.transpose(a[i][0])
    x[i]=np.reshape(x[i],(1025,))
    y[i]=np.array(a[i][1])
    y[i]=np.reshape(y[i],(1025,))
colors='rgbyc'
labs=[r'$V_{p1}:0.4 \rightarrow 0.35km/s$',
      r'$\rho_1:1.9 \rightarrow 2.1kg/m^3$,',
      r'$V_{p2}:5.5 \rightarrow 5.0km/s$',
      r'$V_{s2}:3.0 \rightarrow 3.5km/s$',
      r'$\rho_2:2.5 \rightarrow 2.3kg/m^3$']
for i in range(5) :
    plt.plot(x[i],y[i],color=colors[i],label=labs[i])
plt.legend(fontsize=10)
plt.xlim(1,20)
plt.xticks(np.linspace(1,20,20))
plt.xlabel('Frequency/Hz')
plt.ylabel('H/V ratio amplitude')
plt.title('H/V Ratio')
for x in [2,6,10,14,18] :
    plt.axvline(x=x,ls='--',color='k')
    plt.text(x=x+0.3,y=14,s='f=%.1f'%x,fontsize=12)
plt.savefig(filename='/Users/siqilu/Desktop/HVfigures/parameters.eps',
            format='eps',dpi=5000)
plt.show()