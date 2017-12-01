import numpy as np
import matplotlib.pyplot as plt
import matlab.engine
eng = matlab.engine.start_matlab()
eng.cd('/Users/siqilu/Documents/MATLAB/HoverV')
a=eng.trycomputehv(1,nargout=2)
eng.quit()
'''
def moving_average(a, n) :
    ret = np.cumsum(a, dtype=float)
    ret=ret
    return ret[n - 1:] / n
l=2048
leftf=1
rightf=20
nyfreq=25
psv=np.loadtxt('/Users/siqilu/Desktop/data/crflpsv_1.txt')
sh=np.loadtxt('/Users/siqilu/Desktop/data/crflsh_1.txt')
z=psv[:l,:]
x=psv[l:2*l,:]
spez=np.abs(np.fft.fft(z[:,1]))
spex=np.abs(np.fft.fft(x[:,1]))
spey=np.abs(np.fft.fft(sh[:,1]))
spez=spez[:l/2+1]
spex=spex[:l/2+1]
spey=spey[:l/2+1]
hv=(spex**2+spey**2)/spez
freq=np.linspace(0,nyfreq,num=l/2+1)
plt.plot(freq,hv)
plt.xlim(1,20)
plt.show()
'''
x=np.transpose(a[0])
x=np.reshape(x,(1025,))
y=np.array(a[1])
y=np.reshape(y,(1025,))
plt.plot(x,y)
plt.xlim(1,20)
plt.xlabel('Frequency/Hz')
plt.ylabel('H/V ratio amplitude')
plt.title('H/V Ratio')
plt.xticks(np.linspace(1,20,20))
for x in [2,6,10,14,18] :
    plt.axvline(x=x,ls='--')
    plt.text(x=x+0.3,y=14,s='f=%.1f'%x,fontsize=12)
plt.savefig(filename='/Users/siqilu/Desktop/HVfigures/HV.eps',
            format='eps',dpi=5000)
plt.show()