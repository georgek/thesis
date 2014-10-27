#!/usr/bin/env python

import sys
import cmath

def polar2cart(dist, angle):
    c = cmath.rect(dist, float(angle)/180 * cmath.pi)
    return (round(c.real, 2), round(c.imag, 2))

for d in range(10):
    angles = map(lambda n: (360.0/(8*d))*n, range(8*d)) if d > 0 else [0]
    for a in angles:
        coord = polar2cart(d, a)
        print "{:f} {:f}".format(coord[0], coord[1])

