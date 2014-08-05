#! /usr/bin/env python
##########################################################
##  Staralt clone  [http://catserver.ing.iac.es/staralt/]
##     July 2014
##     MIfA Computer Club
##     https://github.com/MIfA-Computer-Club/HW3
##
##  $ python staralt.py -h 
##########################################################
from utils import *
import argparse
import matplotlib.pyplot as plt
from datetime import date
import numpy as np

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Staralt clone.  Given a date, location, and object (or RA/DEC), display elevation over the course of a night.')
    parser.add_argument('name',nargs='?',type=str,
                        help="Name of object",
                        default=None)
    parser.add_argument('-RA',type=str,
                        help="RA of object 'hh:mm:ss.ss'")
    parser.add_argument('-DEC',type=str,
                        help="DEC of object '[+/-]dd:mm:ss.ss")
    parser.add_argument('-date',type=str,
                        help="Date of observation 'mm/dd/yyyy'. Default=today",
                        default=date.today().strftime('%m/%d/%Y'))
    parser.add_argument('-LAT',metavar='latitude',type=str,
                        help="LAT of observatory '[+/-]dd:mm:ss.ss'",
                        default='44:58:30.93')
    parser.add_argument('-LONG',type=str,metavar='longitude',
                        help="LONG of observatory '[+/-]dd:mm:ss.ss'",
                        default='-93:14:04.26')

    # Parse arguments
    args = parser.parse_args()

    # If name, query coordinates
    if args.name:
        RA, DEC = query(args.name)
        
    elif (args.RA and args.DEC):
        RA, DEC = args.RA, args.DEC

    else:
        raise NameError('Must specify object name or coordinates')

    # GO!
    
    # Generate list of times, 8pm to 8am
    times = ['%i:00:00' % i for i in range(20,24)]
    times += ['0%i:00:00' % i for i in range(0,9)]
    ## times = ['20:00:00', '21:00:00', '22:00:00', '23:00:00',
    ##          '00:00:00', '01:00:00', '02:00:00 ...]

    # Convert times to UTC
    UTCs = map(clock_to_UTC, times)

    # Convert UTC times to JDs
    JDs = [JD(args.date, utc) for utc in UTCs]

    # Convert LAT and LONG to degree format
    lat_d, long_d =  latlong_to_deg(args.LAT, args.LONG)

    # Convert RA, DEC to degree format
    ra_d, dec_d = sex_to_deg(RA, DEC)

    # Calculate LST at each UTC time
    LSTs = [LST(jd, long_d, utc) for jd,utc in zip(JDs, UTCs)]

    # Calculate HAs from RA at each LST angle
    HAs = [RA_to_HA(ra_d, lst) for lst in LSTs]

    # Calculate Alt/Az for each HA
    alts, azs = zip(*[HA_AltAZ(ha, dec_d, lat_d) for ha in HAs])
    
    # Convert UTCs for plotting
    UTCs = np.array(UTCs) % 24
    
    # Plot altitude vs time
    plt.plot(UTCs, alts,'ro', label=' '.join([RA,DEC]))
    plt.xlabel('UTC [hours]')
    plt.ylabel('Altitude [deg]')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
