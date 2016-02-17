import math
import numpy as np
import random

def getangle(v1,v2):
	return math.acos(np.dot(v1,v2)/np.linalg.norm(v1)/np.linalg.norm(v2))*360/6.283

def sum(v1,v2,v3,v4):
 return getangle(v1,v2)+getangle(v2,v3)+getangle(v3,v4)+getangle(v4,v1)
 
def clockwise(v1,v2,v3,v4):
 return 359<sum(v1,v2,v3,v4)<361
 
def coord2point(a,b,c,d,e,f,g,h):
 p1 = [a,b]
 p2 = [c,d]
 p3 = [e,f]
 p4 = [g,h]
 return [p1,p2,p3,p4]

def point2vector(p1,p2,p3,p4):
 v1 = np.subtract(p2,p1)
 v2 = np.subtract(p3,p2)
 v3 = np.subtract(p4,p3)
 v4 = np.subtract(p1,p4)
 return [v1,v2,v3,v4]

def shuffle(v1,v2,v3,v4):
 vs=[v1,v2,v3,v4]
 r1 = random.randint(0,3)
 r2 = random.randint(0,3)
 temp = vs[r1]
 vs[r1] = vs[r2]
 vs[r2] = temp
 return vs
 
def doit(a,b,c,d,e,f,g,h):
 ps = coord2point(a,b,c,d,e,f,g,h)
 vs = point2vector(ps[0],ps[1],ps[2],ps[3])
 while not clockwise(vs[0],vs[1],vs[2],vs[3]):
  ps = shuffle(ps[0],ps[1],ps[2],ps[3])
  vs = point2vector(ps[0],ps[1],ps[2],ps[3])
 return ps

print(doit(1,0,0,0,1,1,0,1))
