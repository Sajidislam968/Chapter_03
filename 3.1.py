from math import pi,sin,sqrt
r = float(input("Enter the length from the center to a vertex: "))
s = 2*r*sin(pi/5)
area = (3*sqrt(3)*s*s)/2
print("The area of the triangle with radius ",r," is ",format(area,".2f"))