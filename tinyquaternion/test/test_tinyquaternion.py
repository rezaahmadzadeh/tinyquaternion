import numpy as np

from tinyQuaternion import Quaternion

q = Quaternion(q=np.array([0., 0., 2., 0.]))
print(q)
print(repr(q))

print(q.vector)
print(q.scalar)
print(q.magnitude)
print(q.is_unit())
print(q.normalized)
print(q.is_unit())
print(q.conjugate)
print(q.inverse)
print(q.axisangle())


q1 = Quaternion(a=np.pi/3, n=np.array([0.,0.,1.]))
q2 = Quaternion(q=np.array([1.,1.,1.,0.]))

print(q1)
print(q2)
print(q1.add(q2))
print(q1.sub(q2))
print(q1.mul(q2))
print(q1.div(q2))


p = np.array([1.,2.,-1.])
print(q1.rotatePoint(p))
