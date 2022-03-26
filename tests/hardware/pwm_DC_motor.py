'''
ESC204 2022W Widget Lab 2, Part 13
Task: Use PWM to modulate the speed of a DC motor.
'''
import board
import time
import digitalio
import pwmio
import sys


dir1_pin = board.D10
dir2_pin = board.D11
en_pin = board.D9

in3 = digitalio.DigitalInOut(dir1_pin)
in4 = digitalio.DigitalInOut(dir2_pin)

in3.direction = digitalio.Direction.OUTPUT
in4.direction = digitalio.Direction.OUTPUT

enb = pwmio.PWMOut(en_pin)

# set initial duty cycle, direction, and step commands
enb.duty_cycle = 0
in3.value = False
in4.value = True

start_time = time.time()
time_limit = 9
while True:
    # rotate motor clockwise
    in3.value, in4.value = (False, True)
    enb.duty_cycle = 40000
    print("Motor is rotating CW")
    time.sleep(5)

    # rotate motor counterclockwise
    in3.value, in4.value = (True, False)
    print("Motor is rotating CCW")
    enb.duty_cycle = 50000
    time.sleep(5)

    # check if we've been doing this for more than the time limit
    total_time = time.time() - start_time
    if total_time > time_limit:
        break

'''
def run_motor(clockwise, duty_cycle):
    in3.value, in4.value (not clockwise, clockwise)
    enb.duty_cycle = duty_cycle
'''
