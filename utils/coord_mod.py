#! /usr/bin/env python
import numpy as np

################
def sex_to_deg(RA, DEC):
    '''
    INPUT
    RA  = string of form: 'hh:mm:ss.ss'
    DEC = string of form: '[+/-]dd:mm:ss.ss'

    OUTPUT
    RA = right ascension, decimal degrees [float]
    DEC = declination, decimal degrees [float]
    '''
    
    # parse the strings
    h,rm,rs = [float(x) for x in RA.split(':')]  
    d,dm,ds = [float(x) for x in DEC.split(':')]
    decimalRA = 15.*(h + rm/60. + rs/3600.)
    decimalDEC = np.sign(d) * (np.abs(d) + dm/60. + ds/3600.)

    return decimalRA, decimalDEC


def latlong_to_deg(LAT, LONG):
    '''
    INPUT
    LAT = string of form: '[+/-]dd:mm:ss.ss'   + = N
    LONG = string of form: '[+/-]dd:mm:ss.ss'  + = E

    OUTPUT
    LAT = latitude, decimal degrees [float]
    LONG = longitude, decimal degrees [float]
    '''
    latd,latm,lats = [float(x) for x in LAT.split(':')]
    lond,lonm,lons = [float(x) for x in LONG.split(':')]
    decimalLAT = latd + latm/60. + lats/3600.
    #radLAT = decimalLAT * np.pi/180.
    decimalLONG = np.sign(lond) * (np.abs(lond) + lonm/60. + lons/3600.)  # * np.cos(radLAT)

    return decimalLAT, decimalLONG

#################
