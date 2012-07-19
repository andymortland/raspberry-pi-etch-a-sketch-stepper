#!/usr/bin/python

import drawlib

try:
    drawlib.octogons(20,8)
  
except (KeyboardInterrupt, SystemExit):
    print "Exiting early..."
finally:

    for pin in drawlib.ALL_PINS:
        drawlib.tearDown(pin)

