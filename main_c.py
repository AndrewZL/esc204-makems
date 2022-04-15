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


def present(uart):
    message = comm.read(uart)
    while message is not "present":
        time.sleep(5)
        message = comm.read(uart)

def setup():
    grasper = GraspModule()
    align = AlignModule()

    return grasper, align
def test():
    grasper, align = setup()
    # grasper.remove()
   #  grasper.close(45000)
    grasper.controlled_move(45000,False)

def main():
    uart = busio.UART(board.GP0, board.GP1, baudrate=9600, timeout=0)

    with open('config.json', 'r') as file:
        config = json.load(file)

    grasper = GraspModule()
    align = AlignModule()

    # every step in the process requires "present" from the responder 
    
    # present()
    # align.load(50000)

    # present()
    grasper.close(45000)
    print("closed")

    # present()
    grasper.remove_cap()
    print("cap removed")

    # present()
    grasper.done_remove_cap()
    print("allowing cap to fall")

    # present()
    grasper.open(45000)
    print("opened")

    # present()
    uart.write(bytearray('z'))
    print('Bottle Done Pre-Processing, Begin Scan')

    message = comm.read(uart)
    while message is not "done scan":
        time.sleep(5)
        message = comm.read(uart)

    align.unload()
    

if __name__ == '__main__':
    main()
