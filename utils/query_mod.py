#! /usr/bin/env python

import astropy
import astroquery.simbad


def query(name):
    '''
    INPUT
    name = object string to query

    OUTPUT
    RA  = string of form: 'hh:mm:ss.ss'
    DEC = string of form: '[+/-]dd:mm:ss.ss'
    '''
    result_table = astroquery.simbad.Simbad.query_object(name)
    ra, dec = result_table['RA'][0], result_table['DEC'][0]
    ra, dec = ':'.join(ra.split()), ':'.join(dec.split())
    return ra, dec


def main():
    name = 'm31'
    ra, dec = query(name)
    print ra, dec


if __name__ == '__main__':
    main()
