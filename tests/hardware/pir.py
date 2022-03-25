'''
ESC204 2022W Widget Lab 2, Part 7
Task: Take readings using a passive infrared sensor.
'''

import time
import board
import digitalio

# Configure the internal GPIO connected to the LED as a digital output
led = digitalio.DigitalInOut(board.LED)
led.direction = digitalio.Direction.OUTPUT

# Setup digital input for PIR sensor:
pir = digitalio.DigitalInOut(board.GP1)
pir.direction = digitalio.Direction.INPUT

while True:
    # set LED value to match PIR sensor output
    pir_value = pir.value
    led.value = pir_value

    # plot PIR sensor output
    if pir_value:
        print((1,))

    else:
        print((0.01,))

    time.sleep(0.2)
