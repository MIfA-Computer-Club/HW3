#! /usr/bin/env python
import numpy as np
###############
def clock_to_UTC(time,UTCoffset=-5):
    '''
    INPUT
    time = string of form: 'hh:mm:ss'  (24-hour time, CDT)
    
    OUTPUT
    UTC = decimal hours [float], can exceed 24
    '''
    #h, m, s = time.split(':')
    h, m, s = [float(x) for x in time.split(':')]
    #h = float(h)
    #m = float(m)
    # = float(s)
    h = h - UTCoffset    
    UTC = h + m/60 + s/3600

    return UTC

def JD(date, UTC):
    '''
    INPUT
    date = string of form: 'mm/dd/yyyy'
    UTC = decimal hours [float]

    OUTPUT
    JD = days since J2000.0, including fraction of a day [float]
    '''
    m, d, y = [float(x) for x in date.split('/')]
    JD = 367*y - (7*(y+((m+9)/12)))/4 + (275*m)/9 + d + 1721013.5 + UTC/24 - .5*np.sign(100*y+m-190002.5) + .5
    #JD = JD - 2400000.5
    JD = JD - 2451545
    return JD
##############
