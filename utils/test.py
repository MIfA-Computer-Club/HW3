#! /usr/bin/env python
import argparse
import sys
sys.path.append("..")
from utils import *
import numpy as np
from astropy.coordinates import SkyCoord
import astropy.units as u

def test_coord(filename,method,in_args,ans,tolerance):
    mname = method.__name__
    out_args = method(*in_args)

    if out_args is None:
        print "   '%s:%s': not implemented" % (filename,mname)
        return

    out_args = SkyCoord(' '.join(out_args),frame='icrs',unit=(u.hourangle,u.deg))
    ans = SkyCoord(' '.join(ans),frame='icrs',unit=(u.hourangle,u.deg))
    diff = out_args.separation(ans).to(u.arcsec).value
    if diff < tolerance:
        print "   '%s:%s': successful!" % (filename,mname)
    else:
        print "   '%s:%s': answer not within tolerance" % (filename,mname)

    return

def test_method(filename,method,in_args,ans,tolerance):
    mname = method.__name__
    out_args = method(*in_args)

    if out_args is None:
        print "   '%s:%s': not implemented" % (filename,mname)
        return
    try:
        diff = np.abs(ans-out_args)
    except Exception as e:
        print "   '%s:%s': %s" % (filename,mname,e)
    else:
        diff = np.mean(diff)
        if diff < tolerance:
            print "   '%s:%s': successful!" % (filename,mname)
        else:
            print "   '%s:%s': answer not within tolerance" % (filename,mname)

    return


def main():
    parser = argparse.ArgumentParser(description='Test client for Staralt utilities')
    parser.add_argument('filelist',nargs='+',help='List of files to test')
    
    #Parse arguments
    args = parser.parse_args()
    
    for filename in args.filelist:
        if filename in ('__init__.py','test.py'):
            continue

        print '\nTesting %s' % filename

        if filename == 'coord_mod.py':
            test_method(filename,sex_to_deg,
                        ("00:42:44.33","41:16:07.50"),
                        np.array([10.684,41.2687]),
                        0.01)
            test_method(filename,latlong_to_deg,
                        ("40:46:26.40","-73:59:03.48"),
                        np.array([40.774,-73.9843]),
                        0.01)
            
        elif filename == 'altaz_mod.py':
            test_method(filename,HA_AltAZ,
                        (54.382617,36.466667,52.5),
                        np.array([49.169122,269.14634]),
                        2.0)
            
        elif filename == 'angle_mod.py':
            test_method(filename,LST,
                        (5396.1458333333489,78.0,15.5),
                        329.652675863475,
                        2.0)  #2456941.1458333335
            test_method(filename,RA_to_HA,
                        (250.425,304.80762),
                        54.382617,
                        2.0)

        elif filename == 'query_mod.py':
            test_coord(filename,query,
                        ('vega',),
                        ('18:36:56.34','+38:47:01.28'),
                       4.0)

        elif filename == 'time_mod.py':
            test_method(filename,clock_to_UTC,
                        ('12:30:00',-5),
                        17.5,
                        0.5)
            test_method(filename,JD,
                        ('08/01/2014',17.5),
                        5326.229170000181,
                        2.0)


if __name__ == '__main__':
    main()



