
from utils.init import init_dc, init_stepper
import json
import time
import board
from adafruit_motor import stepper
import adafruit_hcsr04
import rotaryio

ccw = True

class GraspModule:
    
    def __init__(self):
        with open('config.json', 'r') as file:
            config = json.load(file)
    
        # Initialize DC Motor Grasp
        self.in1, self.in2, self.ena = init_dc(eval(config['grasp']['dir1_pin']), eval(config['grasp']['dir2_pin']), eval(config['grasp']['ena_pin']))
        self.ena.duty_cycle = 0
        # Initialize Stepper Motor Cap Removal
        self.step, self.dir = init_stepper(eval(config['cap_removal']['step_pin']), eval(config['cap_removal']['direction_pin']))
        
        # Initialize Sensing
        # self.prox = adafruit_hcsr04.HCSR04(trigger_pin=board.A1, echo_pin=board.A2)

        # Initialize Encoder
        self.encoder = rotaryio.IncrementalEncoder(eval(config['grasp']['encoder_a']), eval(config['grasp']['encoder_b']))
        self.last_position = 0
    
    def single_step(d):
            """
            Sends a pulse to the STEP output to actuate the stepper motor through one step.
            """
            # pulse high to drive step
            self.step.value = True
            time.sleep(d)

            # bring low in between steps
            self.step.value = False
            time.sleep(d)

    def controlled_move(self,target_speed, direction=ccw):
        timestep = 0.05
        time_running = 0
        self.in1.value, self.in2.value = (direction, not direction)
        self.ena.duty_cycle = target_speed
        self.last_position = self.encoder.position
        time.sleep(timestep * 10) # give time for motor to come to speed
        target_encoder_speed = abs((self.encoder.position - self.last_position)/10)
        print("target", target_encoder_speed)
        # units in encoder are not necessarily units in pwm control, so we can't compare the two. 
        # this assumes that initially, a good speed is attainable
        # if the jam is right away, this method produces garbage
        while True: 
            speed = abs(self.encoder.position - self.last_position)
            if speed < target_encoder_speed * 0.01:
                break
            self.last_position = self.encoder.position
            
            print(self.encoder.position, speed)
            time.sleep(0.05)

            # Mostly for testing - if the motor runs too long, we want to stop
            time_running = time_running + 0.05
            if time_running > 2:
                break
        self.ena.duty_cycle = 0 # stop the motor when we're done

    # grasp
    def close(self, target_speed):
        self.controlled_move(target_speed=target_speed)

    def open(self):
        # We want to open it all the way - the last_position variable records how much it had to close
        self.in1.value, self.in2.value = (False, True)
        self.ena.duty_cycle = 5000
        while(self.last_position - self.encoder.position > 0):
            time.sleep(0.05)
        self.ena.duty_cycle = 0

    # removal
    def remove_cap(self):      
        #  print("Motor spinning CCW")
        self.dir.value = True
        # experimentally 3 seems right
        for i in range(3*200):
            self.single_step(0.005)
        # stop motor
        self.step.value = False
    
    def done_remove_cap(self):
        self.dir.value = False
        for i in range(3*200):
            self.single_step(0.005)
        self.step.value = False
    
    # # sensing
    # def get_distance(self):
    #     return self.prox.distance
    

   