# Nano - Responder

import time
import board
import busio
import adafruit_hcsr04

from scan import ScanModule
from utils import comm


uart = busio.UART(board.TX, board.RX, baudrate=9600, timeout=0)
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A1, echo_pin=board.A0)
scanner = ScanModule()

UPDATE_INTERVAL = 5
last_time_sent = 0

while True:
    try:
        now = time.monotonic()
        ultrasonic_distance = sonar.distance
        if now - last_time_sent >= UPDATE_INTERVAL:
            message = "{:.2f}".format(ultrasonic_distance)        
            uart.write(bytes("<R,"+message+">", "ascii"))
            if comm.signal(uart):
                print("Signal received, bottle present")
                break
            last_time_sent = now
    
    except:
        print("smth wrong idk")

time.sleep(5)

while True:
    try:
        if comm.signal(uart):
            print("Signal received, begin scanning")
            break
    except:
        print("smth wrong idk")

# do scan

scanner.left()
scanner.right()

uart.write(bytes("<R,done scan>", "ascii"))

