# Reads encoder value off the grasping motor
# Currently, not set to do anything interesting, just oscillates directions until we hit a time limit
# We use this to test the encoder and motor function
import board
import time
import digitalio
import pwmio
import sys
import analogio

## Pin Setup
dir1_pin = board.D7
dir2_pin = board.D8
en_pin = board.D11 # not a relevant pin, since we jumped the enable directly to 5V power
# retained so that if we go back to 3.3V power, we know how to layout the board

encoder_A_pin = board.A2 # yellow
encoder_B_pin = board.A1 # green


encoder_B = analogio.AnalogIn(encoder_B_pin)
encoder_A = analogio.AnalogIn(encoder_A_pin) 


in1 = digitalio.DigitalInOut(dir1_pin) # purple
in2 = digitalio.DigitalInOut(dir2_pin) # white

in1.direction = digitalio.Direction.OUTPUT
in2.direction = digitalio.Direction.OUTPUT

# ena = pwmio.PWMOut(en_pin) # again, irrelevant

# set initial duty cycle, direction, and step commands
ena.duty_cycle = 0
in1.value = False
in2.value = True

start_time = time.time()
time_limit = 9

# Continually oscillate direction and read encoder value
while True:
    # rotate motor clockwise
    in1.value, in2.value = (False, True)
    # ena.duty_cycle = 40000
    print("Motor is rotating CW")
    print(encoder_A.value, encoder_B.value) # Next steps are using these values
    time.sleep(1)

    # rotate motor counterclockwise
    in1.value, in2.value = (True, False)
    print("Motor is rotating CCW")
    print(encoder_A.value, encoder_B.value)
    ena.duty_cycle = 50000
    time.sleep(1)

    # Don't want to run for too long and overheat motor: stop after time_limit seconds
    total_time = time.time() - start_time
    if total_time > time_limit:
        break

# We're still learning how to use the encoder, but can't do much testing since the gearbox is broken
# And since we only learned that fairly late, we haven't had time to proxy alternatives

