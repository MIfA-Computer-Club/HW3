#! /usr/bin/env python

#################
def LST(JD, LONG, UTC):
    '''
    INPUT
    JD = days since J2000.0, including fraction of a day [float]
    LONG = decimal degrees [float]
    UTC = decimal hours [float]

    OUTPUT
    LST = local sidereal time, decimal degrees (NOT hours) [float]
    '''
    LST=100.46+.985647*JD+LONG+15*UTC

    if LST>360 or LST <0:
      LST=LST%360
    

    return(LST)
def RA_to_HA(RA, LST):
    '''
    INPUT
    RA = decimal degrees [float]
    LST = decimal degrees [float]

    OUTPUT
    HA = hour angle, decimal degrees [float]  (0 < HA < 360)
    '''
    HA=LST-RA

    if HA<0:
      HA=HA+360
    return(HA)
###############
