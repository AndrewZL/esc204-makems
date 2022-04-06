from utils.init import init_dc, init_stepper
import json
import time
import board
from adafruit_motor import stepper
import adafruit_hcsr04
import rotaryio

class GraspModule:
    def __init__(self):
        with open('config.json', 'r') as file:
            config = json.load(file)
    
        # Initialize DC Motor Grasp
        self.in1, self.in2, self.ena = init_dc(eval(config['grasp']['dir1_pin']), eval(config['grasp']['dir2_pin']), eval(config['grasp']['ena_pin']))
        
        # Initialize Stepper Motor Cap Removal
        # note: 200 is the number of steps per revolution, TODO: put all of this into config later
         # self.step, self.dirn = init_stepper(board.D2, board.D3, 0.005, 200)

        # Initialize Sensing
        # self.prox = adafruit_hcsr04.HCSR04(trigger_pin=board.A1, echo_pin=board.A2)

        # Initialize Encoder
        self.encoder = rotaryio.IncrementalEncoder(eval(config['grasp']['encoder_a']), eval(config['grasp']['encoder_b']))
        self.last_position = 0

    # encoder test
    def encoder_test(self):
        speed = 50000
        self.in1.value, self.in2.value = (True, False)
        self.ena.duty_cycle = speed
        for i in range(0,100):
            print(self.encoder.position, speed)
            time.sleep(0.25)
            if i / 4 == i / 4.0:
                speed = speed - 500
                self.ena.duty_cycle = speed

    # grasp
    def close(self, target_speed):
        time_running = 0
        self.in1.value, self.in2.value = (True, False)
        self.ena.duty_cycle = target_speed
        last_position = self.encoder.position
        time.sleep(0.05) # give time for motor to come to speed
        target_encoder_speed = self.encoder.position - last_position 
        # units in encoder are not necessarily units in pwm control, so we can't compare the two. 
        # this assumes that initially, a good speed is attainable
        # if the jam is right away, this method produces garbage
        while True: 
            speed = self.encoder.position - last_position
            if speed < target_encoder_speed * 0.01:
                break
            last_position = self.encoder.position
            
            print(self.encoder.position, speed)
            time.sleep(0.05)

            # Mostly for testing
            time_running = time_running + 0.05
            if time_running > 2:
                break
        self.ena.duty_cycle = 0 # stop the motor when we're done

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
