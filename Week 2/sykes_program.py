

import math

radius = float(input("Please enter the radius of the circle: "))

diameter = round(2 * radius, 2)

circumference = round(diameter * math.pi, 2)

surfaceArea = round(4 * math.pi * radius**2, 2)

volume = round(4/3 * math.pi * radius**3, 2)

print("The diameter is     : ", diameter)

print("The circumference is: ", circumference)

print("The surface area is : ", surfaceArea)

print("The volume is       : ", volume)
