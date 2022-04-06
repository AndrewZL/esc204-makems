import board
import digitalio
import pwmio
import busio

import time
import json

from grasp import GraspModule
from align import AlignModule

from utils import comm

# This is the Controller - the Pico

uart = busio.UART(board.GP0, board.GP1, baudrate=9600, timeout=0)

with open('config.json', 'r') as file:
    config = json.load(file)

grasper = GraspModule()
align = AlignModule()

grasper.encoder_test()
'''
while True:
    # every step in the process requires "present" from the responder 
    
    message = comm.read(uart)
    if message is not "present":
        continue
      
    
    # scan has detected bottle
    while grasper.get_distance() > 10:
        align.load()

    # bottle in position for grasping
    grasper.close()
    grasper.remove()

    uart.write(bytes("a", "ascii"))



'''
