import math
import numpy as np

def iszero(z):  return abs(z) < .000001

def turnzero(z):
 if (abs(z) < .000001): return 0
 else: return z

# function: matrixtoanglesvector
# input: rotation matrix, type: np.matrix
# output: angles array, type: np.array
def matrixtoanglesvector(m):
 angle = 0
 x = 0
 y = 0
 z = 0
 epsilon = 0.01
 epsilon2 = 0.1
    
 if ((abs(m.item((0,1))-m.item((1,0)))< epsilon) and (abs(m.item((0,2))-m.item((2,0)))< epsilon) and (abs(m.item((1,2))-m.item((2,1)))< epsilon)):
  if ((abs(m.item((0,1))+m.item((1,0))) < epsilon2) and (abs(m.item((0,2))+m.item((2,0))) < epsilon2) and (abs(m.item((1,2))+m.item((2,1))) < epsilon2) and (abs(m.item((0,0))+m.item((1,1))+m.item((2,2))-3) < epsilon2)):
   return np.array([0,1,0,0])
        
  angle = math.pi
  xx = (m.item((0,0))+1)/2
  yy = (m.item((1,1))+1)/2
  zz = (m.item((2,2))+1)/2
  xy = (m.item((0,1))+m.item((1,0)))/4
  xz = (m.item((0,2))+m.item((2,0)))/4
  yz = (m.item((1,2))+m.item((2,1)))/4
        
  if ((xx > yy) and (xx > zz)):
   if (xx< epsilon):
    x = 0
    y = 0.7071
    z = 0.7071
   else:
    x = math.sqrt(xx)
    y = xy/x
    z = xz/x
  elif (yy > zz):
   if (yy< epsilon):
    x = 0.7071
    y = 0
    z = 0.7071
   else:
    y = math.sqrt(yy)
    x = xy/y
    z = yz/y		
  else:
   if (zz< epsilon):
    x = 0.7071
    y = 0.7071
    z = 0
   else:
    z = math.sqrt(zz)
    x = xz/z
    y = yz/z
		
  return np.array([angle,x,y,z])
	

 s = math.sqrt((m.item((2,1)) - m.item((1,2)))*(m.item((2,1)) - m.item((1,2))) + (m.item((0,2)) - m.item((2,0)))*(m.item((0,2)) - m.item((2,0))) + (m.item((1,0)) - m.item((0,1)))*(m.item((1,0)) - m.item((0,1))))
 if (abs(s) < 0.001): s=1
 angle = math.acos(( m.item((0,0)) + m.item((1,1)) + m.item((2,2)) - 1)/2)
 x = (m.item((2,1)) - m.item((1,2)))/s
 y = (m.item((0,2)) - m.item((2,0)))/s
 z = (m.item((1,0)) - m.item((0,1)))/s
 return np.array([angle,x,y,z])

# function: matrixtoangles
# input: rotation matrix, type: np.matrix
# output: angles array, type: np.array
def matrixtoangles(m):
 if(not(iszero(1-abs(m.item(2,0))))):
  y1 = -math.asin(m.item(2,0))
  y2 = math.pi - y1
  x1 = math.atan2(m.item(2,1)/math.cos(y1),m.item(2,2)/math.cos(y1))
  x2 = math.atan2(m.item(2,1)/math.cos(y2),m.item(2,2)/math.cos(y2))
  z1 = math.atan2(m.item(1,0)/math.cos(y1),m.item(0,0)/math.cos(y1))
  z2 = math.atan2(m.item(1,0)/math.cos(y2),m.item(0,0)/math.cos(y2))
  return np.matrix([[x1,y1,z1],[x2,y2,z2]])
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

m = anglestomatrix(90,0,90)
n = matrixtoangles(m)
print (m)
print (n)