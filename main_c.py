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
# It controls:
# the Grasper (grippy and unscrewer)
# the Aligner (roller)

def main():
    uart = busio.UART(board.GP0, board.GP1, baudrate=9600, timeout=0)

    with open('config.json', 'r') as file:
        config = json.load(file)

    grasper = GraspModule()
    align = AlignModule()

    while True:
    # every step in the process requires "present" from the responder 
    
        message = comm.read(uart)
        if message is not "present":
            continue
        
        align.load(50000)

        grasper.close()
        grasper.remove()

        uart.write(bytes("a", "ascii"))

        align.unload()

if __name__ == '__main__':
    main()


# PI 0


uart = busio.UART(board.GP0, board.GP1, baudrate=9600, timeout=0)

comm.read(uart)
uart.write(bytearray('z'))
print('Bottle Present, begin processing')

