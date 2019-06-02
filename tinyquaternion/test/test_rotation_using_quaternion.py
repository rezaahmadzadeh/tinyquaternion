import numpy as np

from tinyQuaternion import Quaternion
from plotCube import plot_cube

# plot the initial cube
p1 = np.array([0.,0.,0.])
p2 = np.array([0.,.1,0.])
p3 = np.array([2.,0.,0.])
p4 = np.array([0.,0.,.1])

print("initial cube:")
print(p1)
print(p2)
print(p3)
print(p4)

cube1 = [
    (p1[0],p1[1],p1[2]), (p2[0],p2[1],p2[2]), (p3[0],p3[1],p3[2]), (p4[0],p4[1],p4[2])
]
plot_cube(cube1)

# define a known quaternion
q = Quaternion(a=np.pi/2, n=np.array([0., 1., 0.]))
# rotate the cube
p1r = q.rotatePoint(p1)
p2r = q.rotatePoint(p2)
p3r = q.rotatePoint(p3)
p4r = q.rotatePoint(p4)

print("rotated cube:")
print(p1r)
print(p2r)
print(p3r)
print(p4r)

cube2 = [
    (p1r[0],p1r[1],p1r[2]), (p2r[0],p2r[1],p2r[2]), (p3r[0],p3r[1],p3r[2]), (p4r[0],p4r[1],p4r[2])
]
plot_cube(cube2)

