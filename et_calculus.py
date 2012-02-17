__author__ = 'win7'

from mathematics import Vector
from math import atan2, degrees, sin

def time_in_air(velocity):

    g = 9.80
    mag = velocity.mag()
    alpha = atan2(velocity[1], velocity[0])

    return 2 * mag * sin(alpha) / g

def range_of_x(velocity):

    g = 9.80
    mag = velocity.mag()
    alpha = atan2(velocity[1], velocity[0])

    return pow(mag, 2) * sin(2 * alpha) / g

def max_height(velocity):

    g = 9.80
    mag = velocity.mag()
    alpha = atan2(velocity[1], velocity[0])

    return pow(mag * sin(alpha), 2) / (2 * g)

def find_all(velocity):

    print '{:.3g} seconds in the air.'.format(time_in_air(velocity))
    print '{:.3g} meters from the origin.'.format(range_of_x(velocity))
    print '{:.3g} meters above the ground.'.format(max_height(velocity))

thirty_seven = Vector(300, 400, 500)

find_all(thirty_seven)