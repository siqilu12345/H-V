import matplotlib.pyplot as plt
import matplotlib.patches as patches
fig1=plt.figure(frameon=False)
ax=fig1.add_axes([0,0,1,1])
p1=patches.Rectangle((0,0),1,0.7,facecolor='red')
p2=patches.Rectangle((0,0.7),1,0.2,facecolor='blue')
ax.add_patch(p1)
ax.add_patch(p2)
plt.text(0.5,0.25,'Basement',ha='center',fontsize=20)
plt.text(0.5,0.8,'Low-speed layer',ha='center',fontsize=20)
ax.set_axis_off()
plt.savefig(filename='/Users/siqilu/Desktop/HVfigures/Model.eps',
            format='eps',dpi=5000)
plt.show()
