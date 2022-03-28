import time
import board 
import digitalio

#  once bottle aligned
# use gearmotor to 

# gear motor closes on neck
# then stepper closes on cap
# and twist to remove

# getting the encoder to work (a side file)

'''
ESC204 2022W Widget Lab 2, Part 13
Task: Use PWM to modulate the speed of a DC motor.
'''
import board
import time
import digitalio
import pwmio
import sys


dir1_pin = board.D7
dir2_pin = board.D8
en_pin = board.D11

encoder_A = board.D18
encoder_B = board.D17

encoder_A.direction = digitalio.Direction.INPUT
encoder_B.direction = digitalio.Direction.INPUT

encoder_A.pull = digitalio.Pull.UP
encoder_B.pull = digitalio.Pull.UP

in1 = digitalio.DigitalInOut(dir1_pin) # purple
in2 = digitalio.DigitalInOut(dir2_pin) # white

in1.direction = digitalio.Direction.OUTPUT
in2.direction = digitalio.Direction.OUTPUT



ena = pwmio.PWMOut(en_pin)

# set initial duty cycle, direction, and step commands
ena.duty_cycle = 0
in1.value = False
in2.value = True

start_time = time.time()
time_limit = 9
while True:
    # rotate motor clockwise
    in1.value, in2.value = (False, True)
    # ena.duty_cycle = 40000
    print("Motor is rotating CW")
    print(encoder_A.value, encoder_B.value)
    time.sleep(1)

    # rotate motor counterclockwise
    in1.value, in2.value = (True, False)
    print("Motor is rotating CCW")
    print(encoder_A.value, encoder_B.value)
    ena.duty_cycle = 50000
    time.sleep(1)

    # check if we've been doing this for more than the time limit
    total_time = time.time() - start_time
    if total_time > time_limit:
        break

'''
def run_motor(clockwise, duty_cycle):
    in1.value, in2.value (not clockwise, clockwise)
    ena.duty_cycle = duty_cycle
'''
