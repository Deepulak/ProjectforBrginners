# cmath module
# Mathematical functions defined in math module 
# of python's standard library process floating point 
# numbers, python library contains cmath module
# Complex number z = x + yj us a Cartesian representation.
# It is internally represented in polar coordinates with
# its modulus r (as returned by built in abs() function)
# and the phase angle 0| (pronouncced as phi) which is 
# counter clockwise angle in radians, between the
# x axis and the line joining x with the origin.
# Follwing diagram illustrates polar repesentation
# of complex number

# polar() function 
# This function return polar representation of 
# a Cartesian notation of complex number.
# The return value is a tuple consisting of modulus and phase
import cmath
a = 2+4j
print(cmath.polar(a)) 

# phase() function
# This function returns counterclockwise angle 
# between x axis and segment joining with 
# a origin. The angle is represented in radians
# and is between pi and -pi with a symbol
print(cmath.phase(a))
#z = x+yj

# rect() funciton
# This function returns Cartesian representation
# of complex number represented in polar form.
# i:e. in modulus phase
print(cmath.rect(47213595499958, 1.1071487177940904))


# cmath.sin() function 
# THis function returns the sine trigonometric
# ratio for phase angle represented in radians.
p = cmath.phase(a)
print(cmath.sin(p))
