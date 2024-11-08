#Mohamed Boudabbous
#300376202
#exo 3
import math

G = 9.81 

def distance(v, angle):
  angle_rad = math.radians(angle)
  d = (2*v**2 * math.sin(angle_rad)*math.cos(angle_rad)) / G
  return d

pi=math.pi
v = 25 
angle=pi/180
distances = []
for angle_rad in range(0, 91, 10):
  d = distance(v, angle)
  distances.append(d)

print(distances)
