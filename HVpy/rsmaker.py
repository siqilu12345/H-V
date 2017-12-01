fn=4
nsource=100
thickness=0.015


xmin=-5
xmax=5
ymin=-5
ymax=5
dmin=0.0001
dmax=thickness
tmin=0
tmax=35
emin=0.01
emax=0.05


import random
import string
import os
with open('/Users/siqilu/Desktop/program/crflexample.txt') as f:
    a=f.readlines()
a[2]=a[2][:20]+'%5d\n' %nsource
mark=a.index('  \n')
c=list()
for i in range(nsource) :
    x=random.uniform(xmin,xmax)
    y=random.uniform(ymin,ymax)
    d=random.uniform(dmin,dmax)
    t=random.uniform(tmin,tmax)
    e=random.uniform(emin,emax)
    c.append('%10.4f%10.4f%10.4f%10.4f%10.4f\n'%(x,y,d,t,e))
a[4]='%10.4f' %thickness +a[4][10:]
a[5]='%10.4f' %thickness +a[5][10:]
a[6]='%10.4f' %(1000+thickness) +a[6][10:]
a[7]='%10.4f' %(1000+thickness) +a[7][10:]
g=a[0:mark+2]+c+a[-6:]
with open('/Users/siqilu/Desktop/program/crfl.dat','w') as f1:
    f1.write(''.join(g))

home=os.getcwd()
os.chdir('/Users/siqilu/Desktop/program')
os.system('./a.out')
os.chdir(home)


with open('/Users/siqilu/Desktop/program/crfl.dat','r') as f:
    a=f.readlines()
with open('/Users/siqilu/Desktop/crfl/crfl'+str(fn)+'.txt','w') as g :
    for i in a :
        g.write(i)
with open('/Users/siqilu/Desktop/program/crfl.sh','r') as f:
    a=f.readlines()
with open('/Users/siqilu/Desktop/data/crflsh_'+str(fn)+'.txt','w') as g :
    for i in a :
        j=i.split(' ')
        s=0
        for k in j :
            if k!='' :
                s=s+1
        if s==2 or s==3:
            g.write(i)
with open('/Users/siqilu/Desktop/program/crfl.psv','r') as f:
    a=f.readlines()
with open('/Users/siqilu/Desktop/data/crflpsv_'+str(fn)+'.txt','w') as g :
    for i in a :
        j=i.split(' ')
        s=0
        for k in j :
            if k!='' :
                s=s+1
        if s==2 or s==3:
            g.write(i)

