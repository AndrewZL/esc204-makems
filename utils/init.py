import board
import digitalio
import pwmio
from adafruit_motor import stepper


def init_dc(dir1_pin, dir2_pin, ena_pin, default_dir='CW'):
    in1 = digitalio.DigitalInOut(dir1_pin)
    in2 = digitalio.DigitalInOut(dir2_pin)

    in1.direction = digitalio.Direction.OUTPUT
    in2.direction = digitalio.Direction.OUTPUT
    # TODO: check these directions lol
    if default_dir == 'CW':
        in1.value = True
        in2.value = False
    else: 
        in1.value = False
        in2.value = True

    ena = pwmio.PWMOut(ena_pin, duty_cycle = 0)

    return in1, in2, ena


def init_stepper(step_pin, dir_pin, delay, steps, default_dir='CW'):
    step_pin = digitalio.DigitalInOut(step_pin)
    dirn_pin = digitalio.DigitalInOut(dir_pin)
        
    step_pin.direction = digitalio.Direction.OUTPUT
    dirn_pin.direction = digitalio.Direction.OUTPUT

    if default_dir == 'CW':
        dirn_pin.value = False
    else:
        dirn_pin.value = True
    
    return step_pin, dirn_pin