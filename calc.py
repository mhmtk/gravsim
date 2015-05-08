from __future__ import division
import math

class object:
	#Should incorp radius of objects to avoid becoming too strong
	aFactor = 1	

	def __init__(self, iPos, iVel, mass, n):
		self.vel = iVel
		self.pos = iPos
		self.mass = mass
		self.xHis = [0]*n
		self.yHis = [0]*n
		self.kHis = [0]*n
		
	def updatePos(self,n):
		self.xHis[n] = self.pos[0]
		self.yHis[n] = self.pos[1]
		self.kHis[n] = self.getKE()
		self.pos[0] += self.vel[0]
		self.pos[1] += self.vel[1]
		
		#print self.mass, self.pos, self.vel

	def getKE(self):
		return .5*self.mass*self.velMag()**2

	def velMag(self):
		return math.sqrt(self.vel[0]**2 + self.vel[1]**2)
	
	def accelerate(self, ax, ay):
		self.vel[0] += ax*self.aFactor
		self.vel[1] += ay*self.aFactor
	

def dataSet(positions, velocities, masses):
	
	timeSet = range(0, 250000)
	objects = []
	G = .000001
	
	for i in range (0, len(masses)):
		objects.append(object(positions[i], velocities[i], masses[i], len(timeSet)))
	
	for t in timeSet:
		for o in objects:	
			disp = []
			acc = []
			dispMag = 0
			
			for o2 in objects:
				if o != o2:
					ox = o.pos[0]
					oy = o.pos[1]
					o2x = o2.pos[0]
					o2y = o2.pos[1]

					disp = [o2x - ox, o2y - oy]
					#print disp
					dispMag = math.sqrt(disp[0]**2 + disp[1]**2)	
					acc = G*o2.mass/(dispMag**2)
					o.accelerate(acc*disp[0]/dispMag, acc*disp[1]/dispMag)

			o.updatePos(t)

	return timeSet, objects
