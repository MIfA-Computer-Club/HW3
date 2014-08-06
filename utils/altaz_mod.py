#! /usr/bin/env python

###############
from math import *

def HA_AltAZ(HA, DEC, LAT):
    '''
    INPUT
    HA = decimal degrees [float]
    DEC = decimal degrees [float]
    LAT = decimal degrees [float]

    OUTPUT
    ALT = altitude, decimal degrees [float]
    AZ = azimuth, decimal degrees [float]
    '''

    HA = radians(HA)
    DEC = radians(DEC)
    LAT = radians(LAT)

    ALT = asin(sin(DEC)*sin(LAT)+cos(DEC)*cos(LAT)*cos(HA))
    A =  acos((sin(DEC) - sin(ALT)*sin(LAT))/(cos(ALT)*cos(LAT)))

    if sin(HA) < 0:
      AZ = A
    else:
      AZ = 2*pi - A

    return degrees(ALT), degrees(AZ)
###############
