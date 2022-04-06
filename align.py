from utils.init import init_dc, init_stepper
import json
import time
import board

class AlignModule:
    def __init__(self):
        with open('config.json', 'r') as file:
            config = json.load(file)
    
        # Initialize DC Motor Grasp
        self.in1, self.in2, self.ena = init_dc(eval(config['align']['dir1_pin']), eval(config['align']['dir2_pin']), eval(config['align']['ena_pin']))
        
    def load(self, speed):
        self.in1.value, self.in2.value = (True, False)
        self.ena.duty_cycle = speed
        time.sleep(1)

    def unload(self):
        self.in1.value, self.in2.value = (False, True)
        self.ena.duty_cycle = 5000
        time.sleep(1)