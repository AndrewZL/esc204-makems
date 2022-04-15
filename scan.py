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
        self.step, self.dirn = init_stepper(board.D2, board.D3)

        # Initialize Sensing
        self.pres = adafruit_hcsr04.HCSR04(trigger_pin=board.A1, echo_pin=board.A2)

        # Photoresistor
        self.photoresistor = analogio.AnalogIn(board.A0) 
        self.ADC_REF = self.photoresistor.reference_voltage

    def single_step(self, d):
        """
        Sends a pulse to the STEP output to actuate the stepper motor through one step.
        """
        # pulse high to drive step
        self.step.value = True
        time.sleep(d)

        # bring low in between steps
        self.step.value = False
        time.sleep(d)

    # slider
    def left(self):
        print("Motor spinning CCW")
        self.dirn.value = True
        for i in range(200):
            self.single_step(0.005)
        # stop motor
        self.step.value = False
        
    def right(self):
        print("Motor spinning CCW")
        self.dirn.value = False
        for i in range(200):
            self.single_step(0.005)
        # stop motor
        self.step.value = False
    
    # sensing
    def get_distance(self):
        return self.prox.distance

    def get_photoresistor(self):
        return self.ADC_REF * (float(self.photoresistor.value)/float(65535)) * 100

