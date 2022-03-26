import board
import digitalio
import pwmio
from adafruit_motor import stepper


def init_dc(dir1_pin, dir2_pin, en_pin, default_dir='CW'):
    in3 = digitalio.DigitalInOut(dir1_pin)
    in4 = digitalio.DigitalInOut(dir2_pin)

    in3.direction = digitalio.Direction.OUTPUT
    in4.direction = digitalio.Direction.OUTPUT
    # TODO: check these directions lol
    if default_dir == 'CW':
        in3.value = True
        in4.value = False
    else: 
        in3.value = False
        in4.value = True

    enb = pwmio.PWMOut(en_pin, duty_cycle = 0)

    return in3, int4, enb


def init_stepper(mstep_pin1, mstep_pin2, mstep_pin3, step_pin, dir_pin, delay, steps, default_dir='CW'):
    step_pin = digitalio.DigitalInOut(step_pin)
    dirn_pin = digitalio.DigitalInOut(dir_pin)
        
    step_pin.direction = digitalio.Direction.OUTPUT
    dirn_pin.direction = digitalio.Direction.OUTPUT

    if default_dir == 'CW':
        dirn_pin.value = False
    else:
        dirn_pin.value = True
    
    return step_pin, dirn_pin

    microstep_pins = (digitalio.DigitalInOut(board.D2),digitalio.DigitalInOut(board.D3),digitalio.DigitalInOut(board.D4))
step_pin = digitalio.DigitalInOut(board.D5)
dirn_pin = digitalio.DigitalInOut(board.D6)

step_pin.direction = digitalio.Direction.OUTPUT
dirn_pin.direction = digitalio.Direction.OUTPUT