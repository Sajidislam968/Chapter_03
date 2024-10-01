from math import acos,sin,cos,radians
x1,y1 = map(float,input("Enter point 1(latitude and longitude) in degrees: ").split(","))
x2,y2 = map(float,input("Enter point 2(latitude and longitude) in degrees: ").split(","))
x1 = radians(x1)
y1 = radians(y1)
x2 = radians(x2)
y2 = radians(y2)
d = 6371.01*acos(sin(x1)*sin(x2)+cos(x1)*cos(x2)*cos(y1-y2))
print(d)

