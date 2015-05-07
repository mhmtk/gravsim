import calc
import matplotlib.pyplot as plt

upper = 15

masses = [200, .001, .001, .001]
massesb = [13, 13, .001, .001]
massesc = [18, 30, .002, .001]
massesd = [100, 100, .001, .001]

positions = [[0,0], [2,1], [1,-1], [1,1]]
positionsa = [[0,-4], [2,8], [1,-1], [2,1]]
positionsb = [[0,-4], [2,8], [1,-1], [2,1]]
positionsc = [[0,-4], [2,8], [1,-1], [2,1]]

velocities = [[0,0], [0,-.002], [-.01, 0], [.01,-.01]]
velocitiesa = [[0,0], [0,-.0018], [-.002, 0], [.002,-.01]]
velocitiesb = [[0,0], [0,-.0015], [-.016, 0], [.016,-.01]]
velocitiesc = [[0,0], [0,-.002], [-.02, 0], [.02,-.01]]

timeSet, orbitCalc = calc.dataSet(positions, velocities, masses)
timeSet2, orbitCalc2 = calc.dataSet(positionsa, velocitiesa, masses)
timeSet3, orbitCalc3 = calc.dataSet(positionsb, velocitiesb, masses)
timeSet4, orbitCalc4 = calc.dataSet(positionsc, velocitiesc, masses)

plt.figure(1)
plt.subplot(231)
for o in orbitCalc:
	plt.plot(o.xHis, o.yHis)
plt.plot(0,0,'ro')
plt.ylim([-5,upper])
plt.xlim([-10,10])

plt.subplot(232)
for o in orbitCalc2:
	plt.plot(o.xHis, o.yHis)
plt.plot(0,0,'ro')
plt.ylim([-5,upper])
plt.xlim([-10,10])

plt.subplot(233)
for o in orbitCalc3:
	plt.plot(o.xHis, o.yHis)
plt.plot(0,0,'ro')
plt.ylim([-5, upper])
plt.xlim([-10, 10])

plt.subplot(234)
for o in orbitCalc4:
	plt.plot(o.xHis, o.yHis)
plt.plot(0,0,'ro')
plt.ylim([-5, upper])
plt.xlim([-10,10])

plt.subplot(235)
for o in orbitCalc:
	plt.plot(timeSet, o.kHis)

#ax2 = ax1.twinx()
#ax2.plot(timeSet, o2.xHis)
plt.show()
