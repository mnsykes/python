"""
Program: sykes_sphere.py
Author: Matthew Sykes
Date: 5/30/20

This program will calculate the diameter, circumference, surface area,
and volume of a sphere

Input: User will input the radius of the sphere

Output: Diameter, circumference, surface area and volume of the sphere
"""

import math

#welcome message
print("Welcome to the Sphere Calculator")
print("--------------------------------\n")

#user input for radius of the sphere
radius = float(input("Please enter the radius of the circle: "))

#declare and initialize variables
diameter = round(2 * radius, 2)

circumference = round(diameter * math.pi, 2)

surfaceArea = round(4 * math.pi * radius**2, 2)

volume = round(4/3 * math.pi * radius**3, 2)

#output
print("\nResults")
print("----------------------")

print("Diameter      : ", diameter)

print("Circumference : ", circumference)

print("Surface area  : ", surfaceArea)

print("Volume        : ", volume)
