# tinyquaternion
A tiny python module for Quaternions




## Using Quaternions for Rotation

To perform this test, we first plot a cube using the function `plotCube.py` provided in the test folder. 


    # plot the initial cube
    p1 = np.array([0.,0.,0.])
    p2 = np.array([0.,.1,0.])
    p3 = np.array([2.,0.,0.])
    p4 = np.array([0.,0.,.1])
    
    cube1 = [
        (p1[0],p1[1],p1[2]), (p2[0],p2[1],p2[2]), (p3[0],p3[1],p3[2]), (p4[0],p4[1],p4[2])
    ]
    plot_cube(cube1)
    
This will result in the following cube:

