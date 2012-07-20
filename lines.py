#!/usr/bin/python

import time
import drawlib

AXIS_X = "X"
AXIS_Y = "Y"

DIRECTION_FORWARD = "FWD"
DIRECTION_BACKWARD = "BACK"

# current cursor position
CURRENT_X = 0
CURRENT_Y = 0 

# track the total number of steps
STEP_COUNTER = 0

STEP_SIZE = 1

def prep_step(axis, direction):
    global CURRENT_X, CURRENT_Y, STEP_SIZE, STEP_COUNTER
    # print "---------- STEP ----------"
    # print "Prior to step, x=%d, y=%d" % (CURRENT_X, CURRENT_Y)
    # print " axis: %s  direction: %s" % (axis, direction)
    if (axis == "X"):
        if (direction == DIRECTION_FORWARD):
            CURRENT_X = CURRENT_X + STEP_SIZE
            drawlib.east(STEP_SIZE)
            inc()
        else:
            # a backwards step
            if (CURRENT_X == 0):
                print "  can't move backwards, CURRENT_X already at zero"
            else:
                CURRENT_X = CURRENT_X - STEP_SIZE
                drawlib.west(STEP_SIZE)
                inc()
    elif (axis == "Y"):
        if (direction == DIRECTION_FORWARD):
            CURRENT_Y = CURRENT_Y + STEP_SIZE
            drawlib.north(STEP_SIZE)
            inc()
        else:
            if CURRENT_Y == 0:
                print "  can't move, CURRENT_Y already at zero"
            else:
                CURRENT_Y = CURRENT_Y - STEP_SIZE
                drawlib.south(STEP_SIZE)
                inc()
    else:
        print "  ERROR - invalid axis: %s" % axis

    # print "After step,    x=%d, y=%d" % (CURRENT_X, CURRENT_Y)

def inc():
    global STEP_COUNTER
    STEP_COUNTER = STEP_COUNTER + 1


def bresenham_line((x,y),(x2,y2)):
    """Brensenham line algorithm"""
    steep = 0
    coords = []
    dx = abs(x2 - x)
    if (x2 - x) > 0: 
        sx = 1
    else: 
        sx = -1
    dy = abs(y2 - y)
    if (y2 - y) > 0: 
        sy = 1
    else: 
        sy = -1
    if dy > dx:
        steep = 1
        x,y = y,x
        dx,dy = dy,dx
        sx,sy = sy,sx
    d = (2 * dy) - dx
    for i in range(0,dx):
        if steep: 
            coords.append((y,x))
        else: 
            coords.append((x,y))
        while d >= 0:
            y = y + sy
            d = d - (2 * dx)
        x = x + sx
        d = d + (2 * dy)
    coords.append((x2,y2))
    return coords

def stepToPoint((x,y)):
    global CURRENT_X, CURRENT_Y, STEP_SIZE, STEP_COUNTER

    # print "Stepping to point (%d, %d)" % (x, y)
    # determine which axis, which direction
    if (x != CURRENT_X):
        # need to move along the X axis
        direction = determine_direction(CURRENT_X, x)
        prep_step(AXIS_X, direction)

    # NOTE - we may need steps in BOTH directions, thus,
    # this is not an ELSE if

    if (y != CURRENT_Y):
        # need to move along the Y axis
        direction = determine_direction(CURRENT_Y, y)
        prep_step(AXIS_Y, direction)

        
def determine_direction(curr, new):
    if (curr > new):
        return DIRECTION_BACKWARD
    else: 
        return DIRECTION_FORWARD

def lineTo(x, y):
    global CURRENT_X, CURRENT_Y, STEP_SIZE, STEP_COUNTER

    line_points = bresenham_line((CURRENT_X, CURRENT_Y), (x, y))
    for point in line_points:
        # print "  next coords: (%d, %d)" % (point[0], point[1]) 
        stepToPoint(point)

def star(magnitude):
    global CURRENT_X, CURRENT_Y

    oneThird = (magnitude / 3)
    oneSixth = (magnitude / 3)
    twoThirds = ((2*magnitude) / 3)
    fiveSixths = magnitude - oneSixth
    half = (magnitude / 2)

    # get to a nice starting point
    # lineTo(CURRENT_X + oneSixth, CURRENT_Y)

    star_start_x = CURRENT_X
    star_start_y = CURRENT_Y

    print "----------------- START STAR -----------------"
    printCurrentCoords()

    # up
    print "----------------- UP -----------------"
    lineTo(star_start_x + half, star_start_y + magnitude)
    printCurrentCoords()

    # down
    print "----------------- DOWN -----------------"
    lineTo(star_start_x + fiveSixths, star_start_y)
    printCurrentCoords()

    # up to the left
    print "----------------- UP -----------------"
    lineTo(star_start_x, star_start_y + twoThirds)
    printCurrentCoords()

    # across
    print "----------------- ACROSS -----------------"
    lineTo(star_start_x + magnitude, star_start_y + twoThirds)
    printCurrentCoords()

    # return to start
    print "----------------- BACK -----------------"
    lineTo(star_start_x, star_start_y)
    printCurrentCoords()


def printCurrentCoords():
    global CURRENT_X, CURRENT_Y
    print " ####### CURRENT COORDINATES: (x=%d, y=%d)" % (CURRENT_X, CURRENT_Y)


try:
    # lineTo(1, 2)
    print ""
    
  
except (KeyboardInterrupt, SystemExit):
    print "Exiting early..."
finally:
    print ""
    print "DONE"


