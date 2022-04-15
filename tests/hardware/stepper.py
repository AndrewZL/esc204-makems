# Use the stepper motor to close the cap "unscrewer"
# This proves functionality, and can be re-run as needed to test the mechanical system
# In later stages, we'll tune the number of rotations to finish removing the cap, 
# but that's out of scope for this widget lab

import time
import board
import digitalio
from adafruit_motor import stepper
from utils.init import init_stepper

DELAY = 0.005
STEPS = 200

step_pin, dirn_pin = init_stepper(board.GP9, board.GP8)

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
