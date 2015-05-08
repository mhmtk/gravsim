import calc
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

upper = 15
"""Awesome chaotic orbit
masses = [200, .001, .001, .001]
positions = [[0,0], [2,1], [1,-1], [1,1]]
velocities = [[0,0], [0,-.002], [-.01,0], [.01,-.01]]
"""

masses = [12, 12]
positions = [[0,1], [2,1]]
velocities = [[0,.002],[0,-.002]]

timeSet, orbitCalc = calc.dataSet(positions, velocities, masses)

o = orbitCalc[0]
o2 = orbitCalc[1]
adata = [o.xHis, o.yHis]
adata2 = [o2.xHis, o2.yHis]
"""
def data_gen():
	t = 0
	cnt = 0
	while cnt < 1000:
		cnt += 1
		yield adata[0][cnt], adata[1][cnt]	
"""
fig, ax = plt.subplots()
line, = ax.plot([],[])
line2, = ax.plot([],[])
ax.set_ylim(-1,3)
ax.set_xlim(-1,3)
xdata, ydata = [],[]
xdata2, ydata2 = [],[] 

def run(i):
	#pt.remove()
	i = 20*i
	t,y = adata[0][i], adata[1][i]
	t2,y2 = adata2[0][i], adata2[1][i]
	pt, = ax.plot(t,y,'ko')
	pt2, = ax.plot(t2,y2,'ko')
	plt.draw()
	pt.remove()
	pt2.remove()
	#comment out following line of code for lines
	t,y,t2,y2 = 0,0,0,0
	xdata.append(t)
	ydata.append(y)
	xdata2.append(t2)
	ydata2.append(y2)	
	line.set_data(xdata, ydata)
	line2.set_data(xdata2, ydata2)
		
	return [line, line2]

#for o in orbitCalc:
#	plt.plot(o.xHis, o.yHis)


ani = animation.FuncAnimation(fig, run, blit=True, interval=.001, repeat=False)

plt.show()
