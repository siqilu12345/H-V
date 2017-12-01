import matplotlib.pyplot as plt
import numpy as np
b=np.genfromtxt('/Users/siqilu/Desktop/crfl/crfl1.txt',skip_header=10,
              skip_footer=6)
fig1=plt.figure()
sources=plt.scatter(b[:,0],b[:,1],marker='o',facecolor=None)
receiver=plt.scatter(0,0,marker='*',s=200,edgecolors='red',
                     facecolor='red')
leg=plt.legend([sources,receiver],['Sources','Receiver'],
               scatterpoints=1,loc=0,fontsize=10)
plt.xlim(-5,5)
plt.ylim(-5,5)
plt.xlabel('x range/km')
plt.ylabel('y range/km')
plt.title('Sources Distribution')
plt.savefig(filename='/Users/siqilu/Desktop/HVfigures/Sources.eps',
            format='eps',dpi=5000)
plt.show()