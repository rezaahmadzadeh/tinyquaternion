# tinyQuaternion
A tiny python module for Quaternions

Author: Reza Ahmadzadeh - 2019

## 1. Installation

Copy the `tinyQuaternion.py` file into your source folder and import the module as follows:

``` python
from tinyQuaternion import Quaternion
```

The only dependency is `numpy`, so import it as follows:

``` python
import numpy as np
```

## 2. Documentation

### 2.1 Define Quaternions

In this package, there are two methods to define a quaternion:

1. using a 4D array representing the elements of a quaternion `q=[w,x,y,z]`. Define the array using numpy's `ndarray`.

``` python
q = Quaternion(q=np.array([0., 0., 1., 0.]))

>>> q
Quaternion(0.0, 0.0, 1.0, 0.0)
```


2. using an axis-angle representation. Use `n` for denoting the axis of rotation and `a` for denoting the angle of rotation in radians.

``` python
q = Quaternion(a=np.pi/3, n=np.array([0.,0.,1.]))

q
Quaternion(0.8660254037844387, 0.0, 0.0, 0.49999999999999994)
```

### 2.2. Get individual elements 

Each element of the quaternion can be retrieved as follows:

``` python
q.w
q.x
q.y
q.z
```
Example:

``` python
>>> q.w
0.8660254037844387
>>> q.x
0.0
>>> q.y
0.0
>>> q.z
0.49999999999999994
>>> 
```

### 2.3. Get vector or scalar parts

``` python
q.scalar
q.vector
```
Example:

``` python
>>> q.scalar
0.8660254037844387
>>> q.vector
array([0. , 0. , 0.5])
>>> 
```

### 2.4. Get magnitude 

``` python
q.magnitude
```

Example 

``` python
>>> q.magnitude
1.0
```

### 2.5. Check if the quaternion is normalized

``` python
q.is_unit()
```

Example:

``` python
>>> q.is_unit()
True
```

### 2.6. Get normalized quaternion

``` python
q.normalized
```

Example:

``` python
>>> q.normalized
Quaternion(0.8660254037844387, 0.0, 0.0, 0.49999999999999994)
```

### 2.7. Get Conjugate

``` python
q.conjugate
```

Example:

``` python
>>> q.conjugate
Quaternion(0.8660254037844387, -0.0, -0.0, -0.49999999999999994)
```

### 2.8. Get Inverse

``` python
q.inverse
```

Example:

``` python
>>> q.inverse
Quaternion(0.8660254037844387, -0.0, -0.0, -0.49999999999999994)
```

### 2.9. Extract Axis-Angle from Quaternion

``` python
q.axisangle()
```

Example:

``` python
>>> q.axisangle()
(array([0., 0., 1.]), 1.0471975511965974)
```

keep in mind that this is not equal to the original quaternion that we defined above. The main reason is that we have performed some operations on the original quaternion. 

### 2.10. Main operations 

``` python
# addition
q1.add(q2)

# subtraction
q1.sub(q2)

# multiplication
q1.mul(q2)

# division
q1.div(q2)
```

Example:

``` python
>>> q1 = Quaternion(np.array([1.,0.,0.,0.]))
>>> q2 = Quaternion(np.array([0.,0.,0.,1.]))
>>> q1.add(q2)
Quaternion(1.0, 0.0, 0.0, 1.0)
>>> q1.sub(q2)
Quaternion(1.0, 0.0, 0.0, -1.0)
>>> q1.mul(q2)
Quaternion(0.0, 0.0, 0.0, 1.0)
>>> q1.div(q2)
Quaternion(0.0, 0.0, 0.0, -1.0)
```

Note that these operations do not perfrom normalization implicitly.

### 2.11. Rotate point in 3D space using Quaternion (axis-angle)

``` python
q.rotatePoint(p)
```

Example:

The point should be define using a 3D numpy array as follows:

``` python
>>> q = Quaternion(a=np.pi/3, n=np.array([0.,0.,1.]))
>>> p = np.array([1.,2.,-1.])
>>> q.rotatePoint(p)
array([-1.23205081,  1.8660254 , -1.        ])
```

## 3. Tutorials

## 3.1. Rotation Using Quaternions

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

