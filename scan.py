from utils.init import init_stepper
import json
import time
import board
from adafruit_motor import stepper
import adafruit_hcsr04
import analogio   


class ScanModule:
    def __init__(self):
        with open('config.json', 'r') as file:
            config = json.load(file)

        # Initialize Stepper Slider 
        self.step, self.dirn = init_stepper(board.D2, board.D3, 0.005, 200)

        # Initialize Sensing
        self.pres = adafruit_hcsr04.HCSR04(trigger_pin=board.A1, echo_pin=board.A2)

        # Photoresistor
        self.photoresistor = analogio.AnalogIn(board.A0) 
        self.ADC_REF = self.photoresistor.reference_voltage

    # slider
    def left(self, speed):
        self.step.onestep(direction=stepper.FORWARD, style=stepper.DOUBLE)
        self.ena.duty_cycle = speed
        time.sleep(1)
    
    def right(self):
        self.step.onestep(direction=stepper.BACKWARD, style=stepper.DOUBLE)
        self.ena.duty_cycle = 5000
        time.sleep(1)
    
    # sensing
    def get_distance(self):
        return self.prox.distance

    def get_photoresistor(self):
        return self.ADC_REF * (float(self.photoresistor.value)/float(65535)) * 100

