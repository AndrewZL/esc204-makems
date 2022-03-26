import time
from urllib.request import proxy_bypass
import board
import adafruit_hcsr04

prox_sensor = adafruit_hcsr04.HCSR04(trigger_pin=board.GP2, echo_pin=board.GP3)
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
