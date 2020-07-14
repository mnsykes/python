"""
Greatest common divisor

"""

num1 = int(input("Enter a number: "))

num2 = int(input("Enter a larger number: "))

gcd1 = num2 % num1

print(gcd1)

gcd2 = num1 % gcd1

print(gcd2)

