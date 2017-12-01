import numpy as np
import matplotlib.pyplot as plt
import matlab.engine
eng = matlab.engine.start_matlab()
eng.cd('/Users/siqilu/Documents/MATLAB/HoverV')
a=eng.trycomputehv(1,nargout=2)
eng.quit()
x=np.transpose(a[0])
x=np.reshape(x,(1025,))
y=np.array(a[1])
y=np.reshape(y,(1025,))
plt.plot(x,1/y)
plt.xlim(1,20)
plt.xlabel('Frequency/Hz')
plt.ylabel('H/V ratio amplitude')
plt.title('H/V Ratio')
plt.xticks(np.linspace(1,20,20))
for x in [4,12] :
    plt.axvline(x=x,ls='--')
    plt.text(x=x+0.3,y=10,s='f=%.1f'%x,fontsize=12)
plt.savefig(filename='/Users/siqilu/Desktop/HVfigures/VH.eps',
            format='eps',dpi=5000)
plt.show()