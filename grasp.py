from utils.init import init_dc, init_stepper
import json
import time
import board
from adafruit_motor import stepper
import adafruit_hcsr04

class GraspModule:
    def __init__(self):
        with open('config.json', 'r') as file:
            config = json.load(file)
    
        # Initialize DC Motor Grasp
        self.in1, self.in2, self.ena = init_dc(eval(config['grasp']['dir1_pin']), eval(config['grasp']['dir2_pin']), eval(config['grasp']['ena_pin']))
        
        # Initialize Stepper Motor Cap Removal
        # note: 200 is the number of steps per revolution, TODO: put all of this into config later
        self.step, self.dirn = init_stepper(board.D2, board.D3, 0.005, 200)

        # Initialize Sensing
        self.prox = adafruit_hcsr04.HCSR04(trigger_pin=board.A1, echo_pin=board.A2)

    # grasp
    def close(self, speed):
        self.in1.value, self.in2.value = (True, False)
        self.ena.duty_cycle = speed
        time.sleep(1)

    def open(self):
        self.in1.value, self.in2.value = (False, True)
        self.ena.duty_cycle = 5000
        time.sleep(1)

    # removal
    def remove(self, speed):
        self.step.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        self.ena.duty_cycle = speed
        time.sleep(1)
    
    def done_remove(self):
        self.step.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        self.ena.duty_cycle = 5000
        time.sleep(1)
    
    # sensing
    def get_distance(self):
        return self.prox.distance
