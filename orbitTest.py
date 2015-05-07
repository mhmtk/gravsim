import calc
import matplotlib.pyplot as plt

upper = 15

masses = [200, .001, .001, .001]
positions = [[0,0], [1,3], [1,-3], [1,1]]
velocities = [[0,0], [0,-.01], [-.01, 0], [.01,-.01]]
velocities2 = [[0,0], [0,-.02], [-.01, 0], [.01,-.01]]
velocities3 = [[0,0], [0,-.03], [-.01, 0], [.01,-.01]]
velocities4 = [[0,0], [0,-.04], [-.01, 0], [.01,-.01]]

timeSet, orbitCalc = calc.dataSet(positions, velocities, masses)
timeSet, orbitCalc2 = calc.dataSet(positions, velocities2, masses)
timeSet, orbitCalc3 = calc.dataSet(positions, velocities3, masses)
timeSet, orbitCalc4 = calc.dataSet(positions, velocities4, masses)



o1 = orbitCalc[0]
o2 = orbitCalc[1]
for t in timeSet:
	if t%50 == 0:
		pass
		#print 't:', t, 'x:', o1.xHis[t], 'y:', o1.yHis[t]

plt.figure(1)
plt.subplot(221)
for o in orbitCalc:
	plt.plot(o.xHis, o.yHis)
plt.ylim([-5,upper])

plt.subplot(222)
for o in orbitCalc2:
	plt.plot(o.xHis, o.yHis)
plt.ylim([-5,upper])

plt.subplot(223)
for o in orbitCalc3:
	plt.plot(o.xHis, o.yHis)
plt.plot(0,0,'ro')
plt.ylim([-5, upper])

plt.subplot(224)
for o in orbitCalc4:
	plt.plot(o.xHis, o.yHis)
plt.plot(0,0,'ro')
plt.ylim([-5, upper])


#ax2 = ax1.twinx()
#ax2.plot(timeSet, o2.xHis)
plt.show()
