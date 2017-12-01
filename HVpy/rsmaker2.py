nsource=18
import os
import numpy as np
import time
'''
os.mkdir('/Users/siqilu/Desktop/crfl')
os.mkdir('/Users/siqilu/Desktop/data')
'''
t1=time.time()
with open('/Users/siqilu/Desktop/program/crflexample.txt') as f:
    aex = f.readlines()
aex[2] = aex[2][:20] + '%5d\n' % 1
mark = aex.index('  \n')
for rlabel in range(3) :
    for dlabel in range(3) :
            for i in range(nsource):
                if rlabel==0 :
                    r=np.random.uniform(8,20)
                elif rlabel==1 :
                    r=np.random.uniform(20,100)
                else :
                    r=np.random.uniform(100,200)
                if dlabel==0 :
                    d=np.random.uniform(1,20)
                elif dlabel==1 :
                    d=np.random.uniform(20,50)
                else :
                    d=np.random.uniform(50,100)
                theta = 2*np.pi / nsource * i
                x = r * np.cos(theta) + 50
                y = r * np.sin(theta)
                t = -30
                if d%10>=7:
                    d=6+np.random.uniform()
                c = ['%10.4f%10.4f%10.4f%10.4f%10.4f\n' % (x, y, d, t, 1)]
                g = aex[0:mark + 2] + c + aex[-6:]
                with open('/Users/siqilu/Desktop/program/crfl.dat', 'w') as f1:
                    f1.write(''.join(g))
                home = os.getcwd()
                os.chdir('/Users/siqilu/Desktop/program')
                os.system('./a.out')
                os.chdir(home)
                with open('/Users/siqilu/Desktop/program/crfl.dat', 'r') as f:
                    a = f.readlines()
                with open('/Users/siqilu/Desktop/crfl/crfl' + 'th'+str(i) +'r'+
                                  str(rlabel)+'d'+str(dlabel)+'.txt','w') as g:
                    for j in a:
                        g.write(j)
                with open('/Users/siqilu/Desktop/program/crfl.sh', 'r') as f:
                    a = f.readlines()
                with open('/Users/siqilu/Desktop/data/crflsh_' + 'th'+str(i)
                                  +'r'+str(rlabel)+'d'+str(dlabel)+'.txt', 'w') as g:
                    for l in a:
                        j = l.split(' ')
                        s = 0
                        for k in j:
                            if k != '':
                                s = s + 1
                        if s == 2 or s == 3:
                            g.write(l)
                with open('/Users/siqilu/Desktop/program/crfl.psv', 'r') as f:
                    a = f.readlines()
                with open('/Users/siqilu/Desktop/data/crflpsv_'+'th'+str(i) +
                                  'r'+str(rlabel)+'d'+str(dlabel)+'.txt', 'w') as g:
                    for l in a:
                        j = l.split(' ')
                        s = 0
                        for k in j:
                            if k != '':
                                s = s + 1
                        if s == 2 or s == 3:
                            g.write(l)
t2=time.time()
print(t2-t1)