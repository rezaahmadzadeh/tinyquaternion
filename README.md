# tinyquaternion
A tiny python module for Quaternions




## Using Quaternions for Rotation

The code can be found in the `test` folder. First import all the required packages:

``` python
import numpy as np
from tinyQuaternion import Quaternion
from plotCube import plot_cube
```

To perform this test, we first plot a cube using the function `plotCube.py` provided in the test folder. 

``` python
# plot the initial cube
p1 = np.array([0.,0.,0.])
p2 = np.array([0.,.1,0.])
p3 = np.array([2.,0.,0.])
p4 = np.array([0.,0.,.1])

cube1 = [
    (p1[0],p1[1],p1[2]), (p2[0],p2[1],p2[2]), (p3[0],p3[1],p3[2]), (p4[0],p4[1],p4[2])
]
plot_cube(cube1)
```
    
This will result in the following cube:

!["initial cube"](https://github.com/rezaahmadzadeh/tinyquaternion/blob/master/tinyquaternion/test/results/Figure_1.png "initial cube")


Now, we define a known quaternion. Assume, we want to rotate about Y-axis by 90 degrees. The quaternion will look like this:

``` python
# define a known quaternion
q = Quaternion(a=np.pi/2, n=np.array([0., 1., 0.]))
```

By using the `a` and `n` keywords, we tell the function that we are representing the quaternion by defining the angle and axis of rotation.


Now, we rotate each point using the quaternion through the method `rotatePoint` as follows:

``` python
# rotate the cube
p1r = q.rotatePoint(p1)
p2r = q.rotatePoint(p2)
p3r = q.rotatePoint(p3)
p4r = q.rotatePoint(p4)
```

and plot the rotated cube 

``` python
cube2 = [
    (p1r[0],p1r[1],p1r[2]), (p2r[0],p2r[1],p2r[2]), (p3r[0],p3r[1],p3r[2]), (p4r[0],p4r[1],p4r[2])
]
plot_cube(cube2)
```

!["rotated cube"](https://github.com/rezaahmadzadeh/tinyquaternion/blob/master/tinyquaternion/test/results/Figure_2.png "rotated cube")

Now let's perform two rotations using quaternions. We consider a new rotation and then combine it with the previous rotation.
Our previous rotation was about Y-axis by 90 degrees. For this one we want to have a rotation about X-axis by 90 degrees. The quaternion will look like this:

``` python
q2 = Quaternion(a=np.pi/2, n=np.array([1.,0.,0.])) # rotate about x by 90
```

Now, we should combine the two quaternions. The rule is that "First rotation should go last", so we can write

``` python
q = q2.mul(q) 
```
This quaternion has the effect of a rotation about Y-axis, followed by a rotation about X-axis.

Now perform the rotation:

``` python
p1r = q.rotatePoint(p1)
p2r = q.rotatePoint(p2)
p3r = q.rotatePoint(p3)
p4r = q.rotatePoint(p4)
```

and plot the rotated cube:

``` python
cube3 = [
    (p1r[0],p1r[1],p1r[2]), (p2r[0],p2r[1],p2r[2]), (p3r[0],p3r[1],p3r[2]), (p4r[0],p4r[1],p4r[2])
]
plot_cube(cube3)
```

!["rotated cube"](https://github.com/rezaahmadzadeh/tinyquaternion/blob/master/tinyquaternion/test/results/Figure_3.png "multiple rotations")

