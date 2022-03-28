# Read the distance of the bottle to the actuators, using an ultrasonic sensor
# Several 
import time
import board
import adafruit_hcsr04

trig_pin = board.A1
echo_pin = board.A2

prox_sensor = adafruit_hcsr04.HCSR04(trigger_pin=trig_pin, echo_pin=echo_pin)
presence = 15
prox = 5

while True:
    # while bottle is not present
    if prox_sensor.distance > presence:
        print('doing nothing', prox_sensor.distance)
    # while bottle is present but farther than threshold
    elif presence > prox_sensor.distance > prox:
        print('moving closer', prox_sensor.distance)
        # here, we'd activate the bottle feed mechanism, not in scope for Widget 3
        time.sleep(2)
    # bottle is present and close enough to grasp
    else:
        # here, we'd activate the grasper, proxyed in widget lab 3 
        print('grasping', prox_sensor.distance)
        time.sleep(2)
        # once the grasping is complete (confirmed by encoder), the cap-unscrewer runs
        print('releasing')
        time.sleep(2)
    time.sleep(1)  
