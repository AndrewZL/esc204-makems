# Use the stepper motor to close the cap "unscrewer"
# This proves functionality, and can be re-run as needed to test the mechanical system
# In later stages, we'll tune the number of rotations to finish removing the cap, 
# but that's out of scope for this widget lab

import time
import board
import digitalio
from adafruit_motor import stepper

DELAY = 0.005
STEPS = 200

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
