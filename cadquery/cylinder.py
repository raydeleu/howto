import cadquery as cq 

height = 100
cylinderRadius = 10

Cylinder = cq.Workplane("XY").cylinder(height,cylinderRadius)

xDim = 10
yDim = 40
zDim = 80

Box      = cq.Workplane("XY").box(xDim,yDim,zDim)

sphereRadius = 20

Sphere      = cq.Workplane("XY").sphere(sphereRadius,(0,0,1),-90,90,360,False,False,True)
Sphere2     = cq.Workplane("XY").sphere(sphereRadius)


xMin = 0
zMin = 0
xMax = 10
zMax = 30 

Wedge       = cq.Workplane("XY").wedge(xDim*2,yDim*2,zDim/2,xMin,zMin,xMax,zMax)

# A wedge can be thought of like a box with a base plane on the XZ-plane
# and directed in the y-direction. 
# The xMin and xMax then describe the rectangle at the distance yDim
# If both xMin and xMax are half xDim, then a perfect point in the middle is created
# The same is true for the z-dimensions. 


