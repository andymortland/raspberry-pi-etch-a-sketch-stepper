#!/usr/bin/python

import time
from quick2wire.gpio import Pin, exported

y_fudge_factor = 0.8

def tearDown(pinObj):
    pinObj.value = 0
    pinObj.unexport()

X_DIRECTION_PIN = 16
X_STEP_PIN = 18

Y_DIRECTION_PIN = 22
Y_STEP_PIN = 26

X_DIR = Pin(X_DIRECTION_PIN, Pin.Out)
X_STEP = Pin(X_STEP_PIN, Pin.Out)

Y_DIR = Pin(Y_DIRECTION_PIN, Pin.Out)
Y_STEP = Pin(Y_STEP_PIN, Pin.Out)

DIRECTION_FORWARD = 1
DIRECTION_BACKWARD = 0

ALL_PINS = [X_DIR, X_STEP, Y_DIR, Y_STEP]


# STEPPER_PAUSE = 0.15
STEPPER_PAUSE = 0.05

X_CONTROLS = [X_STEP, X_DIR]
Y_CONTROLS = [Y_STEP, Y_DIR]

def step(axis, direction):
    dirPin = axis[0]
    stepPin = axis[1]
    # set the direction
    dirPin.value = direction
    # take one step
    stepPin.value = 1
    time.sleep(STEPPER_PAUSE)
    stepPin.value = 0

def east(steps):
    # print " --> east for %d steps" % steps
    stepCounter = 0
    while (stepCounter < steps):
        step(X_CONTROLS, DIRECTION_FORWARD)
        stepCounter = stepCounter + 1

def west(steps):
    # print " <-- west for %d steps" % steps
    stepCounter = 0
    while (stepCounter < steps):
        step(X_CONTROLS, DIRECTION_BACKWARD)
        stepCounter = stepCounter + 1

def north(steps):
    # print " | north for %d steps" % steps
    stepCounter = 0
    while (stepCounter < steps):
        step(Y_CONTROLS, DIRECTION_FORWARD)
        stepCounter = stepCounter + 1

def south(steps):
    # print " | south for %d steps" % steps
    stepCounter = 0
    while (stepCounter < steps):
        step(Y_CONTROLS, DIRECTION_BACKWARD)
        stepCounter = stepCounter + 1

def northeast(steps):
    # print " / northeast for %d steps" % steps
    stepCounter = 0
    while (stepCounter < steps):
        step(X_CONTROLS, DIRECTION_FORWARD)
        step(Y_CONTROLS, DIRECTION_FORWARD)
        stepCounter = stepCounter + 1

def northwest(steps):
    # print " \ northwest for %d steps" % steps
    stepCounter = 0
    while (stepCounter < steps):
        step(X_CONTROLS, DIRECTION_BACKWARD)
        step(Y_CONTROLS, DIRECTION_FORWARD)
        stepCounter = stepCounter + 1

def southeast(steps):
    # print " \ southeast for %d steps" % steps
    stepCounter = 0
    while (stepCounter < steps):
        step(X_CONTROLS, DIRECTION_FORWARD)
        step(Y_CONTROLS, DIRECTION_BACKWARD)
        stepCounter = stepCounter + 1

def southwest(steps):
    # print " / southwest for %d steps" % steps
    stepCounter = 0
    while (stepCounter < steps):
        step(X_CONTROLS, DIRECTION_BACKWARD)
        step(Y_CONTROLS, DIRECTION_BACKWARD)
        stepCounter = stepCounter + 1

def octogon(size):
    north(size)
    northeast(size)
    east(size)
    southeast(size)
    south(size)
    southwest(size)
    west(size)
    northwest(size)

def octogons(largest, smallest):
    if (largest == smallest):
        return
    octogon(largest)
    octogons((largest - 1), smallest)

def square(size):
    east(size)
    south(size)
    west(size)
    north(size)

def nw_triangle(size):
    east(size)
    southwest(size)
    north(size)

def ne_triangle(size):
    east(size)
    south(size)
    northwest(size)

def se_triangle(size):
    south(size)
    west(size)
    northeast(size)

def sw_triangle(size):
    southeast(size)
    west(size)
    north(size)

def squares(largest, smallest):
    if (largest == smallest):
        return
    square(largest)
    squares((largest - 1), smallest)

def square_density(size, spacing):
    if (size <= 5):
        return
    square(size)
    square_density((size - spacing), spacing)

def solid_block(size):
    square_density(size, 1)

def block_density_2(size):
    square_density(size, 2)

def block_density_3(size):
    square_density(size, 3)

def empty_block(size):
    square(size)

def blocks_demo(size):
    solid_block(size)
    east(size/2)
    block_density_2(size)
    east(size/2)
    block_density_3(size)
    east(size/2)
    empty_block(size)
    east(size/2)
    block_density_3(size)
    east(size/2)
    block_density_2(size)
    east(size/2)
    solid_block(size)






