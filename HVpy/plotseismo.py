import numpy as np
import matplotlib.pyplot as plt
l=2048
psv=np.loadtxt('/Users/siqilu/Desktop/data/crflpsv_1.txt')
sh=np.loadtxt('/Users/siqilu/Desktop/data/crflsh_1.txt')
z=psv[:l,:]
x=psv[l:2*l,:]
f, (ax1, ax2, ax3) = plt.subplots(3,1,sharex=True, sharey=True)
plt.xlim(0,40.96)
plt.suptitle('Seismograph',fontsize=20)
f.text(0.5, 0.04, 'Time/s', ha='center',
       fontsize=20)
f.text(0.04, 0.5, 'Velocity', va='center',
       rotation='vertical',fontsize=20)
plt.sca(ax1)
plt.plot(z[:,0],z[:,1])
plt.title('Z Component')
plt.sca(ax2)
plt.plot(x[:,0],x[:,1])
plt.title('X Component')
plt.sca(ax3)
plt.plot(sh[:,0],sh[:,1])
plt.title('Y Component')
plt.savefig(filename='/Users/siqilu/Desktop/HVfigures/Seismo.eps',
            format='eps',dpi=5000)
plt.show()