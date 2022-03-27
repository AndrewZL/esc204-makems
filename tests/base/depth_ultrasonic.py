import time
import board
import adafruit_hcsr04

trig_pin = board.A1
echo_pin = board.A2

prox_sensor = adafruit_hcsr04.HCSR04(trigger_pin=trig_pin, echo_pin=echo_pin)
presence = 20
prox = 5

while True:
    # while bottle is not present
    if prox_sensor.distance > presence:
        print('doing nothing', prox_sensor.distance)
    # while bottle is present but farther than threshold
    elif presence > prox_sensor.distance > prox:
        print('turning motor', prox_sensor.distance)
        time.sleep(2)
    # bottle is present and close enough to grasp
    else:
        print('grasping', prox_sensor.distance)
        time.sleep(2)
        print('releasing')
        time.sleep(2)
    time.sleep(1)  
