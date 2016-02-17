import math
import numpy as np

#from point0 to point3, it must be clockwise or counterclockwise in turn
#x[4],y[4]
x = [0,252*2,421*2,370*2,215*2]
y = [0,85*2,100*2,250*2,261*2]
f = 360*math.sqrt(3)

def iszero(z):  return abs(z) < .000001

def turnzero(z):
 if (abs(z) < .000001): return 0
 else: return z

# function: matrixtoangles
# input: rotation matrix, type: np.matrix
# output: angles array, type: np.array
def matrixtoangles(m):
 if(not(iszero(1-abs(m.item(2,0))))):
  y1 = -math.asin(m.item(2,0))
  y2 = math.pi + y1
  x1 = math.atan2(m.item(2,1)/math.cos(y1),m.item(2,2)/math.cos(y1))
  x2 = math.atan2(m.item(2,1)/math.cos(y2),m.item(2,2)/math.cos(y2))
  z1 = math.atan2(m.item(1,0)/math.cos(y1),m.item(0,0)/math.cos(y1))
  z2 = math.atan2(m.item(1,0)/math.cos(y2),m.item(0,0)/math.cos(y2))
  return np.matrix([[math.degrees(x1),math.degrees(y1),math.degrees(z1)],[math.degrees(x2),math.degrees(y2),math.degrees(z2)]])
 if(iszero(1+m.item(2,0))):
  y = math.pi/2
  z = 'x + ' + math.atan2(m.item(0,1),m.item(0,2))
  return np.matrix([['x',y,z]])
 if(iszero(m.item(2,0)-1)):
  y = -math.pi/2
  z = math.atan2(-m.item(0,1),-m.item(0,2)) + ' - x'
  return np.matrix([['x',y,z]])

# function: anglestomatrix
# input: angles to x, y, and z axis in degrees type: float, float, float
# output: rotation matrix, type: np.matrix
def anglestomatrix(x,y,z):
 xs = turnzero(math.sin(math.radians(x)))
 xc = turnzero(math.cos(math.radians(x)))
 ys = turnzero(math.sin(math.radians(y)))
 yc = turnzero(math.cos(math.radians(y)))
 zs = turnzero(math.sin(math.radians(z)))
 zc = turnzero(math.cos(math.radians(z)))
 xm = np.matrix([[1,0,0],[0,xc,-xs],[0,xs,xc]])
 ym = np.matrix([[yc,0,ys],[0,1,0],[-ys,0,yc]])
 zm = np.matrix([[zc,-zs,0],[zs,zc,0],[0,0,1]])
 return xm*ym*zm

def slope(a,b): return float((y[b]-y[a])/(x[b]-x[a]))

def intercept(a,b): return float(y[a]-x[a]*slope(a,b))

def interx(a,b,c,d):
    return -(intercept(a,b)-intercept(c,d))/(slope(a,b)-slope(c,d))

def intery(a,b,c,d):
    return (slope(a,b)*intercept(c,d)-slope(c,d)*intercept(a,b))/(slope(a,b)-slope(c,d))

def coordtrans1(a): return np.array([a[0]-640, a[1]-360, a[2]+f])

def vectorscale(a): 
    return math.sqrt(math.pow(a[0],2) + math.pow(a[1],2) + math.pow(a[2],2))

#if (iszero(slope(1,2)-slope(3,4)))


xm = interx(1,2,3,4)
ym = intery(1,2,3,4)
xn = interx(1,4,2,3)
yn = intery(1,4,2,3)

vu = coordtrans1(np.array([xm,ym,0]))
vv = coordtrans1(np.array([xn,yn,0]))
vw = np.cross(vu,vv)

su = vectorscale(vu)
sv = vectorscale(vv)
sw = vectorscale(vw)

RotMatrix = np.matrix([[vu[0]/su,vv[0]/sv,vw[0]/sw],
                      [vu[1]/su,vv[1]/sv,vw[1]/sw],
                      [vu[2]/su,vv[2]/sv,vw[2]/sw]])

print(RotMatrix)
print(matrixtoangles(RotMatrix))