'''
ESC204 2022W Widget Lab 2, Part 13
Task: Use PWM to modulate the speed of a DC motor.
'''
import board
import time
import digitalio
import pwmio
import sys
from adafruit_motor import stepper

# set up logic inputs to motor driver ("step" and "pulse") as outputs
in1 = digitalio.DigitalInOut(board.D7)
in2 = digitalio.DigitalInOut(board.D8)
in1.direction = digitalio.Direction.OUTPUT
in2.direction = digitalio.Direction.OUTPUT

# set up PWM output to motor driver
ena = pwmio.PWMOut(board.D11)

# set initial duty cycle, direction, and step commands
ena.duty_cycle = 0
in1.value = False
in2.value = True

start_time = time.time()
time_limit = 9
while True:
    # rotate motor clockwise
    in1.value, in2.value = (False, True)
    ena.duty_cycle = 40000
    print("Motor is rotating CW")
    time.sleep(5)

    # rotate motor counterclockwise
    in1.value, in2.value = (True, False)
    print("Motor is rotating CCW")
    ena.duty_cycle = 50000
    time.sleep(5)

    # check if we've been doing this for more than the time limit
    total_time = time.time() - start_time
    if total_time > time_limit:
        break
