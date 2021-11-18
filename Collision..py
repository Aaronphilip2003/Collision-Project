import matplotlib.pyplot as plt
import numpy as np
import random 

x=[]
y=[]
heights=[]
velocities =[]
times=[]
roundtrip=[]
zeros=[]
timess=[0,0.89]
for i in range(0,50):
  heights.append(4*(0.8**(2*i))) # 4e^2i
  velocities.append(8.94*(0.8**i))# v2-u2=2as
  x=velocities[i]/10#v=u+at
  times.append(x)
  roundtrip.append(2*x)
  zeros.append(0)
totaltime=0
for i in range(0,len(roundtrip)):
  totaltime+=roundtrip[i]
  timess.append(totaltime)
  y.append(0)
  timess.append(totaltime+times[i])
  y.append(heights[i])
y.append(0)
y.append(0)
plt.plot(timess,y)
print(timess)
print(y)
plt.show()
