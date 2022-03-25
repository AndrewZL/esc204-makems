'''
ESC204 2022W Widget Lab 3Mech, Part 6
Task: Run a stepper motor using the A4988 driver.
'''
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Use this example for digital pin control of an H-bridge driver
# like a DRV8833, TB6612 or L298N.

import time
import board
import digitalio
from adafruit_motor import stepper

DELAY = 0.005
STEPS = 200

# You can use any available GPIO pin on both a microcontroller and a Raspberry Pi.
# The following pins are simply a suggestion. If you use different pins, update
# the following code to use your chosen pins.

# To use with a Raspberry Pi:
microstep_pins = (digitalio.DigitalInOut(board.D2),digitalio.DigitalInOut(board.D3),digitalio.DigitalInOut(board.D4))
step_pin = digitalio.DigitalInOut(board.D5)
dirn_pin = digitalio.DigitalInOut(board.D6)

step_pin.direction = digitalio.Direction.OUTPUT
dirn_pin.direction = digitalio.Direction.OUTPUT

# set motor to run with full steps (not microsteps)
for pin in microstep_pins:
    pin.direction = digitalio.Direction.OUTPUT
    pin.value = False

def single_step(d):
    """
    Sends a pulse to the STEP output to actuate the stepper motor through one step.
    """
    # pulse high to drive step
    step_pin.value = True
    time.sleep(d)

    # bring low in between steps
    step_pin.value = False
    time.sleep(d)

# run one revolution CCW
print("Motor spinning CCW")
dirn_pin.value = True
for i in range(STEPS):
    single_step(DELAY)

# run one revolution CW
print("Motor spinning CW")
dirn_pin.value = False
for i in range(STEPS):
    single_step(DELAY)

# stop motor
step_pin.value = False
