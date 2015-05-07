import calc
import matplotlib.pyplot as plt

upper = 15

masses = [20, 20, .001, .001]
positions = [[0,0], [1,3], [1,-3], [1,1]]
positionsa = [[0,0], [2,2], [200,200], [100,100]]
positionsb = [[0,0], [1,3], [1,-3], [1,1]]
positionsc = [[0,0], [1,3], [1,-3], [1,1]]

velocities = [[0,.001], [0,-.01], [-.01, 0], [.01,-.01]]
velocitiesa = [[0,.002], [0,-.002], [-.002, 0], [.002,-.01]]
velocitiesb = [[0,0], [0,-.06], [-.016, 0], [.016,-.01]]
velocitiesc = [[0,0], [0,-.02], [-.02, 0], [.02,-.01]]

timeSet, orbitCalc = calc.dataSet(positions, velocities, masses)
timeSet2, orbitCalc2 = calc.dataSet(positionsa, velocitiesa, masses)
timeSet3, orbitCalc3 = calc.dataSet(positionsb, velocitiesb, masses)
timeSet4, orbitCalc4 = calc.dataSet(positionsc, velocitiesc, masses)


plt.figure(1)
plt.subplot(221)
for o in orbitCalc:
	plt.plot(o.xHis, o.yHis)
plt.plot(0,0,'ro')
plt.ylim([-5,upper])
plt.xlim([-10,10])

plt.subplot(222)
for o in orbitCalc2:
	plt.plot(o.xHis, o.yHis)
plt.plot(0,0,'ro')
plt.ylim([-5,upper])
plt.xlim([-10,10])

plt.subplot(223)
for o in orbitCalc3:
	plt.plot(o.xHis, o.yHis)
plt.plot(0,0,'ro')
plt.ylim([-5, upper])
plt.xlim([-10, 10])

plt.subplot(224)
for o in orbitCalc4:
	plt.plot(o.xHis, o.yHis)
plt.plot(0,0,'ro')
plt.ylim([-5, upper])
plt.xlim([-10,10])

#ax2 = ax1.twinx()
#ax2.plot(timeSet, o2.xHis)
plt.show()
