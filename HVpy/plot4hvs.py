import numpy as np
import matplotlib.pyplot as plt
import matlab.engine
a=[0]*4
x=[0]*4
y=[0]*4
eng = matlab.engine.start_matlab()
eng.cd('/Users/siqilu/Documents/MATLAB/HoverV')
for i in range(4) :
    a[i]=eng.trycomputehv(i+2,nargout=2)
eng.quit()
for i in range(4) :
    x[i]=np.transpose(a[i][0])
    x[i]=np.reshape(x[i],(1025,))
    y[i]=np.array(a[i][1])
    y[i]=np.reshape(y[i],(1025,))
ax=[0]*4
f,ax=plt.subplots(4,1,sharex=True)
plt.suptitle('HV Ratio',fontsize=20)
f.text(0.5, 0.04, 'Frequency/Hz', ha='center',
       fontsize=15)
f.text(0.04, 0.5, 'HV ratio amplitude', va='center',
       rotation='vertical',fontsize=15)
frequency=[[2.5,7.5,12.5,17.5],[1.5,4.5,7.5,10.5,13.5,
                                16.5,19.5],[3.3,10,16.7],
           [10/7,30/7,50/7,10,90/7,110/7,130/7]]
subtit='abcd'
for i in range(4) :
    plt.sca(ax[i])
    plt.plot(x[i],y[i])
    plt.title(s='('+subtit[i]+')')
    for f in frequency[i]:
        plt.axvline(x=f, ls='--')
        plt.text(x=f+0.3, y=10, s='f=%.1f' %f, fontsize=15)
plt.xlim(1,20)
plt.xticks(np.linspace(1,20,20))
plt.savefig(filename='/Users/siqilu/Desktop/HVfigures/4HVs.eps',
            format='eps',dpi=5000)
plt.show()